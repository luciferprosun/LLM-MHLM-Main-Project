#!/usr/bin/env python3
"""Minimal simulation for the MDLH epistemic amplification model.

The script intentionally uses only Python's standard library. It models how
surface complexity and multi-model iteration can grow when validation and
expert review are weak. The output is not empirical evidence; it is a toy model
for reasoning about when an AI-assisted research loop should be treated as a
risk state rather than validation.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)


def amplification_factor(
    n_models: float,
    n_iterations: float,
    surface_complexity: float,
    validation: float,
    expert_review: float,
) -> float:
    """Return the proposed epistemic amplification factor.

    Small epsilons avoid division by zero while preserving the intended
    asymptotic behavior: amplification grows when validation or expert review
    approaches zero.
    """

    eps = 1e-9
    return (n_models * n_iterations * surface_complexity) / (
        max(validation, eps) * max(expert_review, eps)
    )


def simulate_loop(
    n_models: int,
    validation: float,
    expert_review: float,
    steps: int = 12,
    surface_seed: float = 1.0,
) -> list[dict[str, float]]:
    """Simulate an MDLH loop over several documentation iterations."""

    rows: list[dict[str, float]] = []
    surface = surface_seed
    documented_state = 1.0
    for t in range(steps + 1):
        ae = amplification_factor(n_models, max(t, 1), surface, validation, expert_review)
        damping = validation + expert_review
        growth = 1.0 + 0.035 * math.log1p(ae) - 0.06 * damping
        documented_state = max(0.0, documented_state * growth)
        surface = surface * (1.0 + 0.05 * n_models / (1.0 + validation + expert_review))
        rows.append(
            {
                "step": float(t),
                "n_models": float(n_models),
                "validation": validation,
                "expert_review": expert_review,
                "surface_complexity": surface,
                "amplification": ae,
                "documented_state": documented_state,
            }
        )
    return rows


def write_csv(rows: list[dict[str, float]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def polyline(points: list[tuple[float, float]], color: str) -> str:
    joined = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<polyline points="{joined}" fill="none" stroke="{color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'


def write_svg_plot(series: dict[str, list[dict[str, float]]], path: Path) -> None:
    width, height = 1200, 760
    left, right, top, bottom = 90, 50, 80, 90
    plot_w = width - left - right
    plot_h = height - top - bottom
    max_step = max(row["step"] for rows in series.values() for row in rows)
    max_amp = max(row["amplification"] for rows in series.values() for row in rows)
    max_y = max(10.0, max_amp)

    def sx(step: float) -> float:
        return left + (step / max_step) * plot_w

    def sy(value: float) -> float:
        # log scale for readability
        v = math.log10(value + 1.0)
        vmax = math.log10(max_y + 1.0)
        return top + plot_h - (v / vmax) * plot_h

    colors = ["#2563eb", "#dc2626", "#16a34a", "#9333ea"]
    lines = []
    legend = []
    for idx, (name, rows) in enumerate(series.items()):
        color = colors[idx % len(colors)]
        pts = [(sx(row["step"]), sy(row["amplification"])) for row in rows]
        lines.append(polyline(pts, color))
        y = 135 + idx * 34
        legend.append(f'<line x1="840" y1="{y}" x2="895" y2="{y}" stroke="{color}" stroke-width="5"/>')
        legend.append(f'<text x="910" y="{y + 7}" font-size="24" fill="#172033">{name}</text>')

    grid = []
    for i in range(6):
        y = top + i * plot_h / 5
        grid.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + plot_w}" y2="{y:.1f}" stroke="#d5dde8" stroke-width="1"/>')
    for i in range(7):
        x = left + i * plot_w / 6
        grid.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top + plot_h}" stroke="#eef2f7" stroke-width="1"/>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="#f8fafc"/>
  <text x="70" y="48" font-family="Arial, sans-serif" font-size="34" font-weight="700" fill="#0f172a">MDLH Amplification vs Validation</text>
  <text x="70" y="84" font-family="Arial, sans-serif" font-size="20" fill="#475569">Amplification rises when model count and iteration increase while validation remains weak.</text>
  <rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="#ffffff" stroke="#cbd5e1"/>
  {"".join(grid)}
  <line x1="{left}" y1="{top + plot_h}" x2="{left + plot_w}" y2="{top + plot_h}" stroke="#0f172a" stroke-width="2"/>
  <line x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_h}" stroke="#0f172a" stroke-width="2"/>
  {"".join(lines)}
  <text x="{left + plot_w / 2 - 80}" y="{height - 30}" font-family="Arial, sans-serif" font-size="24" fill="#0f172a">Iteration step</text>
  <text x="24" y="{top + plot_h / 2 + 140}" transform="rotate(-90 24,{top + plot_h / 2 + 140})" font-family="Arial, sans-serif" font-size="24" fill="#0f172a">Amplification factor, log scale</text>
  {"".join(legend)}
  <text x="90" y="720" font-family="Arial, sans-serif" font-size="16" fill="#64748b">Toy model: A_e = (N_models * N_iterations * Surface_complexity) / (Validation * Expert_review)</text>
</svg>
'''
    path.write_text(svg, encoding="utf-8")


def main() -> None:
    scenarios = {
        "weak validation": simulate_loop(n_models=6, validation=0.25, expert_review=0.25),
        "moderate validation": simulate_loop(n_models=6, validation=1.0, expert_review=1.0),
        "strong validation": simulate_loop(n_models=6, validation=2.0, expert_review=2.0),
    }
    all_rows = [row for rows in scenarios.values() for row in rows]
    write_csv(all_rows, FIGURES / "amplification_simulation.csv")
    write_svg_plot(scenarios, FIGURES / "amplification_model_plot.svg")
    print(f"Wrote {FIGURES / 'amplification_simulation.csv'}")
    print(f"Wrote {FIGURES / 'amplification_model_plot.svg'}")


if __name__ == "__main__":
    main()
