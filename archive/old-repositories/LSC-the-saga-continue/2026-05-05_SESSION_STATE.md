# Session State - 2026-05-05

## Status

Scalone archiwum MHLM/LLM jest teraz trzymane kanonicznie w:

- `the saga continue/mhlm_ai_research/LLM-MHLM/`

## Co zrobione dzisiaj

- Skopiowano strukturę `LLM` z `Desktop/na poniedzialek/USB_LSC_WORKSPACE/02_MHLM/LLM` do `the saga continue/mhlm_ai_research/LLM-MHLM/`.
- Dodano brakujące modele w strukturze: `kimi` i `openrouter`.
- Wciągnięto surowe odpowiedzi modeli do `models/*/incoming/YYYY-MM-DD/` bez nadpisywania istniejących artefaktów.

## Następny krok (konkret)

1. Dodać dzienny raport syntezy do `the saga continue/mhlm_ai_research/LLM-MHLM/reports/daily/2026-05-05/`.
2. Z “incoming” wyciągnąć wnioski i dopisać je do:
   - `the saga continue/mhlm_ai_research/LLM-MHLM/mhlm/evidence_log.md`
   - `the saga continue/mhlm_ai_research/LLM-MHLM/mhlm/probability_log.md`
3. Jeśli potwierdzimy duplikaty poza `the saga continue/`, dopiero wtedy usuwać kopie z `Desktop/` (po ręcznej akceptacji).

## Update po kontynuacji LSC

Dodano kontrolowany pakiet:

- `baza/model_lsc_6_3_0_unified/LSC_6_3_0_UNIFIED_BEST2_UPDATE.md`
- `baza/model_lsc_6_3_0_unified/ZENODO_UNIFICATION_PLAN.md`
- `baza/model_lsc_6_3_0_unified/zenodo_6_3_0_metadata.json`
- `baza/model_lsc_6_3_0_unified/LSC_6_3_0_unified_zenodo_package.zip`
- `mhlm_ai_research/LLM-MHLM/reports/daily/2026-05-05/LSC_6_3_0_UNIFIED_CONTINUATION_REPORT.md`

Wniosek Zenodo:

- LSC 6.0 i LSC 6.2.0 są już jednym projektem przez concept DOI `10.5281/zenodo.19780615`.
- `LSC Framework v1.2.0` jest osobnym rekordem i powinien zostać opisany jako suplement/reproducibility release.
- Jeśli unikamy nowego DOI, wolno robić tylko metadata-only update rekordu `19878587`.
- Jeśli dodajemy nowy ZIP/PDF jako pliki, Zenodo utworzy nowy version DOI, ale pozostanie ten sam concept DOI.

## Publikacja Zenodo wykonana

- Record: `https://zenodo.org/records/20037838`
- Version DOI: `https://doi.org/10.5281/zenodo.20037838`
- Concept DOI: `https://doi.org/10.5281/zenodo.19780615`
- GitHub commit przed publikacją: `b625fbe`
