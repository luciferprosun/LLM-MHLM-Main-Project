# Duplicate Report (content-hash)

This file lists *known identical* files inside `LLM-MHLM/` that were detected by SHA-256 hashing.

Policy:

- Keep duplicates for now (non-destructive).
- When ready to slim down, pick a canonical path and replace the other copy with either:
  - a symlink to the canonical file, or
  - a short `README.md` pointer file (for archives that dislike symlinks).

## Detected duplicates (2026-05-05 scan)

### PDFs duplicated across “Lsd llm lsc project” vs model artifacts

- `models/codex/artifacts/2026-04-30_codex_halucynation_theory.pdf`
  - identical to `Lsd llm lsc project /codex halucynation theory.pdf`
- `models/gemini/artifacts/2026-04-30_gemini_hallucination_report.pdf`
  - identical to `Lsd llm lsc project /gemini halucynation raport.pdf`
- `models/gpt/artifacts/2026-04-30_gpt_hallucination_theory.pdf`
  - identical to `Lsd llm lsc project /LSC_LLM_Hallucination_Theory_GPT-1.pdf`

### Repo snapshot vs Zenodo package duplicates

These are expected (Zenodo package mirrors the repo snapshot), but they are byte-identical:

- `git/LSC_MDLH_PRO/` duplicates content under `zenodo/LSC_MDLH_PRO/` for some files:
  - `paper/LSC_MDLH_PRO.pdf`
  - `paper/LSC_MDLH_PRO.tex`
  - `code/mdlh_simulation.py`
  - `figures/mdlh_loop_diagram.png`
  - `figures/amplification_model_plot.png`

### Zenodo docs duplicated in DeepSeek incoming bundle

- `zenodo/LSC_6_2_0_PUBLISHED.md`
  - identical to `models/deepseek/incoming/2026-05-01/04_ZENODO_AND_LINKS/LSC_6_2_0_PUBLISHED.md`
- `zenodo/LSC_6_2_2_ADDENDUM.md`
  - identical to `models/deepseek/incoming/2026-05-01/04_ZENODO_AND_LINKS/LSC_6_2_2_ADDENDUM.md`
- `zenodo/LSC_6_2_2_PUBLIC_NOTE.md`
  - identical to `git/LSC_MDLH_PRO/experiments/theory_updates/2026-04-30_public_note.md`

