#!/usr/bin/env python3
"""Generate a changelog from commit messages using the mock LLM.

Usage:
  python starter/changelog_gen.py commits.txt

This script is intentionally simple -- it's a starting point for students to
replace the mock with a real LLM call and add guardrails.
"""
import sys
from pathlib import Path

from ...shared import mock_llm


def read_commits(path: Path) -> str:
    return path.read_text()


def build_prompt(commits_text: str) -> str:
    return f"Generate a short changelog from the following commits:\n\n{commits_text}\n\nFormat as markdown with bullet points."


def main():
    if len(sys.argv) < 2:
        print("Usage: python starter/changelog_gen.py commits.txt")
        raise SystemExit(2)
    commits = read_commits(Path(sys.argv[1]))
    prompt = build_prompt(commits)
    resp = mock_llm.generate(prompt)["text"]
    changelog = "# Changelog\n\n" + resp
    out = Path("generated_CHANGELOG.md")
    out.write_text(changelog)
    print(f"Wrote {out.resolve()}")


if __name__ == "__main__":
    main()
