# Token Saver

An umbrella router for reducing avoidable coding-agent context without hiding the evidence needed to do the work.

Token Saver selects a focused workflow for each task, explains the choice naturally, and ends with an honest `exact`, `estimated`, or `unavailable` token receipt.

## Skills

- `$token-saver` automatically routes the task and produces a token receipt.
- `$repomix` builds a compressed map before exploring an unfamiliar repository.
- `$token-audit` measures observable context overhead and ranks fixes.
- `$errors-only` captures full command output locally and returns bounded failures.
- `$diff-context` starts from changed lines and expands only along justified dependencies.
- `$session-handoff` replaces stale chat history with a verified continuation brief.
- `$docs-slice` retrieves bounded, relevant documentation sections.

The umbrella `$token-saver` skill supports automatic selection. The six specialist skills remain explicit so their instructions are not injected into unrelated prompts. The Repomix skill is bundled; its `repomix` CLI is still an external dependency and is never installed silently.

## Install

```bash
codex plugin marketplace add wenyu0608/token-saver --ref main
codex plugin add token-saver@token-saver
```

Restart Codex, then invoke a skill such as:

```text
$token-saver diagnose the failing test without dumping the full build log
```

## Design

Token Saver optimizes context before it reaches the model. It favors selection over lossy compression, keeps raw diagnostic output locally retrievable, and never edits user configuration without permission.

See [the MVP contract](docs/MVP.md) for routing, measurement levels, and the baseline model.

## License

MIT
