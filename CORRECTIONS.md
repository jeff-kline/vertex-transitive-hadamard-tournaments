# Corrections, withdrawals, and supersession

This repository keeps a visible record of material corrections to released
claims and artifacts.

## Policy

- Minor typographical or navigational fixes may be made on the living default
  branch without changing an archived release.
- A change to a theorem statement, hypothesis, proof dependency, citation that
  affects priority or scope, or verification artifact creates a new version.
  The earlier tag and permanent archive remain unchanged and identifiable.
- A material error will be marked prominently in the README and in this file.
  The affected release will not be deleted or silently replaced.
- If an earlier proof of any of Theorems A–D is found, it will be credited in
  a new version.

Suspected errors may be reported through the repository's issue tracker:
<https://github.com/jeff-kline/vertex-transitive-hadamard-tournaments/issues>.

## Version history

### 0.1.0 — released 2026-11-22

- Tag `v0.1.0` at commit `7e49c29`; version DOI
  [`10.5281/zenodo.24448853`](https://doi.org/10.5281/zenodo.24448853), concept DOI `10.5281/zenodo.24448852`.
- The tagged snapshot retains its prepublication wording (“release
  candidate” in the README, “Draft” on the paper's title page) and carries no
  DOI, because the DOI was minted by Zenodo after the GitHub Release. The
  living repository and paper now carry the active DOI; the archived files
  were not changed.
- Release preparation, before the tag: the dispositions of all audit findings
  are in [audit/LEDGER.md](audit/LEDGER.md).
