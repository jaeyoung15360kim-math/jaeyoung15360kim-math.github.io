#!/usr/bin/env bash
set -euo pipefail

tmp_dir="$(mktemp -d)"
tmp_override="${tmp_dir}/distill-override.yml"
tmp_site="${tmp_dir}/site"
fixture="_posts/2021-05-22-distill-integration-fixture.md"

cleanup() {
  rm -f "${fixture}"
  rmdir _posts 2>/dev/null || true
  rm -rf "${tmp_dir}"
}
trap cleanup EXIT

mkdir -p _posts
cat >"${fixture}" <<'MARKDOWN'
---
layout: distill
title: Distill integration fixture
description: Build-only fixture for the plugin contract
date: 2021-05-22
permalink: /blog/2021/distill-integration-fixture/
giscus_comments: true
mermaid:
  enabled: true
tikzjax: true
authors:
  - name: Jaeyoung Kim
    affiliations:
      name: Seoul National University
---

This temporary post exists only while the integration test runs.
MARKDOWN

cat >"${tmp_override}" <<'YAML'
al_folio:
  features:
    distill:
      enabled: true
giscus:
  repo: jaeyoung15360kim-math/jaeyoung15360kim-math.github.io
  repo_id: R_kgDOExample
  category: Comments
  category_id: DIC_kwDOExample
YAML

bundle exec jekyll build --config "_config.yml,${tmp_override}" -d "${tmp_site}" >/dev/null

distill_page="${tmp_site}/blog/2021/distill-integration-fixture/index.html"
if [ ! -f "${distill_page}" ]; then
  echo "distill integration fixture was not generated" >&2
  exit 1
fi

baseurl="$(ruby -ryaml -rdate -e 'config = YAML.safe_load_file("_config.yml", permitted_classes: [Date], aliases: true) || {}; print config.fetch("baseurl", "").to_s.sub(%r{/$}, "")')"

grep -q 'd-front-matter' "${distill_page}"
grep -Fq "${baseurl}/assets/js/distillpub/template.v2.js" "${distill_page}"
grep -Fq "${baseurl}/assets/js/distillpub/transforms.v2.js" "${distill_page}"
grep -q 'id="giscus_thread"' "${distill_page}"

echo "distill integration checks passed"
