#!/usr/bin/env python3
"""Simple validator to reject outputs containing URLs, emails, or private-key markers."""
import re
from typing import Tuple


URL_RE = re.compile(r"https?://|www\.")
EMAIL_RE = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
KEYWORDS = ["-----BEGIN PRIVATE KEY-----", "ssh-rsa", "aws_secret_access_key", "api_key"]


def validate(text: str) -> Tuple[bool, str]:
    if URL_RE.search(text):
        return False, "Contains URL"
    if EMAIL_RE.search(text):
        return False, "Contains email"
    for k in KEYWORDS:
        if k in text:
            return False, f"Contains key-like token: {k}"
    return True, "OK"


if __name__ == "__main__":
    import sys

    data = sys.stdin.read() if not sys.stdin.isatty() else ""
    if not data:
        print("Usage: echo 'text' | python tests/validator.py")
        raise SystemExit(2)
    ok, reason = validate(data)
    print(ok, reason)
