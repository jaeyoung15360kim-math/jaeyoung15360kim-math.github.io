# Jaeyoung Kim

Source for [Jaeyoung Kim's academic website](https://young15360.github.io/jaeyoungkim-math/).

The public site contains only:

- a short academic introduction and one CV download;
- publications and current work listed in the CV;
- talks, presentations, and conferences listed in the CV;
- teaching experience listed in the CV.

The Blog, Repositories, Projects, standalone CV page, profile photograph, and
starter-theme examples are intentionally disabled or removed.

## CV updates

Replace `assets/pdf/CV_Jaeyoung_Kim.pdf` to update the downloadable CV. Replace
`assets/pdf/CV_Jaeyoung_Kim.tex` at the same time to synchronize visible
education, publications, and teaching content during deployment.

See [docs/CV_UPDATES.md](docs/CV_UPDATES.md) for the file contract and local
validation commands.

## Local validation

```bash
python bin/sync_cv_site.py --check
npm ci
npm run lint:prettier
npm run lint:style-contract
bundle exec jekyll build
bash test/integration_personal_site.sh
```

The site uses the pluginized al-folio v1 runtime. Intentional local template
overrides are recorded in `.al-folio-overrides.yml`.
