import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "token-saver"


class PluginManifestTest(unittest.TestCase):
    def load_json(self, path: Path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_all_plugin_versions_match(self):
        codex = self.load_json(PLUGIN / ".codex-plugin" / "plugin.json")
        claude = self.load_json(PLUGIN / ".claude-plugin" / "plugin.json")
        portable = self.load_json(PLUGIN / "plugin.json")

        self.assertEqual(codex["name"], "token-saver")
        self.assertEqual(claude["name"], "token-saver")
        self.assertEqual(portable["name"], "token-saver")
        self.assertEqual(codex["version"], claude["version"])
        self.assertEqual(codex["version"], portable["version"])

    def test_claude_marketplace_points_to_shared_plugin(self):
        marketplace = self.load_json(ROOT / ".claude-plugin" / "marketplace.json")
        entry = marketplace["plugins"][0]
        manifest = self.load_json(PLUGIN / ".claude-plugin" / "plugin.json")

        self.assertEqual(marketplace["name"], "token-saver")
        self.assertEqual(entry["name"], manifest["name"])
        self.assertEqual(entry["version"], manifest["version"])
        self.assertEqual(entry["source"], "./plugins/token-saver")

    def test_cursor_and_copilot_marketplaces_match_portable_plugin(self):
        portable = self.load_json(PLUGIN / "plugin.json")
        manifests = [
            ROOT / ".cursor-plugin" / "marketplace.json",
            ROOT / ".github" / "plugin" / "marketplace.json",
        ]

        for path in manifests:
            with self.subTest(path=path):
                marketplace = self.load_json(path)
                entry = marketplace["plugins"][0]
                self.assertEqual(entry["name"], portable["name"])
                self.assertEqual(entry["version"], portable["version"])
                self.assertEqual(entry["source"], "./plugins/token-saver")

    def test_repomix_wrapper_supports_both_hosts(self):
        wrapper = (PLUGIN / "scripts" / "run-repomix.sh").read_text(
            encoding="utf-8"
        )

        self.assertIn("CLAUDE_PLUGIN_DATA", wrapper)
        self.assertIn("COPILOT_PLUGIN_DATA", wrapper)
        self.assertIn("PLUGIN_DATA", wrapper)

    def test_output_contract_is_reachable_from_umbrella_skill(self):
        skill = (PLUGIN / "skills" / "token-saver" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        contract = (
            PLUGIN / "skills" / "token-saver" / "references" / "output-contract.md"
        ).read_text(encoding="utf-8")

        self.assertIn("references/output-contract.md", skill)
        self.assertIn("Fast Pass has no branded opening and no receipt", contract)
        self.assertIn("Never print `unavailable`", contract)


if __name__ == "__main__":
    unittest.main()
