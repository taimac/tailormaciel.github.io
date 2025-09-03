#!/usr/bin/env python3
"""
Export GitHub issues + open PRs to a markdown backlog.

Notes:
- Includes open pull requests in an "Active Pull Requests" section.
- Provides diagnostics (counts, PR #90 check).
- Minimal CLI: uses GITHUB_TOKEN and GITHUB_REPO env vars by default.
- Keeps output visible and explicit.
"""
from __future__ import annotations

import os
import sys
from datetime import UTC, datetime
from enum import Enum
from typing import Any

try:
    # prefer packaged helper if available
    from ..utils.http_session import create_session_with_pooling_and_timeout
except Exception:
    import requests

    def create_session_with_pooling_and_timeout():
        s = requests.Session()
        s.headers.update({"User-Agent": "GitHubBacklogExporter/1.0"})
        return s


# --- Configurable defaults ---
DEFAULT_OUTPUT = "docs/backlog_summary.md"
DEFAULT_REPO = "taimac/tailormaciel.github.io"
PER_PAGE = 100
MAX_PAGES = 50


class ExportFormat(Enum):
    SUMMARY = "summary"
    DETAILED = "detailed"


# --- Simple formatter (extendable) ---
class SimpleFormatter:
    def sanitize(self, text: Any) -> str:
        if not isinstance(text, str):
            return ""
        return text.strip()

    def format_issue(self, issue: dict[str, Any]) -> str:
        number = issue.get("number", "?")
        title = self.sanitize(issue.get("title", "No title"))
        url = issue.get("html_url", "#")
        labels = [lb1.get("name", "") for lb1 in issue.get("labels", []) if isinstance(lb1, dict)]
        labels_str = f" `{', '.join(labels)}`" if labels else ""
        state = issue.get("state", "unknown")
        emoji = "🚀" if state == "open" else "✅"
        return f"{emoji} **[#{number}]({url})** {title}{labels_str}\n\n"

    def format_pr(self, pr: dict[str, Any]) -> str:
        number = pr.get("number", "?")
        title = self.sanitize(pr.get("title", "No title"))
        url = pr.get("html_url", "#")
        state = pr.get("state", "unknown")
        emoji = {"open": "🔄", "closed": "❌"}.get(state, "🔁")
        labels = [lb1.get("name", "") for lb1 in pr.get("labels", []) if isinstance(lb1, dict)]
        labels_str = f" `{', '.join(labels)}`" if labels else ""
        body = self.sanitize(pr.get("body", ""))
        preview = (body[:120] + "...") if body and len(body) > 120 else body
        preview_md = f"\n  *{preview}*\n" if preview else ""
        return f"{emoji} **[#{number}]({url})** {title}{labels_str}{preview_md}\n"

    def section_header(self, title: str, count: int) -> str:
        return f"## {title} ({count})\n\n"


