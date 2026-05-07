from __future__ import annotations

import csv
import json
import shutil
import subprocess
from pathlib import Path

from lsc621.data import DATASET_PATH, build_observations, load_dataset
from lsc621.model import run_analysis
from lsc621.simulations import run_simulations
from lsc621.report import render_markdown, render_tex


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "out"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def render_simulation_markdown(summary) -> str:
    lines: list[str] = []
    lines.append("# LSC 6.2.2 Simulation Diagnostics")
    lines.append("")
    lines.append("## Directional Scan")
    lines.append("")
    lines.append("| label | linear bias | quadratic bias | normalization | mean(mu) | mean(traceless) |")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: |")
    for row in summary.scenario_rows:
        lines.append(
            f"| {row.label} | {row.linear_bias:+.6f} | {row.quadratic_bias:+.6f} | {row.normalization:.6f} | {row.mean_mu:+.6f} | {row.mean_traceless:+.6f} |"
        )
    lines.append("")
    lines.append("## Dominant Term Per Observation")
    lines.append("")
    lines.append("| observation | dominant term | contribution | abs share |")
    lines.append("| --- | --- | ---: | ---: |")
    for row in summary.dominant_rows:
        lines.append(
            f"| {row.observation} | {row.term} | {row.contribution:+.6f} | {row.abs_share:.3f} |"
        )
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append(
        "- the isotropic scenario keeps the traceless basis near zero by construction;"
    )
    lines.append(
        "- biased directional weights generate a nonzero traceless mean, which is the effect needed for a genuine sidereal or geometry-dependent signature;"
    )
    lines.append(
        "- the fitted observations are dominated by different basis terms, so the 6.2.2 revision should keep the trace and anisotropy channels separate."
    )
    lines.append("")
    return "\n".join(lines)


def compile_pdf(tex_path: Path) -> None:
    pdflatex = shutil.which("pdflatex")
    if pdflatex is None:
        raise RuntimeError("pdflatex is not available in this environment")
    for _ in range(2):
        subprocess.run(
            [
                pdflatex,
                "-interaction=nonstopmode",
                "-halt-on-error",
                tex_path.name,
            ],
            cwd=tex_path.parent,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    dataset = load_dataset(DATASET_PATH)
    observations = build_observations(dataset)
    result = run_analysis(observations)
    simulations = run_simulations(result, observations)

    (OUT_DIR / "analysis.json").write_text(
        json.dumps(result.to_json(), indent=2, sort_keys=True),
        encoding="utf-8",
    )

    write_csv(
        OUT_DIR / "observations.csv",
        [
            {
                "name": obs.name,
                "experiment": obs.experiment,
                "source": obs.source,
                "observed_r": f"{obs.observed_r:.6f}",
                "feature_length_inv": f"{obs.feature[0]:.8f}",
                "feature_shape": f"{obs.feature[1]:.8f}",
                "feature_source_norm": f"{obs.feature[2]:.8f}",
                "feature_zone_split": f"{obs.feature[3]:.8f}",
                "anchor": str(obs.anchor),
                "citation": obs.citation,
                "notes": obs.notes,
            }
            for obs in observations
        ],
    )

    write_csv(
        OUT_DIR / "predictions.csv",
        [
            {
                "name": row.name,
                "kind": row.kind,
                "observed_r": f"{row.observed_r:.6f}",
                "predicted_r": f"{row.predicted_r:.6f}",
                "residual": f"{row.residual:+.6f}",
                "pull": "" if row.pull is None else f"{row.pull:+.6f}",
            }
            for row in result.anchor_rows + result.validation_rows
        ],
    )

    write_csv(
        OUT_DIR / "loo.csv",
        [
            {
                "omitted": row.name,
                "observed_r": f"{row.observed_r:.6f}",
                "predicted_r": f"{row.predicted_r:.6f}",
                "residual": f"{row.residual:+.6f}",
                "pull": "" if row.pull is None else f"{row.pull:+.6f}",
            }
            for row in result.loo_rows
        ],
    )

    markdown = render_markdown(result)
    (OUT_DIR / "report.md").write_text(markdown, encoding="utf-8")

    sim_markdown = render_simulation_markdown(simulations)
    (OUT_DIR / "simulations.md").write_text(sim_markdown, encoding="utf-8")

    (OUT_DIR / "simulation_summary.json").write_text(
        json.dumps(simulations.to_json(), indent=2, sort_keys=True),
        encoding="utf-8",
    )

    write_csv(
        OUT_DIR / "term_contributions.csv",
        [
            {
                "observation": row.observation,
                "term": row.term,
                "coefficient": f"{row.coefficient:.8f}",
                "feature": f"{row.feature:.8f}",
                "contribution": f"{row.contribution:+.8f}",
                "abs_share": f"{row.abs_share:.6f}",
            }
            for row in simulations.contribution_rows
        ],
    )

    write_csv(
        OUT_DIR / "directional_scan.csv",
        [
            {
                "label": row.label,
                "linear_bias": f"{row.linear_bias:+.6f}",
                "quadratic_bias": f"{row.quadratic_bias:+.6f}",
                "normalization": f"{row.normalization:.8f}",
                "mean_mu": f"{row.mean_mu:+.8f}",
                "mean_traceless": f"{row.mean_traceless:+.8f}",
            }
            for row in simulations.scenario_rows
        ],
    )

    tex = render_tex(result)
    tex_path = OUT_DIR / "lsc_6_2_2_codex_report.tex"
    tex_path.write_text(tex, encoding="utf-8")
    compile_pdf(tex_path)

    print(f"wrote {OUT_DIR / 'analysis.json'}")
    print(f"wrote {OUT_DIR / 'report.md'}")
    print(f"wrote {OUT_DIR / 'simulations.md'}")
    print(f"wrote {OUT_DIR / 'simulation_summary.json'}")
    print(f"wrote {tex_path}")
    print(f"wrote {tex_path.with_suffix('.pdf')}")


if __name__ == "__main__":
    main()
