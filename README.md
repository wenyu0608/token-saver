# token-saver

Five explicit Codex skills for reducing avoidable input context without hiding the evidence needed to do the work.

## Skills

- `$token-audit` measures observable context overhead and ranks fixes.
- `$errors-only` captures full command output locally and returns bounded failures.
- `$diff-context` starts from changed lines and expands only along justified dependencies.
- `$session-handoff` replaces stale chat history with a verified continuation brief.
- `$docs-slice` retrieves bounded, relevant documentation sections.

All skills require explicit invocation. Installing the plugin does not add them to every prompt automatically.

## Install

```bash
codex plugin marketplace add cocolwy/token-saver --ref main
codex plugin add token-saver@token-saver
```

Restart Codex, then invoke a skill such as:

```text
$errors-only run the test suite and show the first actionable failure
```

## Design

Token Saver optimizes context before it reaches the model. It favors selection over lossy compression, keeps raw diagnostic output locally retrievable, and never edits user configuration without permission.

## License

MIT
