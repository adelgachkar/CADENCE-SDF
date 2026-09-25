# CADENCE-SDF: Dynamic Architecture and Void/Lattice Gravity Dynamics
**Version:** 3.6.0  
**Status:** Proposed Mechanistic Revision — not empirically established  
**Framework:** Structural Delimitation Framework (SDF)  

---

## 1. Purpose

CADENCE-SDF is a proposed structural framework in which constraints and boundaries are treated as primary elements in the organization of discrete transitions. The present release is explicitly framed as a **mechanistic hypothesis**, not as an experimentally verified theory.

The central working idea is:

\[
\boxed{
\text{Distinction}
\rightarrow
\text{Boundary}
\rightarrow
\text{Directionality}
\rightarrow
\text{Quantized Transition}
\rightarrow
\text{Cadence}
\rightarrow
\text{Phase/Metric Response}
\rightarrow
\text{Observable}
}
\]

The mechanism is intended to provide a unified explanatory architecture with fewer conceptual conflicts among its assumptions and candidate observables. “Lower contradiction” is a methodological objective, not an empirical result.

## 2. Existing Architectural Chain

The seven-stage notation is retained:

\[
\mathbf{G\to C_{id}\to S\to R\to M\to L\to F}.
\]

See `02_Causal_Architecture/Causal_Sequence_Master.md`.

## 3. Mechanism

The principal mechanistic document is:

`02_Causal_Architecture/Proposed_Mechanism_Low_Contradiction.md`

It introduces:
- distinguishable prior/posterior states;
- boundary-conditioned directionality;
- active/reactive separation;
- bounded reactive/uncertainty states;
- discrete optical phase-step response;
- environmental dependence;
- proposed links to redshift, expansion-like response and rotation;
- strong-field/black-hole behavior as a future limiting test;
- constrained variational form.

## 4. Epistemic Status

The following are **not claimed as established** in this release:
- physical existence of a quantized substrate;
- empirical verification of the SDF mechanism;
- resolution of the Hubble tension;
- replacement of general relativity or Doppler/cosmological redshift;
- elimination of dark matter;
- derivation of black-hole horizon physics.

Numerical and observational statements are therefore classified as **candidate parameters, benchmarks, or tests** unless accompanied by executable evidence.

**Per-number epistemic triage — every number in this repository belongs to exactly one of three classes:**

- **Closed geometry** — exact mathematics *of the model*, derivable on paper; not a measured quantity of nature: δθ = 2π − 5·arccos(1/3) = 7.356103°; φ_max = π/√18 = 0.7405; packing/void radii; multipole-ladder exponents; two-sheet wall exactness.
- **Our own simulations** — reproducible in silico (`09_Validation_and_Simulation/`, `tools/`); no external empirical validation exists for them: κ_hop = 0.025g²ω₀ with g = 0.8 fixed by our Meep cavity benchmark (λ₀ = 320 nm) ⇒ f_c ≈ 30 THz, h·f_c ≈ 0.12 eV; KST benchmarks where actually executed; synthetic-data fits.
- **Real empirical phenomena** — measured in the real world by others: only the **Pantheon+ supernova compilation**, used as *fit input* for the boundary-shape ansätze. The data are real; the SDF interpretation of the residuals is not established and remains a candidate test. (The graphene-wrinkle experiment lives in SPUMA-VACUI as the K2 mechanism anchor.)

No number in this release is presented as a measured property of a real quantized substrate; the substrate itself is a model construct.

## 5. Validation Policy

The KST suite is a protocol specification. A test is not considered verified merely because an acceptance criterion is written in the documentation.

Current release status:

**KST-01..04: BLOCKED — executable inputs/implementations/raw outputs not included in this archive.**

See:
`09_Validation_and_Simulation/Kinetic_Stability_Tests.md`

## 5b. Aligned Protocol Pointer

The unified epistemic protocol shared by the four family repositories (LIMEN, SPUMA, CADENCE, Vault) is canonically documented in
**LIMEN-VACUI `08_Protocol/Aligned-Protocol`** (Persian + EN mirror).

**The sanctity clause (family contract, 2026-09-25):** boundary silence is not vacancy — it is sanctity: peeking over the boundary is forbidden (every appropriation attempt lands in E1, not an answer); every known gap inside the boundary must be **flagged** (an unflagged gap = evasive silence, an E4 violation); and **ambiguity ≠ silence** — inside the boundary, logically resolvable ambiguity is a duty (this repo's BLOCKED KST gates are exactly such flagged gaps); at the pre-boundary there is no proposition to be ambiguous — there is sanctity to respect. Two-realm test: **is a tool conceivable? → ambiguity: work. Not? → silence: revere.** Executed register (7:4): LIMEN `08_Protocol/Two-Realm-Register`.

It formulates: the generative triad (constraint × silence × event), the derived norms E0–E5 (this repo's fail-closed validation policy is E2), the three regimes of silence, registered fundamentality, the three healthy paradox options (C′ recorded silence / C″ reframing / C‴ axiom replacement), and the **invariance-residue test** — the operational criterion separating legitimate dissolution of a frame-made paradox from evasion of a real one. The seven-pivot atlas of accepted physics' unnamed protocol execution is mapped there, labeled `[protocol-mirror]`: CADENCE here is a mirror, not a rival — a residue measurer, not a solver.

## 6. Reproducibility

A scientific verification claim requires, at minimum:
- executable implementation;
- versioned input/configuration;
- raw output;
- environment/dependency record;
- deterministic or seeded execution where applicable;
- acceptance report.

Until these are available, numerical sections remain **proposed methods**, not evidence.

---
