# Backlog Restructure — August 2025

**Repository:** `taimac/tailormaciel.github.io`
**Scope:** Personal Website & File‑Based Knowledge Base
**Related doc:** *Reorganized Project Backlog* (complete, expanded spec of epics/issues)

---

## Executive Summary (TL;DR)

We replaced an outdated backlog with a structured, learning‑oriented plan that aligns with a **file‑based knowledge base**, **minimal Flask backend**, and **Clean Architecture**. The new plan introduces:

* **Stable Backlog IDs (B01…B39)** in issue titles so planning stays consistent while GitHub issue numbers increase.
* **Milestones 0–4** with explicit success criteria and a teaching‑first scope.
* **Epics refactored** around OOP, search, graph, auth, UX, testing, docs, and perf.
* **Labels system & Definition of Done** to enforce quality (70%+ coverage, a11y, security notes, docs).
* **Automation scripts** for creating milestones/labels, importing issues, mapping B‑IDs ↔ GitHub numbers, and closing legacy issues as superseded.

*Outcome:* new issues **#51–#89** (B01…B39) now form the canonical backlog. Legacy items (#28–#44) are marked **superseded** with a pointer to the relevant B‑IDs.

---

## Why We Changed the Backlog

The previous backlog mixed a DB‑centric plan and vague epics. The project pivoted to:

* **Minimal frameworks** to emphasize fundamentals (ES6, Vanilla JS, Flask).
* **File‑based metadata** instead of a database for MVP.
* **Educational architecture**: every issue includes **Learning Goals** and **Acceptance Criteria**.

This required re‑grouping scope by **Clean Architecture layers** and **OOP patterns**, with a clear progression across milestones.

---

## What Changed — At a Glance

### 1) Stable Backlog IDs in Titles

* Every issue title starts with `Bxx — …` (e.g., `B07 — Polymorphic File Explorer Component`).
* Benefits: stable references in docs/PRs/commits even as GitHub issue numbers grow.

### 2) Milestones & Success Criteria

* **Milestone 0**: Dev environment + hybrid skeleton ready
* **Milestone 1**: File‑based foundation & OOP types
* **Milestone 2**: Search + Graph
* **Milestone 3**: Auth + Private content
* **Milestone 4**: UX foundation, testing, docs, performance, deploy

(Full detail in *Reorganized Project Backlog* — “Milestones & Success Criteria”.)

### 3) Epics Refactored

* **EPIC 0** Hybrid foundation (Milestone 0)
* **EPIC 1** OOP file explorer & content management (M1)
* **EPIC 2** Search & metadata processing (M2)
* **EPIC 3** Knowledge graph visualization (M2)
* **EPIC 4** Auth & private content security (M3)
* **EPIC 5** Frontend foundation & UX (M4)
* **EPIC 6** Dev utilities & automation (M4)
* **EPIC 7** Testing & QA (M4)
* **EPIC 8** Documentation (M4)
* **EPIC 9** Performance & production optimization (M4)

Each issue includes **Description**, **Learning Goals**, **Acceptance Criteria**, and suggested **branch name**.

### 4) Labels & Definition of Done

* **Labels**: priority, type, learning focus, component.
* **DoD**: 70%+ coverage for the touched area, a11y pass, security notes, docs updated, CI green.

### 5) Automation & Scripts

