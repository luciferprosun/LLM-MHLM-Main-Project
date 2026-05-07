# LSC: The Saga Continue

Public working archive for reproducible gallium-source analysis, detector-response modeling, and AI-assisted research notes.

This repository is intentionally a living workspace. It keeps the data trail, code, versions, and research notes visible for review by collaborators, reviewers, and grant evaluators.

## Current Contents

```text
baza/
  model_lsc_6_2_0/
  przydatne_dodatki/
  SELECTION_REPORT.md
data/
  codex data.pdf
  dataset.json
  loader.py
  summary_report.md
mhlm_ai_research/
  README.md
  LLM-MHLM/
    README.md
    models/
      iterations/
        2026-05-05/
research_plan/
  LSC_BEST2_MHLM_RESEARCH_PLAN.md
session_notes/
```

## Research Scope

- BEST, GALLEX and SAGE gallium calibration data.
- Detector geometry, source properties, and measured ratios.
- Reproducible model fitting, simulation, and stability checks.
- Separation between raw AI-assisted notes and later verified datasets.
- Public research diary entries and versioned analysis reports.
- LSC 6.2.0 and 6.2.1 continuation toward BEST-2 style modeling.

## Current Theory Base

The current published development base is:

**LSC 6.2.0: A Phenomenological Framework for Neutrino Propagation and Detector-Frame Tensor Anisotropy**

See:

- `baza/SELECTION_REPORT.md`
- `baza/model_lsc_6_2_0/LSC_6_2_0_BASE_THEORY_FOR_BEST2.md`

The current continuation package is:

**LSC 6.3.0 Unified BEST-2 Continuation**

See:

- `baza/model_lsc_6_3_0_unified/LSC_6_3_0_UNIFIED_BEST2_UPDATE.md`
- `baza/model_lsc_6_3_0_unified/ZENODO_UNIFICATION_PLAN.md`
- `baza/model_lsc_6_3_0_unified/zenodo_6_3_0_metadata.json`
- `baza/model_lsc_6_3_0_unified/LSC_6_3_0_PUBLISHED.md`

This continuation does not claim confirmed new physics. It consolidates the
post-6.2.0 repair path into a BEST-2 validation protocol.

Zenodo:

- Version DOI: `https://doi.org/10.5281/zenodo.20037838`
- Concept DOI: `https://doi.org/10.5281/zenodo.19780615`

## Dual Research Track

This archive now has two linked but separate research poles:

- LSC / BEST-2: physics modeling, gallium-source data, and falsifiable predictions.
- MHLM / AI-research: documentation of multi-model AI theory-building, including hallucinations, overclaims, and useful synthesis.

The canonical MHLM archive starts here:

- `mhlm_ai_research/LLM-MHLM/README.md`
- `mhlm_ai_research/LLM-MHLM/models/iterations/2026-05-05/`

Linked MHLM / MDLH repository:

https://github.com/luciferprosun/LSC_MDLH_PRO

The projects are connected by one research program, but they should remain separate repositories.

`LSC_MDLH_PRO_UPDATE` was retired and merged into the main MHLM archive structure.

## Scientific Status

LSC remains an unvalidated theoretical research line. The purpose of this repository is not to claim confirmed new physics, but to keep the data trail, assumptions, calculations, and failure modes visible for review.

## Data Rule

Raw values should remain traceable to sources. Missing values must stay explicit. Derived or interpreted values should be separated from raw data.

## Public Profile Source

For outward-facing descriptions, see:

- `public_profile/README.md`

That file is the shared source of truth for bios, project summaries, and grant-facing wording.

## Quick Data Check

```bash
python3 data/loader.py
```

The repository includes a GitHub Actions workflow that runs this loader check on push and pull request.
