#!/usr/bin/env bash
set -euo pipefail

tmp_dir="$(mktemp -d)"
cleanup() {
  rm -rf "${tmp_dir}"
}
trap cleanup EXIT

site_no_compat="${tmp_dir}/site-no-compat"
site_with_compat="${tmp_dir}/site-with-compat"
override_file="${tmp_dir}/compat-override.yml"

bundle exec jekyll build -d "${site_no_compat}" >/dev/null

baseurl="$(ruby -ryaml -rdate -e 'config = YAML.safe_load_file("_config.yml", permitted_classes: [Date], aliases: true) || {}; print config.fetch("baseurl", "").to_s.sub(%r{/$}, "")')"

index_no_compat="${site_no_compat}/index.html"
grep -Fq "${baseurl}/assets/css/custom.css" "${index_no_compat}"
if grep -Fq "${baseurl}/assets/css/bootstrap-compat.css" "${index_no_compat}"; then
  echo "unexpected bootstrap compatibility stylesheet in default build" >&2
  exit 1
fi
if grep -qiE '<script[^>]+src=["'"'"'][^"'"'"']*jquery[^"'"'"']*["'"'"']' "${index_no_compat}"; then
  echo "unexpected jquery runtime script in default build" >&2
  exit 1
fi

cat >"${override_file}" <<'YAML'
al_folio:
  compat:
    bootstrap:
      enabled: true
YAML

bundle exec jekyll build --config "_config.yml,${override_file}" -d "${site_with_compat}" >/dev/null

index_with_compat="${site_with_compat}/index.html"
grep -Fq "${baseurl}/assets/css/bootstrap-compat.css" "${index_with_compat}"
grep -Fq "${baseurl}/assets/js/bootstrap-compat.js" "${index_with_compat}"
[ -f "${site_with_compat}/assets/css/bootstrap-compat.css" ]
[ -f "${site_with_compat}/assets/js/bootstrap-compat.js" ]

echo "bootstrap compatibility integration checks passed"
