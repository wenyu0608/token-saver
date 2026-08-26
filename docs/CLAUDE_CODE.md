# Claude Code adapter

Token Saver ships the same skills to Codex and Claude Code. The routing rules,
specialist workflows, scripts, and receipt policy live in one plugin directory;
only the host manifests and invocation syntax differ.

## Install from GitHub

Run these commands inside Claude Code:

```text
/plugin marketplace add wenyu0608/token-saver
/plugin install token-saver@token-saver
```

Run `/reload-plugins` after installation. Then invoke the umbrella skill:

```text
/token-saver:token-saver diagnose the failing test without dumping the full build log
```

Specialist skills are also available under the same namespace:

```text
/token-saver:repomix map this repository before analyzing it
/token-saver:errors-only run the failing test and retain only actionable failures
/token-saver:docs-slice answer from the smallest relevant documentation sections
```

## Update

Third-party marketplaces do not have auto-update enabled by default. Update the
marketplace and plugin, then reload plugins:

```text
/plugin marketplace update token-saver
/plugin update token-saver@token-saver
/reload-plugins
```

## Local validation

From the repository root:

```bash
claude plugin validate .
claude --plugin-dir ./plugins/token-saver
```

The Repomix wrapper accepts both host conventions: `CLAUDE_PLUGIN_ROOT` and
`CLAUDE_PLUGIN_DATA` in Claude Code, or `PLUGIN_ROOT` and `PLUGIN_DATA` in Codex.
It still requires explicit approval before a first-time pinned npm download.
