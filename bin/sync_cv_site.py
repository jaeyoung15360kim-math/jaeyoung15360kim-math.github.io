#!/usr/bin/env python3
"""Generate the website's CV-backed data from the canonical LaTeX CV."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "pdf" / "CV_Jaeyoung_Kim.tex"
OUTPUT = ROOT / "_data" / "site_cv.json"


def strip_comments(source: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", line) for line in source.splitlines())


def read_group(text: str, start: int) -> tuple[str, int]:
    while start < len(text) and text[start].isspace():
        start += 1
    if start >= len(text) or text[start] != "{":
        raise ValueError(f"Expected '{{' near: {text[start:start + 40]!r}")

    depth = 0
    for index in range(start, len(text)):
        character = text[index]
        if character == "{" and (index == 0 or text[index - 1] != "\\"):
            depth += 1
        elif character == "}" and (index == 0 or text[index - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return text[start + 1 : index], index + 1
    raise ValueError("Unbalanced braces in CV source")


def sections(source: str) -> dict[str, str]:
    found: list[tuple[str, int, int]] = []
    for match in re.finditer(r"\\cvsect\s*", source):
        name, end = read_group(source, match.end())
        found.append((name.strip(), match.start(), end))

    return {
        name: source[end : found[index + 1][1] if index + 1 < len(found) else len(source)]
        for index, (name, _, end) in enumerate(found)
    }


def macro_entries(body: str, names: dict[str, int]) -> list[tuple[str, list[str]]]:
    pattern = re.compile(r"\\(" + "|".join(re.escape(name) for name in names) + r")\b")
    entries: list[tuple[str, list[str]]] = []
    position = 0

    while match := pattern.search(body, position):
        name = match.group(1)
        cursor = match.end()
        arguments: list[str] = []
        try:
            for _ in range(names[name]):
                argument, cursor = read_group(body, cursor)
                arguments.append(argument)
        except ValueError:
            position = match.end()
            continue
        entries.append((name, arguments))
        position = cursor

    return entries


def replace_macro(text: str, name: str, argument_count: int, keep: int) -> str:
    pattern = re.compile(rf"\\{re.escape(name)}\s*")
    position = 0
    while match := pattern.search(text, position):
        cursor = match.end()
        arguments: list[str] = []
        try:
            for _ in range(argument_count):
                argument, cursor = read_group(text, cursor)
                arguments.append(argument)
        except ValueError:
            position = match.end()
            continue
        text = text[: match.start()] + arguments[keep] + text[cursor:]
        position = match.start()
    return text


def replace_hrefs(text: str) -> str:
    pattern = re.compile(r"\\href\s*")
    position = 0
    while match := pattern.search(text, position):
        cursor = match.end()
        try:
            url, cursor = read_group(text, cursor)
            label, cursor = read_group(text, cursor)
        except ValueError:
            position = match.end()
            continue
        replacement = f"[{clean_latex(label)}]({url.strip()})"
        text = text[: match.start()] + replacement + text[cursor:]
        position = match.start() + len(replacement)
    return text


def clean_latex(value: str) -> str:
    value = replace_hrefs(value)
    for macro in ("textbf", "textit", "emph", "mbox", "MakeUppercase"):
        value = replace_macro(value, macro, 1, 0)
    value = replace_macro(value, "textcolor", 2, 1)
    value = re.sub(r"\\color\s*\{[^{}]*\}", "", value)
    value = re.sub(r"\\begin\s*\{aligned\}(?:\[[^\]]*\])?", "", value)
    value = re.sub(r"\\end\s*\{aligned\}", "", value)
    value = re.sub(r"\\(?:small|large|Large|raggedleft|raggedright)\b", "", value)
    value = value.replace("\\\\", " / ")
    value = value.replace(r"\&", "&")
    value = value.replace(r"\!", "")
    value = value.replace("~", " ")
    value = re.sub(r"\s*/\s*/\s*", " / ", value)
    value = re.sub(r"\s+", " ", value).strip()
    if value.startswith("$") and value.endswith("$"):
        value = value[1:-1].strip()
    return value


def publication_id(title: str) -> str:
    plain = re.sub(r"\\(?:mathrm|mathbb|mathcal|text)\s*\{([^{}]*)\}", r"\1", title)
    plain = plain.replace("$", "").replace("\\", "")
    plain = unicodedata.normalize("NFKD", plain).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-")


def parse_publications(body: str) -> list[dict[str, str]]:
    items = re.split(r"\\item\b", body)[1:]
    publications: list[dict[str, str]] = []
    for raw_item in items:
        raw_item = re.split(r"\\end\s*\{enumerate\}", raw_item, maxsplit=1)[0]
        citation = clean_latex(raw_item)
        match = re.match(
            r"^(.*?)\s*\((\d{4}\+?)\)\.\s*(.*?)\.\s*(.*?)(?:\.)?$",
            citation,
        )
        if not match:
            raise ValueError(f"Could not parse publication entry: {citation}")
        authors, year, title, venue = (part.strip() for part in match.groups())
        publications.append(
            {
                "id": publication_id(title),
                "authors": authors,
                "year": year,
                "title": title,
                "venue": venue,
            }
        )
    return publications


def parse_education(body: str) -> list[dict[str, str]]:
    education: list[dict[str, str]] = []
    for _, arguments in macro_entries(body, {"entry": 4}):
        details = clean_latex(arguments[3]).replace("{", "").replace("}", "")
        details = re.sub(r"\s+", " ", details).strip()
        education.append(
            {
                "date": clean_latex(arguments[0]),
                "title": clean_latex(arguments[1]),
                "institution": clean_latex(arguments[2]),
                "details": details,
            }
        )
    return education


def parse_teaching(body: str) -> list[dict[str, str]]:
    return [
        {
            "date": clean_latex(arguments[0]),
            "title": clean_latex(arguments[1]),
            "institution": clean_latex(arguments[2]),
        }
        for _, arguments in macro_entries(body, {"entr": 3, "entry": 4})
    ]


def build_data(source: str) -> dict[str, object]:
    cv_sections = sections(strip_comments(source))
    required = ("Education", "Publication and Preprints", "Teaching")
    missing = [name for name in required if name not in cv_sections]
    if missing:
        raise ValueError(f"Missing required CV section(s): {', '.join(missing)}")

    return {
        "generated_from": SOURCE.name,
        "education": parse_education(cv_sections["Education"]),
        "publications": parse_publications(cv_sections["Publication and Preprints"]),
        "teaching": parse_teaching(cv_sections["Teaching"]),
    }


def serialized_data() -> str:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Canonical LaTeX CV not found: {SOURCE}")
    data = build_data(SOURCE.read_text(encoding="utf-8"))
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the committed generated data is not synchronized.",
    )
    arguments = parser.parse_args()
    generated = serialized_data()

    if arguments.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != generated:
            print(f"{OUTPUT.relative_to(ROOT)} is out of date.", file=sys.stderr)
            return 1
        print(f"{OUTPUT.relative_to(ROOT)} is synchronized.")
        return 0

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="\n") as output_file:
        output_file.write(generated)
    print(f"Updated {OUTPUT.relative_to(ROOT)} from {SOURCE.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
