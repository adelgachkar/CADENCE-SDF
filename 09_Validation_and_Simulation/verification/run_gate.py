#!/usr/bin/env python3
"""Fail-closed evidence gate for CADENCE-SDF KST verification.

Documentation placeholders do not count as evidence. The gate only passes
when executable code, non-placeholder inputs, raw outputs and a report exist
for every KST.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KSTS = ["KST-01", "KST-02", "KST-03", "KST-04"]

def files_matching(folder, prefix, suffixes=None):
    p = ROOT / folder
    if not p.exists():
        return []
    out = []
    for f in p.iterdir():
        if f.is_file() and f.name.startswith(prefix):
            if suffixes is None or f.suffix.lower() in suffixes:
                out.append(f)
    return out

def main():
    blocked = []
    for kst in KSTS:
        code = files_matching("code", kst, {".py", ".ipynb", ".m", ".jl", ".r"})
        inputs = files_matching("inputs", kst, {".json", ".yaml", ".yml", ".csv", ".toml", ".txt"})
        outputs = files_matching("outputs", kst, {".json", ".csv", ".txt", ".log", ".npz", ".npy", ".parquet"})
        reports = files_matching("reports", kst, {".md", ".txt", ".pdf", ".html"})
        if not all((code, inputs, outputs, reports)):
            blocked.append(kst)

    if blocked:
        print("BLOCKED:", ", ".join(blocked))
        return 2

    print("Evidence files present. Scientific execution/review is still required.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
