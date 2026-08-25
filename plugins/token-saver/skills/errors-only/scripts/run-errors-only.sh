#!/usr/bin/env bash
set -u

if [[ "${1:-}" != "--" || $# -lt 2 ]]; then
  echo "usage: run-errors-only.sh -- command [args...]" >&2
  exit 64
fi
shift

log_file="$(mktemp "${TMPDIR:-/tmp}/token-saver-errors.XXXXXX")"
"$@" >"$log_file" 2>&1
status=$?

echo "exit_code=$status"
echo "full_log=$log_file"

if [[ $status -eq 0 ]]; then
  echo "result=success"
  tail -n 12 "$log_file"
  exit 0
fi

echo "result=failure"
echo "--- actionable matches (max 80) ---"
if command -v rg >/dev/null 2>&1; then
  rg -n -i -m 80 '(^|[^[:alpha:]])(error|fatal|fail(ed|ure)?|exception|panic|traceback|assert(ion)?)([^[:alpha:]]|$)' "$log_file" || true
else
  grep -Eni -m 80 'error|fatal|fail(ed|ure)?|exception|panic|traceback|assert(ion)?' "$log_file" || true
fi
echo "--- final 40 lines ---"
tail -n 40 "$log_file"
exit "$status"
