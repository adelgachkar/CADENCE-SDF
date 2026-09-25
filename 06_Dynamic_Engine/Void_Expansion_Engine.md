---
title: "Void Expansion Engine"
author: "Adel Gachkar"
tags: ["SDF", "06"]
status: "Canonical"
date: 2026-09-20
version: "v3.6.0"
updated: 2026-09-23
doi: "10.5281/zenodo.22412461"
module: "06_Dynamic_Engine"
framework: "CADENCE-SDF-Dynamic-Architecture"
license: "MIT"
lang: "en"
---

# Void Expansion Engine

> **Structural Causal Chain:** **Constraint -> Differential Tension (DeltaPhi) -> Quantized Step (delta s) -> Cadence -> Metric Emergence (g_{mu nu}) -> Observable Dynamics**

## Purpose

This note is a constituent node of the **06_Dynamic_Engine** module of the CADENCE-SDF-Dynamic-Architecture vault. It operationalizes the **expansion engine stage**: how void-under-filament pressure imbalance becomes a step-wise expansion of the lattice, and how that engine projects onto the observed expansion rate H(z). Geometry is treated as emergent in the proposed framework; this is a modeling assumption, not an empirical conclusion.


## Role in the Causal Architecture

- **Stage:** **Constraint -> Differential Tension (DeltaPhi) -> Quantized Step (delta s) -> Cadence -> Metric Emergence (g_{mu nu}) -> Observable Dynamics**
- **Function:** Void expansion as the engine of cosmic dynamics.
- **Upstream input:** structural constraint, differential pressure ΔP_diff, and accumulated differential tension ΔΦ.
- **Downstream output:** step train {δs_n, δτ_n} → cadence ω_c → boundary term ΔH_boundary(z) in the expansion mapping.

## Section 1 — Engine Driver

The engine runs on the structural pressure imbalance (`02_Causal_Architecture/Differential_Pressure_Dynamics.md`, `04_Canonical_SDF_Mapping/Cid_Structural_Constraint.md`):

$$\Delta P_{\text{diff}}(z) = P_{\text{void}}(z) - P_{\text{filament}}(z),\qquad
\Delta\Phi = \nabla\Phi - \nabla\Phi_{\text{ref}}$$

In the boundary regime the cavity stores energy **reactively** and dissipates nothing (`05_Physical_and_Reactive_Medium/Impedance_Network_Model.md`):

$$\lim_{\rho\ll\rho_c} R_{\text{loss}}(\rho)\to 0,\qquad
Z_{\text{medium}} = j\omega L_{\text{foam}} + \frac{1}{j\omega C_{\text{boundary}}}\ \ (\text{reactive survivor})$$

so a void acts as a **reactive energy reservoir**: loaded slowly by ΔP_diff, released in gated quanta.

## Section 2 — Expansion as Quantized Relaxation

Each admissible release advances the local scale by one step (Axiom 3):

$$\delta s_n = s_0\,n,\quad n\in\mathbb{Z}^+,\qquad
\dot{a}_{\text{SDF}} \;\propto\; \frac{\overline{\delta s}}{\overline{\delta\tau}}\;\text{(per admissible site)}$$

with the step clocked by the cadence field ω_c = 1/δτ_n (`03_Cadence_Core/Cadence_Operator_Definition.md`). The kinetic picture is a **relaxation oscillator**: slow loading (ΔΦ, ΔP_diff) → threshold (gated admissibility) → fast release (δs) → reload. Noise times the release; the energy comes from the stored reactive reservoir, never from the noise itself (passive-bath consistency).

## Section 3 — Expansion Mapping

The engine's output enters the effective expansion rate as a boundary term (`01_Axioms/Axiom_02_Constraint_Precedes_Metric.md`, `04_Canonical_SDF_Mapping/L_Lattice_Dynamics.md`, `08_Observational_Mapping/Hubble_Tension_Resolution.md`):

