# COLDREAD-v7: Stage 2 proof audit of `draft/main.tex` (22 Nov 2026 draft, 32 pp)

```text
STAGE: PROOF-AUDIT
VERDICT: VERIFIED (internal arguments), with undischarged external citations listed under DEPENDENCIES
CLAIM: every theorem, proposition, lemma and corollary of main.tex as stated in the body
       (sha256 prefix 2daacc7589d51274); Theorem 8 as "the script census.py implements the stated theorems"
EVIDENCE: line-by-line check of each proof; exact Paley controls; one run of census.py
COVERAGE: all 49 numbered results; conjectures, questions, remarks read but only their checkable
          arithmetic audited
RESOURCES: about 4.5 CPU-seconds in total, single core, nice 19, venv Python (controls 3.0 s + one
           failed first run < 1 s caused by my own typo in a valuation formula + census 0.4 s)
```

No refutation and no gap in any internal proof. Two statement-level defects (abstract; one
sentence in Section 9) and a list of presentation defects are in ERRATA. Several results rest on
theorems quoted from secondary sources; those are marked "cited" below and are not verified here.

## Per-result table

Verdict key: V = VERIFIED (complete argument checked); V-cited = argument checked, but it uses an
external theorem not checked against its primary source.

| No. | Result | Verdict | Notes |
|---|---|---|---|
| 1 | Thm (fourth-power-free) | V | Follows from 4 and 18(1); converse by Paley on F_p, F_{p^3}. |
| 2 | Cor (cube-free => Paley) | V-cited | Uses Kelly/Johnsen via Ito's quotation. Can be made self-contained: character values of a skew Hadamard difference set in Z_p are (-1 ± sqrt(-p))/2, fixed by the squares in Gal(Q(zeta_p)/Q), so every square is a multiplier fixing D, hence D = squares or non-squares. |
| 3 | Cor (Cayley of a p-group) | V-cited | Uses Marušič 1985 (quoted from a 2026 preprint). The deduction from it is correct. |
| 4 | Thm (exponent rule) | V | From 27, 36, 28. Inequality chain r_i^2 <= m < b_K <= p^{2a+1-k} prod r_j^2 checked. |
| 5 | Thm (divisor gap) | V | From 30 and 32. Both claims checked, including u = 1 and t = 1. |
| 6 | Thm (two primes) | V-cited | From 38, 37, 22 and Nagell–Ljunggren (39). The step p^{2a+1} < r^3 needs a >= 1; correct. |
| 7 | Thm (rank / Fitting, intro form) | V | (1) = 52; (2) = 25 and 54; (3) = 55. |
| 8 | Thm (v < 10^5) | V (computational) | census.py matches the theorems rule by rule; one run reproduces every table entry and the open list [54675]. |
| 9 | Lem (S) | V | |
| 11 | Lem (odd order) | V-cited | Feit–Thompson. |
| 12 | Lem (abelian transitive) | V | |
| 13 | Lem (cover) | V | |
| 14 | Lem (orbit matrix) | V | Also checked numerically on the four controls. |
| 15 | Lem (orbit-discriminant law) | V | Positive definiteness makes the orthogonal splitting legitimate. Law is consistent with every prime power (parity computed; numeric controls). |
| 16 | Lem (orbit sums) | V | |
| 17 | Lem (trace) | V | Checked numerically on x->ax, x->x+1, x->ax+1 in all four controls. |
| 18 | Prop (laws; Ito Thm 1, 2) | V | Hall-subgroup counting argument checked. |
| 20 | Lem (prime orbit) | V | Does not need l != p. |
| 21 | Lem (planes) | V | Geometric trichotomy checked. |
| 22 | Prop (r-structure) | V | |
| 23 | Lem (orbits of size p^2) | V | Hilbert–Schmidt count and the alternating-form argument checked. |
| 24 | Lem (solvable, transitive on points of PG(2,r)) | V | Both cases; 3 mod 9 and 24 < 57 checked. |
| 25 | Prop (affine-plane obstruction) | V | All seven steps. Step 4 (|Y| = L) and Step 5 (tr(B)/r integral, Bezout with r∤c) are the load-bearing ones; both hold. |
| 27 | Cor (Fitting) | V | |
| 28 | Lem (chief step) | V | |
| 29 | Prop (chief-step bound) | V | Parity claim n(mu) even, projection to PG(2,r), and M^T M = I+J over F_2 checked. "Chief" is not used beyond K/L elementary abelian (optional generalization). |
| 30 | Prop (tail form) | V | |
| 32 | Lem (D formula) | V | Also brute-forced for n < 3000. |
| 33 | Cor (chief-factor bound) | V | |
| 35 | Lem (small linear groups) | V | 78, 48, 39 checked. |
| 36 | Prop (F(G) a p-group => 3 <= k <= 2a, a >= 2) | V | Burnside basis argument, O_p(G/P) = 1, the p = 3, d = 3 exception all checked. |
| 37 | Lem (Sylow reduction) | V | |
| 38 | Lem (last r-step) | V | |
| 39 | Thm (Nagell–Ljunggren) | cited | Not audited. Scan x <= 10^5, n in {2,3,5,7} finds only (18,7,3). |
| 40 | Lem (fixed plane) | V | (3): r^2 <= n <= p < r^3 checked; (4) congruence checked. |
| 41 | Lem (coordinates) | V | |
| 42 | Lem (directions) | V | |
| 43 | Prop (no plane sign function, r = 5) | V | Coefficient equations and F_3 = a(x_1+t x_2)^3 over F_5 recomputed. |
| 44 | Lem (order = first nonzero moment) | V | |
| 45 | Lem (line sums) | V | L*L = r delta_0 - 1, the count r(r^2-1) over r+1 classes, Newton, h <= m/2 all checked. |
| 46 | Prop (r = 13, 17) | V | Degree inequalities r+1, r+3, r+5 < 2r-2 and deg F >= 9 > 8 hold for both r. |
| 47 | Prop (r = 41) | V | h = 9 exclusion, 4d-84 < d, the exponent table 18, 13, 16, 21, and the unique lowest monomial checked. |
| 48 | Thm (Singer families) | V | 31, 307, 1723 prime and 3 mod 4 (checked). |
| 50 | Lem (converse) | V | |
| 51 | Thm (p r^4) | V | Both cases. The short descent (the one flagged as unaudited in the draft) is correct: E acts regularly on the r^2 cells of a block, so H = R_x fixes each cell of the block and, by 40(3), no vertex outside Ux. Uses Thm 1 only; no circularity. |
| 52 | Lem (rank bound) | V | AM–GM step, supermodularity of phi, induction via Z_1 = Y^perp checked. |
| 53 | Thm (gate) | V | |
| 54 | Cor (ord_p(r) >= 4k) | V | |
| 55 | Thm (Fitting class) | V | |
| 59 | Thm (p 3^{2k}) | V | Table of primes recomputed (3^j - 1 for j <= 11); ord_3851(3) = 11; 15404 > 14641. |
| 62 | Prop (Ito's question => Fitting conjecture) | V | |
| 63 | Prop (Hall–Higman application) | V-cited | Hypotheses match Theorem B as standardly stated (Gorenstein 11.1.1, recalled from memory, not re-read): p-solvable, O_p = 1, faithful in characteristic p; the exceptions need a nonabelian Sylow 2-subgroup when p is odd, impossible in odd order. |
| 66 | Prop (no automorphism with p cycles of length p^{k-1}, k >= 5) | V | Phi_{p^{k-1}}(X) = Phi_p(X^d) and the equal-coefficient argument checked. Consistent with Paley (Sylow p-subgroups there have small exponent). |

Remarks 10, 31, 34, 49, 56, 57, 58, 64, 67: arithmetic in 31, 49, 56, 64, 67 checked (witnesses
(2,6,847), (2,6,91); 5-part of |GL(d,3)|; 140/84, 369512/684). Weingartner, Feng, Muzychuk, McKay,
Mansilla statements are not audited.

## Priority items

1. Headline chain 17 -> 14, 15 -> 25 -> 4 -> 1 -> 2, 3: sound. No step uses a later result.
2. Newer sections: 29, 30, 6, 40, 43, 46, 47, 48, 51, 52, 53, 55, 36, 59, 63 all check.
3. Interfaces. Dependency order is acyclic: Thm 1 uses 25, 28, 36 only; 29 uses 28; 51 uses 40 and
   Thm 1; 6 and 40 use 29 through 38. Every application of 22, 15, 16 to G_1 = N_G(R) is legitimate
   because G_1 is transitive and the subgroup is normal in G_1.
4. Census: script and theorems agree; output equals the table.
5. Vacuity. No result excludes a prime power: 4, 30, 33, 36, 6, 48, 51, 59 require a second prime;
   5 holds at t = p^a with D(t) = p (27, 343) or 3 (3^5, 3^7); 15, 14, 17 verified numerically at
   27, 343, 3^5, 3^7; 20, 21, 23, 52 with l = p are satisfied by translation subgroups; 63's
   hypothesis holds for Paley on F_{p^n}, n < p. Every exclusion result for a prime r != p is a
   necessary condition whose hypothesis (a vertex-transitive example of non-prime-power order) is
   not known to be satisfiable; that is the content of Ito's question. The draft says so only after
   Theorem 4. Lemma 45 is conditional on a plane sign function of order r = 1 mod 4, of which none
   is known.
6. Ito quotations (Theorems 1 to 4, "Classic and seemingly only examples", "further possibility",
   the Kelly/Johnsen sentence, the Lam footnote, Lemma 5 on p. 39) compared with the PDF: accurate.

## ERRATA

### Correctness (statement level; no proof affected)
- C1. Abstract: "at orders p^{2a+1} r^{2e} ... the second prime satisfies r < p^a" omits a >= 1. Read
  literally at a = 0 it asserts non-existence at every order p r^{2e}, which is not proved.
- C2. Section 9, after the table: "Row 6 is empty because the orders ... are already assigned to
  row 5." Not all are: 29403 = 3^5 11^2 and 41067 = 3^5 13^2 fail Theorem 6 (r >= 9), pass row 5,
  and are assigned to row 4. Say "rows 4 or 5".

### Presentation
- P1. Prop 63 refers to "the second paragraph of the case k = 2" of Prop 36; that case is one
  paragraph. Point to the sentences from "The group G acts on V" to "H acts faithfully on V".
- P2. Overloaded letters within single sections: u (cofactor in v = p^{2a+1}u^2 and Ito's exponent
  in q^{2u}, both in Section 5); L (chief term, the number r^2+r+1, the quadratic character, the
  lines L_i); Q (orbit matrix and the polynomial in Lemma 45, both used near Thm 51); T (tournament,
  indeterminate in 46, polynomial E - X^m in 47); H, E, A, D, K, M.
- P3. Lemma 23, "Step 1: P elementary abelian" reads as a claim; it is the assumption of the step.
- P4. Prop 46: say explicitly that d < r because pi(f) != 0 in every direction (Lemma 45(1)), before
  invoking Lemma 42.
- P5. Prop 29: the hypothesis "consecutive terms of a chief series" can be weakened to "K/L
  elementary abelian" (optional generalization, not a defect).
- P6. State once, near Theorem 4 or in the introduction, that all exclusion theorems are necessary
  conditions and may be vacuous.
- P7. Open [VERIFY] boxes: Marušič 1985, Kelly/Johnsen, Nagell/Ljunggren/Terai, Hall–Higman,
  Weingartner, Feng, Muzychuk, McKay, Mansilla. Corollary 2 can drop its dependency (see table).

## DEPENDENCIES
Discharged: all internal lemmas. Remaining (not verified from primary sources): Feit–Thompson;
P. Hall; Nagell–Ljunggren (Thm 6); Marušič (Cor 3); Kelly–Johnsen (Cor 2, removable); Hall–Higman
Theorem B (Prop 63); Weingartner (Remark 34); Feng, Muzychuk, McKay catalogue (Remark 67).

## Overall verdict
VERIFIED: every proof in the manuscript is complete and correct as written, conditional on the
cited external theorems. Theorem 8 is reproduced by the script. Fix C1 and C2 before release.
VERIFIED here means I checked each inference; it is one reader of the same model family as some of
the authors of the proofs, not a formalisation.

## EXPOSURE
- Read in this order: cold-examiner SKILL.md; draft/main.tex in full (sha256 prefix 2daacc7589d51274; census.py 7cf1731e0cdcc37f;
  file dated 22 Nov 09:50); draft/census.py; draft/main.aux (numbering
  only); Ito 1984 PDF, all six pages, after forming verdicts on Sections 1 to 8.
- Not read: any working note or earlier audit under reviews/, including the other files in checks/
  (I saw their names in a directory listing only). I did not consult them afterwards either; no
  specific doubt required it.
- Unavoidable exposure inside the manuscript: the Draft boxes name earlier audits and their
  verdicts ("admit, bounded"; "four audits"), and say which argument in Thm 51 was unaudited.
- Tools: checks/coldread_v7_controls.py (written for this audit); one run of draft/census.py.
- No searches over signs, groups or matrices were made. The manuscript was not edited.