* `create_milestones_and_labels.sh` — idempotently creates labels/milestones expected by issues.
* `issues_with_backlog_ids.csv` — source data for bulk import (one row per issue).
* `import_backlog_with_gh.py` — imports issues via `gh` CLI (proved successful; created #51–#89).
* `bulk_close_old_issues_BIDs.sh` — labels + comments + closes legacy issues as **not planned**.
* `generate_backlog_id_mapping.sh` — prints a Markdown table mapping **B‑IDs ↔ GitHub #**.

---

## Migration We Performed

1. **Created** milestones/labels (safe to re‑run).
2. **Imported** 39 issues with B‑IDs (now **#51–#89**).
3. **Labeled** new issues with `backlog-import-2025-08` for Project auto‑add.
4. **Closed** legacy issues as **not planned** with explanation and B‑ID pointers.
5. **Enabled** Project workflow: Auto‑add items with filter

   ```text
   repo:taimac/tailormaciel.github.io is:issue label:backlog-import-2025-08
   ```
6. **(Optional)** Generated B‑ID mapping table via `generate_backlog_id_mapping.sh` and saved to `docs/backlog-map.md`.

---

## Legacy → New Backlog Mapping (superseded)

> Old issues are preserved for history and discussion; we add a comment/label and close as “not planned”.

| Legacy Issue | Superseded by Backlog IDs       | Notes                                                      |
| -----------: | ------------------------------- | ---------------------------------------------------------- |
|          #28 | B01 B02 B03 B04                 | Hybrid foundation now split across Milestone 0 issues      |
|          #29 | B05 B06 B07 B08                 | OOP filesystem + core UI components                        |
|          #30 | B12 B32 B33 B34                 | Services layer + docs alignment                            |
|          #31 | B16 B17 B18 B31                 | Auth, access control, session + security tests             |
|          #32 | B07 B08 B19 B20 B21 B22 B23 B24 | UI explorer through nav/styling/error patterns             |
|          #33 | B06 B09 B12 B15                 | Content types, search engine, services, graph discovery    |
|          #34 | B28 B29 B30 B31                 | Testing: FE, BE, integration, security/static checks       |
|          #35 | B10 B11 B13 B14 B15             | Indexing, filtering/tagging, graph data & viz & discovery  |
|          #36 | B35 B36 B37 B38 B39             | Perf & deploy: caching/compress/render/asset/deploy        |
|          #40 | B02 B10                         | **Special:** DB setup dropped; file‑based metadata + index |
|          #41 | B19 B20 B21 B22 B23 B24         | App shell/routing, styling, a11y, error states, build      |
|          #42 | B25 B26 B27 B28 B29 B30 B31     | Utilities + tests suite                                    |
|          #43 | B27 B28 B29 B31 B39             | Deploy + tests + security + deploy config                  |
|          #44 | B32 B33 B34                     | Documentation set                                          |

> Exact GitHub numbers for B‑IDs live in `docs/backlog-map.md` (generate via `generate_backlog_id_mapping.sh`).

---

## Project Board Setup

* **Auto‑add Workflow (On):**

  ```text
  repo:taimac/tailormaciel.github.io is:issue label:backlog-import-2025-08
  ```
* **Backfill once:** In the Project, click **+ Add items** and search with the same filter; select all and **Add**.
* **Recommended View (Board):**

  * **Group by:** Milestone
  * **Sort by:** Title (keeps B01…B39 ordered)
  * **Fields:** Title, Assignees, Milestone, Status, Labels
* **Optional Rules:** on add → set Status = `Todo`; on Status change → move columns.

---

## Development Workflow Guardrails

* **Branch naming:** `feature/issue-<N>-short-slug` → PR into `dev`.
* **Security‑first:** input validation, token handling, HTTPS, least privilege.
* **Clean Architecture:** Presentation → Application → Domain → Infrastructure; dependencies point inward.
* **OOP Focus:** Encapsulation, Abstraction, Inheritance, Polymorphism; Factory, Strategy, Observer (as relevant per issue).

---

## Impact on In‑Flight Work

* Open PRs against legacy issues should be rebased to the corresponding **B‑ID issue** (see mapping table). Add `Fixes #<new-number>` in PR descriptions.
* Any references to old issue numbers in docs should be updated to **B‑ID** form or new GitHub numbers.

---

## Next Steps (Checklist)

* [ ] Ensure **Issues** are enabled in the repo (done).
* [ ] Confirm Project **Auto‑add** is **On** with the filter above.
* [ ] Run `generate_backlog_id_mapping.sh --out docs/backlog-map.md` and commit the file.
* [ ] Close remaining legacy issues as **not planned** (script patched to use `--reason "not planned"`).
* [ ] Start **Milestone 0**: B01–B04.
* [ ] Keep `docs/CHANGELOG.md` updated per milestone.

---

## Appendix A — Teaching Rationale (selected examples)

* **B05–B08 (OOP foundation):** Builds type hierarchy and polymorphic UI—teaches abstraction and decoupling between model/services/presentation.
* **B09–B11 (Search/Filters):** Strategy pattern makes ranking pluggable; reinforces SOLID and testability.
* **B13–B15 (Graph):** Data structures + traversal (BFS/DFS) link CS fundamentals to real UX.
* **B16–B18 (Security):** JWT, access control, session hygiene—shows secure defaults and error design.
* **B28–B31 (QA/Sec):** Tests enforce the DoD; static analysis and token tamper tests shift security left.

---

## Appendix B — Commands We Used (for reproducibility)

```bash
# Create milestones & labels (idempotent)
bash create_milestones_and_labels.sh

# Import issues using GitHub CLI (created #51–#89)
python3 import_backlog_with_gh.py --owner taimac --repo tailormaciel.github.io --csv issues_with_backlog_ids.csv

# Close legacy issues as superseded (uses "not planned")
bash bulk_close_old_issues_BIDs.sh

# Generate mapping table B‑ID ↔ GitHub issue number
OWNER=taimac REPO=tailormaciel.github.io ./generate_backlog_id_mapping.sh --out docs/backlog-map.md
```

---

# GitHub Issue Importer

## Overview

This Python script (`import_backlog_with_gh.py`) is designed to bulk import GitHub issues from a CSV file into a GitHub repository using the GitHub CLI (`gh`) tool. It's particularly useful for migrating issues from other systems, restoring archived issues, or bulk-creating issues from a structured backlog.

## Core Concept

The script reads issue data from a CSV file and creates corresponding GitHub issues, with built-in safeguards to:
- Avoid creating duplicate issues
- Handle missing labels and milestones gracefully
- Provide clear feedback on the import process

## Prerequisites

1. **GitHub CLI (`gh`)** must be installed and authenticated
2. **Repository access** - you need write permissions to create issues
3. **Issues enabled** - the target repository must have Issues feature enabled
4. **CSV file** with properly formatted issue data

## CSV File Format

The script expects a CSV file (default: `issues_with_backlog_ids.csv`) with the following columns:

| Column | Required | Description |
|--------|----------|-------------|
| `title` | Yes | The issue title |
| `body` | Yes | The issue description/content |
| `labels` | No | Comma-separated list of label names |
| `milestone` | No | Milestone name to assign |

### Example CSV:
```csv
title,body,labels,milestone
"Fix login bug","Users cannot login with special characters in password","bug,priority-high","v1.2.0"
"Add dark mode","Implement dark theme for better UX","enhancement,ui","v2.0.0"
"Update documentation","API docs need refresh","documentation",""
```

## Usage

### Basic Usage
```bash
python3 import_backlog_with_gh.py --owner myorg --repo myproject
```

### Using Environment Variables
```bash
export OWNER=myorg
export REPO=myproject
python3 import_backlog_with_gh.py
```

### Custom CSV File
```bash
python3 import_backlog_with_gh.py --owner myorg --repo myproject --csv my_issues.csv
```

## Command Line Arguments

- `--owner, -o`: GitHub repository owner (username or organization)
- `--repo, -r`: Repository name
- `--csv`: Path to CSV file (default: `issues_with_backlog_ids.csv`)

Both `--owner` and `--repo` can be set via `OWNER` and `REPO` environment variables.

## How It Works

### 1. Validation Phase
- Verifies GitHub CLI is authenticated
- Checks if the target repository exists
- Confirms Issues are enabled on the repository

### 2. Import Phase
For each row in the CSV:

1. **Duplicate Check**: Searches existing issues by title to avoid duplicates
2. **Issue Creation**: Attempts to create the issue with all metadata (labels, milestone)
3. **Graceful Fallback**: If labels/milestone don't exist, retries without them
4. **Progress Reporting**: Provides clear feedback on each operation

### 3. Safety Features
- **Duplicate Prevention**: Skips issues that already exist (by title match)
- **Secure Body Handling**: Uses temporary files to safely handle issue bodies with special characters
- **Error Recovery**: Continues processing even if individual issues fail
- **Clear Logging**: Reports success, warnings, and errors for each operation

## Output Examples

```
CREATED: Fix login bug
SKIP (exists): Add dark mode  
WARN: create with labels/milestone failed: milestone "v3.0.0" not found
Retrying without labels/milestone…
CREATED (no labels/milestone): Update documentation
ERROR creating Invalid issue title: title cannot be empty
Done.
```

## Error Handling

The script handles several error scenarios gracefully:

- **Authentication issues**: GitHub CLI not logged in
- **Repository access**: Insufficient permissions or repo doesn't exist
- **Missing labels/milestones**: Retries without metadata if they don't exist
- **Malformed CSV**: Continues processing valid rows
- **Network issues**: Reports failures but continues with remaining issues

## Best Practices

1. **Test First**: Run on a test repository to verify your CSV format
2. **Backup**: Keep your original CSV file as a backup
3. **Small Batches**: For large backlogs, consider processing in smaller chunks
4. **Pre-create Labels**: Create labels and milestones in GitHub before import for best results
5. **Review Duplicates**: The duplicate check is title-based only, so ensure unique titles

## Limitations

- Duplicate detection is based only on issue titles
- Cannot set assignees, projects, or other advanced GitHub issue features
- Requires GitHub CLI to be properly configured
- No progress bar for large imports
- Labels and milestones must exist in the repository (or will be skipped)

## Use Cases

- **System Migration**: Moving issues from Jira, Trello, or other project management tools
- **Backup Restoration**: Restoring issues from exported data
- **Bulk Creation**: Creating multiple similar issues from templates
- **Historical Import**: Adding archived issues back to active repositories

*If this document changes, update the date in the filename and briefly summarize edits at the top.*
