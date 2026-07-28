# Updating the CV and website

The canonical CV files are:

- `assets/pdf/CV_Jaeyoung_Kim.pdf` — the single downloadable CV linked from the homepage.
- `assets/pdf/CV_Jaeyoung_Kim.tex` — the structured source used to refresh the website.

Replace one or both files using the same filenames and push the change to `main`.
The deploy workflow then:

1. refreshes `_data/site_cv.json` from the LaTeX sections `Education`,
   `Publication and Preprints`, and `Teaching`;
2. commits the generated data when it changed;
3. rebuilds and deploys the site.

A PDF-only replacement updates the downloadable CV. To change the visible education,
publication, or teaching lists, include the matching LaTeX update. Keep using the
existing `\cvsect`, `\entry`, and `\entr` structure so the importer can read it.

Publication abstracts and destination links are intentionally maintained in
`_data/publication_details.yml`, because they are not part of the CV. Add an entry
whose key matches the generated publication `id` when a public abstract or link
becomes available.

Run the synchronization locally with:

```bash
python bin/sync_cv_site.py
```

Verify that the generated file is current with:

```bash
python bin/sync_cv_site.py --check
```
