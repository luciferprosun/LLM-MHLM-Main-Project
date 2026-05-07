# LSC 6.2.3  
## A Conservative Phenomenological Framework for Testing Detector-Frame Response Anisotropy in Neutrino Anomaly Data

**Status:** unvalidated phenomenological model  
**Version:** 6.2.3  
**Scope:** neutrino anomaly analysis, detector-response modelling, falsification testing, AI-assisted provenance audit  
**Associated audit layer:** MHLM / MDLH  
**Scientific position:** no confirmed new physics is claimed

---

## 1. Executive Summary

LSC 6.2.3 is a conservative phenomenological framework designed to test whether selected neutrino anomaly residuals can be partly described by small detector-frame response effects.

The model does not claim discovery of sterile neutrinos, primordial black holes, new forces, dark-sector particles, or a confirmed modification of the Standard Model. Instead, it defines a falsifiable mathematical ansatz that can be tested against existing neutrino data and rejected if it fails external constraints.

The main object of LSC 6.2.3 is a detector-frame response term separated into two components:

1. an isotropic trace component, representing normalization-like or scalar response effects;
2. a traceless anisotropic tensor component, representing possible direction-dependent detector response.

The model is intended to be compared against simpler explanations, including normalization shifts, cross-section uncertainties, detector systematics, standard oscillation models, and sterile-neutrino benchmark models.

A secondary purpose of this release is methodological. Because the LSC research line has been developed with extensive AI assistance, LSC 6.2.3 is paired with an MHLM / MDLH audit layer. The audit layer documents the risk that multiple language models can stabilize a coherent but unvalidated scientific theory. This audit does not validate the physics model. It records provenance, claim evolution, overclaim risk, and the distinction between mathematical coherence and empirical evidence.

---

## 2. Conservative Theory Goal

The goal of LSC 6.2.3 is to test whether a small, explicitly parameterized detector-frame response term can account for structured residuals in selected neutrino anomaly datasets without conflicting with established external constraints.

The model is treated as a phenomenological ansatz and falsification target, not as evidence for confirmed new physics.

Its scientific value is measured by:

- reproducibility;
- predictive constraint;
- comparison against simpler models;
- external consistency;
- transparent failure criteria;
- usefulness as an audit case for AI-assisted theory development.

LSC 6.2.3 should be considered successful only if it produces constrained, reproducible, independently testable signatures that outperform simpler alternatives after parameter penalties and uncertainty propagation.

---

## 3. Scientific Motivation

Several neutrino datasets contain residual structures or anomalies that have motivated different interpretations, including detector effects, cross-section revisions, sterile-neutrino oscillations, and broader beyond-Standard-Model scenarios.

LSC 6.2.3 does not attempt to solve all neutrino anomalies. It focuses on a narrower question:

Can a detector-frame response model, containing an isotropic trace term and a traceless anisotropic term, improve the description of selected residuals while remaining compatible with independent constraints?

This framing is intentionally conservative. The model is not presented as a replacement for standard neutrino physics. It is presented as a testable residual-analysis layer.

---

## 4. Relation to Sterile-Neutrino Models

Sterile-neutrino models remain an important comparison class for neutrino anomaly studies. Some sterile-neutrino frameworks are designed for short-baseline oscillation anomalies, while others address cosmological sterile-neutrino production or sterile-neutrino dark matter.

The external repository `JakeSpisak/Sterile-Neutrinos` is relevant as a computational and conceptual benchmark because it models sterile-neutrino production in the early Universe through scattering-induced decoherence and dark-sector population transfer. That mechanism is not the same as LSC 6.2.3.

LSC 6.2.3 does not claim to confirm or refute that sterile-neutrino dark-sector scenario. Instead, it uses sterile-neutrino modelling as a comparison class:

- sterile-neutrino models introduce new particle states;
- LSC 6.2.3 introduces an effective detector-frame response term;
- sterile-neutrino cosmology is constrained by relic abundance, X-ray bounds, structure formation, and early-Universe dynamics;
- LSC 6.2.3 is constrained by detector residuals, angular dependence, sidereal tests, energy response, and compatibility with independent neutrino experiments.

