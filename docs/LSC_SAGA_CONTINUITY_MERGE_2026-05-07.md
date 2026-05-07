# LSC-the-saga-continue Continuity Merge (2026-05-07)

This document records selective migration from `luciferprosun/LSC-the-saga-continue` into `LLM-MHLM-Main-Project`.

## Goal

- preserve continuity artifacts that were missing in monorepo
- avoid duplicate payloads already present by hash
- avoid importing secret-bearing files

## Added To LSC

- `LSC/reproducibility/continuity/SELECTION_REPORT_2026-04-30.md`
- `LSC/reproducibility/continuity/SAGA_BAZA_README.md`
- `LSC/reproducibility/continuity/DATA_MANIFEST_2026-05-05.md`
- `LSC/reproducibility/zenodo-checks/zenodo_19780616_lsc_6_0.json`
- `LSC/reproducibility/zenodo-checks/zenodo_19843361_lsc_v1_2_0.json`
- `LSC/reproducibility/zenodo-checks/zenodo_19878587_lsc_6_2_0.json`
- `LSC/theory/future/prism-exploratory/gemini_lsc_prism_intro.md`
- `LSC/theory/future/prism-exploratory/gpt_report_LSC61_prism.pdf`
- `LSC/theory/future/LSC-6.2.3-dev/lsc623_model.py`

## Added To MHLM

- `MHLM/epistemic-analysis/legacy/*` (legacy framing and planning docs)
- `MHLM/ai-workflows/ops/SESSION_END_CHECKLIST.md`
- `MHLM/evaluation/daily-reports/2026-04-30/GEMINI_LSC_WORKING_REPORT_2026-04-30.md`
- `MHLM/figures/legacy/lsc_collective_hallucination_case_study.{png,svg}`
- `MHLM/reproducibility/zenodo-archives/LSC_MDLH_PRO/legacy-from-saga/*`

## Added To Archive

- `archive/old-repositories/LSC-the-saga-continue/*` (session notes, legacy README, traffic report, plan)
- `archive/legacy-builds/LSC_MDLH_PRO_zenodo_package_from_saga.zip`

## Explicitly Excluded

- `mhlm_ai_research/LLM-MHLM/models/openrouter/incoming/2026-05-02/opeanrouterscc.py`

Reason: file contains API key material and is not safe to import into public history.
