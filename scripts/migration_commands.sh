#!/usr/bin/env bash
set -euo pipefail

# Run from repo root: /home/l/migration-work/LLM-MHLM-Main-Project

if [[ ! -d ".git" ]]; then
  echo "Repository not initialized. Run: git init && git checkout -b main"
  exit 1
fi

add_subtree_once() {
  local prefix="$1"
  local source_repo="$2"
  local source_branch="$3"

  if [[ -d "$prefix" ]]; then
    echo "skip subtree $prefix (already exists)"
    return 0
  fi

  git subtree add --prefix "$prefix" "$source_repo" "$source_branch"
}

add_subtree_once "LSC/theory/LSC-4.2-Ultra" "/home/l/github-audit/LSC-4.2-ULTRA-REZ-QUE" "main"
add_subtree_once "LSC/theory/LSC-5.0.0" "/home/l/github-audit/LSC-5.0-GPT-interpreter" "master"
add_subtree_once "LSC/theory/LSC-6.0" "/home/l/github-audit/LSC-6.0" "main"
add_subtree_once "MHLM/MDLH-v1.0" "/home/l/Desktop/prace dark neutrino /the saga continue /LLM-MHLM/git/LSC_MDLH_PRO" "main"
add_subtree_once "LSC/simulations/legacy/neutrino-oscillations-pbh" "/home/l/neutrino-oscillations-pbh" "master"

mkdir -p "LSC/theory/LSC-6.2.0" "LSC/theory/LSC-6.2.2" "LSC/theory/LSC-6.3.0"
cp -a "/home/l/the saga continue/baza/model_lsc_6_2_0/." "LSC/theory/LSC-6.2.0/"
cp -a "/home/l/the saga continue/mhlm_ai_research/LLM-MHLM/models/deepseek/incoming/2026-05-01/02_LSC_6_2_2_CODEX/." "LSC/theory/LSC-6.2.2/"
cp -a "/home/l/the saga continue/baza/model_lsc_6_3_0_unified/." "LSC/theory/LSC-6.3.0/"

mkdir -p "LSC/validation/LSC-6.2.1-codex" "LSC/datasets/gallium-core" "LSC/simulations/legacy/lsc55" "LSC/simulations/legacy/lsc60"
cp -a "/home/l/the saga continue/6.2.1/codex/." "LSC/validation/LSC-6.2.1-codex/"
cp -a "/home/l/the saga continue/data/." "LSC/datasets/gallium-core/"
cp -a "/home/l/the saga continue/baza/przydatne_dodatki/lsc55_math_and_tests/." "LSC/simulations/legacy/lsc55/"
cp -a "/home/l/the saga continue/baza/przydatne_dodatki/lsc60_simulation/." "LSC/simulations/legacy/lsc60/"

mkdir -p "MHLM/logs/model-tracks" "MHLM/evaluation/daily-reports" "MHLM/reproducibility/zenodo-archives"
cp -a "/home/l/the saga continue/mhlm_ai_research/LLM-MHLM/models/." "MHLM/logs/model-tracks/"
cp -a "/home/l/the saga continue/mhlm_ai_research/LLM-MHLM/reports/daily/." "MHLM/evaluation/daily-reports/"
cp -a "/home/l/the saga continue/mhlm_ai_research/LLM-MHLM/zenodo/." "MHLM/reproducibility/zenodo-archives/"

find . -type d -name "__pycache__" -prune -exec rm -rf {} +

mkdir -p "docs/reports"
find LSC MHLM -type f \( -iname "*.pdf" -o -iname "*.csv" -o -iname "*.json" -o -iname "*.txt" -o -iname "*.dat" \) -print0 \
  | xargs -0 sha256sum | sort > "docs/reports/artifact_hashes.txt"

cut -d ' ' -f1 "docs/reports/artifact_hashes.txt" | uniq -d > "docs/reports/duplicate_hashes.txt" || true

echo "Migration staging complete. Review with: git status"
