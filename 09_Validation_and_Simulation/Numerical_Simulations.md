---
title: "Numerical Simulations and Metric Verification"
version: "v3.5.1"
status: "Method Specification — Not Verified"
date: "2026-09-11"
framework: "CADENCE-SDF-Dynamic-Architecture"
license: "CC-BY-4.0"
doi: "10.5281/zenodo.22412461"
---

# Numerical Simulations and Metric Verification

## 1. Candidate Metric Mapping

The current candidate metric mapping is

\[
g_{\mu\nu}^{(n)}
=
\eta_{\mu\nu}
+
\alpha_{\rm metric}
\left(
\frac{\omega_c(x,\tau)}{\omega_{\rm ref}}
\right)
\left(
\frac{\nabla_\mu\Phi\nabla_\nu\Phi}
{\|\nabla\Phi\|^2+\varepsilon_{\rm reg}}
\right)
\]

where $\omega_{\rm ref}$ is a reference cadence scale with the same dimensions as $\omega_c$ and $\alpha_{\rm metric}$ is dimensionless (dimensionally consistent with the canonical ansatz in `04_Canonical_SDF_Mapping/M_Metric_Emergence.md`; the older dimensionally inconsistent form is superseded).

This is a **model ansatz**. It is not established as a derived field equation.

## 2. Working Parameters

Previous working values are retained for reproducibility of future tests:

- \(\alpha_{\rm metric}=2.1\)
- \(\varepsilon_{\rm reg}=10^{-5}\)

They are not presented as empirically fitted constants.

## 3. Required Numerical Evidence

A statement that numerical integration “demonstrates” a property must be accompanied by:
- source code;
- parameter/configuration file;
- initial/boundary conditions;
- dependency/environment record;
- raw output;
- convergence test;
- independent rerun.

No such evidence is included in this release.

## 4. Candidate Checks

Future execution should test:
1. behavior as \(\nabla\Phi\to0\);
2. sensitivity to \(\varepsilon_{\rm reg}\);
3. signature and determinant behavior;
4. convergence under step refinement;
5. dependence on boundary conditions;
6. behavior in weak-, intermediate- and strong-field regimes.

**Status:** NOT VERIFIED.

## Verification Gate

See `verification/VERIFICATION_MANIFEST.md` and `verification/run_gate.py`. The gate is fail-closed and does not treat documentation as evidence.
