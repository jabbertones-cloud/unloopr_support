"""Public support parity checks for the deployed seven-role suite, no network required."""
from pathlib import Path
import unittest
import re

ROOT = Path(__file__).resolve().parents[1]
SEVEN = (
    "Unloopr", "Handroll Rehab", "Lego Builder", "Overwrite Guard",
    "AgentGit", "StateLayer", "Sweepr",
)

class SupportSuiteParityTest(unittest.TestCase):
    def read(self, rel):
        return (ROOT / rel).read_text(encoding="utf-8")

    def test_all_seven_in_human_and_agent_entry_points(self):
        for rel in ("README.md", "docs/suite.md", "docs/current-product.md",
                    "llms.txt", "llms-full.txt", "docs/faq/faq.md", "SUPPORT.md"):
            with self.subTest(rel=rel):
                body = self.read(rel)
                for name in SEVEN:
                    self.assertIn(name, body)

    def test_availability_and_verifiable_release(self):
        suite = self.read("docs/suite.md")
        readme = self.read("README.md")
        llms = self.read("llms.txt")
        self.assertIn("a11974cb61e0cd23a6e85745ba05b4a017d2fad2", suite)
        self.assertIn("12798e66-480d-4ad1-a019-a4245e8014a3", suite)
        self.assertIn("November 17, 2026", suite)
        self.assertIn("HTTP 503", suite)
        self.assertIn("Internal preview", suite)
        self.assertIn("not a hosted code writer", suite)
        self.assertIn("not seven publicly available subscriptions", readme)
        self.assertIn("Only Unloopr is a free public self-service web scanner", llms)

    def test_issue_report_choices_are_truthful(self):
        for name in ("bug_report", "feature_request"):
            form = self.read(f".github/ISSUE_TEMPLATE/{name}.yml")
            for value in ("Lego Builder", "Handroll Rehab", "Overwrite Guard",
                          "StateLayer", "Sweepr", "Other / not sure"):
                self.assertIn(value, form)
            self.assertIn("secrets", form.lower())
            self.assertIn("required: false", form)

    def test_generated_full_facts_are_same_as_sources(self):
        full = self.read("llms-full.txt")
        for rel in ("README.md", "llms.txt", "docs/suite.md",
                    "docs/current-product.md", "docs/getting-started.md",
                    "docs/pricing.md", "docs/faq/faq.md"):
            body = self.read(rel).splitlines()
            content = "\n".join(body[1:]).strip()
            with self.subTest(rel=rel):
                self.assertIn(content, full)

    def test_links_targets_exist(self):
        sources = ("README.md", "docs/suite.md", "docs/current-product.md",
                   "SUPPORT.md", "llms.txt", "docs/getting-started.md",
                   "docs/pricing.md", "docs/faq/faq.md")
        checked = 0
        for rel in sources:
            body = self.read(rel)
            for target in re.findall(r"\]\(([^)]+)\)", body):
                if target.startswith(("https://", "http://", "#", "mailto:")):
                    continue
                relative = target.split("#", 1)[0].split("?", 1)[0]
                if not relative:
                    continue
                checked += 1
                with self.subTest(source=rel, target=relative):
                    self.assertTrue((ROOT / rel).parent.joinpath(relative).is_file())
        self.assertGreaterEqual(checked, 30, "Link validation must inspect real links")

if __name__ == "__main__":
    unittest.main()
