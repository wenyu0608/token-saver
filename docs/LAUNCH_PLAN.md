# Phase 1 Launch Plan

## Objective

Recruit 20–50 relevant Alpha users and learn whether they voluntarily use Token Saver a second and
third time. Reach is secondary to qualified installs, completed first tasks, and repeat usage.

## Audience

- Developers using Codex, Cursor, or Claude Code on large repositories, logs, and documents.
- AI coding power users who notice context-window or token-cost problems.
- Small engineering teams experimenting with agent workflows.

## Positioning

Lead with the problem and the safety boundary:

> AI coding agents often load too much context—or remove too much when they try to save tokens.
> Token Saver routes each task through the smallest safe workflow, and switches to Full Fidelity
> when omissions could change the answer.

Avoid claiming an average savings percentage. Use only the reproducible DreamZero benchmark and
label it as one measured case, not expected user performance.

## Seven-day launch sequence

- **Day 1 — Founder story:** Explain the short-question overhead feedback that changed Fast Pass.
- **Day 2 — Product demo:** Show one prompt, selected workflow, focused context, and honest receipt.
- **Day 3 — Safety story:** Explain why debugging can escalate from Focused to Full Fidelity.
- **Day 4 — Reproducible proof:** Publish the DreamZero method, commit, scope, and calculation.
- **Day 5 — Build in public:** Share the first user feedback and the specific product correction.
- **Day 6 — Comparison:** Contrast raw context dumping, lossy summarization, and Token Saver routing.
- **Day 7 — Feedback call:** Ask users to install, run one real task, and report where routing failed.

Cross-post the same core story with platform-native edits:

- X: concise hook, visual/demo, repository link, one direct feedback request.
- LinkedIn: founder lesson, problem framing, evidence, and a professional use case.
- Reddit/Hacker News: technical design, reproducibility, limitations, and open questions; avoid ad copy.
- Chinese channels: bilingual launch notes for V2EX, 即刻, 小红书, and relevant developer groups.

## Launch kit checklist

- [ ] One 30–60 second screen recording of install → task → receipt.
- [ ] One architecture graphic: task → fidelity gate → focused/full workflow → model.
- [ ] X launch post and a four-post technical thread.
- [ ] LinkedIn and Chinese-language adaptations.
- [ ] GitHub issue/discussion template for routing failures and false savings claims.
- [ ] Lightweight feedback form covering install success, task type, repeat intent, and trust.

## Metrics

- Qualified repository visits and installation attempts.
- Successful first task.
- Second use within seven days (primary signal).
- Routing correction rate and Full Fidelity escalation rate from manual feedback.
- Users willing to join a Founding Pro interview.

Do not optimize for impressions alone. Do not add network telemetry during Phase 1; collect feedback
manually and keep the deferred telemetry plan in `ROADMAP.md`.
