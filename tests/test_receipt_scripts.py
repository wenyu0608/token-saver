from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
SCRIPTS = ROOT / "plugins" / "token-saver" / "scripts"


class ReceiptScriptsTest(unittest.TestCase):
    def test_mixed_content_receipt_keeps_images_separate(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            full = temp / "full.txt"
            sliced = temp / "sliced.txt"
            full.write_text("a" * 4000, encoding="utf-8")
            sliced.write_text("b" * 400, encoding="utf-8")
            manifests = []
            for label, source, pages in (("baseline", full, 12), ("optimized", sliced, 3)):
                manifest = temp / f"{label}.json"
                subprocess.run(
                    [sys.executable, SCRIPTS / "capture_candidate.py", "--label", label,
                     "--text", source, "--image-pages", str(pages), "--output", manifest],
                    check=True,
                )
                manifests.append(manifest)

            completed = subprocess.run(
                [sys.executable, SCRIPTS / "estimate_receipt.py", "--method", "docs-slice",
                 "--baseline-manifest", manifests[0], "--optimized-manifest", manifests[1], "--json"],
                check=True, capture_output=True, text=True,
            )
            receipt = json.loads(completed.stdout)
            self.assertEqual(receipt["baseline_input_tokens"], 1000)
            self.assertEqual(receipt["optimized_input_tokens"], 100)
            self.assertEqual(receipt["baseline_image_pages"], 12)
            self.assertEqual(receipt["optimized_image_pages"], 3)
            self.assertEqual(receipt["image_pages_saved_percent"], 75.0)

    def test_missing_baseline_stays_observed_only(self) -> None:
        completed = subprocess.run(
            [sys.executable, SCRIPTS / "estimate_receipt.py", "--method", "docs-slice", "--json"],
            check=True, capture_output=True, text=True,
        )
        self.assertEqual(json.loads(completed.stdout)["measurement"], "observed-only")

    def test_missing_baseline_uses_canonical_footer(self) -> None:
        completed = subprocess.run(
            [sys.executable, SCRIPTS / "estimate_receipt.py", "--method", "docs-slice"],
            check=True, capture_output=True, text=True,
        )
        self.assertEqual(
            completed.stdout.strip(),
            "Token Saver 账单｜已处理约 0 tokens｜未记录可比基线，不估算节省",
        )

    def test_estimated_footer_reports_net_saving(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            baseline = temp / "baseline.txt"
            optimized = temp / "optimized.txt"
            baseline.write_text("a" * 4000, encoding="utf-8")
            optimized.write_text("b" * 400, encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, SCRIPTS / "estimate_receipt.py", "--method", "docs-slice",
                 "--baseline", baseline, "--optimized", optimized],
                check=True, capture_output=True, text=True,
            )
            self.assertEqual(
                completed.stdout.strip(),
                "Token Saver 账单｜文本候选约 1,000 → 100 tokens｜估算净节省约 900（90.0%）",
            )

    def test_full_fidelity_only_claims_navigation_savings(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            baseline = temp / "baseline.txt"
            optimized = temp / "optimized.txt"
            baseline.write_text("n" * 4000, encoding="utf-8")
            optimized.write_text("i" * 400, encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, SCRIPTS / "estimate_receipt.py", "--method", "full-fidelity",
                 "--baseline", baseline, "--optimized", optimized, "--fidelity-mode", "full"],
                check=True, capture_output=True, text=True,
            )
            self.assertIn("完整证据已保留", completed.stdout)
            self.assertIn("导航上下文约 1,000 → 100 tokens", completed.stdout)

    def test_full_fidelity_without_baseline_makes_no_savings_claim(self) -> None:
        completed = subprocess.run(
            [sys.executable, SCRIPTS / "estimate_receipt.py", "--method", "full-fidelity",
             "--fidelity-mode", "full"],
            check=True, capture_output=True, text=True,
        )
        self.assertEqual(
            completed.stdout.strip(),
            "Token Saver 账单｜完整证据已保留｜本轮不主张 token 节省",
        )


if __name__ == "__main__":
    unittest.main()
