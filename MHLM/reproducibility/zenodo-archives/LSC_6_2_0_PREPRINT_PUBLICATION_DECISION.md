# LSC 6.2.0 Zenodo Publication Decision

Date: 2026-04-29

## Decision

Best publication strategy:

Publish **LSC 6.2.0** as a **new version of the existing LSC 6.0 conceptual Zenodo record**, not as a detached standalone record.

Base record:

- Record: https://zenodo.org/records/19780616
- DOI: https://doi.org/10.5281/zenodo.19780616
- Concept DOI: https://doi.org/10.5281/zenodo.19780615

## Why This Is Best

- LSC 6.2.0 is a direct theoretical continuation of LSC 6.0.
- Zenodo new-version workflow preserves the research lineage under the same concept DOI.
- A new version receives its own version DOI while remaining visibly connected to the prior record.
- This is stronger for grant review than an isolated new record, because it shows continuity, iteration, public archive discipline, and reproducibility.

## Public Framing

LSC 6.2.0 should be described as:

```text
Latest preprint-stage continuation of the LSC 6.0 phenomenological framework.
Prepared for arXiv submission; currently awaiting category endorsement.
Not presented as confirmed new physics.
```

## arXiv Status

Endorsement pending:

https://arxiv.org/auth/endorse?x=7KLAMS

## Prepared Package

Folder:

```text
/home/l/Desktop/LLM/zenodo/LSC_6_2_0_PREPRINT
```

ZIP:

```text
/home/l/Desktop/LLM/zenodo/LSC_6_2_0_PREPRINT_zenodo_package.zip
```

Metadata:

```text
/home/l/Desktop/LLM/zenodo/LSC_6_2_0_PREPRINT/metadata/zenodo.json
/home/l/Desktop/LLM/zenodo/LSC_6_2_0_PREPRINT/metadata/CITATION.cff
/home/l/Desktop/LLM/zenodo/LSC_6_2_0_PREPRINT/metadata/ZENODO_UPLOAD_NOTES.md
```

## Zenodo Draft Created

Draft deposition:

```text
https://zenodo.org/deposit/19878587
```

Reserved version DOI:

```text
10.5281/zenodo.19878587
```

Status:

```text
unsubmitted / not published
```

Uploaded files:

```text
LSC_6_2_0_preprint.pdf
LSC_6_2_0_arxiv_source.zip
main.tex
LSC_6_2_0_model_map.png
LSC_6_2_0_social_preview.png
README.md
CHANGELOG_LSC_6_2_0.md
BUILD_LOG.md
SOURCE_NOTES.txt
zenodo.json
CITATION.cff
ZENODO_UPLOAD_NOTES.md
LSC_6_2_0_PREPRINT_zenodo_package.zip
```

## Final Publish Command

Run only after final approval:

```bash
python3 - <<'PY'
import json, pathlib, urllib.request
token = pathlib.Path('/home/l/.config/zenodo/token').read_text().strip()
req = urllib.request.Request(
    'https://zenodo.org/api/deposit/depositions/19878587/actions/publish',
    data=b'{}',
    headers={
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
        'User-Agent': 'codex-zenodo-publish/1.0',
    },
    method='POST',
)
with urllib.request.urlopen(req, timeout=120) as resp:
    print(resp.status)
    print(resp.read().decode())
PY
```

## Original Manual Zenodo Steps

1. Open the existing LSC 6.0 record:
   https://zenodo.org/records/19780616
2. Choose **New version**.
3. Use title:
   `LSC 6.2.0: A Phenomenological Framework for Neutrino Propagation and Detector-Frame Tensor Anisotropy`
4. Set version:
   `6.2.0-preprint`
5. Set publication type:
   `Preprint`
6. Upload files from:
   `/home/l/Desktop/LLM/zenodo/LSC_6_2_0_PREPRINT`
7. Use metadata from:
   `metadata/zenodo.json`
8. Publish only after final review of wording and files.

## Do Not Do

- Do not claim arXiv acceptance.
- Do not claim confirmed new physics.
- Do not create a disconnected Zenodo record unless the new-version workflow is blocked.
