# Release audits of 22 November 2026

Three process-separated AI reviews of commit 46473a4 (paper as approved by the
author, before the title change). Read-only; fresh contexts; the two proof
auditors did not see earlier reviews before writing. Findings are condensed
from the returned reports; every defect is listed with its disposition.

## 1. Claims consistency (README, paper, CITATION.cff, ADMISSION, records)

Verdict: CONSISTENT AFTER FIXES. Ran `make verify` (MATCH); checked census
counts (sum 25000; 20181 = 25000 − 4819), page count, PDF hash, manifest, the
README result numbers against `main.aux`, citations against the bibliography,
README math rendering, and the absence of private paths and process-history
phrases in the paper.

| # | Finding | Class | Disposition |
|---|---|---|---|
| 1 | Abstract, README introduction and CFF omit "p = 3 when a = 4" from Theorem C | sharpening | kept: accurate and author-approved; the full statement is in the theorem and in README What is new |
| 2 | Same surfaces omit "p ≡ 3 (mod 4)" in Theorem B's conclusion | sharpening | kept, as for 1 |
| 3 | README evidence table omitted Ito's Theorem 1 and the Paley case as inputs to Theorem D | documentation | fixed |
| 4 | README linear-bound bullet lacked "v not a power of p" and the meaning of k | missing hypothesis | fixed |
| 5 | Proposition 44 called new in README and PRIOR-ART but not in the paper's novelty sentence | documentation | fixed in the paper |
| 6 | VERIFICATION.md used draft version numbers | documentation | fixed |
| 7 | CFF says version 0.1.0 while README says no version is released | documentation | intended; flips together at tagging |

## 2. Proof audit, Sections 1–7 and "What remains"

STAGE: PROOF-AUDIT. Verdict: VERIFIED for the mathematics in scope. Every
numbered result rebuilt: Lemmas 3–10, Proposition 11, Theorem 12, Corollaries
13–14, 16, Lemma 15, Proposition 17, Lemma 18, Proposition 19 (Steps 1–7),
Corollary 20, Lemma 21, Proposition 22, Lemmas 23–25, Proposition 26,
Theorem B, Corollaries 1–2, Proposition 44 (with an exact Paley(27) control:
an automorphism with 3 cycles of length 9 sits exactly at the borderline
k = 3). Ito's quotations and page numbers were checked against the original.
Unchecked here: Marušič, Mansilla, JLZ, Feng, Muzychuk, McKay sources (checked
separately in CITATIONS-v9.md and MANSILLA-v9.md).

| # | Finding | Class | Disposition |
|---|---|---|---|
| 1 | "then v ≡ 3 (mod 4)" fails for the one-vertex tournament; v > 1 not a standing assumption | documentation | fixed (introduction and Section 2) |
| 2 | Reid–Brown sketch: the skew Hadamard matrix is the bordered matrix plus the identity | documentation | fixed |
| 3 | Mansilla's orders are odd prime powers | documentation | fixed |
| 4 | "uses S² = J − vI on one orbit or fibre at a time" ignores the orbit matrix and Theorem 52 | documentation | reworded |
| 5 | Remark 45: the Muzychuk count needs a pinpoint source | documentation | already cited to Muzychuk §6, p. 8 (checked in CITATIONS-v9.md); wording now says Muzychuk showed it |

## 3. Proof audit, Sections 8–10 and Appendix, with an independent census

STAGE: PROOF-AUDIT. Verdict: VERIFIED for the scope. Every result in the
Fitting-subgroup section (Lemmas basic, forms, rep, uA, types; Theorems
linear, center, endpoint, powers; Theorem C), the gate and Corollary ord,
Theorem fixedpart, Theorem A, Theorem D and its row table, and the Appendix
(prefix bound, fittingclass, Lemmas sylow, lastr, fixedplane; Theorem pr4)
was rebuilt. Uses of Hall–Higman, Aschbacher–Smith and Dixon match the quoted
hypotheses (sources themselves checked in CITATIONS-v9.md). No circularity:
the Appendix uses only Sections 2–7 and the gate.

Census: a new implementation written from the theorem statements alone,
before reading `code/census.py`, gives the same rows (18388, 1622, 7, 29,
134, 1), the same row-4 and row-7 orders, no unassigned order, and 0
disagreements in 25000 when compared order by order. Each rule of
`census.py` implements its theorem's hypotheses and none is broader. Every
rule except Theorem B is needed by some order; 19375 needs the
$p=r^2+r+1$ branch of Theorem pr4.

| # | Finding | Class | Disposition |
|---|---|---|---|
| 1 | The fact that each chief-step ratio is a power of the step's characteristic is proved only inside Lemma chief | documentation | stated in the Section 6 preamble |
| 2 | Theorem center: the case "p = 3 and k < 3" is vacuous under the hypotheses | documentation | kept; harmless |
| 3 | Theorem endpoint Step 2 uses Galois descent and Galois's theorem on solvable groups of prime degree without citation | documentation | kept; standard facts |
| 4 | Theorem fixedpart (1) could use p ≤ 4a − 5 | sharpening | not applied (mathematics frozen) |

Resources: under 5 CPU-seconds in total across the three reviews, single
core.
