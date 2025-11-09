#!/usr/bin/env python3
"""Starter incident summarizer that uses the mock LLM to create a summary and runbook draft.

Usage:
  python starter/summarizer.py starter/sample_alerts/alert1.json

This script is safe for classroom demos (uses `shared/mock_llm.py`).
"""
import sys
from pathlib import Path

# allow running the script directly by adding the repo root to sys.path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from shared import mock_llm


def read_alert(path: Path) -> str:
    return path.read_text()


def build_prompt(alert_text: str) -> str:
    return (
        "Summarize the following incident alert and propose triage steps. "
        "Include a short runbook draft and a confidence note.\n\n" + alert_text
    )


def main():
    if len(sys.argv) < 2:
        print("Usage: python starter/summarizer.py starter/sample_alerts/alert1.json")
        raise SystemExit(2)
    path = Path(sys.argv[1])
    alert = read_alert(path)
    prompt = build_prompt(alert)
    resp = mock_llm.generate(prompt)["text"]
    out = Path("generated_incident_summary.txt")
    out.write_text(resp)
    print(f"Wrote {out.resolve()}")


if __name__ == "__main__":
    main()