This distinction must remain explicit.

The correct statement is:

LSC 6.2.3 tests whether some residual structures attributed to new neutrino-sector physics could instead be partly described by detector-frame response effects. It does not exclude sterile-neutrino physics.

---

## 5. Model Structure

The baseline expectation for a neutrino event rate is written as:

\[
N_0(E,t,\Omega) =
\Phi(E,t,\Omega)
\cdot
P_{\alpha \rightarrow \beta}(E,L)
\cdot
\sigma(E)
\cdot
\epsilon_0(E,t,\Omega)
\]

where:

- \( \Phi \) is the neutrino flux;
- \( P_{\alpha \rightarrow \beta} \) is the standard oscillation probability;
- \( \sigma \) is the interaction cross-section;
- \( \epsilon_0 \) is the baseline detector efficiency or response.

LSC 6.2.3 modifies the detector-response layer, not the fundamental neutrino state by default.

The effective detector response is written:

\[
\epsilon_{\text{LSC}}(E,t,\Omega)
=
\epsilon_0(E,t,\Omega)
\left[
1
+
\lambda_0 f_0(E,t)
+
\lambda_A n_i A^{ij} n_j f_A(E,t)
\right]
\]

where:

- \( \lambda_0 \) is the isotropic trace-response amplitude;
- \( f_0(E,t) \) is an isotropic response function;
- \( \lambda_A \) is the anisotropic response amplitude;
- \( A^{ij} \) is a symmetric traceless tensor in the detector frame;
- \( n_i \) is the incoming neutrino direction unit vector in detector coordinates;
- \( f_A(E,t) \) is the anisotropic energy/time response function.

The tensor satisfies:

\[
A^{ij} = A^{ji}
\]

and

\[
\text{Tr}(A) = A^i_i = 0
\]

This separation is essential. Without separating the trace from the traceless component, the anisotropic term can accidentally absorb ordinary normalization error.

The predicted event rate becomes:

\[
N_{\text{LSC}}(E,t,\Omega)
=
N_0(E,t,\Omega)
\left[
1
+
\lambda_0 f_0(E,t)
+
\lambda_A n_i A^{ij} n_j f_A(E,t)
\right]
\]

The residual is:

\[
R(E,t,\Omega)
=
\frac{
N_{\text{obs}}(E,t,\Omega)
-
N_0(E,t,\Omega)
}{
N_0(E,t,\Omega)
}
\]

and the LSC residual model is:

\[
R_{\text{LSC}}(E,t,\Omega)
=
\lambda_0 f_0(E,t)
+
\lambda_A n_i A^{ij} n_j f_A(E,t)
\]

---

## 6. Interpretation of the Tensor Term

The tensor term in LSC 6.2.3 is not claimed to be a fundamental physical field.

It is treated as an effective parameterization of possible detector-frame anisotropy.

Possible interpretations include:

1. detector geometry effects;
2. reconstruction-direction bias;
3. source-position response variation;
4. unmodelled efficiency anisotropy;
5. environmental or time-dependent detector effects;
6. statistical overfitting;
7. an artifact of AI-assisted model construction.

Only after strict validation could any physical interpretation be considered.

The default interpretation is detector-response phenomenology.

---

## 7. Data Targets

LSC 6.2.3 may be tested against the following data categories.

### 7.1 Primary anomaly targets

- BEST inner-zone and outer-zone gallium-source measurements;
- GALLEX calibration data;
- SAGE calibration data;
- combined gallium-source ratios.

### 7.2 External constraint targets

- KATRIN endpoint constraints;
- solar-neutrino consistency;
- IceCube high-energy neutrino constraints;
- standard three-flavor oscillation data;
- detector-specific calibration data where available.

### 7.3 Comparison models

LSC 6.2.3 must be compared against:

