# Contributing

## Branching

- Use feature branches per migration unit:
  - `migrate/lsc-4-2`
  - `migrate/lsc-5-0`
  - `migrate/lsc-6-x`
  - `migrate/mhlm-core`

## Commit Rules

- Keep commits scoped to one migration concern.
- Prefer moves/renames over copy duplication.
- Never remove DOI, citation, or release metadata without replacement link.

## Data and Artifacts

- Do not commit caches, temporary exports, or generated noise artifacts.
- Keep canonical PDFs and datasets in one location; use references/manifests for legacy duplicates.

## Scientific Wording

- Do not represent unvalidated models as confirmed physics.
- Keep distinction between hypothesis, simulation, and validation status explicit.
