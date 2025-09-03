#!/usr/bin/env bash
set -euo pipefail
OWNER="${OWNER:-your-user-or-org}"
REPO="${REPO:-your-repo}"
superseded_label="superseded-by-2025-08"
gh label create "$superseded_label" -R $OWNER/$REPO --force || true
declare -A MAP
MAP[28]="B01 B02 B03 B04"
MAP[29]="B05 B06 B07 B08"
MAP[30]="B12 B32 B33 B34"
MAP[31]="B16 B17 B18 B31"
MAP[32]="B07 B08 B19 B20 B21 B22 B23 B24"
MAP[33]="B06 B09 B12 B15"
MAP[34]="B28 B29 B30 B31"
MAP[35]="B10 B11 B13 B14 B15"
MAP[36]="B35 B36 B37 B38 B39"
MAP[41]="B19 B20 B21 B22 B23 B24"
MAP[42]="B25 B26 B27 B28 B29 B30 B31"
MAP[43]="B27 B28 B29 B31 B39"
MAP[44]="B32 B33 B34"

for n in "${!MAP[@]}"; do
  echo "Closing #$n as superseded in $OWNER/$REPO"
  gh issue edit "$n" -R "$OWNER/$REPO" --add-label "$superseded_label"
  gh issue comment "$n" -R "$OWNER/$REPO" --body "This legacy issue is superseded by the Aug 2025 Backlog items: ${MAP[$n]} (Backlog IDs). Closing to reduce noise while preserving history."
  gh issue close "$n" -R "$OWNER/$REPO" --reason "not planned"
done

# Special case: database setup (old #40) — won't do
if gh issue view 40 -R "$OWNER/$REPO" &>/dev/null; then
  gh issue edit 40 -R "$OWNER/$REPO" --add-label "$superseded_label"
  gh issue comment 40 -R "$OWNER/$REPO" --body "We pivoted to a file-based metadata approach (no DB) for MVP. Superseded by Backlog IDs B02 and B10."
  gh issue close 40 -R "$OWNER/$REPO" --reason "not planned"
fi
echo "Done."
