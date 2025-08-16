#!/usr/bin/env bash
set -euo pipefail

# Repo to scan (env overrides welcome)
OWNER="${OWNER:-your-user-or-org}"
REPO="${REPO:-your-repo}"

# Range of Backlog IDs (two digits, inclusive)
: "${FROM:=01}"
: "${TO:=39}"

command -v gh >/dev/null || { echo "This script requires 'gh'."; exit 1; }
command -v jq >/dev/null || { echo "This script requires 'jq'."; exit 1; }

echo "| Backlog ID | GitHub Issue | Title |"
echo "|-----------:|-------------:|-------|"

for i in $(seq -w "$FROM" "$TO"); do
  title_prefix="B${i} —"
  data=$(
    gh issue list -R "$OWNER/$REPO" --state all --limit 400 --json number,title \
    | jq -r --arg p "$title_prefix" '
        .[] | select(.title | startswith($p))
        | [.number, .title] | @tsv
      ' | head -n1 || true
  )

  if [ -n "${data:-}" ]; then
    num=$(echo "$data" | cut -f1)
    title=$(echo "$data" | cut -f2-)
    echo "| B${i} | #${num} | ${title} |"
  else
    echo "| B${i} | (not found) | — |"
  fi
done