- normalization-only correction;
- cross-section uncertainty correction;
- standard three-flavor oscillation baseline;
- sterile-neutrino oscillation benchmark;
- detector-systematics model;
- null model.

If LSC 6.2.3 does not outperform simpler models after parameter penalties, it should not be treated as a preferred explanation.

---

## 8. Core Claims

The following claims are allowed in LSC 6.2.3.

### Claim 1

LSC 6.2.3 is an unvalidated phenomenological model for testing detector-frame response effects in neutrino anomaly data.

### Claim 2

The model separates isotropic normalization-like effects from traceless anisotropic effects.

### Claim 3

The model is falsifiable through cross-validation, sidereal tests, angular residual analysis, energy-dependence tests, and external constraint checks.

### Claim 4

The model does not claim confirmed new physics.

### Claim 5

The MHLM / MDLH audit layer documents the AI-assisted development process and the risk of stabilizing coherent but unvalidated scientific narratives.

### Claim 6

Sterile-neutrino models remain a valid comparison class. LSC 6.2.3 does not exclude sterile-neutrino explanations.

---

## 9. Claims That Must Be Removed or Weakened

The following claims should not appear in LSC 6.2.3.

### Remove

- LSC solves the Gallium anomaly.
- LSC proves new physics.
- LSC confirms primordial black holes around the Sun.
- LSC replaces sterile neutrinos.
- LSC disproves the Standard Model.
- AI discovered the theory.
- Multiple LLMs independently validated the theory.
- The tensor term is a confirmed physical field.
- The model explains all neutrino anomalies.
- LSC is confirmed by BEST.
- LSC is confirmed by IceCube.
- LSC proves a dark-sector mechanism.

### Weaken

Instead of:

“LSC explains the Gallium anomaly.”

Use:

“LSC tests whether detector-frame response terms can reduce or structure gallium-source residuals.”

Instead of:

“Sterile neutrinos are unnecessary.”

Use:

“LSC evaluates a non-sterile detector-response channel without excluding sterile-neutrino interpretations.”

Instead of:

“The tensor describes real spacetime anisotropy.”

Use:

“The tensor is an effective parameterization of possible detector-frame anisotropy.”

Instead of:

“AI validated the theory.”

Use:

“AI tools assisted drafting, critique, code generation, and audit documentation. Scientific validity depends on reproducible analysis and independent review.”

Instead of:

“PBHs regulate neutrino flux.”

Use:

“Earlier LSC versions explored compact-object-inspired mechanisms. LSC 6.2.3 does not require that interpretation.”

---

## 10. Testable Hypotheses

### Hypothesis 1: Detector-response residual structure

Selected neutrino anomaly residuals may contain a detector-frame response component not captured by the baseline model.

### Hypothesis 2: Trace-anisotropy separation

A model separating scalar normalization from traceless anisotropy may describe residual structure better than a single scalar correction.

### Hypothesis 3: Sidereal or orientation dependence

If the anisotropic component is meaningful, residuals may show repeatable dependence on detector orientation, source geometry, or sidereal phase.

### Hypothesis 4: Energy-dependent residual signature

The response term may produce an energy-dependent residual pattern distinguishable from pure flux suppression.

### Hypothesis 5: AI-stabilized artifact possibility

If LSC only appears coherent in text but fails reproducible testing, it should be classified as an AI-stabilized speculative artifact rather than a physical model.

---

## 11. Falsifiable Predictions

### Prediction 1: Sidereal modulation

If the anisotropic detector-frame term is meaningful, time-binned residuals should show repeatable sidereal-phase dependence after correction for environmental and detector-operation variables.

Falsification condition:

The anisotropic component is weakened or rejected if no sidereal-phase structure is observed at the predicted amplitude, or if the fitted phase changes randomly across datasets.

### Prediction 2: Trace and anisotropy separation

The isotropic trace term and traceless anisotropic term should be statistically distinguishable.

Falsification condition:

The anisotropic term is weakened if it collapses into a scalar normalization shift or becomes unconstrained under uncertainty propagation.

