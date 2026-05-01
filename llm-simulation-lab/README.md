# LLM Simulation Lab

Status: experimental

This directory is the reproducible simulation workspace for the LSC / MHLM
model-lineage archive. It is designed to test how multiple language-model
layers can amplify, correct, or constrain a scientific claim over time.

The lab does not validate the LSC physics line. It provides a controlled
simulation layer for studying model agreement, disagreement, validation
pressure, and hallucination-risk pressure.

## Purpose

- Archive model-level decisions as structured data.
- Simulate how coherence can increase before external validation.
- Compare constructive, integrative, conservative, reproducibility-focused, and
  adversarial review roles.
- Produce small reproducible outputs that can be inspected, versioned, and
  extended.

## Current Files

```text
llm-simulation-lab/
  README.md
  methodology.md
  simulate.py
  scenarios/
    lsc_mhlm_seed.json
  outputs/
    lsc_mhlm_seed_report.md
    lsc_mhlm_seed_timeseries.csv
```

## Run

From the repository root:

```bash
python3 llm-simulation-lab/simulate.py
```

The script reads:

```text
llm-simulation-lab/scenarios/lsc_mhlm_seed.json
```

and writes:

```text
llm-simulation-lab/outputs/lsc_mhlm_seed_report.md
llm-simulation-lab/outputs/lsc_mhlm_seed_timeseries.csv
```

## Interpretation

The simulation tracks four values:

- `apparent_coherence`: how coherent the model-generated archive appears.
- `audit_pressure`: how much review and falsification pressure is present.
- `hallucination_risk`: estimated pressure toward unsupported stabilization.
- `amplification`: toy-model multiplier driven by model count, iteration,
  coherence, and weak review.

These values are not empirical measurements. They are working variables for
building a more rigorous future benchmark.

Signal tags: `#LuciferSun #Codex #FlameBornLLC`
