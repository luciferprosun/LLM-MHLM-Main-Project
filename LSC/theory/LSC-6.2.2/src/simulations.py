from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .model import AnalysisResult


@dataclass(frozen=True)
class ContributionRow:
    observation: str
    term: str
    coefficient: float
    feature: float
    contribution: float
    abs_share: float


@dataclass(frozen=True)
class DominantContributionRow:
    observation: str
    term: str
    contribution: float
    abs_share: float


@dataclass(frozen=True)
class DirectionalScenarioRow:
    label: str
    linear_bias: float
    quadratic_bias: float
    normalization: float
    mean_mu: float
    mean_traceless: float


@dataclass(frozen=True)
class SimulationSummary:
    contribution_rows: list[ContributionRow]
    dominant_rows: list[DominantContributionRow]
    scenario_rows: list[DirectionalScenarioRow]

    def to_json(self) -> dict:
        return {
            "contribution_rows": [row.__dict__ for row in self.contribution_rows],
            "dominant_rows": [row.__dict__ for row in self.dominant_rows],
            "scenario_rows": [row.__dict__ for row in self.scenario_rows],
        }


def _weighted_directional_moments(linear_bias: float, quadratic_bias: float, *, nodes: int = 256) -> tuple[float, float, float]:
    mu, weights = np.polynomial.legendre.leggauss(nodes)
    profile = 1.0 + linear_bias * mu + quadratic_bias * mu**2
    if np.any(profile <= 0.0):
        raise ValueError("directional weight must remain positive on [-1, 1]")
    normalization = float(np.sum(weights * profile))
    mean_mu = float(np.sum(weights * profile * mu) / normalization)
    mean_traceless = float(np.sum(weights * profile * (mu**2 - (1.0 / 3.0))) / normalization)
    return normalization, mean_mu, mean_traceless


def directional_scan() -> list[DirectionalScenarioRow]:
    scenarios = [
        ("isotropic", 0.0, 0.0),
        ("mild_forward_bias", 0.25, 0.0),
        ("mild_backward_bias", -0.25, 0.0),
        ("quadrupolar_bias", 0.0, 0.30),
        ("combined_bias", 0.25, 0.30),
    ]
    rows: list[DirectionalScenarioRow] = []
    for label, linear_bias, quadratic_bias in scenarios:
        normalization, mean_mu, mean_traceless = _weighted_directional_moments(linear_bias, quadratic_bias)
        rows.append(
            DirectionalScenarioRow(
                label=label,
                linear_bias=linear_bias,
                quadratic_bias=quadratic_bias,
                normalization=normalization,
                mean_mu=mean_mu,
                mean_traceless=mean_traceless,
            )
        )
    return rows


def decompose_fit_terms(result: AnalysisResult, observations: list) -> tuple[list[ContributionRow], list[DominantContributionRow]]:
    contribution_rows: list[ContributionRow] = []
    dominant_rows: list[DominantContributionRow] = []
    coeff_names = result.coefficient_names
    coeffs = result.coefficients

    for obs in observations:
        term_values = [float(coeff * feature) for coeff, feature in zip(coeffs, obs.feature, strict=True)]
        abs_sum = float(sum(abs(value) for value in term_values))
        if abs_sum == 0.0:
            abs_sum = 1.0

        for name, coeff, feature, contribution in zip(coeff_names, coeffs, obs.feature, term_values, strict=True):
            contribution_rows.append(
                ContributionRow(
                    observation=obs.name,
                    term=name,
                    coefficient=float(coeff),
                    feature=float(feature),
                    contribution=float(contribution),
                    abs_share=float(abs(contribution) / abs_sum),
                )
            )

        dominant_idx = int(np.argmax(np.abs(term_values)))
        dominant_rows.append(
            DominantContributionRow(
                observation=obs.name,
                term=coeff_names[dominant_idx],
                contribution=float(term_values[dominant_idx]),
                abs_share=float(abs(term_values[dominant_idx]) / abs_sum),
            )
        )

    return contribution_rows, dominant_rows


def run_simulations(result: AnalysisResult, observations: list) -> SimulationSummary:
    contribution_rows, dominant_rows = decompose_fit_terms(result, observations)
    scenario_rows = directional_scan()
    return SimulationSummary(
        contribution_rows=contribution_rows,
        dominant_rows=dominant_rows,
        scenario_rows=scenario_rows,
    )
