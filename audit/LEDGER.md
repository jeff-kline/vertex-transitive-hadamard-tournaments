# Review ledger

All reviews below were process-separated AI reviews. They are not independent
expert peer review. Each defect is labelled error, gap, missing hypothesis,
sharpening or documentation. Review reports are copied verbatim into
[reviews/](reviews/); their relative links point into the working directories
where they were written and are not part of this repository. Draft numbering
changed between versions; each report states the version it examined.

| Date | Scope | Verdict | Dispositions |
|---|---|---|---|
| 2026-11-21 | classification below $10^4$ (isolated attack and proof audit of each component) | VERIFIED | earlier record; superseded by the reviews below |
| 2026-11-22 | five-page sketch (claims, citations, order 27) | findings applied | Cayley corollary via Marušič (sharpening); Kelly–Johnsen credit (documentation); order-27 uniqueness from McKay's catalogue (sharpening); Mansilla caveat (documentation). [Report](reviews/SKETCH-REVIEW-2026-11-22.md) |
| 2026-11-22 | full seventh draft, cold read | VERIFIED, conditional on quoted theorems | abstract's two-prime claim needed $a,e\ge1$ (missing hypothesis); census row labels (documentation); direct proof for Corollary 2 (sharpening). [Report](reviews/COLDREAD-v7.md) |
| 2026-11-22 | descent in the $pr^4$ theorem | VERIFIED | none. [Report](reviews/AUDIT-pr4-descent.md) |
| 2026-11-22 | census, independent re-implementation (seventh-draft rules) | MATCH | none. [Report](reviews/CENSUS-INDEPENDENT.md) |
| 2026-11-22 | five proofs shortened in the ninth draft | VERIFIED | Dixon's theorem needs a finite group and a perfect field (missing hypothesis, applied). [Report](reviews/AUDIT-v9-shortened.md) |
| 2026-11-22 | primary-source citation check, 20 references | 16 YES, 1 PARTIAL, 3 NOT ACCESSED | Dixon statement (missing hypothesis); Garcia title (documentation); Gorenstein locator replaced by an inline proof; Kelly–Johnsen kept as historical credit with the direct proof; Mansilla settled by the next row. [Report](reviews/CITATIONS-v9.md) |
| 2026-11-22 | Mansilla (2004), full text | none doubly regular | Proposition 44 restored; the earlier caveat removed (documentation). [Report](reviews/MANSILLA-v9.md) |
| 2026-11-22 | census of this repository (`make verify`) | MATCH | — |
| 2026-11-22 | release audits: claims consistency; full cold read in two halves; census re-implemented from the theorem statements | CONSISTENT AFTER FIXES; VERIFIED; VERIFIED; census 0 disagreements in 25000 | v > 1 made explicit (documentation); Reid–Brown sketch adds the identity (documentation); Mansilla's orders are odd (documentation); methods paragraph reworded (documentation); chief-step ratio fact stated (documentation); README linear-bound hypotheses and Theorem D inputs (missing hypothesis, documentation); Proposition 44 added to the paper's novelty sentence (documentation). [Report](reviews/RELEASE-AUDITS-2026-11-22.md) |

Which system found which result is recorded in
[ATTRIBUTION.md](ATTRIBUTION.md).
