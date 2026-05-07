# LSC 6.2.2 Simulation Diagnostics

## Directional Scan

| label | linear bias | quadratic bias | normalization | mean(mu) | mean(traceless) |
| --- | ---: | ---: | ---: | ---: | ---: |
| isotropic | +0.000000 | +0.000000 | 2.000000 | +0.000000 | +0.000000 |
| mild_forward_bias | +0.250000 | +0.000000 | 2.000000 | +0.083333 | +0.000000 |
| mild_backward_bias | -0.250000 | +0.000000 | 2.000000 | -0.083333 | +0.000000 |
| quadrupolar_bias | +0.000000 | +0.300000 | 2.200000 | +0.000000 | +0.024242 |
| combined_bias | +0.250000 | +0.300000 | 2.200000 | +0.075758 | +0.024242 |

## Dominant Term Per Observation

| observation | dominant term | contribution | abs share |
| --- | --- | ---: | ---: |
| BEST_inner | beta_source | +0.839852 | 0.582 |
| BEST_outer | beta_source | +0.839852 | 0.576 |
| BEST_ratio | beta_shape | -0.109193 | 0.447 |
| GALLEX_Cr1 | beta_source | +0.839852 | 0.540 |
| GALLEX_Cr2 | beta_source | +0.839852 | 0.540 |
| GALLEX_combined | beta_source | +0.839852 | 0.540 |
| SAGE_51Cr | beta_source | +0.839852 | 0.516 |
| SAGE_37Ar | beta_source | +1.024281 | 0.565 |

## Interpretation

- the isotropic scenario keeps the traceless basis near zero by construction;
- biased directional weights generate a nonzero traceless mean, which is the effect needed for a genuine sidereal or geometry-dependent signature;
- the fitted observations are dominated by different basis terms, so the 6.2.2 revision should keep the trace and anisotropy channels separate.
