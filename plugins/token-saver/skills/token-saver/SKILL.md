---
name: token-saver
description: Save context for repositories, noisy output, long documents, or session history. Fast-pass short questions when optimization costs more than it saves.
---

# Token Saver

Decide first without reading any reference:

- **Fast Pass:** If the prompt and current short context are enough, do not read references or child skills. Answer normally with `⚡ Token Saver｜Fast Pass：轻任务，跳过优化器` and end with `Token Saver 账单｜本轮未启用压缩｜入口开销约 250 tokens`.
- **Optimize:** If work requires a repository, diff, noisy command, long document, or long-session handoff, read [the router](references/router.md), use only the selected method, then read [the receipt rules](references/receipt.md) after comparable artifacts exist.

Never load Router or Receipt merely to answer a savings question about a short task. Never claim access to hidden harness usage. Lead with the result; number multi-step work; keep lists to five items.
