# LSC-6.0 and LSC-4.2 Final Merge (2026-05-07)

## Scope

Comparison and merge performed between:

- `luciferprosun/LSC-6.0`
- `luciferprosun/LSC-4.2-ULTRA-REZ-QUE`
- target monorepo `luciferprosun/LLM-MHLM-Main-Project`

## Result

- `LSC-4.2-ULTRA-REZ-QUE`: no unique files remained; already fully represented in `LSC/theory/LSC-4.2-Ultra/`.
- `LSC-6.0`: 22 unique files were merged into `LSC/theory/LSC-6.0/`.

## Merged additions from LSC-6.0

- `releases/LSC_v1.2.0_release/*` (metadata, figures, code, paper, release notes)
- `releases/LSC_6.2.0_preprint/metadata/ZENODO_UPLOAD_NOTES.md`
- `releases/LSC_6.2.0_preprint/PUBLISHED.md`
- `docs/external_reviews/*`
- updated source-level files where content differed (`README.md`, `.zenodo.json`)

## Deduplication rule

Only content absent by SHA256 hash in the main repository was added or updated.
