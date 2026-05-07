# LSC 6.2.2 Addendum

Date: 2026-04-30

This note extends the existing DOI-backed LSC records without changing their DOI.

## What changed

- The detector-response bookkeeping in the LSC 6.2.x line was corrected.
- The isotropic trace is now explicit.
- The directional detector term remains traceless.
- The base ansatz no longer mixes the detector term with an unqualified `1 / E^2` factor.
- A fixed celestial frame is now used for sidereal tests.
- Deterministic simulations were added for trace/anisotropy separation and term decomposition.

## Why this matters

This is a formal repair path, not a validation claim.
The current result is:

- exact anchor fit remains,
- leave-one-out stability remains weak,
- the theory is now better structured for defense and review,
- the DOI trail on Zenodo should remain unchanged so previously shared grant links stay valid.

## Linked materials

- GitHub theory update note: https://github.com/luciferprosun/LSC_MDLH_PRO/blob/main/experiments/theory_updates/2026-04-30_lsc_6_2_2_correction.md
- Local corrected package: `the saga continue /6.2.2/`
- DeepSeek review note: `LSC 6.2.0 formal critique`

