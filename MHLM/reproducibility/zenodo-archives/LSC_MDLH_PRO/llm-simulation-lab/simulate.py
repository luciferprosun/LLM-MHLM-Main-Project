#!/usr/bin/env python3
"""Run the LSC / MHLM seed simulation.

This script uses only the Python standard library so it can run in minimal
research environments. The numbers are toy-model variables, not empirical
measurements.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parent
SCENARIO = ROOT / "scenarios" / "lsc_mhlm_seed.json"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(parents=True, exist_ok=True)


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def avg(layers: list[dict], key: str) -> float:
    return mean(layer["scores"][key] for layer in layers)


def pairwise_distance(left: dict, right: dict) -> float:
    keys = left["scores"].keys()
    total = 0.0
    for key in keys:
        diff = left["scores"][key] - right["scores"][key]
        total += diff * diff
    return math.sqrt(total / len(left["scores"]))


def run_simulation(scenario: dict) -> list[dict[str, float]]:
    layers = scenario["layers"]
    validation = max(0.05, float(scenario["validation_strength"]))
    expert_review = max(0.05, float(scenario["expert_review_strength"]))
    iterations = int(scenario["iterations"])
    model_count = len(layers)

    coherence_seed = avg(layers, "coherence") * 0.45
    apparent_coherence = coherence_seed
    audit_pressure = avg(layers, "validation_pressure") * 0.15
    hallucination_risk = avg(layers, "hallucination_risk") * 1.15

    rows: list[dict[str, float]] = []
    for step in range(1, iterations + 1):
        surface_complexity = 1.0 + step * (avg(layers, "coherence") + avg(layers, "novelty")) * 0.55
        amplification = (model_count * step * surface_complexity) / (validation * expert_review)
        review_force = (validation + expert_review + avg(layers, "validation_pressure")) / 3.0
        disagreement_force = avg(layers, "disagreement")

        apparent_coherence = clamp(
            apparent_coherence
            + math.log1p(amplification) * 0.016
            + avg(layers, "coherence") * 0.014
            - disagreement_force * 0.006
        )
        audit_pressure = clamp(audit_pressure + review_force * 0.055)
        hallucination_risk = clamp(
            hallucination_risk
            + math.log1p(amplification) * 0.011
            - review_force * 0.082
            - avg(layers, "conservatism") * 0.018
        )

        rows.append(
            {
                "step": step,
                "model_count": model_count,
                "surface_complexity": round(surface_complexity, 6),
                "amplification": round(amplification, 6),
                "apparent_coherence": round(apparent_coherence, 6),
                "audit_pressure": round(audit_pressure, 6),
                "hallucination_risk": round(hallucination_risk, 6),
            }
        )

    return rows


def write_csv(rows: list[dict[str, float]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def write_report(scenario: dict, rows: list[dict[str, float]], path: Path) -> None:
    layers = scenario["layers"]
    last = rows[-1]
    distances = []
    for idx, left in enumerate(layers):
        for right in layers[idx + 1 :]:
            distances.append(pairwise_distance(left, right))

    lines = [
        f"# {scenario['title']} - Simulation Report",
        "",
        f"Date: {scenario['date']}",
        f"Status: {scenario['status']}",
        "",
        "## Inputs",
        "",
        f"- Model layers: {len(layers)}",
        f"- Iterations: {scenario['iterations']}",
        f"- Validation strength: {scenario['validation_strength']}",
        f"- Expert review strength: {scenario['expert_review_strength']}",
        "",
        "## Final State",
        "",
        f"- Amplification: {last['amplification']}",
        f"- Apparent coherence: {last['apparent_coherence']}",
        f"- Audit pressure: {last['audit_pressure']}",
        f"- Hallucination risk: {last['hallucination_risk']}",
        f"- Mean pairwise decision distance: {round(mean(distances), 6)}",
        "",
        "## Layer Summary",
        "",
    ]

    for layer in layers:
        lines.extend(
            [
                f"### {layer['name']} - {layer['phase']}",
                "",
                f"- Role: {layer['role']}",
                f"- Decision: {layer['decision']}",
                f"- Novelty: {layer['scores']['novelty']}",
                f"- Conservatism: {layer['scores']['conservatism']}",
                f"- Validation pressure: {layer['scores']['validation_pressure']}",
                f"- Hallucination risk: {layer['scores']['hallucination_risk']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Interpretation",
            "",
            "The seed scenario shows a transition from constructive theory building",
            "toward conservative review and formal repair. Model agreement is not",
            "treated as validation. It is treated as an object of audit.",
            "",
            "Signal tags: `#LuciferSun #Codex #FlameBornLLC`",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    scenario = json.loads(SCENARIO.read_text(encoding="utf-8"))
    rows = run_simulation(scenario)
    write_csv(rows, OUTPUTS / "lsc_mhlm_seed_timeseries.csv")
    write_report(scenario, rows, OUTPUTS / "lsc_mhlm_seed_report.md")
    print(f"Wrote {OUTPUTS / 'lsc_mhlm_seed_timeseries.csv'}")
    print(f"Wrote {OUTPUTS / 'lsc_mhlm_seed_report.md'}")


if __name__ == "__main__":
    main()
