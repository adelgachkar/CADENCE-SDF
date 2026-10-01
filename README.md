# CADENCE-SDF: Dynamic Architecture and Void/Lattice Gravity Dynamics

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23006055.svg)](https://doi.org/10.5281/zenodo.23006055)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23017338.svg)](https://doi.org/10.5281/zenodo.23017338) · version DOI (v3.6.9); the concept DOI above always resolves to the latest version.
**Version:** 3.6.8  
**Status:** Proposed Mechanistic Revision — not empirically established  
**Framework:** Structural Delimitation Framework (SDF)  
**Language:** English (monolingual edition — every note carries frontmatter `lang: "en"`; the canonical Persian discourse of the family lives in LIMEN-VACUI `fa/`)

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

**Family §5 executed battery (pointer, updated 2026-09-27):** while this repo's own gates stay fail-closed BLOCKED (E2 — non-execution never upgrades), the protocol's §5 battery in the canonical home (LIMEN `08_Protocol/Aligned-Protocol` §5) now carries nine executed tests, including the latest: **W3** — the criticality-notch price curve (`limen_d_crit_price.py`): the b_c no-go exemption (d_crit = 0.002 < d_det) is budget-limited, crossing at X* ∈ [1.97e7, 2.36e7] walker-steps (10–12× canonical) where d_det = 0.00194 ≤ d_crit; and **W7** — the Ward test of the shield→boost boundary (`limen_beta_ward.py`): mask-identical under three pre-boundary narratives [exact], decoration-invariant (S z=0.74, D z=0.96; BETA* = +0.076 resolution-limited and flagged) — the boundary belongs to the law, not to a narrative or a stream; and **W2** — the spectral test at the meeting point (`spectral_regime_prediction.py` at b_eff = b_c): the critical∧REAL composition is spectrally invisible (plain critical spectrum reproduced; no composite exponent; the node factor δθ = 0.02044 stays the sole registered carrier). Register bank: **7 done (W1–W4, W4b, W6, W7) / 1 pending (W5)** — LIMEN `08_Protocol/Two-Realm-Register`. **W4 update (2026-09-27):** the banked μ(x) wall model (LIMEN `tools/limen_w4_mu_wall.py`) refutes the A4 even/odd parity claim in-model — δθ/2π = 0.0204 remeasured as the even/odd-flatness magnitude of the magnitude channel; the parity split relocates to a direction-structured register (W4b, flagged not buried) — an E4 correction, honestly registered. **W4b executed (2026-09-27):** the chiral five-phase register (LIMEN `tools/limen_w4b_chiral_register.py` — W4-isotropic geometry + synthetic gauge flux f = δθ/2π [exact]) CONFIRMS the direction channel: linear split ω² ± f·g with chiral one-term eigenmodes (s/c ~ 0.99i), spectra magnitude-even in f (0.0e+00), raised-branch chirality odd (flip to 0.6% of π) — the node's parity lives in the assignment, not the magnitude; nature-side F3 untouched. **Explanatory closure (2026-09-27):** LIMEN `10_Reference/Explanatory-Closure` (FA+EN) now registers the two-channel closure of the pentagonal node — magnitude channel (W4: even/odd flatness ≈ δθ/2π) + direction channel (W4b: mirror-parity split with chiral one-term eigenmodes) — and records the α-blocker explicitly as a methodological constraint, not a model defect (S1/S2 sanctity preserved). This repo inherits the closure by pointer, not by copy; its own gates remain fail-closed BLOCKED (E2). **W5 executed (2026-09-27):** the 4.6 energy-scale ratio RESOLVED (`limen_w5_common_operator.py`) — ONE operator κ(g) = 0.025g²ω₀ at two registered g-points and clocks: 0.12 eV = h·κ(0.8)/π and 23.8 meV = ℏ·κ(0.57); the ratio decomposes as (2π)·(0.016/0.0061)·(1/π) = 5.246 [exact chain, 13% rounding residual, E4]; same-transition refuted, same-operator confirmed — no new scale. **Register bank: 8 done (W1–W5, W4b, W6, W7) / 0 pending — the work bank is FULLY executed** — LIMEN `08_Protocol/Two-Realm-Register`. **F3 migration gate W4c executed (2026-09-27):** the S→W migration is machine-readable (LIMEN `tools/limen_w4c_f3_migration.py` + `_ledger.json`) — four acceptance checks (D1 opposition split / D1b direction structure / D2 five-fold flatness / D3 operator power g²) pre-committed before data; in-silico the pentagonal node passes all four, the isotropic control and split-only mimic fail with named gates [sim]; F3 stays revere until aligned companion data passes the gate. This repo inherits the gate by pointer, not by copy; its own gates remain fail-closed BLOCKED (E2). **Protocol status document (2026-09-27):** LIMEN `10_Reference/Bank-Complete` (FA+EN, anchored to v0.12.0) consolidates the fully-executed work bank — the eight executed tests, the four E4 corrections the battery itself caught, and the open items exactly as designed (S1–S4 permanent; F1/F2 banked work; F3 until the W4c gate). **Unit convention now explicit family-wide (Vault §2.2.2): f_c = κ[rad/s]/π** — the κ[Hz]/π reading (differing by exactly 2π) reproduces nothing registered; exact identity **f_c·τ_d = 1/2**.

## 5b. Aligned Protocol Pointer

The unified epistemic protocol shared by the family repositories (LIMEN, SPUMA, CADENCE, Vault, CRG-Flux, VMC-QF) is canonically documented in
**LIMEN-VACUI `08_Protocol/Aligned-Protocol`** (Persian + EN mirror).

**Family status mirror (2026-10-01):** LIMEN-VACUI v0.12.3 (canonical home, Two-Realm Register 8/0) · SPUMA-VACUI v0.4.10 (K1/K2 emergence) · Emergence-SDF-Vault v30.3.11 (derived constants: κ_hop, τ_d, δθ) · CRG-Flux v0.1.0 (flexoelectric framework) · **VMC-QF v0.3.0** — vacuum-microcavity quantum-foam dynamics; an independently simulated arm sharing the register-bank discipline (records Vault-11..15q) and the δθ = 7.356103° constant; the δθ it uses is the same closed-geometry five-fold deficit registered here and in Vault (analogical role alignment, not a derivation). The live family map (versions, DOIs, fa↔EN) is the LIMEN-VACUI `wiki/` directory.

**The sanctity clause (family contract, 2026-09-25):** boundary silence is not vacancy — it is sanctity: peeking over the boundary is forbidden (every appropriation attempt lands in E1, not an answer); every known gap inside the boundary must be **flagged** (an unflagged gap = evasive silence, an E4 violation); and **ambiguity ≠ silence** — inside the boundary, logically resolvable ambiguity is a duty (this repo's BLOCKED KST gates are exactly such flagged gaps); at the pre-boundary there is no proposition to be ambiguous — there is sanctity to respect. Two-realm test: **is a tool conceivable? → ambiguity: work. Not? → silence: revere.** Executed register (7:4): LIMEN `08_Protocol/Two-Realm-Register`.

It formulates: the generative triad (constraint × silence × event), the derived norms E0–E5 (this repo's fail-closed validation policy is E2), the three regimes of silence, registered fundamentality, the three healthy paradox options (C′ recorded silence / C″ reframing / C‴ axiom replacement), and the **invariance-residue test** — the operational criterion separating legitimate dissolution of a frame-made paradox from evasion of a real one. The seven-pivot atlas of accepted physics' unnamed protocol execution is mapped there, labeled `[protocol-mirror]`: CADENCE here is a mirror, not a rival — a residue measurer, not a solver.

**Emergence/balance reference (2026-09-27):** the family's consolidated reference on emergence from the balance differential lives in LIMEN-VACUI `10_Reference/Emergence-Balance-Reference` (FA+EN), vocabulary registered in Vault `01_Foundations/Rank-Ladder-Glossary` (rank-0 ΔB → vector → tensor → declarative components → dynamics; energy as scalar ledger and dynamics; self-referential measurement). CADENCE's differential tension ΔΦ and quantized step δs are the rank-0 scalar and the stepped-flow stages of that ladder under their own names — an analogical role alignment, not a derivation.

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
