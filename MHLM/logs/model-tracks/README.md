# Model-Specific Review Folders

Use these folders to separate what each model contributed to the theory line.

## Iterations

Use `iterations/YYYY-MM-DD/` for dated snapshots of the model archive.
Each iteration should contain one lowercase folder per model and date-stamped
final artifacts.

## Codex

- reproducible analysis
- code changes
- fit diagnostics
- numerical checks

## Gemini

- literature synthesis
- alternative derivations
- gap analysis
- source checks

## GPT

- narrative cleanup
- report drafting
- synthesis from prior notes
- editorial alignment

## Manus

- Track Manus-generated integration and packaging work from the 5.5 phase.

## DeepSeek

- Track DeepSeek deep-review outputs and source-gap checks.

## Kimi

- Track Kimi/Qwen-style long-form synthesis and prompt-driven reports.

## OpenRouter

- Track outputs produced via OpenRouter (model-routing wrapper), including the exact model name in filenames or notes.

## Other

- use for future models or manual human review

Format for each model folder:

- `README.md` - what this model is responsible for
- `notes.md` - dated notes on what it changed
- `artifacts/` - PDFs, tables, exports, screenshots, or reports

For iteration snapshots, use:

- `YYYY-MM-DD_FINAL_<MODEL>.md`
- `YYYY-MM-DD_FINAL_<MODEL>.pdf`
