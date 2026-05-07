# Codex Notes

## 2026-04-30

- Created the reproducible 6.2.1 continuation analysis.
- Added fit diagnostics, validation predictions, and leave-one-out checks.
- Main result: exact anchor fit, weak predictive stability.

## 2026-04-30 - lineage forensics

- Reviewed the full local lineage from `LSC 3.5` through `LSC 6.2.1`.
- Evidence-backed contribution: turned the theory from narrative fit into explicit validation diagnostics.
- Key scientific change introduced: exposed that anchor fitting does not survive leave-one-out.
- Source basis: `LSC 6.2.1` analysis outputs plus local archive comparison against `LSC 4.2`, `LSC 5.0@`, `LSC 5.5`, and `LSC 6.0`.
- MHLM relevance: strongest audit signal so far, because the model line now has a documented stability failure instead of only polished prose.

## 2026-04-30 - 6.2.2 correction and simulations

- Produced the corrected 6.2.2 continuation package.
- Main update: explicit trace plus traceless detector split, fixed-frame sidereal logic, and deterministic simulation outputs.
- Source basis: 6.2.1 validation outputs and the DeepSeek formal critique.
- MHLM relevance: the audit trail now contains both a failure mode and a formal repair path, which is useful for documenting how the theory line evolved across model outputs.
