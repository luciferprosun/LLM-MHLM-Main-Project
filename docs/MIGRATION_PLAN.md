# Migration Plan

## Target Public Repositories

1. `LLM-MHLM-Main-Project` (this monorepo)
2. `Akasha-Chronicles` (website/frontend only)

## Detected Source Repositories

- `/home/l/the saga continue` (`LSC-the-saga-continue`)
- `/home/l/github-audit/LSC-4.2-ULTRA-REZ-QUE`
- `/home/l/github-audit/LSC-5.0-GPT-interpreter`
- `/home/l/github-audit/LSC-6.0`
- `/home/l/Desktop/prace dark neutrino /the saga continue /LLM-MHLM/git/LSC_MDLH_PRO`
- `/home/l/neutrino-oscillations-pbh`
- `/home/l/akasha-chronicles-site`
- `/home/l/site-project-flame-update`
- `/home/l/Akasha-project-page-desing`
- `/home/l/Star-3d-model-`

## Confirmed LSC Placement Rule

`neutrino-oscillations-pbh` belongs inside `LSC`, not `MHLM`.

Assigned path:

`LSC/simulations/legacy/neutrino-oscillations-pbh/`

## Import Sequence

1. Import LSC 4.2 repository into `LSC/theory/LSC-4.2-Ultra/`.
2. Import LSC 5.0 repository into `LSC/theory/LSC-5.0.0/`.
3. Import LSC 6.0 repository into `LSC/theory/LSC-6.0/`.
4. Import selected 6.2.0/6.2.2/6.3.0 assets from `the saga continue`.
5. Import `LSC_MDLH_PRO` into `MHLM/MDLH-v1.0/`.
6. Import `neutrino-oscillations-pbh` into `LSC/simulations/legacy/neutrino-oscillations-pbh/`.
7. Deduplicate by checksum and keep canonical artifact path with manifest references.

## Non-Destructive Rule

No deletion from source repositories until:

- monorepo import is complete,
- artifact hash manifests are generated,
- DOI/citation link checks are passed.
