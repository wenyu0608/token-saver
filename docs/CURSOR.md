# Cursor adapter

Token Saver uses the Agent Plugins open standard supported by Cursor. The same
portable `plugin.json`, skills, scripts, and references are also used by GitHub
Copilot; there is no separate copy of the routing logic.

## Use now

In Cursor, open **Customize → Rules → Add Rule → Remote Rule (GitHub)** and add:

```text
https://github.com/wenyu0608/token-saver/tree/main/plugins/token-saver
```

Restart Cursor if the skills do not appear immediately. Invoke the umbrella
skill from Agent chat:

```text
/token-saver diagnose the failing test without dumping the full build log
```

Cursor may also select the skill automatically when the task needs repository,
document, diff, log, or handoff context optimization.

## Local plugin test

For plugin development, link the shared plugin directory into Cursor's local
plugin directory, then reload the window:

```bash
mkdir -p ~/.cursor/plugins/local
ln -s /absolute/path/to/token-saver/plugins/token-saver \
  ~/.cursor/plugins/local/token-saver
```

## Marketplace

The repository includes `.cursor-plugin/marketplace.json` and is ready for a
submission at `https://cursor.com/marketplace/publish`. Public one-click plugin
installation becomes available after Cursor's review. Team and Enterprise users
can import the GitHub repository as a team marketplace before public listing.
