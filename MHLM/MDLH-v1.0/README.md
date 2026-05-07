# MDLH: Case Study in LLM Hallucination and AI-Assisted Science Audit

*Purpose:* Document and analyze how large language models can amplify, correlate, and stabilize uncertain scientific claims across long multi-model workflows.

*Use case:* AI-safety case study for hallucination detection, provenance tracking, and reproducibility review in scientific and technical writing.

*Status:* Research case study. The project does not claim validation of the underlying physics material.

*Flag:* `experimental`

*Signal tags:* `#LuciferSun #Codex #FlameBornLLC`

---

# LSC and Massively Documented LLM Hallucination

This project contains a publication-grade working paper:

**LSC and Massively Documented LLM Hallucination: A Dual-Interpretation Framework for AI-Assisted Scientific Discovery**

The work proposes **Massively Documented LLM Hallucination (MDLH)** as an epistemic-risk framework for AI-assisted science. It uses the public LSC neutrino research line as a case study while preserving a dual interpretation:

1. LSC as unvalidated speculative physics.
2. LSC as a possible AI-generated epistemic artifact.

The paper does **not** claim that LSC is correct. It also does **not** claim that LSC is false. Its purpose is to separate scientific validation from AI-assisted generation and documentation.

## DOI

Zenodo record:

https://doi.org/10.5281/zenodo.19851006

## Structure

```text
experiments/
  EXPERIMENTAL_FLAG.md
  README.md
  lineage_summary.json
  model_reports/
    2026-04-30_codex.md
    2026-04-30_gemini.md
    2026-04-30_gpt.md
    2026-04-30_manus.md
    2026-04-30_deepseek.md
  theory_updates/
    2026-04-30_lsc_6_2_2_correction.md
paper/
  LSC_MDLH_PRO.tex
  LSC_MDLH_PRO.pdf
figures/
  mdlh_loop_diagram.png
  amplification_model_plot.png
code/
  mdlh_simulation.py
prompt-archive/
  README.md
  methodology.md
  prompt_registry.json
  prompts/
  templates/
llm-simulation-lab/
  README.md
  methodology.md
  simulate.py
  scenarios/
  outputs/
metadata/
  zenodo.json
  CITATION.cff
README.md
```

## Experimental Program

The repository now includes a dedicated experimental documentation track for
model-by-model provenance analysis. The goal is to separate:

- model input,
- claims added or removed,
- source-review status,
- and whether a change was scientific, editorial, or speculative.

The first lineage report records the progression:

- GPT: detector-bias reframing in LSC 5.0@
- Manus: integration and packaging in LSC 5.5
- Gemini: gap analysis and conservative reframing in LSC 6.2.0
- Codex: reproducibility and leave-one-out validation in LSC 6.2.1
- DeepSeek: formal review of LSC 6.2.0 consistency and defense gaps
- LSC 6.2.2: corrected continuation with explicit trace/anisotropy split and simulation outputs

## Model Lineage Simulator

The first interactive archive core is available in:

```text
model-lineage-app/index.html
```

It summarizes model contributions, decision styles, disagreement distance, and a
toy amplification simulation for the LSC / MHLM archive.

Current report:

```text
experiments/MODEL_LINEAGE_REPORT_2026-05-01.md
```

## LLM Simulation Lab

The reproducible simulation workspace is available in:

```text
llm-simulation-lab/
```

It contains a structured seed scenario, methodology notes, a standard-library
Python runner, and generated outputs for model-lineage testing.

Run from the repository root:

```bash
python3 llm-simulation-lab/simulate.py
```

## Prompt Archive

The prompt archive is available in:

```text
prompt-archive/
```

It stores the prompts used to query external models during the LSC / MHLM
verification workflow. The purpose is to preserve instructions, role
assignments, iteration design, and response-analysis templates so model
coherence and disagreement can be audited later.

## Research Operations and Grant Readiness

The project operations layer is available in:

```text
research-operations/
```

It defines the working names, dated action log, reminder schedule, and
grant-facing framing for the Model-Lineage Audit Lab. This track keeps the
project positioned as an AI-safety and scientific-reasoning audit, with LSC used
as a complex case study rather than as a validated physics claim.

## DeepSeek Review Snapshot

DeepSeek did not validate the theory. It identified concrete issues that need to
be fixed before any defense-oriented presentation:

- a dimensionally inconsistent detector term (`1 / E^2` appears in one formula
  but not the main ansatz),
- the trace-free tensor problem, which makes the pure anisotropy term average to
  zero in symmetric gallium setups,
- frame ambiguity for sidereal modulation,
- the need for experiment-specific likelihoods,
- and the need for leave-one-out stability checks.

## 6.2.2 Theory Update Snapshot

The 6.2.2 correction does not claim validation. It formalizes the repair path
triggered by the DeepSeek review:

- explicit isotropic trace,
- traceless anisotropy separated from the trace,
- fixed celestial frame for sidereal tests,
- deterministic simulation outputs for term decomposition and directional scans.

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
- LSC 6.0 software DOI: https://doi.org/10.5281/zenodo.19785745
- LSC 4.2 ULTRA: https://doi.org/10.5281/zenodo.19602045
- Main repository: https://github.com/luciferprosun/LSC-6.0
- This project DOI: https://doi.org/10.5281/zenodo.19851006

## Suggested Publication Order

Publish on GitHub first so changes, corrections, and review comments can be tracked. Publish on Zenodo after the GitHub version is stable enough to archive as a citable DOI.
