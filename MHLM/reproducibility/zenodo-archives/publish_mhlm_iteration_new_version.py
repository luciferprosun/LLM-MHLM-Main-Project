#!/usr/bin/env python3
"""Publish a new Zenodo version for the MHLM/MDLH iteration archive."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


API = "https://zenodo.org/api"
SOURCE_DEPOSITION_ID = 19851006
TOKEN_FILE = os.path.expanduser("~/.config/zenodo/token")
EXPECTED_CONCEPT_DOI = "10.5281/zenodo.19851005"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PACKAGE = os.path.join(BASE_DIR, "LSC_MDLH_PRO_zenodo_package_iterations_2026-05-05.zip")
NOTE = os.path.join(BASE_DIR, "MHLM_ITERATION_ARCHIVE_EXTENSION_2026-05-05.md")
PDF = os.path.join(BASE_DIR, "LSC_MDLH_PRO", "paper", "LSC_MDLH_PRO.pdf")


METADATA = {
    "metadata": {
        "title": (
            "LSC and Massively Documented LLM Hallucination: "
            "Prompt Archive, Simulation Lab, and Model-Lineage Extension"
        ),
        "upload_type": "publication",
        "publication_type": "workingpaper",
        "publication_date": "2026-05-05",
        "description": (
            "<p>This new version extends the MHLM / MDLH publication with a "
            "curated model-lineage archive for the LSC theory-building process. "
            "It adds prompt provenance, dated LLM iteration snapshots, "
            "model-specific theory tracks, an experimental simulation lab, "
            "and grant-facing audit material.</p>"
            "<p>The 2026-05-05 archive adds "
            "<code>iterations/LSC_theory_by_LLM/</code>, preserving final "
            "views and supporting artifacts for Codex, DeepSeek, Gemini, GPT, "
            "Kimi, Manus, and related model slots. The update improves audit "
            "transparency around model agreement, correction paths, hallucination "
            "risk, and overclaim pressure.</p>"
            "<p>This version does not claim that the LSC physics line is "
            "validated. It keeps the dual interpretation of the original record: "
            "LSC remains an unvalidated physics hypothesis requiring independent "
            "testing, while the same archive is used as a documented AI-safety "
            "case study in Massively Documented LLM Hallucination.</p>"
        ),
        "creators": [
            {
                "name": "LuciferSun",
                "affiliation": "Independent Research",
            }
        ],
        "access_right": "open",
        "license": "cc-by-4.0",
        "version": "1.2.0-prompt-simulation-lab",
        "language": "eng",
        "keywords": [
            "large language models",
            "AI safety",
            "hallucination",
            "scientific epistemology",
            "open science",
            "neutrino physics",
            "LSC",
            "AI-assisted research",
            "model lineage",
            "prompt archive",
            "reproducibility",
        ],
        "related_identifiers": [
            {
                "identifier": "10.5281/zenodo.19851006",
                "relation": "isNewVersionOf",
                "scheme": "doi",
            },
            {
                "identifier": "10.5281/zenodo.19780615",
                "relation": "references",
                "scheme": "doi",
            },
            {
                "identifier": "10.5281/zenodo.20037838",
                "relation": "references",
                "scheme": "doi",
            },
            {
                "identifier": "https://github.com/luciferprosun/LSC_MDLH_PRO",
                "relation": "isSupplementedBy",
                "scheme": "url",
            },
            {
                "identifier": "https://github.com/luciferprosun/LSC-the-saga-continue",
                "relation": "isSupplementedBy",
                "scheme": "url",
            },
        ],
        "notes": (
            "New version adding the 2026-05-05 LSC_theory_by_LLM iteration "
            "archive and audit materials. This is an AI-research and provenance "
            "update, not a validation claim for LSC physics."
        ),
    }
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def token() -> str:
    value = os.environ.get("ZENODO_TOKEN")
    if not value and os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r", encoding="utf-8") as handle:
            value = handle.read().strip()
    if not value:
        fail("Missing Zenodo token. Set ZENODO_TOKEN or ~/.config/zenodo/token.")
    return value


def request_json(method: str, url: str, auth: str | None, data: dict | None = None) -> dict:
    body = None
    headers = {"Accept": "application/json"}
    if auth:
        headers["Authorization"] = f"Bearer {auth}"
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            payload = response.read().decode("utf-8")
            return json.loads(payload) if payload else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        fail(f"{method} {url} failed with HTTP {exc.code}: {detail}")
    except urllib.error.URLError as exc:
        fail(f"{method} {url} failed: {exc}")


def request_empty(method: str, url: str, auth: str) -> None:
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {auth}"}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120):
            return
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        fail(f"{method} {url} failed with HTTP {exc.code}: {detail}")
    except urllib.error.URLError as exc:
        fail(f"{method} {url} failed: {exc}")


def upload_file(bucket_url: str, path: str, auth: str, name: str | None = None) -> None:
    filename = name or os.path.basename(path)
    url = bucket_url.rstrip("/") + "/" + urllib.parse.quote(filename)
    with open(path, "rb") as handle:
        data = handle.read()
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {auth}",
            "Content-Type": "application/octet-stream",
        },
        method="PUT",
    )
    try:
        with urllib.request.urlopen(req, timeout=300):
            return
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        fail(f"PUT {url} failed with HTTP {exc.code}: {detail}")
    except urllib.error.URLError as exc:
        fail(f"PUT {url} failed: {exc}")


def ensure_files() -> None:
    for path in [PACKAGE, NOTE, PDF]:
        if not os.path.exists(path):
            fail(f"Required file is missing: {path}")


def main() -> None:
    ensure_files()
    auth = token()

    record = request_json("GET", f"{API}/records/{SOURCE_DEPOSITION_ID}", None)
    if record.get("conceptdoi") != EXPECTED_CONCEPT_DOI:
        fail(f"Unexpected concept DOI: {record.get('conceptdoi')!r}")

    new_version = request_json(
        "POST",
        f"{API}/deposit/depositions/{SOURCE_DEPOSITION_ID}/actions/newversion",
        auth,
    )
    draft_url = new_version.get("links", {}).get("latest_draft")
    if not draft_url:
        fail("Zenodo did not return latest_draft link.")

    draft = request_json("GET", draft_url, auth)
    draft_id = draft.get("id")
    if not draft_id:
        fail("Draft ID missing after newversion.")

    for item in draft.get("files", []):
        name = item.get("filename") or item.get("key") or ""
        if name.endswith(".zip"):
            file_url = item.get("links", {}).get("self")
            if file_url:
                request_empty("DELETE", file_url, auth)

    draft = request_json("PUT", f"{API}/deposit/depositions/{draft_id}", auth, METADATA)
    bucket = draft.get("links", {}).get("bucket")
    if not bucket:
        fail("Draft bucket link missing.")

    upload_file(bucket, PDF, auth, "LSC_MDLH_PRO.pdf")
    upload_file(bucket, PACKAGE, auth)
    upload_file(bucket, NOTE, auth)

    published = request_json(
        "POST",
        f"{API}/deposit/depositions/{draft_id}/actions/publish",
        auth,
    )

    print(json.dumps({
        "published_id": published.get("id"),
        "submitted": published.get("submitted"),
        "doi": published.get("doi"),
        "conceptdoi": published.get("conceptdoi"),
        "title": published.get("metadata", {}).get("title"),
        "version": published.get("metadata", {}).get("version"),
        "html": published.get("links", {}).get("html"),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
