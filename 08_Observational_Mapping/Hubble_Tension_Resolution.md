---
title: "Hubble Tension: Proposed Boundary-Cadence Interpretation"
version: "v3.5.1"
status: "Proposed Observational Mapping — Not a Resolution Claim"
date: "2026-09-11"
author: "Adel Gachkar"
framework: "CADENCE-SDF-Dynamic-Architecture"
lineage: "v3.4.2 -> v3.5.1"
license: "MIT"
doi: "10.5281/zenodo.22412461"
---

# Hubble Tension: Proposed Boundary-Cadence Interpretation

## 1. Scope

This note does **not** claim that the Hubble tension has been resolved. It records a candidate SDF mechanism for testing whether environmental boundary/cadence effects could contribute to differences between early- and late-universe inferences.

The numerical values below are retained as **working benchmark values from the previous release**, not as fitted or validated SDF results.

## 2. Proposed Mechanism

The candidate chain is

\[
\rho_{\rm env}
\rightarrow
\{\sigma_B,D_{\rm eff},\omega_c,n_{\rm eff}\}
\rightarrow
\Delta\Phi_{\rm opt}
\rightarrow
\mathcal O_{\rm cosmological}.
\]

A candidate phenomenological form previously used in the project is retained for testing:

\[
\Delta H_{\rm boundary}(z)
=
\Delta H_c
\left[
1+\left(\frac{z}{z_c}\right)^\alpha
\right]^{-1}.
\]

At this stage this is a **parametric ansatz**, not a derived law.

## 3. Working Benchmark Parameters

- Early-universe baseline: \(H_0^{\rm Early}=67.4\pm0.5\ {\rm km\,s^{-1}\,Mpc^{-1}}\)
- Late-universe benchmark: \(H_0^{\rm Late}=73.04\pm1.04\ {\rm km\,s^{-1}\,Mpc^{-1}}\)
- Difference used as a benchmark: \(\Delta H_c=5.64\pm0.42\ {\rm km\,s^{-1}\,Mpc^{-1}}\)
- \(z_c=0.15\pm0.02\)
- \(\alpha=2.10\pm0.08\)

These values must not be described as SDF measurements until a documented fit with data, likelihood, covariance and uncertainty propagation exists.

## 4. Candidate Observational Tests

| Test | Proposed signature | Current status |
|---|---|---|
| BAO / standard-ruler measurements | possible environment- or redshift-dependent residual | Testable |
| Supernova residuals | possible boundary/environment correlation | Testable |
| Strong-lensing / compact-object environments | possible propagation-phase residual | Testable |
| Growth observables | possible environment-dependent modification | Testable |
| Void vs dense-region comparison | correlated change in \(z_{\rm prop}\) and local expansion estimate | Testable |

No item in this table is marked “verified” or “resolved”.

## 5. Redshift Decomposition

The proposed SDF contribution is represented separately from other redshift mechanisms:

\[
1+z_{\rm obs}
=
(1+z_{\rm known})(1+z_{\rm SDF}),
\]

where \(z_{\rm SDF}\) is a placeholder for the proposed cumulative phase-step contribution.

The model must eventually distinguish:
- Doppler contribution;
- gravitational contribution;
- cosmological contribution;
- proposed structural/propagation contribution.

The present document does not determine their relative magnitudes.

## 6. Algorithmic Benchmark

```python
import numpy as np

def hubble_boundary_ansatz(
    z, H0_base=67.4, delta_Hc=5.64, z_c=0.15, alpha=2.1,
    Omega_m=0.315
):
    """Phenomenological SDF benchmark; not a fitted/validated law."""
    E_z = np.sqrt(Omega_m * (1 + z)**3 + (1 - Omega_m))
    transition = 1.0 / (1.0 + (z / z_c)**alpha)
    return H0_base * E_z + delta_Hc * transition
```

This function is a reproducible **ansatz**, not evidence.

## 7. Required Evidence for a Resolution Claim

A future resolution claim requires:
1. public dataset/version;
2. covariance matrix or likelihood;
3. parameter-fitting code;
4. priors and nuisance model;
5. posterior/likelihood output;
6. comparison with baseline models;
7. out-of-sample or independent-data test;
8. residual analysis.

Until then the title and language remain deliberately non-assertive.