### Prediction 3: Cross-detector consistency

If the detector-frame response model is meaningful, fitted anisotropy parameters should transform consistently between detector geometries.

Falsification condition:

The model is weakened if each experiment requires unrelated free tensor parameters with no shared structure.

### Prediction 4: Energy-residual structure

LSC-like response terms should produce an energy-dependent residual pattern distinguishable from simple flux suppression or sterile-neutrino oscillation fits.

Falsification condition:

The model is weakened if the same residual improvement is reproduced by a simpler normalization or calibration model with fewer parameters.

### Prediction 5: External constraint survival

Parameter values that improve gallium-source residuals should not contradict KATRIN, IceCube, solar-neutrino data, or standard three-flavor oscillation constraints.

Falsification condition:

The model is weakened or rejected if the parameter range needed to improve gallium data is excluded by independent measurements.

---

## 12. Falsification Plan

### Step 1: Freeze the model specification

Before fitting, create a locked file:

`LSC_6_2_3_MODEL_SPEC.md`

This file must define:

- equations;
- parameters;
- priors or parameter bounds;
- datasets;
- comparison models;
- success thresholds;
- failure thresholds.

No equation should be changed after seeing the fit results without incrementing the version number.

### Step 2: Define baseline models

The model must be compared against:

1. null model;
2. normalization-only correction;
3. cross-section correction;
4. standard three-flavor expectation;
5. sterile-neutrino benchmark;
6. detector-systematics benchmark.

### Step 3: Run leave-one-out validation

Fit on one subset and test on another.

Examples:

- fit BEST inner, test BEST outer;
- fit BEST outer, test BEST inner;
- fit BEST, test GALLEX/SAGE;
- fit GALLEX/SAGE, test BEST.

### Step 4: Penalize extra parameters

Use AIC, BIC, Bayesian evidence, or another transparent model-comparison metric.

LSC 6.2.3 should not be considered preferred unless it improves fit quality after accounting for additional degrees of freedom.

### Step 5: Test sidereal and angular structure

If timestamps and geometry are available, test whether the anisotropic term predicts stable orientation-dependent or sidereal-phase residuals.

### Step 6: Test against external constraints

Any fitted parameter region must be checked against:

- KATRIN;
- IceCube;
- solar-neutrino data;
- standard oscillation global fits;
- detector calibration constraints.

### Step 7: Archive negative results

If the model fails, the failure should be archived.

A failed LSC 6.2.3 test is still scientifically useful because it constrains a class of detector-response explanations and contributes to the MHLM / MDLH audit record.

---

## 13. Relation to MHLM / MDLH

The LSC research line was developed through an extended AI-assisted workflow involving drafting, critique, code generation, mathematical restructuring, literature comparison, and version-to-version synthesis.

This creates an epistemic risk.

Multiple language models can converge on coherent language and internally consistent structure without providing independent scientific validation.

Therefore, LSC 6.2.3 is paired with MHLM / MDLH as an audit layer.

The audit layer tracks:

- claim provenance;
- unsupported claim persistence;
- overclaim amplification;
- model-to-model reinforcement;
- correction history;
- whether AI-generated coherence is being mistaken for evidence.

The MHLM / MDLH audit does not prove that LSC is true.

It also does not prove that LSC is false.

Its purpose is to make the development process transparent and reviewable.

The correct public framing is:

LSC 6.2.3 is the physics test package.

MHLM / MDLH is the epistemic-risk and provenance audit package.

They are connected by methodology, not by evidence.

---

## 14. Recommended Public Statement

LSC 6.2.3 is not a discovery claim.

It is a falsifiable detector-response model for neutrino anomaly analysis, released with reproducible code, explicit failure criteria, and an MHLM / MDLH audit trail documenting the risks of AI-assisted theory development.

The project does not claim confirmed new physics.

It asks whether a constrained detector-frame response model can survive comparison against simpler explanations and independent neutrino constraints.

