# Archive Strategy

## Private/Archive Routing Rules

Send to private/archive when material is:

- duplicated without archival necessity
- unfinished and not reproducible
- unrelated to LSC/MHLM core lines
- generated cache/export noise
- screenshot or UI preview clutter

## Suggested Routing

- `github-audit/*` mirror clones -> `archive/old-repositories/` (or private backup)
- incomplete side projects (`Akasha-WebSite-index.html`, stale experiments) -> private archive repo
- temporary ZIP packaging duplicates -> `archive/legacy-builds/`
- deprecated hypothesis branches and obsolete notes -> `archive/deprecated/`
- unstable exploratory scripts -> `archive/experimental/`

## DOI Continuity Rule

Never archive away the only copy of:

- DOI metadata (`.zenodo.json`, `zenodo*.json`)
- release notes/changelog that maps version lineage
- citation records and publication links

If moving to archive, keep pointer files in active paths.
