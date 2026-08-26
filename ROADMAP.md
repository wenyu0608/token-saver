# Token Saver Roadmap

Token Saver follows an open-core model: local safety and useful context reduction remain free;
paid products monetize automation, measurement, integrations, history, and team governance.

## Free and open source

- Umbrella router, Fast Pass, Focused, and Full Fidelity safety behavior.
- Repomix, Diff Context, Errors Only, Docs Slice, Session Handoff, and basic Token Audit.
- Local candidate capture and honest `exact`, `estimated`, or `observed-only` receipts.
- Codex, Cursor, and Claude Code installers/adapters.
- Local raw evidence retention and reproducible public benchmarks.

Safety controls must not become a paywall. Full Fidelity, truthful receipts, and local-only operation
stay free.

## Pro

Target: individual developers and power users. Candidate price after validation: USD 9–15/month.

- Provider-aware tokenizers and cache/cost-aware accounting.
- Usage history, project dashboards, trends, and savings reports.
- Adaptive routing learned from local preferences and task outcomes.
- Premium workflows for large PDFs, monorepos, CI logs, research, and long-running sessions.
- Cross-harness configuration sync and priority updates.

## Team

Target: engineering teams. Candidate price after validation: USD 20–30/user/month, with a small-team
minimum or annual plan.

- Shared routing policy, token budgets, allowlists, and Full Fidelity requirements.
- Aggregated dashboards without uploading prompts, source code, paths, or raw logs.
- CI/PR integrations, team benchmarks, quality regression checks, and administrative controls.
- Central license management and exportable cost/savings reports.

## Enterprise

- SSO/SAML, audit logs, retention controls, regional storage, and support SLA.
- Self-hosted or private control plane for regulated codebases.
- Custom adapters, policy packs, procurement, and annual contracts.

## Commercial sequence

1. Prove repeat usage with 20–50 active alpha users and collect task-level feedback manually.
2. Ship a local dashboard and exportable anonymous report before any network telemetry.
3. Launch a paid founding-user Pro plan; keep checkout and licensing outside the plugin until the
   Codex ecosystem documents a native paid-plugin channel.
4. Add Team only after individual retention and receipt credibility are strong.
5. Sell outcomes—reduced context cost with maintained task quality—not unverifiable token claims.

## Deferred telemetry TODO

- [ ] Add local-only counters and `token-saver stats`.
- [ ] Add one-click anonymous feedback export.
- [ ] Define a privacy spec, deletion policy, event schema, and threat model.
- [ ] Consider opt-in anonymous telemetry only after the above; default it off.
- [ ] Never collect prompts, responses, source code, file paths, repository URLs, raw logs, or user
      identity through product analytics.
