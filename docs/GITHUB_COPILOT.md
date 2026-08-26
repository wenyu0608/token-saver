# GitHub Copilot adapter

Token Saver is packaged as an Agent Plugin for GitHub Copilot CLI. It reuses the
same skills, scripts, references, and receipt policy as the Codex, Claude Code,
and Cursor adapters.

## Install from GitHub

```bash
copilot plugin marketplace add wenyu0608/token-saver
copilot plugin install token-saver@token-saver
```

Start a new Copilot CLI session, then verify and invoke the skill:

```text
/skills list
/token-saver diagnose the failing test without dumping the full build log
```

The specialist skills remain available as `/repomix`, `/errors-only`,
`/docs-slice`, `/diff-context`, `/session-handoff`, `/token-audit`, and
`/full-fidelity`.

## Update

```bash
copilot plugin update token-saver@token-saver
```

Copilot caches installed plugins. Update the plugin and begin a new session
after a release rather than expecting an active session to change live.
