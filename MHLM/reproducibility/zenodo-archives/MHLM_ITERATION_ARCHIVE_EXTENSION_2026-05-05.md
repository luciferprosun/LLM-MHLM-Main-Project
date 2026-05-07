# MHLM Iteration Archive Extension - 2026-05-05

This note accompanies the DOI-preserving update of the Zenodo record:

- Record: https://zenodo.org/records/19851006
- DOI: https://doi.org/10.5281/zenodo.19851006

## Scope of the update

The published MHLM / MDLH package has been extended with a structured archive
layer for model-lineage and hallucination-audit provenance.

Added layers inside the public package:

- `experiments/`
- `prompt-archive/`
- `llm-simulation-lab/`
- `model-lineage-app/`
- `mhlm/`
- `iterations/LSC_theory_by_LLM/`
- `grant/`

## Why this matters

The MHLM paper is about the risk that multi-model AI workflows can make a
scientific line appear increasingly mature before independent validation is in
place.

For that claim to be auditable, the publication should expose:

- prompts,
- dated model snapshots,
- per-model theory tracks,
- correction notes,
- and explicit logs of evidence and uncertainty.

## Scientific status

This update improves archive transparency and grant readiness.

It does not validate the LSC theory line and does not claim that model
agreement is evidence of truth.
