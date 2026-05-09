# LLM/MHLM Main Project

Unified public research monorepo for:

- LSC / SC neutrino phenomenology
- MHLM / MDLH AI-assisted epistemology

This repository is organized for reproducibility, archival continuity, and grant-facing scientific documentation.

## Scientific Status

The LSC line is an unvalidated phenomenological research program.  
The MHLM/MDLH line is an epistemic and AI-safety audit framework.  
Archival publication does not imply physical validation.

## Structure

```text
docs/
LSC/
  theory/
    LSC-4.2-Ultra/
    LSC-5.0.0/
    LSC-6.0/
    LSC-6.2.0/
    LSC-6.2.2/
    LSC-6.3.0/
    future/
  papers/
  figures/
  datasets/
  simulations/
  validation/
  notebooks/
  references/
  reproducibility/
MHLM/
  MDLH-v1.0/
  convergence-analysis/
  ai-workflows/
  reproducibility/
  prompts/
  logs/
  papers/
  evaluation/
  epistemic-analysis/
shared/
  discord-server-bot-owl/
archive/
```

## LSC Summary

LSC tracks a continuous version lineage from 4.2 to 6.3.0 with preserved DOI and release continuity.  
Current evolution chain:

1. LSC 4.2 Ultra (DOI: 10.5281/zenodo.19602045)
2. LSC 5.0.0 (historical bridge release)
3. LSC 6.0 (DOI: 10.5281/zenodo.19780616 / software 10.5281/zenodo.19785745)
4. LSC 6.2.0 (DOI: 10.5281/zenodo.19878587)
5. LSC 6.2.2 (formal correction layer)
6. LSC 6.3.0 (DOI: 10.5281/zenodo.20037838, concept 10.5281/zenodo.19780615)

## MHLM Summary

MHLM/MDLH documents multi-model convergence, epistemic amplification risk, provenance, and reproducibility auditing for AI-assisted scientific pipelines.

Primary MHLM/MDLH DOI:

- 10.5281/zenodo.19851006

## Reproducibility

All major theory and simulation branches should keep:

- explicit version tags
- source/data/provenance separation
- deterministic build instructions
- changelog and citation metadata

## Community Infrastructure

Shared operational tooling for public-facing project coordination can live under `shared/`.

Current community tooling:

- `shared/discord-server-bot-owl/` - Discord server bot and research assistant layer for GitHub, Zenodo, publications, grant tracking, and OpenRouter/Owl-backed chat workflows

## Migration Notes

Formal migration map and command plan:

- `docs/MIGRATION_PLAN.md`
- `docs/DUPLICATE_RESOLUTION.md`
- `scripts/migration_commands.sh`
