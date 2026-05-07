# Merge Plan: `LSC_MDLH_PRO_UPDATE` -> `LSC_MDLH_PRO`

Date: 2026-05-05

Goal: merge the useful additions from `LSC_MDLH_PRO_UPDATE` into the main MHLM repo without deleting the existing database/archive layer.

## Keep as canonical

- `LSC_MDLH_PRO` stays the primary repo.
- `LSC_MDLH_PRO_UPDATE` is treated as a patch/staging repo.
- No base files are removed from the main repo.

## Files to merge

1. `code/lsc623_model.py`
   - Add as a new module in the main repo.
   - Purpose: 6.2.3 detector-response model implementation.

2. `experiments/theory_updates/2026-05-02_lsc_6_2_3_framework.md`
   - Add as a new theory-update note.
   - Purpose: formal write-up for the 6.2.3 expansion.

3. `experiments/theory_updates/2026-04-30_lsc_6_2_2_correction.md`
   - Keep the existing main-repo file.
   - Append the 2026-05-02 expansion section from `UPDATE`.
   - Do not replace the whole file unless the main-repo version is missing the same repair logic.

## Files to leave unchanged

- `README.md`
- `experiments/README.md`
- `experiments/lineage_summary.json`
- `model-lineage-app/*`
- `llm-simulation-lab/*`
- `metadata/*`
- `prompt-archive/*`
- `research-operations/*`

## Merge rule

- Preserve the original base content.
- Merge only the new theory step and its code support.
- If a line is duplicated verbatim in both repos, keep the main repo version unless the `UPDATE` version is strictly more specific.

## Recommended next commit shape

- `Add lsc623 model`
- `Add 6.2.3 framework note`
- `Extend 6.2.2 correction with 6.2.3 transition`

