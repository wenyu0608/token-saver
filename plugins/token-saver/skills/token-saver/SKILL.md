---
name: token-saver
description: Route coding-agent tasks through the smallest suitable context-saving workflow, report what was enabled in natural language, and produce an honest token receipt. Use when the user asks to save tokens, reduce context, or invokes Token Saver; do not claim exact savings without a measured baseline.
---

# Token Saver

Select context before it reaches the model, then report the result without interrupting the task.

1. Classify the task and enable only the relevant methods from [the router](references/router.md). Combine methods only when each removes a distinct source of context.
2. Put one short, natural status line before the answer. Vary the wording to fit the task, for example: `本次已启用：Diff Context，先从改动定位问题。` Avoid a fixed “匹配到……” template.
3. Perform the user's task using the selected workflow. Keep raw evidence locally retrievable when filtering tool output.
4. Append a compact receipt using [the receipt rules](references/receipt.md). Report `exact`, `estimated`, or `unavailable`; never invent a counterfactual baseline.
5. Format the substantive answer for quick scanning: lead with the action or conclusion, number multi-step instructions, and keep ordinary lists to five items or fewer.

The receipt is secondary to task success. If compression hides required evidence, retrieve the original context and record the fallback as optimizer overhead.
