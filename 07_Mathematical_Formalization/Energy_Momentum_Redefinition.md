---
title: "Energy Momentum Redefinition"
author: "Adel Gachkar"
tags: ["SDF", "07"]
status: "Canonical"
date: 2026-09-20
version: "v3.6.0"
updated: 2026-09-23
doi: "10.5281/zenodo.22412461"
module: "07_Mathematical_Formalization"
framework: "CADENCE-SDF-Dynamic-Architecture"
license: "MIT"
lang: "en"
---

# Energy Momentum Redefinition

> **Structural Causal Chain:** **Constraint -> Differential Tension (DeltaPhi) -> Quantized Step (delta s) -> Cadence -> Metric Emergence (g_{mu nu}) -> Observable Dynamics**

## Purpose

This note is a constituent node of the **07_Mathematical_Formalization** module of the CADENCE-SDF-Dynamic-Architecture vault. It formalizes the **energy–momentum budget of the relaxation substrate**: what plays the role of energy and momentum when the fundamental objects are constraint, tension, and quantized relaxation steps — and how the budget stays consistent with the second law and with the passive-bath picture. Geometry is treated as emergent in the proposed framework; this is a modeling assumption, not an empirical conclusion.


## Role in the Causal Architecture

- **Stage:** **Constraint -> Differential Tension (DeltaPhi) -> Quantized Step (delta s) -> Cadence -> Metric Emergence (g_{mu nu}) -> Observable Dynamics**
- **Function:** Energy-momentum redefined as the structural constraint budget.
- **Upstream input:** reactive reservoirs of the medium (`05_Physical_and_Reactive_Medium/Impedance_Network_Model.md`), accumulated tension ΔΦ.
- **Downstream output:** the conserved-aggregate structure entering metric emergence (`04_Canonical_SDF_Mapping/M_Metric_Emergence.md`) and flux observables (`04_Canonical_SDF_Mapping/F_Flux_and_Field.md`).

## Section 1 — Energy as Reactive Storage

In the boundary regime the medium is reactive-dominant (`05_Physical_and_Reactive_Medium/Impedance_Network_Model.md`, `05_Physical_and_Reactive_Medium/Active_Reactive_Harmonic_Band_Model.md`):

$$Z_{\text{medium}} = \underbrace{R_{\text{loss}}}_{\to\,0}\;+\;j\omega L_{\text{foam}} + \frac{1}{j\omega C_{\text{boundary}}}
\qquad\Longrightarrow\qquad
\bar{E}_{\text{reactive}} = \tfrac12 L_{\text{foam}}\,I^2 + \frac{Q_{\text{boundary}}^2}{2 C_{\text{boundary}}}$$

Energy is **stored reactively** while the dissipative channel is closed (|Φ| ≈ 0 in the limit — a model-level statement). The oscillatory exchange between L_foam and C_boundary is the substrate analogue of kinetic↔potential exchange; the corresponding harmonic band is catalogued in `05_Physical_and_Reactive_Medium/Active_Reactive_Harmonic_Band_Model.md`.

## Section 2 — Work Quantum of a Step

The elementary energetic currency is the step. Writing s₀ = c_eff·δτ_n with the step-propagation speed bounded by the causal limit:

$$w_{\text{step}} \sim \Delta\Phi\cdot s_0 = \Delta\Phi\cdot c_{\text{eff}}\,\delta\tau_n$$

In the microscopic realization proposed for the companion model, the per-step action is the coupling quantum:

$$\hbar\kappa_{\text{hop}} = \hbar\cdot 0.025\,g^2\omega_0 \approx 56\text{–}62\ \text{meV}\ \ (\lambda_0=320\,\text{nm},\ g\in[0.7,0.9])
\qquad\gg\quad k_BT(300\,\text{K})\approx 26\ \text{meV}$$

Consequences of the hierarchy ℏκ_hop > k_BT (factor ≈ 2.2 at the benchmark g = 0.8) at optical working scale: (i) the noise bath cannot motor directional work — it can only **time** the gated release (Kramers trigger); (ii) the stored phase debt, not the bath, pays for each release; (iii) scaling the lattice scale a upward drives the hierarchy toward ℏκ ~ k_BT and eventually the thermal-noise regime. The passive-bath bound (no directional work from an equilibrium noise bath) is the second-law wall; the registered engine asymmetry is the constraint geometry (rectifier) plus the pressure imbalance ΔP_diff (pump), with the noise bath acting only as trigger.

