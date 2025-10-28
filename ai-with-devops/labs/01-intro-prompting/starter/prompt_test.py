#!/usr/bin/env python3
"""Starter script to exercise prompt design against a mock LLM.

Run it with: python starter/prompt_test.py
"""
import os
from pathlib import Path

try:
    # prefer a real client if available (not required)
    import openai  # type: ignore
    HAVE_OPENAI = True
except Exception:
    HAVE_OPENAI = False

from ...shared import mock_llm  # relative import when used as package


def get_response(prompt: str) -> str:
    if HAVE_OPENAI and os.environ.get("OPENAI_API_KEY"):
        # A minimal, optional path — instructor can extend this.
        resp = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
        return resp.choices[0].text
    # fallback to mock
    return mock_llm.generate(prompt)["text"]


def main():
    p = Path(__file__).resolve().parents[2]
    print("[lab01] Running prompt_test — using mock LLM if no key set")
    prompt = (
        "You are a helpful assistant. Explain in one sentence how to create a user in a PostgreSQL DB. "
        "Keep the response short and do not include private keys or emails."
    )
    out = get_response(prompt)
    print("--- LLM OUTPUT ---")
    print(out)


if __name__ == "__main__":
    main()
