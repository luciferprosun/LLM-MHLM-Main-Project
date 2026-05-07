# LSC and Massively Documented LLM Hallucination

This project contains a publication-grade working paper:

**LSC and Massively Documented LLM Hallucination: A Dual-Interpretation Framework for AI-Assisted Scientific Discovery**

The work proposes **Massively Documented LLM Hallucination (MDLH)** as an epistemic-risk framework for AI-assisted science. It uses the public LSC neutrino research line as a case study while preserving a dual interpretation:

1. LSC as unvalidated speculative physics.
2. LSC as a possible AI-generated epistemic artifact.

The paper does **not** claim that LSC is correct. It also does **not** claim that LSC is false. Its purpose is to separate scientific validation from AI-assisted generation and documentation.

## Structure

```text
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

## Suggested Publication Order

Publish on GitHub first so changes, corrections, and review comments can be tracked. Publish on Zenodo after the GitHub version is stable enough to archive as a citable DOI.
