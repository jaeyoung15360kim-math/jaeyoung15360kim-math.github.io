#!/usr/bin/env bash
set -euo pipefail

tmp_dir="$(mktemp -d)"
tmp_site="${tmp_dir}/site"

cleanup() {
  rm -rf "${tmp_dir}"
}
trap cleanup EXIT

python bin/sync_cv_site.py
bundle exec jekyll build -d "${tmp_site}" >/dev/null

home="${tmp_site}/index.html"
publications="${tmp_site}/publications/index.html"
talks="${tmp_site}/talks/index.html"
teaching="${tmp_site}/teaching/index.html"

for page in "${home}" "${publications}" "${talks}" "${teaching}"; do
  test -f "${page}"
done

for removed_route in blog repositories projects cv books news plugins; do
  if [ -e "${tmp_site}/${removed_route}/index.html" ]; then
    echo "unexpected removed route: /${removed_route}/" >&2
    exit 1
  fi
done

test "$(grep -o 'href="mailto:jaeyoungkim22@snu.ac.kr"' "${home}" | wc -l)" -eq 1
test "$(grep -o '/assets/pdf/CV_Jaeyoung_Kim.pdf' "${home}" | wc -l)" -eq 1
! grep -qiE 'prof_pic|einstein|selected publications' "${home}"
! grep -qiE '>blog<|>repositories<|>CV<' "${home}"

grep -q '<summary>Abstract</summary>' "${publications}"
grep -q 'https://doi.org/10.1142/S0129055X22500210' "${publications}"
grep -q 'https://arxiv.org/abs/2105.00709' "${publications}"
! grep -qiE 'bibtex|\\.bib' "${publications}"

grep -q 'Differential and Integral Calculus Practice' "${teaching}"
grep -q 'Teaching Volunteer' "${teaching}"
! grep -qiE 'Data Science|Machine Learning|Topics Covered|Textbooks|Grading' "${teaching}"

echo "personal site integration checks passed"
