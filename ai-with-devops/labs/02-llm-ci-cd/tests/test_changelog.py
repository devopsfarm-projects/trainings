from pathlib import Path
import sys

# Add ai-with-devops root to sys.path so tests can import shared modules when
# pytest collects them from a nested folder.
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from shared import mock_llm


def test_mock_changelog_contains_bullet():
    commits = "feat: add login\nfix: payments bug\n"
    prompt = f"Generate a short changelog from the following commits:\n\n{commits}\n\nFormat as markdown with bullet points."
    resp = mock_llm.generate(prompt)["text"]
    assert "-" in resp or "*" in resp
