# Token Saver MVP

## Product contract

Token Saver routes a task to the smallest useful context workflow, preserves access to filtered evidence, and emits an auditable receipt. Task success has priority over token reduction.

Machine-readable receipts conform to [`schema/token-receipt.schema.json`](../schema/token-receipt.schema.json). A representative router decision is in [`schema/router-decision.example.json`](../schema/router-decision.example.json).

## Pipeline

```text
task -> router -> context optimizer -> agent harness -> model
                 |                         |
                 +---- before/after meter -+

model response -> scan-friendly formatter -> user
```

The free plugin supplies routing, local optimizers, and local estimates. A future paid service can add provider-aware exact usage, cache-aware cost accounting, team policy, history, and quality monitoring.

## MVP acceptance criteria

1. Route repository, changed-code, noisy-command, documentation, and long-session tasks without loading unrelated workflows.
2. Every invocation begins with a natural one-line disclosure of the enabled method and reason.
3. Every invocation ends with an `exact`, `estimated`, or `observed-only` receipt; user-facing copy never exposes a bare “unavailable” state.
4. Filtered source material remains locally retrievable, and a failed compression can fall back to the original.
5. Benchmarks compare task success as well as net input tokens.
6. Exact and high-risk work enters `Full Fidelity`: unique evidence remains in scope, and receipts only count navigation or deduplication savings.

## Baseline capture

A baseline is the context candidate before Token Saver filters it. For example, a test command may produce a 40,000-token log; `errors-only` may pass 1,200 tokens plus 80 tokens of routing instructions. The local measurement is:

```text
baseline = full log candidate             40,000
optimized = bounded diagnostic             1,200
optimizer overhead = routing instructions     80
net saved                                  38,720
```

No duplicate model request is required. Exact measurement needs the actual serialized payload and the target tokenizer. Until agent harnesses expose that payload consistently, label file- or byte-derived measurements as estimates.

The heavy-task path captures a lightweight inventory before filtering and a second inventory after
filtering. Text is estimated independently from visual pages; image pages are never converted into
text tokens. This lets mixed-document receipts report, for example, `text 46.5K → 3.8K tokens` and
`charts 12 → 3 pages` without manufacturing a cross-modal total.

## Packaging sequence

1. Ship the Codex plugin from this repository.
2. Add a shared local CLI that installs agent-specific adapters.
3. Add Cursor rules/MCP and Claude Code plugin/hooks over the same router contract.
4. Add an opt-in cloud control plane only after local measurement is trusted.
