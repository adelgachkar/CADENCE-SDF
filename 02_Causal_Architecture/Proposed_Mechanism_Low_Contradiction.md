---
title: "Proposed SDF Mechanism: Distinction, Boundary, Directionality and Phase Response"
version: "v3.5.1"
status: "Proposed Mechanism — Not Empirically Established"
date: "2026-09-11"
author: "Adel Gachkar"
framework: "CADENCE-SDF-Dynamic-Architecture"
lineage: "v3.4.2 -> v3.5.1"
license: "MIT"
lang: "en"
doi: "10.5281/zenodo.22412461"
---

# Proposed SDF Mechanism

> **Epistemic status:** This document states a proposed mechanism intended to reduce conceptual tension among the framework's assumptions and several classes of observables. It is **not presented as proof, verification, or established physical fact**.

## 1. Mechanistic Premise

The mechanism begins with a distinction between a prior and a posterior admissible structural state:

\[
S_{\rm pre}\neq S_{\rm post}.
\]

A transition between distinguishable states requires a delimiting condition. The boundary is therefore treated as an active constraint on admissible transitions rather than as mere absence of structure.

\[
\boxed{
\text{Distinction}
\rightarrow
\text{Boundary}
\rightarrow
\text{Directionality}
\rightarrow
\text{Admissible Transition}
}
\]

Directionality is represented by the ordered transition

\[
S_n \xrightarrow{\;T_{\mathcal C}\;} S_{n+1},
\]

with an oriented increment

\[
\Delta s_n,\qquad \Delta\Phi_n,\qquad \Delta\Phi_n^{\rm sign}.
\]

The framework does not require that the underlying substrate be continuously stretched in order for a sequence of observable phase steps to change.

## 2. Boundary as a Dynamic Condition

Let \(\Omega\) be an admissible structural region and \(\partial\Omega\) its boundary. The boundary determines which transitions are permitted:

\[
T_{\mathcal C}:\;S_n\mapsto S_{n+1},
\qquad
T_{\mathcal C}\in\mathcal A(\partial\Omega,\mathcal C).
\]

A cavity or low-density region is therefore interpreted, at the mechanism level, as a region with a modified boundary condition and modified reactive/transport response. It is **not automatically identified with literal emptiness**.

## 3. Active/Reactive Separation

The medium response is decomposed schematically as

\[
Z_{\rm medium}=R_{\rm loss}+Z_{\rm reactive},
\]

\[
Z_{\rm reactive}
=
j\omega L_{\rm foam}
+\frac{1}{j\omega C_{\rm boundary}}.
\]

The proposed zero-boundary interpretation concerns the limit

\[
R_{\rm loss}\rightarrow0,
\]

while \(Z_{\rm reactive}\) may remain non-zero.

Thus "zero boundary" means zero active-loss component in the limiting idealization, **not zero total physical response**.

## 4. Uncertainty / Reactive Domain

The reactive domain is represented as an admissible set rather than unrestricted freedom:

\[
\mathcal U_R
=
\{S_n:\mathcal C(S_n)=1\}.
\]

Active and reactive components enter this domain with distinct roles: the reactive component represents bounded holding/storage and harmonic persistence, while the active component represents directed transition. Both are restricted by finite band and spectral support. The transition is selected by the boundary constraint and cadence:

\[
(\mathcal C,\Delta\Phi,Z_{\rm medium})
\rightarrow
S_n\rightarrow S_{n+1}.
\]

The uncertainty interpretation is therefore **bounded multiplicity of admissible states**, not absence of structure.

## 4A. Constraint Alignment as the Generator of Emergent Law

The mechanism is further constrained by the working principle that the law is an emergent output of the mutual alignment of constraints, rather than an independently imposed rule:

$$
\{C_i\}\rightarrow\operatorname{Align}(C_i)\rightarrow L_{\rm emergent}.
$$

Local alignment may fluctuate while a coarse-grained law remains statistically stable. This distinction is important for retaining dynamics without requiring every microscopic step to be identical. See [[Constraint_Alignment_Emergent_Law]] and [[Statistical_Phase_Step_Dynamics]].

## 5. Optical Phase-Step Interface

The proposed interface from structural dynamics to observables is

\[
\boxed{
(\mathcal C,\Delta\Phi,D_{\rm eff},\omega_c,n_{\rm eff})
\rightarrow
\Delta\Phi_{\rm opt}
\rightarrow
\Pi_C
\rightarrow
\text{observable}
}
\]

where \(D_{\rm eff}\) denotes an effective number/measure of available structural degrees of freedom and \(\Pi_C\) denotes projection into the constrained observable sector.

A cumulative phase response may be represented schematically by

\[
\Phi_{\rm obs}
=
\sum_i \Delta\Phi_{{\rm opt},i},
\]

with

\[
\Delta\Phi_{{\rm opt},i}
=
F(\rho_i,\sigma_{B,i},D_{{\rm eff},i},\omega_{c,i},n_{{\rm eff},i}).
\]

The function \(F\) is **not yet derived** in this release.

## 6. Proposed Redshift Mechanism

The working hypothesis is that part of an observed redshift may arise from cumulative changes in optical phase-step propagation through a structured medium:

\[
z_{\rm prop}
=
\mathcal Z
\left[
\{\Delta\Phi_{{\rm opt},i}\}
\right].
\]

A qualitative directional hypothesis is

\[
D_{\rm eff}\downarrow
\quad\Longrightarrow\quad
\Delta\Phi_{\rm cumulative}\downarrow
\quad\Longrightarrow\quad
z_{\rm prop}\downarrow,
\]