$$H_{\text{eff}}(z) = H_{\text{metric}}(z) + \Delta H_{\text{boundary}}(z),\qquad
\Delta H_{\text{boundary}}(z) = \kappa_c\,\frac{\Delta P_{\text{diff}}(z)}{\rho_{\text{crit}}c^2}\cdot\Big[1-\exp\!\big(-z_c/(z+\epsilon)\big)\Big]$$

with working benchmark parameters (v3.5.1, traceable to Module 08; not SDF measurements):

| Parameter | Value | Status |
|---|---|---|
| H₀ benchmark | 67.4 km/s/Mpc | working benchmark |
| κ_c (rate form) | 5.64 km/s/Mpc | working benchmark |
| z_c | 0.15 | working benchmark |
| α | 2.1 | alternative-shape parameter (`S_transition`) |

**Shape status (Pantheon+ adjudication, 2026-09-20):** the two boundary transition shapes used across the project —

$$\mathcal{S}_{\text{EXP}}(z)=1-\exp\!\big(-z_c/(z+\epsilon)\big)\quad\text{vs.}\quad
\mathcal{S}_{\text{POW}}(z)=\big[1+(z/z_c)^\alpha\big]^{-1}$$

— are statistically indistinguishable on Pantheon+ SNe (Δχ² ≈ 1; SN data alone cannot adjudicate). The boundary term ΔH_boundary is likewise **not demanded by Pantheon+** in additive form (ΔH_c ≈ 0 fitted). Both shapes remain registered ansätze; the canonical adjudication record is the fitting tool `fit_transition_forms.py` of the companion Emergence-SDF-Vault repository, `data/pantheon+_SH0ES.dat` input, and the companion note `01_Axioms/Pre-Friedmann...` chain there. No resolution claim is made.

## Section 4 — Redshift Accounting

Expansion observables decompose multiplicatively (Axiom 3, Module 08):

$$1+z_{\text{obs}} = (1+z_{\text{metric}})\,(1+\delta z_{\text{foam}}),\qquad
\delta z_{\text{foam}} = \int_0^s \frac{\nabla|Z_{\text{medium}}|}{Z_0}\,ds$$

The engine therefore predicts environment-correlated residuals: void-line-of-sight probes vs. filament-line-of-sight probes should differ at the level of δz_foam — a falsifiable signature (`08_Observational_Mapping/Hubble_Tension_Resolution.md`, candidate tests table).

## Section 5 — Coupling to the Companion Model

In the companion Emergence-SDF-Vault model, the void is realized as a closed tetrahedral cavity network: the void fraction (statistical void limit), the hop-coupling rate κ_hop = 0.025 g² ω₀ (g ∈ [0.7, 0.9], FDTD benchmark p ≈ 3.3 confirming the w³ neck law), and the derived delay τ_d = π/2κ_hop give the engine its **microscopic clock**:

$$\tau_d = \frac{\pi}{2\,\kappa_{\text{hop}}}\ \Longleftrightarrow\ \omega_c \equiv \frac{1}{\delta\tau_n}\ \sim\ \kappa_{\text{hop}}\ \ (\text{candidate microscopic realization})$$

This identification is a candidate bridge between the two frameworks, not a derived identity; it is recorded here because Module 06 is where the clocking of the engine must ultimately live.

## Cross-Links

- [[Causal_Sequence_Master]] — master ordering of all stages.
- [[Cadence_Operator_Definition]] — operator-level definition of cadence.
- [[M_Metric_Emergence]] — how g_{μν} crystallizes from cadenced relaxation.
- [[SDF_Canonical_Lexicon]] — canonical definitions.
- `06_Dynamic_Engine/Lattice_Deformation_Kinetics.md` — the same kinetics in deformation (non-expansion) form.

---
*Author: Adel Gachkar — SDF Theory, v3.6.0 — DOI: 10.5281/zenodo.22412461*

## Mechanistic Status

See [[Proposed_Mechanism_Low_Contradiction]] for the proposed distinction → boundary → directionality → transition mechanism and its epistemic limits. The expansion mapping is a **candidate ansatz**; Pantheon+ does not demand an additive boundary term; no resolution claim is made anywhere in this note.