# --- Detailed formatter (rich output) ---
class DetailedFormatter(SimpleFormatter):
    """
    DetailedFormatter extends SimpleFormatter to include metadata and longer previews.

    OOP notes:
    - Inheritance: reuses formatting logic from SimpleFormatter.
    - Polymorphism: exporter can use either formatter interchangeably.
    - SRP: formatting responsibilities isolated in formatter classes.

    Security notes:
    - Reuses sanitize() to avoid injecting raw content into markdown.
    """

    def _fmt_meta(self, item: dict[str, Any]) -> str:
        parts: list[str] = []
        user = item.get("user") or {}
        if user.get("login"):
            parts.append(f"author: {self.sanitize(user.get('login'))}")
        if item.get("created_at"):
            parts.append(f"created: {self.sanitize(item.get('created_at'))}")
        if item.get("comments") is not None:
            parts.append(f"comments: {item.get('comments')}")
        assignees = [a.get("login") for a in item.get("assignees", []) if isinstance(a, dict) and a.get("login")]
        if assignees:
            parts.append(f"assignees: {', '.join(self.sanitize(a) for a in assignees)}")
        return " • ".join(parts)

    def format_issue(self, issue: dict[str, Any]) -> str:
        """
        Render a full issue: title, labels, milestone, metadata, full body, reactions and full comments.
        """
        base = super().format_issue(issue).rstrip("\n")
        # full body (not truncated) - sanitized
        body = self.sanitize(issue.get("body", "") or "")
        meta = self._fmt_meta(issue)
        milestone = issue.get("_milestone_title")
        milestone_md = f"\n  _milestone: {self.sanitize(milestone)}_\n" if milestone else ""
        reactions = issue.get("_reactions", {})
        reactions_md = ""
        if isinstance(reactions, dict) and reactions.get("total_count"):
            # keep keys in a named list to avoid long inline expressions and enforce spaces after commas
            reaction_keys = [
                "+1",
                "-1",
                "laugh",
                "hooray",
                "confused",
                "heart",
                "rocket",
                "eyes",
            ]
            reaction_parts = [f"{k}={reactions.get(k)}" for k in reaction_keys if reactions.get(k) is not None]
            reactions_md = "  _reactions: " + ", ".join(reaction_parts) + "_\n"
        comments = issue.get("_comments_list", []) or []
        comments_md = ""
        if comments:
            comments_md = "\n**Comments**\n\n"
            for c in comments:
                author = c.get("user", {}).get("login", "unknown")
                created = c.get("created_at", "")
                body_c = self.sanitize(c.get("body", "") or "")
                # keep moderate length for comments but include full if short
                preview = body_c if len(body_c) <= 1000 else body_c[:1000] + "..."
                comments_md += f"- _{author} • {created}_\n\n  {preview}\n\n"
        preview_line = f"\n{body}\n" if body else ""
        meta_line = f"\n  _{meta}_\n" if meta else ""
        return f"{base}{milestone_md}{meta_line}{reactions_md}{preview_line}{comments_md}\n"

    def format_pr(self, pr: dict[str, Any]) -> str:
        """
        Render a full pull request: use PR html_url, include body, meta, reactions and comments.
        """
        pr_url = pr.get("pull_request", {}).get("html_url") or pr.get("html_url", "#")
        number = pr.get("number", "?")
        title = self.sanitize(pr.get("title", "No title"))
        labels = [lb1.get("name", "") for lb1 in pr.get("labels", []) if isinstance(lb1, dict)]
        labels_str = f" `{', '.join(labels)}`" if labels else ""
        state = pr.get("state", "unknown")
        emoji = {"open": "🔄", "closed": "❌"}.get(state, "🔁")
        meta = self._fmt_meta(pr)
        reactions = pr.get("_reactions", {})
        reactions_md = ""
        if isinstance(reactions, dict) and reactions.get("total_count"):
            reaction_keys = [
                "+1",
                "-1",
                "laugh",
                "hooray",
                "confused",
                "heart",
                "rocket",
                "eyes",
            ]
            reaction_parts = [f"{k}={reactions.get(k)}" for k in reaction_keys if reactions.get(k) is not None]
            reactions_md = "  _reactions: " + ", ".join(reaction_parts) + "_\n"
        body = self.sanitize(pr.get("body", "") or "")
        body_line = f"\n{body}\n" if body else ""
        comments = pr.get("_comments_list", []) or []
        comments_md = ""
        if comments:
            comments_md = "\n**Comments**\n\n"
            for c in comments:
                author = c.get("user", {}).get("login", "unknown")
                created = c.get("created_at", "")
                body_c = self.sanitize(c.get("body", "") or "")
                preview = body_c if len(body_c) <= 1000 else body_c[:1000] + "..."
                comments_md += f"- _{author} • {created}_\n\n  {preview}\n\n"
        # split long return into multiple shorter f-strings to satisfy line-length checks
        return (
            f"{emoji} **[#{number}]({pr_url})** {title}{labels_str}\n"
            f"  _{meta}_\n"
            f"{reactions_md}"
            f"{body_line}"
            f"{comments_md}\n"
        )


