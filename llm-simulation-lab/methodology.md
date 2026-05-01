# Methodology

The LLM Simulation Lab treats each model contribution as a decision layer.
Each layer is assigned structured scores between `0.0` and `1.0`.

## Decision Vector

Each model layer currently has six dimensions:

- `novelty`: how much new theory structure the layer introduced.
- `conservatism`: how much the layer reduced overclaiming.
- `validation_pressure`: how much it pushed toward testing, falsification, or
  reproducibility.
- `hallucination_risk`: how much the layer may have stabilized unsupported
  structure.
- `coherence`: how much it made the archive internally consistent.
- `disagreement`: how much it diverged from previous framing.

## Simulation Logic

The simulation is intentionally small and auditable. At each step it estimates:

```text
amplification =
  model_count * step * surface_complexity
  / (validation_strength * expert_review_strength)
```

Then it updates:

- apparent coherence,
- audit pressure,
- hallucination-risk pressure.

Strong validation and expert review damp hallucination risk. Model count,
iteration count, and high surface complexity increase amplification.

## Guardrails

- The simulation is not evidence that LSC is true.
- Agreement between models is not treated as validation.
- Disagreement is preserved as useful audit data.
- Repair layers are labeled as repair, not proof.

## Next Extensions

1. Add claim-level scoring.
2. Add source-citation quality per claim.
3. Add prompt and response hashes.
4. Add model-to-model contradiction clustering.
5. Add reviewer-weighted validation scores.
6. Add export to the interactive `model-lineage-app`.
