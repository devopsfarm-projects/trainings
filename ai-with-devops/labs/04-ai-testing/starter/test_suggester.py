#!/usr/bin/env python3
"""Starter test suggester that uses the mock LLM to return test names/skeletons."""
from ...shared import mock_llm


def suggest_tests(function_code: str) -> str:
    prompt = f"Suggest unit test names and short skeletons for the following function:\n\n{function_code}\n\nReturn bullets."
    return mock_llm.generate(prompt)["text"]


if __name__ == "__main__":
    sample = "def add(a, b):\n    return a + b\n"
    print(suggest_tests(sample))