## Section 3 — Momentum as Constraint Flux

Momentum is carried by the gradient structure of the constraint potential:

$$p_\mu^{\text{(struct)}} \;\sim\; \frac{\nabla_\mu \Phi}{\omega_{\text{ref}}}\qquad
\text{(candidate normalization; } \omega_{\text{ref}} \text{ fixes the action scale)}$$

so the stress-like object entering the metric ansatz (`04_Canonical_SDF_Mapping/M_Metric_Emergence.md`) is the **reactive source**:

$$T_{\mu\nu}^{(\text{struct})}\;\hat{=}\;\alpha_{\text{metric}}\,
\Big(\frac{\omega_c}{\omega_{\text{ref}}}\Big)
\frac{\nabla_\mu\Phi\,\nabla_\nu\Phi}{\|\nabla\Phi\|^2+\varepsilon_{\text{reg}}}
\qquad
g_{\mu\nu} = \eta_{\mu\nu} + T_{\mu\nu}^{(\text{struct})}$$

Dimensional admissibility follows from the dimensionless cadence ratio and the dimensionless gradient quotient; ε_reg → 0⁺ regularizes the kinetic singularity. This identification is a candidate mapping, not a derivation.

## Section 4 — Budget Closure at the Oscillator Level

Across one full relaxation-oscillator cycle (load → threshold → release → reload):

$$\underbrace{\int_{\text{cycle}}\sigma_\Phi\,\delta s\,d\tau}_{\text{pump work (constraint realignment)}}\;=\;
\underbrace{\sum_{\text{releases}} w_{\text{step}}}_{\text{steps paid from storage}}\;+\;
\underbrace{\int_{\text{cycle}} R_{\text{loss}}\,I^2\,d\tau}_{\to\,0\ \text{in boundary regime}}$$

Passive stability requires Re[Z_medium] ≥ 0 at all times (`05_Physical_and_Reactive_Medium/Impedance_Network_Model.md`), i.e. the budget never runs in reverse. The cycle is a **debt ledger**: loading accumulates phase/tension debt; the gated release settles it; noise sets the release epoch only. This mirrors the phase-debt oscillator of the companion model (N_c = π/δθ steps per cycle, period-2 subharmonic π/0 alternating).

## Section 5 — Aggregate Accounting

Over N steps (`03_Cadence_Core/Statistical_Phase_Step_Dynamics.md`):

$$S_N=\sum_{n=1}^{N}\delta s_n,\qquad
\tau_N=\sum_{n=1}^{N}\delta\tau_n,\qquad
W_N=\sum_{n=1}^{N}w_{\text{step},n},\qquad
v_N=\frac{S_N}{\tau_N}\le c$$

Residuals ε_x,n may fluctuate locally while their aggregates converge; the observer accesses only the aggregate ratios. Physical step fluctuation ≠ observer measurement error (canonical separation of Module 03).

## Cross-Links

- [[Causal_Sequence_Master]] — master ordering of all stages.
- [[Cadence_Operator_Definition]] — operator-level definition of cadence.
- [[M_Metric_Emergence]] — how g_{μν} crystallizes from cadenced relaxation.
- [[SDF_Canonical_Lexicon]] — canonical definitions.
- `06_Dynamic_Engine/Void_Expansion_Engine.md` — the engine that spends this budget.
- `06_Dynamic_Engine/Lattice_Deformation_Kinetics.md` — the kinetics that schedule it.

---
*Author: Adel Gachkar — SDF Theory, v3.6.0 — DOI: 10.5281/zenodo.22412461*

## Mechanistic Status

See [[Proposed_Mechanism_Low_Contradiction]] for the proposed distinction → boundary → directionality → transition mechanism and its epistemic limits. The energy–momentum identification here is a **candidate formalization**: it makes the project's energy claims explicit and checkable, and equal status is not claimed for it beyond the model.
