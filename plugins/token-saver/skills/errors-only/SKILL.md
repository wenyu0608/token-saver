---
name: errors-only
description: Run a noisy build, test, lint, or log command while keeping full output on disk and returning only actionable failures. Use for commands expected to produce large repetitive output; do not use when exact full stdout is the requested artifact.
---

# Errors Only

Keep raw output out of the model context.

1. Resolve the exact command from the user or project configuration. Do not invent flags that change test coverage or behavior.
2. Run `scripts/run-errors-only.sh -- <command> [args...]`. The script stores the complete log in a temporary file and prints a bounded diagnostic view.
3. Report the exit code, log path, first actionable error, and failing test or target. Read more from the saved log only when the bounded view is insufficient.
4. Preserve the full log until the current debugging task finishes. Do not commit it.

Do not pipe a command directly through `head`, `grep`, or `tail`: that can hide the real exit status or terminate the producer early. The wrapper captures first, filters second, and returns the original command status.
