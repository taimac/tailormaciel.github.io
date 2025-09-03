# Import the New Backlog (B01…B39) into GitHub

## 1) Create milestones and labels
```bash
export OWNER=your-user-or-org
export REPO=your-repo
bash create_milestones_and_labels.sh
```

## 2) Import issues (B-IDs baked into titles)
Requires: https://www.npmjs.com/package/github-csv-tools
```bash
npm i -g github-csv-tools
githubCsvTools issues_with_backlog_ids.csv -o $OWNER -r $REPO
```

## 3) Auto-add imported issues to your Project (UI)
Project → Workflows → Auto-add to project → filter:
```
label:backlog-import-2025-08
```
Turn it **On**.

## 4) Close superseded legacy issues (28–44)
```bash
bash bulk_close_old_issues_BIDs.sh
```

## 5) (Optional) Generate Backlog ID → GitHub # mapping
```bash
# needs gh + jq
bash generate_backlog_id_mapping.sh
```
