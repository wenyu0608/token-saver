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


if __name__ == "__main__":
    unittest.main()
