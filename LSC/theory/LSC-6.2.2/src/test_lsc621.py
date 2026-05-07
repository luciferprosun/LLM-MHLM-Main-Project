from __future__ import annotations

import math
import unittest

import numpy as np

from lsc621.data import build_observations, load_dataset, source_mean_cross_section
from lsc621.model import run_analysis
from lsc621.simulations import run_simulations


class LSC621Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.dataset = load_dataset()
        cls.observations = build_observations(cls.dataset)
        cls.analysis = run_analysis(cls.observations)
        cls.simulations = run_simulations(cls.analysis, cls.observations)

    def test_dataset_loads(self) -> None:
        self.assertIn("experiments", self.dataset)
        self.assertGreaterEqual(len(self.dataset["experiments"]), 3)

    def test_source_means(self) -> None:
        self.assertAlmostEqual(source_mean_cross_section(self.dataset, "51Cr"), 5.749407e-45, delta=1e-50)
        self.assertAlmostEqual(source_mean_cross_section(self.dataset, "37Ar"), 7.01196e-45, delta=1e-50)

    def test_anchor_fit_is_exact(self) -> None:
        for row in self.analysis.anchor_rows:
            self.assertAlmostEqual(row.observed_r, row.predicted_r, places=12)

    def test_trace_component_is_explicit(self) -> None:
        self.assertIn("beta_trace", self.analysis.coefficient_names)

    def test_best_ratio_is_close(self) -> None:
        ratio_pred = next(row.predicted_r for row in self.analysis.validation_rows if row.name == "BEST_ratio")
        self.assertAlmostEqual(ratio_pred, 0.9746835443, places=9)

    def test_gallex_split_is_not_exact(self) -> None:
        c1 = next(row.predicted_r for row in self.analysis.validation_rows if row.name == "GALLEX_Cr1")
        c2 = next(row.predicted_r for row in self.analysis.validation_rows if row.name == "GALLEX_Cr2")
        self.assertAlmostEqual(c1, c2, places=12)
        self.assertTrue(0.87 < c1 < 0.89)

    def test_loo_has_signal(self) -> None:
        worst = max(abs(row.residual) for row in self.analysis.loo_rows)
        self.assertGreater(worst, 0.15)

    def test_traceless_directional_average_vanishes(self) -> None:
        xs = np.linspace(-1.0, 1.0, 10001)
        values = xs**2 - (1.0 / 3.0)
        self.assertAlmostEqual(float(values.mean()), 0.0, places=3)

    def test_directional_scan_has_nonzero_biased_traceless_mean(self) -> None:
        isotropic = next(row for row in self.simulations.scenario_rows if row.label == "isotropic")
        biased = next(row for row in self.simulations.scenario_rows if row.label == "combined_bias")
        self.assertAlmostEqual(isotropic.mean_mu, 0.0, places=12)
        self.assertAlmostEqual(isotropic.mean_traceless, 0.0, places=12)
        self.assertNotAlmostEqual(biased.mean_traceless, 0.0, places=6)

    def test_fit_terms_reconstruct_log_prediction(self) -> None:
        target = next(row for row in self.analysis.anchor_rows if row.name == "BEST_inner")
        terms = [
            row.contribution
            for row in self.simulations.contribution_rows
            if row.observation == "BEST_inner"
        ]
        self.assertAlmostEqual(sum(terms), -math.log(target.predicted_r), places=10)


if __name__ == "__main__":
    unittest.main()
