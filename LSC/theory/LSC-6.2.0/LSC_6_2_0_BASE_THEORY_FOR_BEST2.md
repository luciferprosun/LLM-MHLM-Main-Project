# LSC 6.2.0 Base Theory for BEST-2 Development

Working status: development base, not confirmed physics.

This file extracts the current usable core from the LSC line for future BEST-2 style modeling. It is based on the published LSC 6.2.0 preprint package and should be treated as the controlled starting point for new calculations.

## Public Anchors

- GitHub repository: https://github.com/luciferprosun/LSC-6.0
- GitHub release: https://github.com/luciferprosun/LSC-6.0/releases/tag/v6.2.0-preprint
- Zenodo record: https://zenodo.org/records/19878587
- DOI: https://doi.org/10.5281/zenodo.19878587
- Concept DOI: https://doi.org/10.5281/zenodo.19780615

## Core Claim Boundary

LSC 6.2.0 is not evidence of confirmed new physics. It is a phenomenological ansatz for testing whether propagation-level effects plus detector-frame reconstruction anisotropy can reproduce or constrain anomaly-like behavior in gallium source experiments without immediately treating sterile neutrinos as the only possible explanation.

## Main Variables

- `E_infty`: conserved reference energy.
- `E_true`: propagation-level true energy.
- `E_rec`: detector-level reconstructed energy.
- `G(g_mu_nu, Phi(x))`: dimensionless propagation factor.
- `D_ij`: effective spatial detector-response tensor in the lab frame.
- `Delta D_ij`: anisotropic detector-response component.
- `p_hat^i`: reconstructed direction unit vector.
- `alpha_D`: detector-level coupling coefficient.
- `delta_G`: small propagation correction.
- `delta`: dimensionless anisotropy magnitude.
- `n_i`: preferred detector-frame direction.

## Core Equations

Propagation-level energy:

```text
E_true(x) = E_infty * G(g_mu_nu, Phi(x))
```

Detector reconstruction:

```text
E_rec = E_true * [1 + alpha_D * D_ij * p_hat^i * p_hat^j]
```

Null recovery:

```text
Phi -> 0
alpha_D -> 0
E_rec -> E_infty
```

First-order propagation expansion:

```text
G(g_mu_nu, Phi(x)) = 1 + delta_G(x) + O(delta_G^2)
```

Detector tensor split:

```text
D_ij = D_ij^iso + Delta D_ij
```

Fractional energy shift:

```text
Delta E / E ~= delta_G + alpha_D * Delta_D
Delta_D = D_ij * p_hat^i * p_hat^j
```

Traceless rank-2 anisotropy:

```text
D_ij = delta * (n_i n_j - delta_ij / 3)
```

Directional contraction:

```text
D_ij * p_hat^i * p_hat^j = delta * [(p_hat dot n)^2 - 1/3]
```

Effective energy for oscillation phase:

```text
E_eff(x) = E_true(x) * [1 + alpha_D * D_ij * p_hat^i * p_hat^j]
```

Oscillation phase:

```text
Delta Phi_ij = integral_0^L [Delta m_ij^2 / (2 * E_eff(x))] dx
```

Binned comparison:

```text
chi^2 = sum_k [N_obs,k - N_pred,k(D_ij, delta_G)]^2 / sigma_k^2
sigma_k^2 = sigma_stat,k^2 + sigma_sys,k^2
```

## BEST-2 Development Direction

The next model should use real or simulated two-zone/three-zone geometry and compare predicted integrated rates against measured gallium source ratios.

Minimum BEST-2 modeling targets:

1. Reproduce BEST inner and outer zone predictions using published geometry.
2. Add explicit source extension rather than only point-source approximation.
3. Integrate survival/reconstruction response over gallium volume.
4. Fit or bound `alpha_D`, `delta_G`, `delta`, and the detector-frame vector `n_i`.
5. Test whether `R_out / R_in = 0.97 +/- 0.07` constrains the tensor term.
6. Compare with GALLEX/SAGE source data to avoid overfitting BEST only.
7. Check tension with KATRIN and IceCube as external vetoes.

## Data Inputs Already Collected

The repo currently contains:

- `data/dataset.json`: Codex structured gallium dataset.
- `baza/przydatne_dodatki/lsc60_simulation/`: previous LSC 6.0 toy gallium response.
- `baza/przydatne_dodatki/lsc55_math_and_tests/`: earlier tensor math and test scripts.

External data still needed:

- full BEST extraction-cycle table,
- covariance/systematic uncertainty model,
- exact GALLEX source geometry,
- exact SAGE source geometry,
- updated gallium cross-section table with primary references,
- KATRIN/IceCube exclusion curves in machine-readable form.

## Why Not Use Older Versions as the Main Base

LSC 5.5 contains useful tensor mathematics and local tests, but it is less cleanly framed and contains stronger speculative language. LSC 6.0 cleaned the public phenomenology. LSC v1.2.0 improved reproducibility. LSC 6.2.0 combines those gains and adds the explicit detector-frame rank-2 tensor in the most defensible public form.

## Guardrails

- Do not claim discovery.
- Do not treat AI agreement as validation.
- Do not mix detector-systematic anisotropy with neutrino-sector anisotropy without nuisance parameters.
- Do not use plot-digitized or AI-generated values unless marked as provisional.
- Keep raw data separate from fitted/derived values.

