# LSC / BEST-2 / MHLM Research Plan

Date: 2026-04-30
Status: working plan, not a scientific claim

## Purpose

This repository is the public working archive for the LSC continuation toward a BEST-2 style confrontation.

The project has two connected but separate poles:

1. LSC physics pole: build, document and test the LSC 6.2.0 detector-frame tensor-anisotropy model against gallium anomaly data.
2. MHLM / AI-research pole: document how multiple LLM systems contribute to the theory-building process, including useful synthesis, hallucinations, overclaims and model-to-model disagreement.

The goal is not to announce a confirmed discovery at this stage. The goal is to create a transparent trail of data, assumptions, model versions, AI-generated analyses, and falsifiable predictions before confrontation with BEST-2 or BEST-2-like experimental inputs.

For public-facing wording, follow `public_profile/README.md` so GitHub, Cloudflare, Zenodo-linked pages, and profile bios stay aligned.

## Linked Repositories

- LSC continuation and gallium data: https://github.com/luciferprosun/LSC-the-saga-continue
- MHLM / MDLH related AI-theory project: https://github.com/luciferprosun/LSC_MDLH_PRO
- LSC 6.2.0 base line: https://github.com/luciferprosun/LSC-6.0

These repositories should remain separate projects. This repository keeps the LSC physics data and theory-continuation archive. The MHLM / MDLH repository remains the dedicated project for the model/hypothesis around AI-mediated theory development.

## Working Hypothesis

LSC 6.2.0 is treated as a phenomenological ansatz:

- detector-frame tensor response may shift reconstructed or effective neutrino response;
- gallium anomaly data are used as a strict test case, not as proof;
- the model must survive comparison with BEST, GALLEX, SAGE and non-gallium constraints;
- if the model cannot make falsifiable predictions, it must be rewritten or rejected.

## Dual-Pole Structure

### Pole A: Physics / LSC

Primary question:

Can a detector-frame anisotropic tensor-response model reproduce the gallium deficit without conflicting with known constraints?

Required outputs:

- clean BEST inner/outer geometry model;
- volume-integrated prediction for `R_inner`, `R_outer` and `R_outer/R_inner`;
- comparison against GALLEX and SAGE;
- explicit table of parameters and priors;
- list of predictions that would falsify LSC;
- separation between raw data, derived data and interpretation.

### Pole B: MHLM / AI-Research

Primary question:

Can we document how AI systems accelerate, distort or hallucinate scientific theory-building in a high-stakes physics topic?

Required outputs:

- diary of model contributions by source: Codex, Gemini and later other models;
- hallucination log: unsupported claims, inflated confidence, false citations, confused terminology;
- useful synthesis log: valid summaries, extracted datasets, code generation, literature mapping;
- versioned reports from different models using the same prompt family;
- comparison table showing where models agree, disagree or overclaim.

## Research Phases

### Phase 1: Archive Hygiene

- Keep all data in `data/`.
- Keep selected theory base in `baza/`.
- Keep research plans in `research_plan/`.
- Keep AI/model-process notes in `mhlm_ai_research/`.
- Keep session state notes in `session_notes/`.

### Phase 2: BEST-2 Toy Model

- Implement geometry integration for BEST inner and outer zones.
- Start with point-source approximation.
- Add finite source-size correction only after the baseline model is reproducible.
- Fit provisional parameters only against published BEST ratios.
- Mark every fit as exploratory until independently checked.

### Phase 3: Legacy Gallium Cross-Check

- Run the same model against GALLEX Cr1, GALLEX Cr2, SAGE Cr and SAGE Ar.
- Track whether the same parameter family can describe all experiments.
- If separate parameters are needed per experiment, document this as weakness unless a physical reason is shown.

### Phase 4: Constraint Check

- Compare the interpretation against KATRIN, reactor, solar and IceCube constraints.
- Do not claim that KATRIN fully eliminates all sterile-neutrino models.
- Do state that simple high-mixing sterile interpretations are under strong tension.
- Separate detector-systematics explanations from new-physics explanations.

### Phase 5: Prediction Table

Prepare a public table with:

- predicted `R_inner`;
- predicted `R_outer`;
- predicted `R_outer/R_inner`;
- expected dependence on source isotope;
- expected dependence on detector orientation or geometry;
- result that would falsify the current LSC version.

### Phase 6: Multi-Model MHLM Reports

For each AI model report:

- store original or cleaned report;
- mark it as unverified unless checked against sources;
- extract claims into a claim table;
- classify claims as supported, plausible, speculative, unsupported or wrong;
- compare model behavior across Codex, Gemini and later models.

## Minimum Standard Before Public Scientific Claim

No "solution", "discovery" or "eureka" language should be used unless the repository contains:

- reproducible code;
- source-linked datasets;
- fit results with uncertainties;
- falsifiable predictions;
- explicit comparison to alternative explanations;
- documented negative checks and failure modes.

Until then, this is an open research archive and an AI-assisted theory-development diary.
