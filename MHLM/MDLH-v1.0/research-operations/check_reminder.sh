#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_FILE="$ROOT_DIR/research-operations/reminder_run_log.md"
TODAY="$(date +%F)"
NOW="$(date -Is)"

case "$TODAY" in
  2026-05-01)
    MESSAGE="Step 1 active: operations layer created; review pending changes and commit."
    ;;
  2026-05-02|2026-05-03)
    MESSAGE="Step 2 due: review Gemini output, archive another model response, update simulation comparison."
    ;;
  2026-05-04|2026-05-05|2026-05-06|2026-05-07)
    MESSAGE="Step 3 due: prepare grant abstract, MVP metrics, dataset spec, and outreach note."
    ;;
  2026-05-08)
    MESSAGE="Step 4 due: decide whether the Zenodo continuation is ready for publication review."
    ;;
  *)
    MESSAGE="No dated step is due today. Check research-operations/reminders.md for the next target."
    ;;
esac

{
  echo
  echo "## $NOW"
  echo
  echo "$MESSAGE"
} >> "$LOG_FILE"

printf '%s\n' "$MESSAGE"

