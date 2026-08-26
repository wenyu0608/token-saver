#!/usr/bin/env bash
set -euo pipefail

readonly REPOMIX_VERSION="1.14.0"

if command -v repomix >/dev/null 2>&1; then
  exec repomix "$@"
fi

if ! command -v npx >/dev/null 2>&1; then
  echo "token-saver: Repomix requires Node.js/npm; neither a local repomix nor npx was found." >&2
  exit 69
fi

if [[ "${TOKEN_SAVER_ALLOW_DOWNLOAD:-0}" != "1" ]]; then
  echo "token-saver: Repomix is not cached locally." >&2
  echo "After approving a one-time npm download, rerun with:" >&2
  echo "TOKEN_SAVER_ALLOW_DOWNLOAD=1 ${BASH_SOURCE[0]} [repomix arguments]" >&2
  exit 69
fi

cache_root="${PLUGIN_DATA:-${TMPDIR:-/tmp}/token-saver-data}/npm-cache"
mkdir -p "$cache_root"
export npm_config_cache="$cache_root"
exec npx --yes "repomix@${REPOMIX_VERSION}" "$@"
