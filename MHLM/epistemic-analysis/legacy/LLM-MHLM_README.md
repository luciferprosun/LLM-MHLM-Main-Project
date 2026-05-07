# LLM-MHLM Canonical Archive

This is the canonical archive for model-by-model MHLM work.

## Read First

- `PROJECT_INDEX.md` for the current map
- `models/README.md` for the folder rules
- `models/iterations/README.md` for dated snapshots
- `models/iterations/2026-05-05/INDEX.md` for the latest cleaned snapshot

## Structure

- `models/<model>/` stores raw working notes and artifacts.
- `models/<model>/incoming/YYYY-MM-DD/` stores imported source material.
- `models/iterations/YYYY-MM-DD/` stores the cleaned, GitHub-facing snapshot.
- `reports/daily/YYYY-MM-DD/` stores day-level synthesis.
- `mhlm/` stores evidence and probability logs.

## Current Snapshot

- `2026-05-05` is the current cleaned snapshot.
- It contains one folder per model in lowercase.
- It uses date-stamped `FINAL_*` files for stable linking.

## Rule of Thumb

If a file is for active editing, keep it in the working model folder.
If a file is for publication-style navigation, keep it in the dated iteration snapshot.

