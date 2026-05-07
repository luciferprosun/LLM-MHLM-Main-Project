# Duplicate Resolution Strategy

## Principle

Keep one canonical binary/data artifact per content hash.  
Replace extra copies with indexed references in manifests.

## Canonical Priority

1. Official version/theory folder for the release line.
2. Zenodo-packaged canonical record copy.
3. Website copy (only when website delivery requires direct asset presence).
4. Legacy/archive copies.

## Known High-Impact Duplicates

- `LSC_6_2_0_preprint.pdf` exists in multiple research and website paths.
- `LSC_MDLH_PRO.pdf` exists in MHLM repo and website download folders.
- LSC60 release PDFs duplicated across LSC repo and website download folders.
- model-iteration PDFs duplicated between `models/iterations/*` and `zenodo/*`.

## Action

- Keep canonical file in `LSC/theory/*` or `MHLM/MDLH-v1.0/*`.
- Keep website copies only in `Akasha-Chronicles/downloads/`.
- Move all non-canonical duplicates to `archive/legacy-builds/` or replace with manifest pointers.
