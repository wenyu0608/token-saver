---
name: session-handoff
description: Produce a compact, evidence-backed continuation brief for a fresh coding-agent task. Use before ending or replacing a long session; do not use as a substitute for completing a short active task.
---

# Session Handoff

Create a handoff that can replace stale conversation history.

1. Re-read the current user objective, `git status --short`, and the smallest relevant diff. Do not rely only on memory.
2. Write a compact Markdown brief with exactly these sections: `Goal`, `Verified state`, `Changes`, `Failed attempts`, and `Next action`.
3. Include exact file paths, commands, exit codes, and unresolved decisions. Omit narration, obsolete hypotheses, successful read-only commands, and intermediate reasoning.
4. Mark every unverified claim explicitly. Never convert an assumption into a fact during compression.
5. Save the brief only when the user requests a file; otherwise return it in chat. A future task must validate it against current Git state before acting.

Target 500–1,500 tokens. Preserve safety constraints and the user's acceptance criteria even when this exceeds the target.
