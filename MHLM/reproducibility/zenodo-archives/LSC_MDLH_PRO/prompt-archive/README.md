# Prompt Archive

Status: experimental research infrastructure

The Prompt Archive stores the prompts used to query external AI systems during
the LSC / MHLM model-lineage audit. It is designed to make model behavior
inspectable across iterations, providers, and scientific roles.

## Purpose

This archive supports two linked research goals:

1. LSC development: identify whether external models can improve, falsify, or
   repair the LSC neutrino-anomaly framework.
2. MHLM / MDLH audit: test whether model outputs converge because the theory is
   becoming stronger, or because multiple systems stabilize the same unvalidated
   narrative.

## Scope

The archive records:

- prompt text,
- target model,
- assigned model role,
- iteration number,
- expected output schema,
- links to project context,
- later response-analysis metadata.

The archive does not treat model agreement as validation. Agreement, divergence,
correction, refusal, and hallucination are all research signals.

## Directory Structure

```text
prompt-archive/
  README.md
  methodology.md
  prompt_registry.json
  prompts/
    2026-05-01_iteration_1_gemini.md
    2026-05-01_iteration_1_gpt.md
    2026-05-01_iteration_1_deepseek.md
    2026-05-01_iteration_1_manus_telegram.md
    2026-05-01_iteration_2_cross_review.md
    2026-05-01_iteration_3_final_verdict.md
  templates/
    response_analysis_template.md
```

## Project Context Links

- Public archive: https://akasha-chronicles.pages.dev
- Model Lineage Simulator: https://luciferprosun.github.io/akasha-chronicles/model-lineage/
- LSC repository: https://github.com/luciferprosun/LSC-6.0
- MHLM / MDLH repository: https://github.com/luciferprosun/LSC_MDLH_PRO
- LSC 6.2.0 preprint: https://doi.org/10.5281/zenodo.19878587
- MHLM / MDLH record: https://doi.org/10.5281/zenodo.19851006

Signal tags: `#LuciferSun #Codex #FlameBornLLC`
