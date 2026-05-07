# LSC 6.2.2 Changelog

## Main correction

The 6.2.2 revision fixes the detector-response bookkeeping in the 6.2.x line.

## Changes

- Made the isotropic trace explicit.
- Kept the anisotropic piece traceless.
- Removed the mixed use of `1 / E^2` from the base ansatz.
- Defined the preferred direction in a fixed celestial frame for sidereal tests.
- Kept the exact-anchor / weak-LOO status unchanged.
- Added deterministic simulation outputs for trace/anisotropy separation and term decomposition.

## Interpretation

6.2.2 improves mathematical hygiene and defense structure.
It does not claim the physics is validated.
