# Router

Choose from observable task signals. Do not load every child skill merely because it is installed.

| Signal | Method | Initial context |
| --- | --- | --- |
| Changed code, PR, regression | `diff-context` | Status, diff stat, bounded hunks, direct dependencies |
| Unfamiliar repository or broad architecture question | `repomix` when installed | Compressed repo map, then requested files |
| Noisy test, build, lint, or logs | `errors-only` | Exit status, bounded failures, retained raw log |
| Focused question over large docs | `docs-slice` | Up to five ranked sections |
| Long session about to continue elsewhere | `session-handoff` | Verified 500–1,500 token brief |
| Context-cost investigation | `token-audit` | Observable instructions and injected artifacts |

For an unfamiliar repository, prefer a repo map over dumping all source files. If Repomix is unavailable, use `rg --files`, targeted symbol search, and bounded reads; state the fallback rather than installing software without authorization.

Common combinations:

- Code fix: `diff-context + errors-only`.
- Repository explanation: `repomix + docs-slice`.
- Long debugging session: `errors-only + session-handoff`.
- Optimization review: `token-audit` followed by only the highest-impact applicable method.

Do not route ordinary short questions through an optimizer when its instructions or tool schema would cost more context than it removes.
