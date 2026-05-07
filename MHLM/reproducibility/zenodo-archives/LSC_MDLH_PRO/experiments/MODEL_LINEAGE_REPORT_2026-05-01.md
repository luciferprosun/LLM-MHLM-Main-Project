# LSC / MHLM Model Lineage Report - 2026-05-01

Status: experimental archive core

This report summarizes the first model-lineage archive for the LSC / MHLM
project. It is not a validation claim. It records how different AI systems
changed the theory line, where they agreed, where they disagreed, and how the
archive can simulate correlated confidence versus real review pressure.

## Summary

The current archive shows a staged pattern:

- GPT and Manus mainly amplified, integrated, and narratively stabilized the
  LSC theory line.
- Gemini shifted the project toward conservative uncertainty handling.
- Codex converted part of the theory into reproducible diagnostics and exposed
  weak leave-one-out stability.
- DeepSeek supplied the most formal critique, identifying dimension,
  tensor-average, and frame-definition problems.
- LSC 6.2.2 became the repair layer: useful as formal correction, not as
  confirmation.

The central MHLM signal is that apparent coherence can grow through repeated
model interaction before external validation exists. For this reason, model
agreement is treated as evidence to audit, not evidence of truth.

## Model Contributions

| Layer | LSC phase | Main effect | Scientific status |
| --- | --- | --- | --- |
| GPT | LSC 5.0@ | Reframed anomaly language toward detector-side energy misestimation | Historical, not validation |
| Manus | LSC 5.5 | Integrated propagation and detector-side lines into a preprint package | Packaging, not validation |
| Gemini | LSC 6.2.0 | Forced true/reconstructed energy separation and explicit uncertainty | Conservative review |
| Codex | LSC 6.2.1 | Built reproducible diagnostics and leave-one-out checks | Validation-layer critique |
| DeepSeek | LSC 6.2.0 review | Found formal consistency problems requiring repair | Source-backed critique |
| LSC 6.2.2 | Correction layer | Split isotropic trace from traceless anisotropy and added simulations | Repair, not validation |

## Decision Pattern

The first two layers increased coherence and publication readiness. The later
layers increased disagreement, validation pressure, and falsification pressure.
That transition is valuable: it gives the project a measurable archive of how
AI-generated scientific structure can be strengthened, challenged, and repaired.

## Simulation Core

The first application prototype is in:

```text
model-lineage-app/index.html
```

It models:

- apparent coherence,
- hallucination-risk pressure,
- validation pressure,
- pairwise model disagreement,
- model decision vectors,
- amplification under weak versus strong review.

The current simulation is a toy model. It is designed as the trunk of a future
application where new model reports, prompts, outputs, and source citations can
be added over time.

## Next Build Steps

1. Add import/export for model reports.
2. Add source-citation scoring per claim.
3. Add prompt lineage and response lineage views.
4. Add claim-level agreement/disagreement clustering.
5. Publish a live GitHub Pages demo once the app is stable.

Signal tags: `#LuciferSun #Codex #FlameBornLLC`
