#!/usr/bin/env bash
set -euo pipefail

# Run from: /home/l/migration-work/LLM-MHLM-Main-Project

ROOT="$(pwd)"

git init
git checkout -b main

# Import with history preservation.
git subtree add --prefix LSC/theory/LSC-4.2-Ultra "/home/l/github-audit/LSC-4.2-ULTRA-REZ-QUE" main
git subtree add --prefix LSC/theory/LSC-5.0.0 "/home/l/github-audit/LSC-5.0-GPT-interpreter" master
git subtree add --prefix LSC/theory/LSC-6.0 "/home/l/github-audit/LSC-6.0" main
git subtree add --prefix MHLM/MDLH-v1.0 "/home/l/Desktop/prace dark neutrino /the saga continue /LLM-MHLM/git/LSC_MDLH_PRO" main
git subtree add --prefix LSC/simulations/legacy/neutrino-oscillations-pbh "/home/l/neutrino-oscillations-pbh" master

# Copy selected LSC 6.2.0/6.2.2/6.3.0 content from active workspace (no history path).
mkdir -p LSC/theory/LSC-6.2.0 LSC/theory/LSC-6.2.2 LSC/theory/LSC-6.3.0
cp -a "/home/l/the saga continue/baza/model_lsc_6_2_0/." LSC/theory/LSC-6.2.0/
cp -a "/home/l/the saga continue/mhlm_ai_research/LLM-MHLM/models/deepseek/incoming/2026-05-01/02_LSC_6_2_2_CODEX/." LSC/theory/LSC-6.2.2/
cp -a "/home/l/the saga continue/baza/model_lsc_6_3_0_unified/." LSC/theory/LSC-6.3.0/

# Cleanup obvious transient files.
find . -type d -name "__pycache__" -prune -exec rm -rf {} +

git add .
git commit -m "chore: initialize unified LLM/MHLM research monorepo and import LSC lineage"

# Generate duplicate hash report (PDF/CSV/JSON/TXT/DAT).
mkdir -p docs/reports
find LSC MHLM -type f \( -iname "*.pdf" -o -iname "*.csv" -o -iname "*.json" -o -iname "*.txt" -o -iname "*.dat" \) \
  -print0 | xargs -0 sha256sum | sort > docs/reports/artifact_hashes.txt

awk '{print $1}' docs/reports/artifact_hashes.txt | uniq -d > docs/reports/duplicate_hashes.txt || true