but the monotonicity and functional form must be derived or tested rather than assumed.

This mechanism is intended to be compared against, not silently substituted for, Doppler and cosmological redshift contributions.

## 7. Strong-Field / Black-Hole Boundary as a Limiting Case

A strong gravitational environment is treated as a useful limiting test of the same mechanism. If the effective boundary constraint approaches a saturation regime,

\[
\sigma_B\rightarrow\sigma_{\rm sat},
\qquad
D_{\rm eff}\rightarrow D_{\min},
\]

the phase-transfer response may approach a strong-field limit:

\[
z_{\rm prop}\rightarrow \mathcal Z_{\rm strong}.
\]

The framework does **not** claim in this document that this limit has already been derived or that it reproduces the general-relativistic result. The purpose is to define a concrete benchmark: a single mechanism should eventually specify its weak-field, intermediate-field, and strong-field behavior.

## 8. Expansion / Volumetric Compensation

A local structural deficit is hypothesized to induce compensatory reconfiguration:

\[
\Delta\rho<0
\rightarrow
\sigma_B
\rightarrow
\Gamma_n
\rightarrow
\Delta V_n.
\]

For discrete transitions,

\[
\frac{1}{V}\frac{dV}{dt}
\sim
\frac{1}{V}\sum_n\Gamma_n\Delta V_n,
\]

so a macroscopic expansion-like rate can be viewed as the coarse-grained output of discrete structural transitions. This is a **mechanistic proposal**, not an observational determination.

## 9. Rotation as a Second Observable Channel

The same environmental state may contribute an additional acceleration channel:

\[
a_{\rm obs}(r)
=
a_{\rm matter}(r)+a_{\rm SDF}(r),
\]

\[
a_{\rm SDF}
=
F_a(\Delta\rho,\sigma_B,D_{\rm eff},\omega_c,\Gamma).
\]

The corresponding orbital relation is

\[
v^2(r)=r\,a_{\rm obs}(r).
\]

This is intended as a falsifiable alternative mechanism to be quantified; it is **not** a claim that dark matter has been disproved.

## 10. Environmental Unification

A central working hypothesis is that environmental state variables feed several observables:

\[
\boxed{
\{\rho_{\rm env},\sigma_B,D_{\rm eff},\omega_c,n_{\rm eff}\}
\rightarrow
\{z_{\rm prop},a_{\rm SDF},H_{\rm local},c_{\rm eff}\}
}
\]

The scientific value of this proposal depends on whether the same parameterization can account for multiple observables without introducing independent ad-hoc parameters for each one.

## 11. Substrate Cost, Causal Limit, and Temporal Residual

A candidate substrate cost is decomposed as

$$C_{\rm sub}=C_c+C_t,$$

where $C_c$ denotes causal-propagation cost and $C_t$ denotes temporal residual/memory. At the kinematic level a candidate effective step duration is

$$\delta\tau_{\rm eff}=\delta\tau_{\min}+\delta\tau_{\rm res},\qquad \delta\tau_{\rm res}\ge0,$$

giving

$$v_{\rm eff}=\frac{\delta s}{\delta\tau_{\rm eff}}\le c.$$

This is a proposed mechanism-level interpretation. No constitutive law for $C_{\rm sub}$ or $\delta\tau_{\rm res}$ is claimed in this release.

## 12. Fixed Constants and Effective Propagation

The mechanism keeps fundamental constants as fixed reference quantities unless a future derivation demonstrates otherwise:

\[
c_{\rm fundamental}=c.
\]

An effective propagation quantity may nevertheless be introduced,

\[
c_{\rm eff}=F_c(n_{\rm eff},\omega_c,\Delta\Phi),
\]

to represent propagation through the structured medium. The notation \(c_{\rm eff}\) must not be interpreted as a replacement for the causal invariant \(c\) without an explicit derivation.

## 13. Minimum-Action Compatibility

The proposed mechanism is compatible, at the formal level, with a constrained variational statement:

\[
\boxed{
\delta\left(
S+\sum_i\lambda_i C_i
\right)=0
}
\]

where \(S\) is an action functional and \(C_i=0\) are admissibility constraints.

This expression is a structural placeholder until a well-defined action, field variables, boundary terms, and dimensions are supplied.

## 14. What This Mechanism Claims — and Does Not Claim

### Claims at the framework level
- Distinguishable states can be represented by ordered transitions.
- Boundaries can be treated as active constraints on those transitions.
- Discrete cadence can be used to represent admissible structural updates.
- Reactive and dissipative responses can be separated conceptually.
- Observable redshift, expansion-like response, and rotational response are proposed as potentially related outputs of environmental state.

### Explicitly not claimed
- No empirical proof of the substrate is claimed.
- No observational validation is claimed in this file.
- No resolution of the Hubble tension is claimed.
- No replacement of GR, Doppler redshift, or \(\Lambda\)CDM is claimed by declaration.
- No claim that a black-hole horizon has been derived from the present mechanism is made.
- No claim that dark matter is disproved is made.

## 15. Falsifiability Requirements

The mechanism becomes scientifically discriminating only when it supplies:

1. A dimensional definition of \(D_{\rm eff}\).
2. A derived \(F\) for optical phase response.
3. A derived relation between boundary state and \(\Gamma_n,\Delta V_n\).
4. A strong-field limiting relation.
5. Independent datasets and covariance-aware tests.
6. Reproducible numerical implementations and raw outputs.

Until these are supplied, the mechanism remains a **proposed low-contradiction explanatory architecture**.
