#!/usr/bin/env python3
"""Entry point for the PR commenter demo action.

Behavior:
- If `GITHUB_TOKEN` is not set, the script prints the comment it would post and exits 0.
- If `GITHUB_TOKEN` is set and `GITHUB_EVENT_PATH` points to a pull_request event, it will POST
  the comment to the PR via the GitHub API using the Issues Comments endpoint.

This file is safe for classroom demos: it will not attempt network calls without a token.
"""
import os
import sys
import json
from pathlib import Path

import requests


def read_comment_from_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return ""
    return p.read_text()


def read_comment_from_stdin() -> str:
    if sys.stdin.isatty():
        return ""
    return sys.stdin.read()


def get_pr_number_from_event(event_path: str):
    try:
        data = json.loads(Path(event_path).read_text())
    except Exception:
        return None
    # try pull_request then issue
    pr = data.get("pull_request") or data.get("issue")
    if pr and isinstance(pr, dict):
        return pr.get("number")
    return None


def post_comment(repo: str, pr_number: int, comment: str, token: str):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "ai-with-devops-course-demo",
    }
    resp = requests.post(url, json={"body": comment}, headers=headers, timeout=15)
    return resp


def main(argv):
    comment = ""
    if len(argv) > 1 and argv[1]:
        comment = read_comment_from_file(argv[1])
    if not comment:
        comment = read_comment_from_stdin()
    if not comment:
        print("No comment provided (use comment-file input or pipe content). Exiting.")
        return 0

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("[demo] GITHUB_TOKEN not set — would post the following comment to the PR:")
        print("---")
        print(comment)
        print("---")
        return 0

    repo = os.environ.get("GITHUB_REPOSITORY")
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not repo or not event_path:
        print("GITHUB_REPOSITORY or GITHUB_EVENT_PATH missing; cannot determine PR. Exiting.")
        return 2

    pr_number = get_pr_number_from_event(event_path)
    if not pr_number:
        print("Could not find pull request number in event payload. Exiting.")
        return 2

    try:
        resp = post_comment(repo, pr_number, comment, token)
    except Exception as e:
        print(f"Network error posting comment: {e}")
        return 2

    if resp.status_code >= 200 and resp.status_code < 300:
        print(f"Posted comment to {repo}#{pr_number} (status {resp.status_code})")
        return 0
    else:
        print(f"Failed to post comment: {resp.status_code} {resp.text}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
