#!/usr/bin/env bash
set -euo pipefail

skill_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
plugin_root="$(cd "${skill_root}/../.." && pwd)"

exec "${plugin_root}/scripts/run-repomix.sh" "$@"
