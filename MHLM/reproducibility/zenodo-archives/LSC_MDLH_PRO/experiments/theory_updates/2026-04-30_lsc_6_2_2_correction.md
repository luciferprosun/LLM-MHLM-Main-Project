# LSC 6.2.2 Correction

Date: 2026-04-30

## Trigger

DeepSeek review of LSC 6.2.0 identified formal problems that had to be fixed
before the theory line could be defended cleanly.

## What Changed

- explicit isotropic trace added to the detector-response bookkeeping,
- traceless anisotropy kept separate from the trace term,
- mixed `1 / E^2` usage removed from the base ansatz,
- preferred direction defined in a fixed celestial frame so sidereal tests are meaningful,
- deterministic simulation outputs added for term decomposition and directional scans.

## What Did Not Change

- the framework remains phenomenological,
- the anchor-fit / weak-LOO status remains unchanged,
- no validation claim is made.

## Why This Matters

The correction keeps the theory line readable for future review:

- the trace term can carry net rate shifts,
- the traceless term can carry directional residuals,
- the simulation layer shows how both pieces behave under biased and unbiased directional averages.

### 2026-05-02 Expansion (Transition to 6.2.3)

Further analysis during the development of version 6.2.3 has refined the understanding of the 6.2.2 correction:

- **Benchmark Integration:** The need for external benchmarks, such as the `JakeSpisak/Sterile-Neutrinos` repository, was identified to contrast the LSC phenomenological approach with standard dark-sector/sterile-neutrino cosmological models.
- **Formalized Residuals:** The residual model $R_{LSC}(E, t, \Omega)$ has been explicitly derived as a sum of isotropic and anisotropic components, ensuring that normalization errors are not misidentified as directional signals.
- **Epistemic Audit:** The 6.2.2 correction is now recognized as a critical bridge to the MHLM / MDLH audit layer, documenting how AI-assisted reviews (like the DeepSeek trigger) directly influence theory refinement.
