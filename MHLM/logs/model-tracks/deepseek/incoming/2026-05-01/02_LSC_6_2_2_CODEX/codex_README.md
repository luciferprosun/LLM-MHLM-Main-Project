# LSC 6.2.2 Codex Workspace

Working package for the LSC 6.2.2 continuation.

This folder is intentionally separate from the 6.2.0 base theory. It contains:

- a small, reproducible data model for BEST, GALLEX and SAGE;
- a first-pass phenomenological fit to the extracted ratios;
- an explicit trace-plus-traceless interpretation of the detector tensor;
- diagnostic simulations for geometry, source cross sections and zone splitting;
- unit tests;
- a generated PDF report.

## Build

```bash
cd "/home/l/Desktop/prace dark neutrino /the saga continue /6.2.2/codex"
python3 build.py
```

Outputs are written to `out/`.
The build also writes a simulation digest (`simulations.md`,
`simulation_summary.json`, `term_contributions.csv`,
`directional_scan.csv`) so the trace channel and traceless channel can be
audited separately.

## Model Status

This is an exploratory calibration layer, not a claim of confirmed new physics.
It uses published gallium source-experiment values as anchor points and reports
where the fit is stable and where it is not.

The 6.2.2 revision separates:

- isotropic trace,
- traceless anisotropy,
- detector-geometry nuisance terms.
