#!/usr/bin/env bash
set -euo pipefail
OWNER="${OWNER:-your-user-or-org}"
REPO="${REPO:-your-repo}"
echo "Creating milestones in $OWNER/$REPO"
gh api repos/$OWNER/$REPO/milestones -f title='Milestone 0' -f description='Development Environment Ready' || true
gh api repos/$OWNER/$REPO/milestones -f title='Milestone 1' -f description='File-Based Foundation & OOP' || true
gh api repos/$OWNER/$REPO/milestones -f title='Milestone 2' -f description='Knowledge Graph & Search' || true
gh api repos/$OWNER/$REPO/milestones -f title='Milestone 3' -f description='Auth & Private Content' || true
gh api repos/$OWNER/$REPO/milestones -f title='Milestone 4' -f description='Advanced Features & Prod' || true
echo "Creating labels in $OWNER/$REPO"
gh label create "priority-critical" -R $OWNER/$REPO --force || true
gh label create "priority-high" -R $OWNER/$REPO --force || true
gh label create "priority-medium" -R $OWNER/$REPO --force || true
gh label create "priority-low" -R $OWNER/$REPO --force || true
gh label create "type-epic" -R $OWNER/$REPO --force || true
gh label create "type-feature" -R $OWNER/$REPO --force || true
gh label create "type-bug" -R $OWNER/$REPO --force || true
gh label create "type-enhancement" -R $OWNER/$REPO --force || true
gh label create "type-refactor" -R $OWNER/$REPO --force || true
gh label create "type-documentation" -R $OWNER/$REPO --force || true
gh label create "learning-oop" -R $OWNER/$REPO --force || true
gh label create "learning-architecture" -R $OWNER/$REPO --force || true
gh label create "learning-security" -R $OWNER/$REPO --force || true
gh label create "learning-patterns" -R $OWNER/$REPO --force || true
gh label create "learning-frontend" -R $OWNER/$REPO --force || true
gh label create "component-files" -R $OWNER/$REPO --force || true
gh label create "component-metadata" -R $OWNER/$REPO --force || true
gh label create "component-graph" -R $OWNER/$REPO --force || true
gh label create "component-auth" -R $OWNER/$REPO --force || true
gh label create "component-ui" -R $OWNER/$REPO --force || true
gh label create "component-utilities" -R $OWNER/$REPO --force || true
gh label create "component-testing" -R $OWNER/$REPO --force || true
gh label create "component-docs" -R $OWNER/$REPO --force || true
gh label create "component-performance" -R $OWNER/$REPO --force || true
gh label create "backlog-import-2025-08" -R $OWNER/$REPO --force || true
echo "Done."
