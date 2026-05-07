# Prototype Fund Alignment Review

Date: 2026-05-01

## Short Verdict

The project is not ready for a final Prototype Fund application yet, but it is
ready for pre-application shaping.

The strongest grant framing is not "neutrino theory validation". The strongest
framing is an open-source software prototype for auditing correlated LLM
hallucinations in scientific and technical reasoning.

## Recommended Application Name

Model-Lineage Audit Lab: Open-Source Detection of Correlated LLM Hallucinations
in Scientific Reasoning

## Prototype Fund Fit

### Strong Fit

- Open-source software prototype.
- Public-interest technology.
- AI safety and hallucination analysis.
- Reproducible prompt and response archive.
- Scientific and technical documentation provenance.
- Software infrastructure for auditability.
- Data-security adjacent: reduces risk from unverified AI-generated scientific
  or technical claims entering public workflows.

### Needs Improvement Before Application

- Define a user group in plain language.
- Describe the exact prototype that will exist after six months.
- Add a lightweight UI roadmap.
- Add evaluation metrics.
- Add data and privacy assumptions.
- Clarify license and sustainability plan.
- Separate the software tool from the LSC case study.

## User Groups

- independent researchers using LLMs in literature review or theory drafting;
- open-science maintainers reviewing AI-assisted submissions;
- journalists and public-interest investigators checking technical claims;
- educators teaching AI literacy and scientific reasoning;
- small research teams without institutional AI-audit infrastructure.

## Six-Month Prototype Scope

The prototype should aim to deliver:

- prompt and response ingestion;
- model identity and date tracking;
- claim extraction;
- cross-model agreement and disagreement scoring;
- hallucination-risk annotations;
- source-status labels;
- static public report export;
- minimal web dashboard;
- reproducible example dataset using the existing LSC / MHLM archive.

## What Zenodo Should Say

Zenodo should emphasize the archive as a research artifact and software
prototype seed:

- open-source audit infrastructure;
- public-interest AI safety;
- reproducibility;
- model-lineage documentation;
- prompt and response provenance;
- high-stakes scientific reasoning as the case study.

Zenodo should not be updated with stronger physics claims or claims of
validated discovery.

## Decision for 2026-05-01

Do not publish a new Zenodo version today.

Recommended action:

- keep the online Zenodo draft unpublished;
- keep the grant-readiness package local;
- add this alignment review to Git;
- after at least two real model-response reports are archived, rebuild the
  Zenodo draft package and then decide whether to upload it.

## Prototype Fund Readiness Score

- Concept clarity: medium.
- Social value framing: medium-high after this update.
- Technical prototype clarity: medium.
- Evidence of activity: high.
- Grant application readiness: not yet.
- Pre-application readiness: yes.

