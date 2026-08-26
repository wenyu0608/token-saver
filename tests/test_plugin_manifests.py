import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "token-saver"


class PluginManifestTest(unittest.TestCase):
    def load_json(self, path: Path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_codex_and_claude_versions_match(self):
        codex = self.load_json(PLUGIN / ".codex-plugin" / "plugin.json")
        claude = self.load_json(PLUGIN / ".claude-plugin" / "plugin.json")

        self.assertEqual(codex["name"], "token-saver")
        self.assertEqual(claude["name"], "token-saver")
        self.assertEqual(codex["version"], claude["version"])

    def test_claude_marketplace_points_to_shared_plugin(self):
        marketplace = self.load_json(ROOT / ".claude-plugin" / "marketplace.json")
        entry = marketplace["plugins"][0]
        manifest = self.load_json(PLUGIN / ".claude-plugin" / "plugin.json")

        self.assertEqual(marketplace["name"], "token-saver")
        self.assertEqual(entry["name"], manifest["name"])
        self.assertEqual(entry["version"], manifest["version"])
        self.assertEqual(entry["source"], "./plugins/token-saver")

    def test_repomix_wrapper_supports_both_hosts(self):
        wrapper = (PLUGIN / "scripts" / "run-repomix.sh").read_text(
            encoding="utf-8"
        )

        self.assertIn("CLAUDE_PLUGIN_DATA", wrapper)
        self.assertIn("PLUGIN_DATA", wrapper)


if __name__ == "__main__":
    unittest.main()
