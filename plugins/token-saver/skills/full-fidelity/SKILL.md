---
name: full-fidelity
description: Preserve and inspect complete in-scope evidence for exhaustive debugging, verification, audits, and high-risk correctness work. Use when omissions could change the conclusion; do not use for ordinary triage or repository orientation.
---

# Full Fidelity

Optimize navigation without removing unique evidence.

1. State the exact review boundary: files, logs, document pages, time range, commands, and environments.
2. Preserve each in-scope artifact locally. Build a compact index, but keep raw sources retrievable.
3. Inspect all evidence required by the boundary. Follow cross-file, cross-process, state, ordering, setup/teardown, and environment dependencies when relevant.
4. Record coverage and unresolved gaps. Do not describe sampling, summaries, or bounded windows as exhaustive review.
5. Attribute token savings only to navigation, deduplication, or presentation. If complete evidence entered model context, make no savings claim for that evidence.

Use `Focused` triage first only when the user did not request exhaustive review and the risk gate does
not require this mode. Switch here immediately when filtered evidence is inconclusive or potentially
causal material was omitted.
