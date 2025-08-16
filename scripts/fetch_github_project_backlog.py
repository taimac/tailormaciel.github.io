#!/usr/bin/env python3
"""
GitHub Issues to Single Markdown File
Simple version for learning
"""
import argparse
import requests
import os
from datetime import datetime


class SimpleIssuesExporter:

    """
    Exports GitHub issues to a markdown backlog file.

    OOP: Encapsulates all export logic for maintainability.
    Security: Uses environment variable for token, never logs secrets.
    Clean Code: Single Responsibility - only fetches and exports issues.
    """

    def __init__(self, repo, token):
        self.repo = repo  # "tailormaciel/tailormaciel.github.io"
        self.token = token
        self.api_url = f"https://api.github.com/repos/{repo}/issues"

    def get_issues(self):
        """Fetch all issues from GitHub"""
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json",
        }
        session = requests.Session()
        all_items = []
        page = 1
        per_page = 100

        try:
            while True:
                params = {"state": "all", "per_page": per_page, "page": page}
                resp = session.get(self.api_url, headers=headers, params=params, timeout=30)
                resp.raise_for_status()
                batch = resp.json()
                all_items.extend(batch)
                if "next" in (resp.links or {}):
                    page += 1
                else:
                    break
            return all_items
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching issues: {e}")
            return []

    def export_backlog(self):
        """Export all issues to single markdown file"""
        print(f"📥 Fetching issues from {self.repo}...")

        issues = self.get_issues()
        if not issues:
            print("❌ No issues found or API error")
            return

        # Filter out pull requests (GitHub API includes them)
        actual_issues = [issue for issue in issues if "pull_request" not in issue]
        open_issues = [i for i in actual_issues if i["state"] == "open"]
        closed_issues = [i for i in actual_issues if i["state"] == "closed"]

        print(
            f"📋 Found {len(actual_issues)} issues ({len(open_issues)} open, {len(closed_issues)} closed)"
        )

        # Create docs directory
        os.makedirs("docs", exist_ok=True)

        # Build markdown content
        content = f"""# 📋 Development Backlog

**Repository**: [{self.repo}](https://github.com/{self.repo})
**Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Total Issues**: {len(actual_issues)} | **Open**: {len(open_issues)} | **Closed**: {len(closed_issues)}

---

"""

        # Add open issues first
        if open_issues:
            content += "## 🚀 Open Issues (To Do)\n\n"
            for issue in sorted(open_issues, key=lambda x: x["number"]):
                content += self.format_issue(issue)

        # Add closed issues
        if closed_issues:
            content += "## ✅ Completed Issues\n\n"
            for issue in sorted(closed_issues, key=lambda x: x["number"], reverse=True):
                content += self.format_issue(issue)

        # Save to file
        filepath = "docs/backlog.md"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Exported to {filepath}")
        print(f"🔍 Open in VS Code: code {filepath}")

    def format_issue(self, issue):
        """Format single issue as markdown"""
        number = issue["number"]
        title = issue["title"]
        body = issue.get("body", "") or "*No description*"
        state = issue["state"]
        labels = [label["name"] for label in issue.get("labels", [])]
        html_url = issue["html_url"]

        # Status emoji
        status_emoji = "🟢" if state == "open" else "✅"

        # Labels formatting
        labels_str = ""
        if labels:
            labels_str = " | " + " ".join([f"`{label}`" for label in labels])

        return f"""### {status_emoji} Issue #{number}: {title}

**Status**: {state.upper()}{labels_str}
**GitHub**: [{html_url}]({html_url})

**Description**:
{body}

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

"""


# Usage


def main():
    parser = argparse.ArgumentParser(
        description="Export GitHub issues to a markdown backlog file."
    )
    parser.add_argument(
        "--repo",
        type=str,
        help="GitHub repository in the form owner/repo (e.g., octocat/Hello-World)",
    )
    args = parser.parse_args()

    REPO = args.repo or os.environ.get("GITHUB_REPO") or "taimac/tailormaciel.github.io"
    TOKEN = os.environ.get("GITHUB_TOKEN")

    if not TOKEN:
        print("⚠️  GITHUB_TOKEN environment variable not found")
        TOKEN = input("Enter your GitHub token: ").strip()
        if not TOKEN:
            print("❌ Token required!")
            return
    else:
        print("✅ Using GITHUB_TOKEN from environment")

    exporter = SimpleIssuesExporter(REPO, TOKEN)
    exporter.export_backlog()


if __name__ == "__main__":
    main()
