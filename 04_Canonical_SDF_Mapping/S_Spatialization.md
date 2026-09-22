---
title: "S — Spatialization"
author: "Adel Gachkar"
tags: ["SDF", "04", "Mapping"]
status: "Canonical"
date: 2026-09-08
version: "v3.5.1"
doi: "10.5281/zenodo.22412461"
module: "04_Canonical_SDF_Mapping"
framework: "CADENCE-SDF-Dynamic-Architecture"
license: "MIT"
---

# S — Spatialization
## فضایی‌سازی S

> **Structural Causal Chain:**
> Constraint → Differential Tension (ΔΦ) → Quantized Step (δs) → Cadence → Metric Emergence (g_μν) → Observable Dynamics

**Purpose / هدف:**
Convert the cadenced relaxation record into spatial extent.
تبدیل رکورد آرامش کادنس‌دار به گستره فضایی.

**Role in Causal Architecture:**
- **Stage:** S (third term of the canonical sequence)
- **Function:** Spatialization operator S: relaxation history becomes spatial extent.

  $$S:\; \{\delta s_k\}_{k=1}^{N} \longmapsto s = \sum_{k=1}^{N} \delta s_k = s_0\sum_{k=1}^{N} n_k,\quad n_k\in\mathbb{Z}^+$$

  The accumulated path $s$ is the integration variable of foam-induced phase:

  $$\delta z_{\text{foam}} = \int_0^s \frac{\nabla|Z_{\text{medium}}|}{Z_0}\,ds
     = \oint \Gamma_{\text{impedance}}\, d\ell$$

  with medium impedance:

  $$Z_{\text{medium}}(z,\rho) = R_{\text{loss}}(\rho) + j\omega L_{\text{foam}}(\rho) + \frac{1}{j\omega C_{\text{boundary}}(\rho)}$$

  and fractal dimension decay $D_f(\rho) \approx D_{f,0}\cdot e^{-\rho/\rho_c}$
  controlling the density-gradient source $\nabla|Z_{\text{medium}}|$.
- **Upstream:** Cid
- **Downstream:** R (internal distance relations over $s$)
