---
name: token-saver
description: Save context for repositories, noisy output, long documents, or session history. Fast-pass short questions when optimization costs more than it saves.
---

# Token Saver

Decide first without reading any reference:

- **Fast Pass:** If the prompt and current short context are enough, do not read references or child skills. Answer normally; omit Token Saver status and receipt. End only with `提示：这是简单任务，下次无需启用 Token Saver。`
- **Optimize:** If work requires a repository, diff, noisy command, long document, or long-session handoff, read [the router](references/router.md), use only the selected method, and capture a lightweight candidate inventory before filtering. Read [the receipt rules](references/receipt.md) after comparable artifacts exist.

Never load Router or Receipt merely to answer a savings question about a short task. Never claim access to hidden harness usage. Lead with the result; number multi-step work; keep lists to five items.
