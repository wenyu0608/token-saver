---
name: token-audit
description: Measure avoidable coding-agent input context from instruction files, installed skills, tool configuration, generated artifacts, and likely noisy outputs. Use when context limits, latency, or token cost are a concern; do not use for authentication tokens.
---

# Token Audit

Measure before recommending changes.

1. Run `python3 scripts/audit_context.py [project-root]`.
2. Separate fixed overhead from task-dependent context. Fixed overhead includes `AGENTS.md`, skill entrypoints, and tool configuration; task-dependent context includes file reads, logs, diffs, web pages, and conversation history.
3. Rank at most five avoidable sources by estimated impact. Label byte-derived token counts as estimates; do not claim access to hidden harness token accounting.
4. Recommend the smallest reversible change first. Never delete or rewrite user configuration without explicit permission.
5. Re-measure observable files after an approved change and report before/after estimates.

Ignore dependency trees and generated directories unless they are being injected into context. A large file on disk costs no model tokens until the harness includes it.
