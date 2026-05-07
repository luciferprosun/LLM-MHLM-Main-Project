# LSC and Massively Documented LLM Hallucination

This project contains a publication-grade working paper:

**LSC and Massively Documented LLM Hallucination: A Dual-Interpretation Framework for AI-Assisted Scientific Discovery**

The work proposes **Massively Documented LLM Hallucination (MDLH)** as an epistemic-risk framework for AI-assisted science. It uses the public LSC neutrino research line as a case study while preserving a dual interpretation:

1. LSC as unvalidated speculative physics.
2. LSC as a possible AI-generated epistemic artifact.

The paper does **not** claim that LSC is correct. It also does **not** claim that LSC is false. Its purpose is to separate scientific validation from AI-assisted generation and documentation.

## 2026-05-05 Archive Extension

This package extends the public MHLM / MDLH record with a curated archive layer
for model-specific theory development and hallucination-audit provenance.

The added public archive components are:

- `experiments/` - model-lineage reports and theory-update notes,
- `prompt-archive/` - prompts, templates, and prompt registry,
- `llm-simulation-lab/` - reproducible simulation workspace and outputs,
- `model-lineage-app/` - lightweight browser app for the lineage case study,
- `mhlm/` - evidence log, probability log, and contribution tracking,
- `iterations/LSC_theory_by_LLM/` - dated snapshots and model tracks for the
  LSC theory line,
- `grant/` - grant-facing framing notes suitable for prototype discussions,
- `updates/` - extension notes describing what changed in this Zenodo package.

The purpose of the extension is to make the MHLM publication usable as a
grant-facing archive of AI-assisted scientific reasoning, while preserving a
clear distinction between:

1. theory development,
2. model-to-model reinforcement,
3. formal correction pressure,
4. and empirical validation status.

## Structure

```text
experiments/
prompt-archive/
llm-simulation-lab/
model-lineage-app/
mhlm/
iterations/
  LSC_theory_by_LLM/
grant/
updates/
paper/
  LSC_MDLH_PRO.tex
  LSC_MDLH_PRO.pdf
figures/
  mdlh_loop_diagram.png
  amplification_model_plot.png
code/
  mdlh_simulation.py
metadata/
  zenodo.json
  CITATION.cff
README.md
```

## Iteration Archive

The public iteration archive is now available in:

```text
iterations/LSC_theory_by_LLM/
```

It contains:

- `2026-05-05/` - a dated snapshot of final views from Codex, DeepSeek,
  Gemini, GPT, Kimi, Manus, and other model slots,
- `model_tracks/` - per-model notes, role definitions, and selected artifacts
  showing how the theory line evolved across models.

This archive is intended for provenance review and grant-facing auditability.
It is not a claim that model agreement validates the theory.

## Build Paper

From the project root:

```bash
cd paper
pdflatex LSC_MDLH_PRO.tex
pdflatex LSC_MDLH_PRO.tex
```

## Reproduce Amplification Figure

```bash
python3 code/mdlh_simulation.py
rsvg-convert -w 1200 -h 760 figures/amplification_model_plot.svg -o figures/amplification_model_plot.png
```

## Case Materials Referenced

- LSC Framework v1.2.0: https://doi.org/10.5281/zenodo.19843361
- LSC 6.0 working paper: https://doi.org/10.5281/zenodo.19780616
- LSC concept DOI: https://doi.org/10.5281/zenodo.19780615
- LSC 6.3.0 unified continuation: https://doi.org/10.5281/zenodo.20037838
- LSC 6.0 software DOI: https://doi.org/10.5281/zenodo.19785745
- LSC 4.2 ULTRA: https://doi.org/10.5281/zenodo.19602045
- Main repository: https://github.com/luciferprosun/LSC-6.0
- Continuation archive: https://github.com/luciferprosun/LSC-the-saga-continue

## Suggested Publication Order

Publish on GitHub first so changes, corrections, and review comments can be tracked. Publish on Zenodo after the GitHub version is stable enough to archive as a citable DOI.
