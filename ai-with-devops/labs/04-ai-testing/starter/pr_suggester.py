#!/usr/bin/env python3
"""Starter script used by CI example to suggest tests for a PR.

This script is intentionally simple and prints the suggested comment text to
stdout. In a real Action you would use the GitHub API to post a comment on the PR.
"""
import sys
from pathlib import Path

from ...shared import mock_llm


def suggest_tests_from_diff(diff_text: str) -> str:
    prompt = (
        "You are a test-writing assistant. Suggest unit test names and short skeletons "
        "based on the following diff or changed file contents:\n\n" + diff_text + "\n\nReturn as bullet points."
    )
    return mock_llm.generate(prompt)["text"]


def main():
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        if path.exists():
            diff_text = path.read_text()
        else:
            diff_text = ""
    else:
        # read from stdin
        diff_text = sys.stdin.read()

    comment = suggest_tests_from_diff(diff_text)
    print("--- SUGGESTED TESTS (comment body) ---")
    print(comment)


if __name__ == "__main__":
    main()
