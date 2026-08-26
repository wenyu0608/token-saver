# Social Launch Copy

Release: <https://github.com/wenyu0608/token-saver/releases/tag/v0.3.2-alpha.4>

## X launch thread

### 1/7

I built an open-source tool to save tokens in AI coding agents.

Then an early user found a one-line question where the “optimizer” added ~1.2K tokens instead.

That feedback changed the product.

Introducing Token Saver v0.3.2 Alpha 4 🧵

### 2/7

Most context tools make one bet: compress more.

But different tasks need different treatment:

- Short question → no optimizer
- Large repo or logs → focused context
- Exact debugging or audits → no evidence loss

Token Saver chooses before it compresses.

### 3/7

Token Saver now has three paths:

⚡ Fast Pass — stays out of simple tasks

🎯 Focused — reduces large repos, logs, diffs, and docs

🔍 Full Fidelity — preserves complete evidence when omissions could change the answer

Saving tokens never overrides correctness.

### 4/7

The open-source bundle includes:

- Repomix
- Diff Context
- Errors Only
- Docs Slice
- Session Handoff
- Token Audit

One router selects the smallest useful workflow instead of loading every optimization method.

### 5/7

The receipt matters as much as the compression.

Token Saver labels measurements as exact, estimated, or observed-only. It separates text from visual pages and refuses to invent savings when no comparable baseline exists.

No “trust me, we saved 90%” metrics.

### 6/7

One reproducible case: DreamZero.

Candidate context went from 379,765 to 57,098 estimated tokens—a measured 85% reduction for that specific commit and scope.

It is a reproducible case study, not a promise that every task saves 85%.

### 7/7

Token Saver is open source, local-first, and still Alpha.

I’m looking for 20–50 developers to try it on one real task—large repos, noisy logs, long docs, or difficult debugging—and tell me where the router gets it wrong.

Try it: https://github.com/wenyu0608/token-saver

## LinkedIn launch post

Token Saver is an open-source context router for AI coding agents—and its first important feature
came from discovering that the optimizer itself could waste tokens.

I originally built it to combine several context-saving techniques: repository compression,
focused diffs, error-only logs, document slicing, and session handoffs.

Then an early user tried it on a one-line question.

The question needed almost no context, but Token Saver loaded roughly 1,200 tokens of routing and
receipt instructions. The optimization layer cost more than it could save.

That feedback changed the product.

Token Saver now chooses one of three paths before it compresses anything:

⚡ **Fast Pass** stays out of simple tasks.

🎯 **Focused** reduces large repositories, logs, diffs, and documents to the smallest useful
context.

🔍 **Full Fidelity** preserves complete evidence for exhaustive debugging, security-sensitive
reviews, migrations, concurrency problems, flaky tests, and any task where an omission could change
the conclusion.

It also produces an honest receipt. Measurements are labeled as exact, estimated, or observed-only.
Text and visual pages are reported separately. If there is no comparable baseline, Token Saver does
not manufacture a savings percentage.

For one reproducible DreamZero case study, the candidate context went from 379,765 to 57,098
estimated tokens—an 85% reduction for that specific commit and scope. That is evidence from one
measured case, not a promise about average performance.

The project is open source, local-first, and currently at **v0.3.2 Alpha 4**.

I am looking for 20–50 developers to test it on a real task. I am especially interested in cases
where it:

- selects the wrong workflow;
- spends more context than it saves;
- removes evidence that turns out to matter; or
- correctly escalates a debugging task into Full Fidelity.

If AI coding agents are becoming part of the development stack, context should be treated as a
budget—and correctness as the constraint that budget cannot override.

Project and installation instructions:
https://github.com/wenyu0608/token-saver

#opensource #AIcoding #Codex #ContextEngineering #DeveloperTools
