# Compute Access Request: LSC 6.0 Numerical Validation

## Purpose

Request access to high-memory accelerator hardware for numerical validation of the LSC 6.0 phenomenological model.

This request does not present LSC 6.0 as validated physics. The goal is to determine whether the model is numerically stable, falsifiable, and worth further expert review.

## Target Hardware

Suitable platforms include:

- AMD Instinct MI300X-class GPUs with 192 GB HBM
- Google Cloud TPU v5p-class accelerators with high-bandwidth memory
- NVIDIA B200-class accelerators with high-memory configuration
- equivalent high-memory HPC nodes

## Project Context

Project: LSC 6.0  
Type: AI-assisted phenomenological neutrino model  
Status: unvalidated; requires numerical verification  
Repository: https://github.com/luciferprosun/LSC-6.0  
Related record: https://doi.org/10.5281/zenodo.19780616  

## Computational Problem

The current validation path involves a large state-space evaluation with an estimated memory footprint near 85 GB. This exceeds typical 24 GB consumer GPU capacity and leaves limited practical headroom on 96 GB devices once framework overhead, batching, precision choices, and intermediate tensors are included.

## Workload Definition

The computation includes:

1. Evaluation of effective Hamiltonian extensions:

   ```text
   H_eff = H_vac + H_matter + H_grav + H_LSC
   ```

2. Numerical sweeps over:

   - neutrino energy range from MeV to PeV,
   - radial distance or environment parameter,
   - coupling parameter alpha_LSC,
   - detector-response or anisotropy parameters where applicable.

3. Stability tests:

   - eigenvalue behavior,
   - sensitivity to perturbations,
   - convergence under discretization,
   - failure modes under parameter variation.

4. Optional parameter exploration:

   - Monte Carlo sampling,
   - sparse grid search,
   - reduced precision versus full precision comparison.

## Estimated Compute Profile

- Memory requirement: approximately 85 GB for the current full tensor path
- Precision: FP32 for initial sweeps; FP64 or mixed verification for selected cases
- Runtime estimate: 50 to 100 accelerator-hours depending on batching and precision
- Parallelism: moderate; single high-memory accelerator preferred for the baseline run
- Software path: Python/JAX or equivalent numerical stack

## Success Criteria

The experiment is successful if it produces a reproducible answer to the following questions:

1. Does the model produce numerically stable solutions?

   - consistent eigenvalue structure,
   - bounded sensitivity under small perturbations,
   - convergence under grid refinement.

2. Does the parameter space show physically structured behavior or non-physical instability?

   - structured regions would justify further expert review,
   - chaotic or divergent behavior would support falsification or major revision.

3. Can the required computation be reduced?

   - memory profiling,
   - tensor decomposition,
   - sparse or batched evaluation,
   - smaller validation kernels.

## Deliverables

- Reproducibility report
- Open-source validation code
- Parameter-sweep outputs
- Dataset suitable for Zenodo archival
- Technical validation note or preprint

## Requested Support

The requested support is access to high-memory compute and, if possible, technical review of the workload design. The goal is not endorsement of the physics claim. The goal is independent numerical validation or falsification of the computational model.

