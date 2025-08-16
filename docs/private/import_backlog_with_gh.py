#!/usr/bin/env python3
import argparse, csv, json, subprocess, tempfile, sys, os

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def issue_exists(owner, repo, title):
    q = f'title:"{title}"'
    r = run([
        "gh","issue","list","-R",f"{owner}/{repo}",
        "--state","all","--limit","1","--search",q,"--json","number"
    ])
    if r.returncode != 0:
        print("WARN: gh search failed:", r.stderr.strip(), file=sys.stderr)
        return False
    try:
        arr = json.loads(r.stdout or "[]")
        return bool(arr)
    except json.JSONDecodeError:
        return False

def create_issue(owner, repo, title, body, labels, milestone):
    # write body to a temp file so quoting is safe
    with tempfile.NamedTemporaryFile("w+", delete=False) as tf:
        tf.write(body)
        tf.flush()
        base = ["gh","issue","create","-R",f"{owner}/{repo}","-t",title,"-F",tf.name]
        for lab in labels:
            base += ["-l", lab]
        if milestone:
            base += ["-m", milestone]
        r = run(base)
    if r.returncode == 0:
        print(f"CREATED: {title}")
        return True
    # Retry without labels/milestone if they don't exist yet
    print(f"WARN: create with labels/milestone failed: {r.stderr.strip()}\nRetrying without labels/milestone…")
    r2 = run(["gh","issue","create","-R",f"{owner}/{repo}","-t",title,"-F",tf.name])
    if r2.returncode == 0:
        print(f"CREATED (no labels/milestone): {title}")
        return True
    print(f"ERROR creating {title}: {r2.stderr.strip()}", file=sys.stderr)
    return False

def main():
    ap = argparse.ArgumentParser(description="Import backlog issues via GitHub CLI (gh).")
    ap.add_argument("--owner", "-o", default=os.environ.get("OWNER"), required=False)
    ap.add_argument("--repo", "-r", default=os.environ.get("REPO"), required=False)
    ap.add_argument("--csv", default="issues_with_backlog_ids.csv")
    args = ap.parse_args()
    if not args.owner or not args.repo:
        print("Set --owner and --repo (or export OWNER/REPO).", file=sys.stderr)
        sys.exit(2)

    # quick auth/repo sanity
    rv = run(["gh","repo","view",f"{args.owner}/{args.repo}","--json","hasIssuesEnabled","-q",".hasIssuesEnabled"])
    if rv.returncode != 0 or rv.stdout.strip() != "true":
        print("ERROR: Repo not found or Issues disabled. Enable Issues in Settings, then retry.", file=sys.stderr)
        sys.exit(2)

    with open(args.csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row["title"].strip()
            if issue_exists(args.owner, args.repo, title):
                print(f"SKIP (exists): {title}")
                continue
            labels = [l.strip() for l in (row.get("labels") or "").split(",") if l.strip()]
            milestone = (row.get("milestone") or "").strip()
            body = row["body"]
            create_issue(args.owner, args.repo, title, body, labels, milestone)
    print("Done.")

if __name__ == "__main__":
    main()
