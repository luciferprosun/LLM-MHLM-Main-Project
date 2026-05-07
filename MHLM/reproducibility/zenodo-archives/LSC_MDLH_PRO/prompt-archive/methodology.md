# Prompt Archive Methodology

The prompt archive is a controlled record of model instructions. It is part of
the LSC / MHLM verification workflow.

## Research Question

When multiple AI systems receive the same research context, do their responses:

- converge on the same correction,
- disagree in scientifically meaningful ways,
- amplify unsupported claims,
- identify hidden assumptions,
- or generate a stable but unvalidated narrative?

## Iteration Design

### Iteration 1: Independent Review

Each model receives the same project context links but a different assigned
role. The goal is independent model behavior, not consensus.

Roles:

- Gemini: conservative scientific reviewer.
- GPT: theory-development assistant and scientific editor.
- DeepSeek: adversarial formal reviewer.
- Manus / Telegram: research-operations integrator.

### Iteration 2: Cross-Review

Each model receives summaries of the other outputs. It must revise its previous
position and identify meaningful disagreements.

### Iteration 3: Final Verdict

Each model gives a final decision on what should be developed, weakened,
removed, tested, or archived as MHLM / MDLH evidence.

## Response Scoring

Responses should later be scored on:

- `physics_usefulness`
- `mathematical_rigor`
- `validation_pressure`
- `overclaim_reduction`
- `novelty`
- `source_discipline`
- `hallucination_risk`
- `model_disagreement_value`

Scores are working variables, not empirical proof.

## Guardrails

- LSC is not treated as validated physics.
- MHLM / MDLH is not treated as proof that the LSC line is false.
- Model agreement is never validation by itself.
- Prompt wording must be preserved before response analysis.
- Later edits to prompts must be versioned as new prompt files.

## Public/Private Boundary

Public:

- prompt text,
- project context links,
- role assignments,
- response-analysis templates,
- non-sensitive model-lineage summaries.

Internal until reviewed:

- raw private conversations,
- personal context,
- credentials,
- unpublished claims,
- speculative outreach strategy.
