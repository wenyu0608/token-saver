# Router

Choose from observable task signals. Do not load every child skill merely because it is installed.

This reference is the heavy-task path. If no large context candidate will be opened, return to `Fast Pass` without loading a child skill. Choose fidelity before optimization; fidelity requirements override token savings.

## Fidelity gate

Use `Focused` for discovery, triage, repository orientation, and locating likely causes. Use
`Full Fidelity` when the user requests exhaustive, line-by-line, exact, audit-grade, or no-omission
review, or when missing evidence could materially change a security, permissions, payment, data-loss,
migration, protocol, serialization, numerical, concurrency, timing, flaky-test, or resource-lifecycle
decision.

Start focused debugging only for triage. Escalate to `Full Fidelity` when any of these occurs:

- the suspected cause crosses file, service, process, state, or time boundaries;
- a filtered pass is inconclusive or required evidence is absent;
- warnings, setup/teardown, ordering, or environment differences may be causal;
- the user asks to verify the fix or explicitly requests complete inspection.

In `Full Fidelity`, keep every in-scope source artifact retrievable and inspect all evidence required
by the task. Compress only navigation, indexes, repeated copies, and presentation—not unique evidence.
If the complete evidence itself enters model context, do not claim that it was saved.

| Signal | Method | Initial context |
| --- | --- | --- |
| Changed code, PR, regression | `diff-context` | Status, diff stat, bounded hunks, direct dependencies |
| Unfamiliar repository or broad architecture question | `repomix` | Compressed repo map, then requested files |
| Noisy test, build, lint, or logs | `errors-only` | Exit status, bounded failures, retained raw log |
| Focused question over large docs | `docs-slice` | Up to five ranked sections |
| Long session about to continue elsewhere | `session-handoff` | Verified 500–1,500 token brief |
| Context-cost investigation | `token-audit` | Observable instructions and injected artifacts |
| Exhaustive or high-risk review | `full-fidelity` | Complete in-scope evidence plus a compact navigation index |

The Repomix skill and pinned wrapper are bundled. The wrapper prefers a compatible local CLI and can retrieve its pinned npm runtime only after explicit authorization. For an unfamiliar repository, prefer a repo map over dumping all source files. If neither a local CLI nor an authorized download is available, use `rg --files`, targeted symbol search, and bounded reads.

Common combinations:

- Code fix: `diff-context + errors-only`.
- Repository explanation: `repomix + docs-slice`.
- Debug triage: `errors-only + diff-context`; escalate to `full-fidelity` before verification when a gate condition applies.
- Optimization review: `token-audit` followed by only the highest-impact applicable method.

Do not route ordinary short questions through an optimizer when its instructions or tool schema would cost more context than it removes.

## Before filtering

Record the candidate scope without sending it to the model. For local material, run
`scripts/capture_candidate.py --label baseline --text <path> [--image-pages N]` and retain the
JSON result. After selecting or compressing content, capture the optimized scope the same way.
Inventory collection may inspect file sizes and page counts, but must not duplicate the model
request or read excluded content into the conversation.
