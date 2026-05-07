# Introduction

LSC 6.2 is a conservative extension draft of the public LSC 6.0
framework. The public LSC 6.0 record is available at
<https://zenodo.org/records/19780616>, and the related GitHub release is
available at
<https://github.com/luciferprosun/LSC-6.0/releases/tag/v1.0.0>. We
propose a detector-frame tensor ansatz for neutrino energy
reconstruction and angular response.

The effect can be interpreted as an effective direction- and
energy-dependent phase correction, without invoking a literal refractive
index for neutrinos. The model remains phenomenological.

# Theoretical Framework

The core LSC 6.0 observable ansatz is retained,
$$E_{\rm true}(x)=E_\infty\,G(g_{\mu\nu},\Phi(x)),$$
$$E_{\rm rec}=E_{\rm true}\left(1+\alpha_D D_{ij}\hat p^i\hat p^j\right).$$
Here $G$ is a dimensionless propagation factor, $E_\infty$ is the
conserved reference energy, $D_{ij}$ is an effective spatial
detector-response tensor in the laboratory frame, $\hat p^i$ is the
reconstructed direction unit vector, and $\alpha_D$ controls the
detector-level contribution. The limiting condition is
$$\lim_{\Phi\to 0,\,\alpha_D\to 0}E_{\rm rec}=E_\infty.$$

# Mathematical Formulation

The propagation factor is expanded as
$$G(g_{\mu\nu},\Phi(x))=1+\delta_G(x)+O(\delta_G^2).$$ The detector
tensor is decomposed into isotropic and anisotropic components,
$$D_{ij}=D^{\rm iso}_{ij}+\Delta D_{ij}.$$ The effective fractional
shift is then $$\frac{\Delta E}{E}\simeq \delta_G+\alpha_D\Delta_D,
 \qquad
 \Delta_D=D_{ij}\hat p^i\hat p^j.$$

The anisotropic part is parameterized by a traceless rank-2 tensor,
$$D_{ij}=\delta\left(n_i n_j-\frac{1}{3}\delta_{ij}\right),$$ where
$\delta$ is the dimensionless anisotropy magnitude and $n_i$ is a
preferred detector-frame direction. For an IceCube-style implementation,
$n_i$ may be aligned with a measured ice-flow or
crystal-orientation-fabric axis; the corresponding ice-light propagation
anisotropy is treated as a detector systematic, not automatically as a
neutrino-sector signal. The contraction entering the observable response
is $$D_{ij}\hat p^i\hat p^j=
 \delta\left[(\hat p\cdot n)^2-\frac{1}{3}\right].$$

The reconstructed energy is therefore modeled as
$$E_{\rm rec}(\hat p)=E_{\rm true}\left(1+\alpha_D D_{ij}\hat p^i\hat p^j\right).$$
A bounded first-order effect may be summarized as
$$\Delta m_{ij,{\rm eff}}^2\simeq
 \Delta m_{ij}^2\left(1+\epsilon_D\right),
 \qquad
 \epsilon_D=D_{kl}\hat p^k\hat p^l .$$

The effective energy entering the oscillation phase is
$$E_{\rm eff}(x)=E_{\rm true}(x)
 \left[1+\alpha_D D_{ij}\hat p^i\hat p^j\right].$$ The oscillation phase
is then written in the standard ultra-relativistic form
$$\Delta \Phi_{ij}=
 \int_0^L \frac{\Delta m_{ij}^2}{2E_{\rm eff}(x)}\,dx .$$ This is a
compact phenomenological ansatz and not a microscopic derivation. In the
limit $D_{ij}\to 0$ and $\delta_G\to 0$, the standard three-flavor
neutrino oscillation framework is recovered.

# Phenomenological Implications

The relevant output of LSC 6.2 is a set of test classes: angular
anisotropy, detector dependence, energy-dependent residuals, and
sidereal modulation. Representative archive diagnostics are shown in
Figs. <a href="#fig:lsc62-framework" data-reference-type="ref"
data-reference="fig:lsc62-framework">1</a>–<a href="#fig:lsc62-katrin" data-reference-type="ref"
data-reference="fig:lsc62-katrin">4</a>. A representative value
$\delta\sim 0.05$ is used for illustration; it is not a fitted or
claimed measurement.

For binned event data, the conservative comparison can be written as
$$\chi^2=\sum_k
 \frac{\left[N_{{\rm obs},k}-N_{{\rm pred},k}(D_{ij},\delta_G)\right]^2}
 {\sigma_k^2},$$ with
$$\sigma_k^2=\sigma_{{\rm stat},k}^2+\sigma_{{\rm sys},k}^2.$$ Each bin
$k$ may include reconstructed energy, zenith angle, azimuth, and time. A
null test corresponds to $D_{ij}\rightarrow 0$ and
$\delta_G\rightarrow 0$ within experimental uncertainties.

<figure id="fig:lsc62-framework">
<img src="figures/fig1_framework.png" />
<figcaption>Unified propagation and detector-response
framework.</figcaption>
</figure>

<figure id="fig:lsc62-anisotropy">
<img src="figures/fig2_anisotropy.png" />
<figcaption>Anisotropic response diagnostic for angular or directional
effects.</figcaption>
</figure>

<figure id="fig:lsc62-scan">
<img src="figures/fig3_parameter_scan.png" />
<figcaption>Parameter-scan diagnostic for effective LSC
coefficients.</figcaption>
</figure>

<figure id="fig:lsc62-katrin">
<img src="figures/fig4_katrin.png" />
<figcaption>KATRIN-style consistency diagnostic.</figcaption>
</figure>

# Discussion

The tensor language is the primary mathematical structure of LSC 6.2.
The effect can be interpreted as an effective direction- and
energy-dependent phase correction, without invoking a literal refractive
index for neutrinos. The model must be checked against gallium source
experiments, KATRIN beta-spectrum constraints, IceCube anisotropy
searches, and standard three-flavor oscillation data. Known IceCube
ice-light propagation anisotropies, including crystal-orientation fabric
and hole-ice effects, must be treated as backgrounds or nuisance
systematics before any neutrino-sector interpretation is attempted.

# Conclusion

LSC 6.2 provides a stable arXiv-safe synthesis of the LSC 6.0 effective
model with an explicit detector-frame anisotropy tensor. The next
required step is numerical fitting with explicit priors on $\delta_G$,
$\alpha_D$, and the angular coefficients of $D_{ij}$.

# References

<div class="thebibliography">

9 L. Wolfenstein, Neutrino oscillations in matter, Phys. Rev. D 17, 2369
(1978). S. P. Mikheyev and A. Yu. Smirnov, Resonant amplification of
neutrino oscillations in matter and solar neutrino spectroscopy, Sov. J.
Nucl. Phys. 42, 913 (1985). V. V. Barinov et al., Results from the
Baksan Experiment on Sterile Transitions (BEST), Phys. Rev. Lett. 128,
232501 (2022). KATRIN Collaboration, Direct neutrino-mass constraints
from tritium beta decay. IceCube Collaboration, searches for Lorentz
violation and anisotropy in high-energy neutrinos. B. J. Carr and S. W.
Hawking, Black holes in the early Universe, Mon. Not. R. Astron. Soc.
168, 399 (1974). LuciferSun, LSC 4.2 ULTRA public record, Zenodo,
<https://doi.org/10.5281/zenodo.19602045>. LuciferSun, LSC 6.0 public
record, Zenodo, <https://zenodo.org/records/19780616>. LuciferSun, LSC
6.0 GitHub release,
<https://github.com/luciferprosun/LSC-6.0/releases/tag/v1.0.0>.

</div>