# --- Exporter implementation ---
class GitHubIssuesExporter:
    """
    Fetch issues (and detect PRs) then export to markdown.

    OOP: Encapsulation (single class for export behavior), small formatter class for SRP.
    """

    def __init__(
        self,
        repo: str,
        token: str,
        output_file: str = DEFAULT_OUTPUT,
        export_format: ExportFormat = ExportFormat.SUMMARY,
        debug_pr90: bool = False,
        fetch_comments: bool = True,
    ):
        # choose repo/token from params or environment
        self.repo = repo or DEFAULT_REPO
        self.token = token or os.environ.get("GITHUB_TOKEN", "")
        self.output_file = output_file

        # allow export format override via env var or param (string or Enum)
        env_fmt = os.environ.get("EXPORT_FORMAT", "")
        if isinstance(export_format, ExportFormat):
            self.export_format = export_format
        else:
            fmt = (env_fmt or str(export_format or "")).lower()
            if fmt == "detailed" or fmt == ExportFormat.DETAILED.value:
                self.export_format = ExportFormat.DETAILED
            else:
                self.export_format = ExportFormat.SUMMARY

        self.debug_pr90 = debug_pr90 or (os.environ.get("SHOW_DEBUG_PR90") == "1")
        self.formatter = DetailedFormatter() if self.export_format == ExportFormat.DETAILED else SimpleFormatter()
        self.session = create_session_with_pooling_and_timeout()
        # Control whether per-item comments are fetched (useful to avoid extra API calls)
        self.fetch_comments_enabled = bool(fetch_comments)

        # ensure token set in headers if available
        if hasattr(self.session, "headers"):
            if self.token:
                self.session.headers.update({"Authorization": f"token {self.token}"})
            self.session.headers.update({"Accept": "application/vnd.github.v3+json"})

        # basic validation
        if "/" not in self.repo:
            raise ValueError("repo must be owner/name")

    def _issues_api_url(self) -> str:
        return f"https://api.github.com/repos/{self.repo}/issues"

    def fetch_all_items(self) -> list[dict[str, Any]]:
        """
        Fetch all items from /issues endpoint (includes PRs). Uses pagination and circuit breaker.
        Returns an empty list on network / API errors to allow graceful handling by callers/tests.
        """
        items: list[dict[str, Any]] = []
        page = 1
        while page <= MAX_PAGES:
            params = {"state": "all", "per_page": PER_PAGE, "page": page}
            try:
                resp = self.session.get(self._issues_api_url(), params=params)
                # Prefer using raise_for_status() so tests that mock raise_for_status behave correctly.
                resp.raise_for_status()
                batch = resp.json()
            except Exception as exc:
                # Network / HTTP error: be tolerant and return what we have (or empty)
                # Use a clear message but avoid exposing sensitive details.
                print(f"❌ HTTP request failed while fetching page {page}: {exc}")
                return items

            if not isinstance(batch, list) or len(batch) == 0:
                # no more pages
                break

            items.extend(batch)

            # if returned items < per_page then last page
            if len(batch) < PER_PAGE:
                break

            page += 1

        return items

    def fetch_comments(self, issue_number: int) -> list[dict[str, Any]]:
        """
        Fetch comments for a given issue/PR (paginated). Returns list of comment dicts.
        """
        comments: list[dict[str, Any]] = []
        page = 1
        url = f"https://api.github.com/repos/{self.repo}/issues/{issue_number}/comments"
        while page <= MAX_PAGES:
            params = {"per_page": PER_PAGE, "page": page}
            try:
                resp = self.session.get(url, params=params)
                resp.raise_for_status()
            except Exception:
                # don't fail the whole export on comments fetch errors
                print(f"⚠️ Warning: failed to fetch comments for #{issue_number}")
                break

            batch = resp.json()
            if not isinstance(batch, list) or not batch:
                break

            comments.extend(batch)
            if len(batch) < PER_PAGE:
                break
            page += 1

        return comments

    def classify_items(self, items: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        """
        Separate issues and pull requests.
        Returns (issues, pull_requests)
        """
        issues: list[dict[str, Any]] = []
        prs: list[dict[str, Any]] = []
        for it in items:
            if isinstance(it, dict) and "pull_request" in it:
                prs.append(it)
            else:
                issues.append(it)
        return issues, prs

    def build_markdown(self, issues: list[dict[str, Any]], prs: list[dict[str, Any]]) -> str:
        """
        Build final markdown content including PRs.
        """
        total = len(issues) + len(prs)
        open_issues = [i for i in issues if i.get("state") == "open"]
        closed_issues = [i for i in issues if i.get("state") == "closed"]
        open_prs = [p for p in prs if p.get("state") == "open"]
        closed_prs = [p for p in prs if p.get("state") != "open"]

        ts = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")
        header = (
            "# 📋 Development Backlog\n\n"
            f"Repository: {self.repo}\n\n"
            f"Exported: {ts}\n\n"
            + ("Total items fetched: " f"{total} | Issues: {len(issues)} | PRs: {len(prs)}\n\n---\n\n")
        )

        content = header

        # Attach comments and any additional remote fields to items for detailed output
        def enrich_items(list_of_items: list[dict[str, Any]]):
            for it in list_of_items:
                num = it.get("number")
                if not num:
                    continue
                # optionally fetch full comments for detail
                if self.fetch_comments_enabled:
                    try:
                        it["_comments_list"] = self.fetch_comments(num)
                    except Exception:
                        it["_comments_list"] = []
                else:
                    it["_comments_list"] = []
                # reactions may be present already; ensure safe structure
                it["_reactions"] = it.get("reactions", {}) or {}
                # ensure milestone and assignees are explicit
                it["_milestone_title"] = (it.get("milestone") or {}).get("title")
                it["_assignees"] = [a.get("login") for a in it.get("assignees", []) if isinstance(a, dict)]

        # Enrich open and closed groups
        enrich_items(open_prs)
        enrich_items(open_issues)
        enrich_items(closed_prs)
        enrich_items(closed_issues)

        # Active PRs first (visible development)
        if open_prs:
            content += self.formatter.section_header("Active Pull Requests", len(open_prs))
            for pr in sorted(open_prs, key=lambda x: x.get("number", 0), reverse=True):
                content += self.formatter.format_pr(pr)

        # Planned work (open issues)
        if open_issues:
            content += self.formatter.section_header("Open Issues", len(open_issues))
            for issue in sorted(open_issues, key=lambda x: x.get("number", 0), reverse=True):
                content += self.formatter.format_issue(issue)

        # Completed PRs and issues
        if closed_prs:
            content += self.formatter.section_header("Closed Pull Requests", len(closed_prs))
            for pr in sorted(closed_prs, key=lambda x: x.get("number", 0), reverse=True):
                content += self.formatter.format_pr(pr)

        if closed_issues:
            content += self.formatter.section_header("Closed Issues", len(closed_issues))
            for issue in sorted(closed_issues, key=lambda x: x.get("number", 0), reverse=True):
                content += self.formatter.format_issue(issue)

        return content

    def export(self) -> bool:
        """
        Full export flow with visible diagnostics.
        """
        print(f"🚀 Starting export for {self.repo}...")
        items = self.fetch_all_items()
        print(f"📡 Fetched {len(items)} total items from GitHub API")
        if not items:
            print("❌ No items returned from API")
            return False

        issues, prs = self.classify_items(items)
        print(f"📋 Classified: {len(issues)} issues, {len(prs)} pull requests (total {len(items)})")

        # debug: check for #90 explicitly (only if enabled)
        if self.debug_pr90:
            found90 = next((it for it in items if it.get("number") == 90), None)
            if found90:
                typ = "PR" if "pull_request" in found90 else "Issue"
                print(f"🔍 Found #90 as {typ}: {found90.get('title', '(no title)')}")
                print(f"   URL: {found90.get('html_url')}")

        md = self.build_markdown(issues, prs)

        # Diagnostic: show resolved output path before writing
        print(f"🔧 Diagnostic: resolved output file -> {self.output_file!r}")
        # Show absolute path for clarity
        try:
            import pathlib

            print(f"🔧 Diagnostic: absolute path -> {pathlib.Path(self.output_file).resolve()!s}")
        except Exception:
            pass

        # ensure output dir exists
        out_dir = os.path.dirname(self.output_file) or "."
        try:
            os.makedirs(out_dir, exist_ok=True)
            with open(self.output_file, "w", encoding="utf-8") as fh:
                fh.write(md)
            print(f"✅ Exported to {self.output_file}")
            # hint to open in editor (non-blocking)
            print(f"🔍 Open: code {self.output_file}    (or use your preferred editor)")
            return True
        except Exception as e:
            print(f"❌ Failed to write output: {e}")
            return False


# --- CLI entrypoint ---
def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    # Diagnostic: show CLI args as seen by the module
    print(f"🔧 Diagnostic: main called with argv = {argv!r}")
    repo = os.environ.get("GITHUB_REPO", DEFAULT_REPO)
    token = os.environ.get("GITHUB_TOKEN", "")
    out = DEFAULT_OUTPUT
    fmt_flag = None
    debug_pr90 = False
    fetch_comments_flag = True

    # simple CLI flags: --repo owner/name --out file --format/-f detailed --debug-pr90
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in ("--repo", "-r") and i + 1 < len(argv):
            repo = argv[i + 1]
            i += 2
            continue
        if a in ("--out", "-o") and i + 1 < len(argv):
            out = argv[i + 1]
            i += 2
            continue
        if a in ("--format", "-f") and i + 1 < len(argv):
            fmt_flag = argv[i + 1]
            i += 2
            continue
        if a == "--debug-pr90":
            debug_pr90 = True
            i += 1
            continue
        if a == "--no-comments":
            fetch_comments_flag = False
            i += 1
            continue
        i += 1

    # determine export format enum
    export_fmt = (
        ExportFormat.DETAILED
        if (fmt_flag or os.environ.get("EXPORT_FORMAT", "")).lower() == "detailed"
        else ExportFormat.SUMMARY
    )

    exporter = GitHubIssuesExporter(
        repo=repo,
        token=token,
        output_file=out,
        export_format=export_fmt,
        debug_pr90=debug_pr90,
        fetch_comments=fetch_comments_flag,
    )
    success = exporter.export()
    return 0 if success else 2


# Ensure module run as script or with -m executes the CLI
if __name__ == "__main__":
    raise SystemExit(main())
