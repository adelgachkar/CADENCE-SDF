# -*- coding: utf-8 -*-
"""One-shot metadata normalizer for the CADENCE-SDF v3.5.1 vault.

Rules:
- license: CC-BY-4.0 for every file with YAML frontmatter that lacks it.
- YAML frontmatter: added (minimal, canonical) to substantive vault notes that
  lack it. README / verification placeholder READMEs / the manifest are left
  without YAML (they are not canonical vault notes; the manifest is deliberately
  minimal and fail-closed).
- Adds framework + doi keys to substantive notes missing them so every canonical
  note carries the release identity.
Idempotent: running twice changes nothing further.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_YAML = {
    os.path.normpath("README.md"),
    os.path.normpath("09_Validation_and_Simulation/verification/VERIFICATION_MANIFEST.md"),
    os.path.normpath("09_Validation_and_Simulation/verification/code/README.md"),
    os.path.normpath("09_Validation_and_Simulation/verification/inputs/README.md"),
    os.path.normpath("09_Validation_and_Simulation/verification/outputs/README.md"),
    os.path.normpath("09_Validation_and_Simulation/verification/reports/README.md"),
}

MODULE_TITLES = {
    "02_Causal_Architecture/Differential_Pressure_Dynamics.md": "Differential Pressure Dynamics",
    "05_Physical_and_Reactive_Medium/Impedance_Network_Model.md": "Impedance Network Model",
}

TODAY = "2026-09-20"


def add_yaml(txt, rel):
    title = MODULE_TITLES.get(rel, os.path.splitext(os.path.basename(rel))[0].replace("_", " "))
    module = os.path.dirname(rel).replace("\\", "/")
    block = (
        "---\n"
        f'title: "{title}"\n'
        'author: "Adel Gachkar"\n'
        'tags: ["SDF"]\n'
        'status: "Canonical"\n'
        f'date: {TODAY}\n'
        'version: "v3.5.1"\n'
        'doi: "10.5281/zenodo.22412461"\n'
        'license: "CC-BY-4.0"\n'
        f'module: "{module}"\n'
        'framework: "CADENCE-SDF-Dynamic-Architecture"\n'
        "---\n\n"
    )
    return block + txt


def add_keys(txt):
    """Add license/framework/doi inside existing frontmatter when missing."""
    m = re.match(r"^---\n(.*?\n)---\n", txt, re.S)
    if not m:
        return txt, False
    body = m.group(1)
    changed = False
    lines = body.rstrip("\n").split("\n")

    def has(key):
        return any(l.strip().startswith(key + ":") for l in lines)

    if not has("license"):
        lines.append('license: "CC-BY-4.0"')
        changed = True
    if not has("framework"):
        lines.append('framework: "CADENCE-SDF-Dynamic-Architecture"')
        changed = True
    if not has("doi"):
        lines.append('doi: "10.5281/zenodo.22412461"')
        changed = True
    if not changed:
        return txt, False
    new_fm = "---\n" + "\n".join(lines) + "\n---\n"
    return new_fm + txt[m.end():], True


changed_files = []
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d != ".obsidian"]
    for f in fn:
        if not f.endswith(".md"):
            continue
        p = os.path.join(dp, f)
        rel = os.path.normpath(os.path.relpath(p, ROOT))
        txt = open(p, encoding="utf-8").read()
        orig = txt
        if rel in SKIP_YAML:
            new, ch = add_keys(txt)  # add_keys is a no-op without frontmatter
        else:
            m = re.match(r"^---\n(.*?\n)---\n", txt, re.S)
            if m:
                new, ch = add_keys(txt)
            else:
                new = add_yaml(txt, rel)
                ch = True
        if ch and new != orig:
            open(p, "w", encoding="utf-8", newline="\n").write(new)
            changed_files.append(rel)

print("updated:", len(changed_files))
for r in changed_files:
    print(" -", r)
