# LLM / LSC Work Index

This folder tracks the evolution of the LSC theory line and the MHLM analysis.

Current organization:

- `models/iterations/YYYY-MM-DD/` - dated snapshots of the model lineage archive.
- `models/codex/` - Codex outputs, model-specific notes, and artifacts.
- `models/gemini/` - Gemini outputs, model-specific notes, and artifacts.
- `models/gpt/` - GPT outputs, model-specific notes, and artifacts.
- `models/manus/` - Manus integration and packaging notes.
- `models/deepseek/` - DeepSeek deep-review notes and artifacts.
- `models/kimi/` - Kimi long-form synthesis, prompts, and reports.
- `models/openrouter/` - OpenRouter-routed outputs (record underlying model name).
- `models/other/` - future models or manual reviews.
- `reports/daily/YYYY-MM-DD/` - daily synthesis reports.
- `mhlm/` - probability tracking, evidence log, and review notes.
- `ops/` - session-end and emergency checklists.

Latest theory update:

- `the saga continue /6.2.2/` - corrected 6.2.x continuation with explicit trace/anisotropy split and simulation outputs.
- `baza/model_lsc_6_3_0_unified/` - unified LSC 6.3.0 BEST-2 continuation and Zenodo unification plan.

Rules:

- Every report should be dated.
- Every model contribution should be logged in its own folder.
- Every archived snapshot should use a dated iteration folder.
- The daily report should state: model, data used, changes introduced, and whether the change is scientific, editorial, or speculative.
- Do not store raw tokens here.
- At the end of a work session, update the daily report and the model logs.
