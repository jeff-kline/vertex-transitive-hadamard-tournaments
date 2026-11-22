# Audit: Theorem 51 (`thm:pr4`), order p r^4, and the descent to order p r^2

```text
STAGE: PROOF-AUDIT
VERDICT: VERIFIED
```

**CLAIM.** `draft/main.tex` (sha256 `2daacc75…5232d801`, 1094 lines), Theorem 51
(`thm:pr4`, lines 799–816): for odd primes p ≠ r with p ≡ 3 (mod 4) and p < r^4 there is
no vertex-transitive Hadamard (doubly regular) tournament of order p r^4. The descent is
the second case of the proof (p = r^2+r+1), with Lemma 50 (`lem:converse`) and Lemma 40
(`lem:fixedplane`). The verdict covers the proof as written, conditional only on the
standard facts the manuscript quotes (Feit–Thompson, Hall subgroups, Fitting subgroup).

## EVIDENCE: the proof rebuilt

Notation: G transitive on X, |X| = v = p r^4, S the signed matrix.

**Case p ≠ r^2+r+1 (lines 805).**
1. O_p(G) = 1: its orbits would have size p (a p-power > 1 dividing v), giving r^4 blocks,
   prime to p; Prop. 18(3) (quotient law) forbids this. Checked.
2. A minimal normal Z is elementary abelian of characteristic dividing v, hence an
   r-group. Orbit size h ∈ {r,…,r^4}; Lemma 15 (`lem:disc`) needs ν_r(v) = 4 even, gives
   ν_r(v/h) even, so h ∈ {r^2, r^4}. Checked.
3. h = r^4: p orbits, one stabilizer each (Lemma 12), index r^4, covering Z by the
   fixed-point law (elements of Z have order prime to p). Lemma 13 gives p > r^4. This is
   the only place p < r^4 is used. Checked.
4. h = r^2: Prop. 22 (`prop:r-structure`) gives r^2+r+1 | p r^2, hence = p. Checked.

**Case p = r^2+r+1 (lines 807–816).** Here p < r^3 < r^4 automatically.
5. Lemma 40 with e = 2, hypotheses match (r odd prime, p = r^2+r+1 prime ≡ 3 mod 4,
   v = p r^{2e}). I re-derived it:
   - K: last chief step of characteristic r with ratio > 1 (Lemma 38). b_K is a p-power
     dividing v and b_K > 1 (already by Lemma 28, b_K > m), so b_K = p; K-orbits Δ_i of
     size r^4. Prop. 29 is cited but not needed for this.
   - Lemma 37: R ∈ Syl_r(K) transitive on each Δ_i, G_1 = N_G(R) transitive on X (Frattini),
     U = Ω_1(Z(R)) ⊴ G_1, U-orbit size r^d with d even and r^d < p < r^3, so d = 2.
   - Prop. 22 applied to (G_1, U): U ≅ C_r^3, all r^2+r+1 = p lines are stabilizers; the
     stabilizer is constant on Δ_i (R centralizes U); p blocks, p lines, so a bijection.
   - (3): Fix(H) for H = R_x lies in Δ_i (L_i ≤ H, L_i ∩ L_j = 1), has n = [N_R(H):H]
     points, n ≥ r^2 since H centralizes U. The stabilizers R_y are G_1-conjugate, at most
     p|R|/(n|H|) of them, and cover R; so n ≤ p < r^3 and n = r^2, Fix(H) = Ux. Checked.
6. Cells = U-orbits: b = p r^2 cells of size r^2, r^2 per block. Q = Q_U.
7. Cells in different blocks: stabilizers L_i ≠ L_j, [L_iL_j : L_j] = r; Lemma 16 gives an
   odd multiple of r. Checked.
8. Cells in the same block. R_0 = kernel of R on all cells, E = R/R_0 ≠ 1, Ẑ = preimage of
   Ω_1(Z(E)). U ≤ R_0 ≤ Ẑ; Ẑ ⊴ G_1 because R_0 = R ∩ ker(G_1 on cells) is normal in G_1 and
   Ω_1(Z(E)) is characteristic. Ẑ-orbits: common size r^{2+c} inside a block, unions of
   cells. Lemma 15 needs only equal orbit sizes: ν_r(p r^{2-c}) even, so c ∈ {0,2}. c = 0
   would put Ẑ in R_0, but Ẑ/R_0 ≠ 1. So Ẑ is transitive on every block, Ω_1(Z(E)) is
   transitive on the r^2 cells of Δ_i, its image there is regular and self-centralizing
   (Lemma 12), and the image of E, which centralizes it, equals it. Checked.
9. H = R_x fixes the cell O = Ux, so by regularity it fixes every cell of Δ_i setwise.
   Fix(H) = O by step 5, so H has no fixed vertex in O' ≠ O; H is an r-group, so its orbits
   on O' have length divisible by r; S[x,·] is H-invariant. Hence r | Q[O,O']. Checked.
10. Lemma 14: off-diagonal entries odd, diagonal 0 (skew), row norm v − r^2 = r^2(b−1)
    with b−1 off-diagonal entries each of absolute value ≥ r. So all are ±r. S' = Q/r is
    skew, 0 on the diagonal, ±1 off it, S'S'^T = (v/r^2)I − J = bI − J. Checked.
11. Lemma 50: S'^T 1 = 0 from 1^T S'S'^T 1 = 0; the count n_1 = n_2, n_1+n_2−n_3−n_4 = −1,
    total b−2 gives n_1 = (b−3)/4 for every ordered pair. Checked; b = p r^2 ≡ 3 (mod 4).
12. G_1 permutes the cells transitively and Q[gO,gO'] = Q[O,O'], so the image of G_1 in
    Sym(cells) is a transitive group of automorphisms.

**Answers to the brief.**
- Induced object: yes, a doubly regular tournament. Vertex set: the p r^2 orbits of
  U = Ω_1(Z(R)) ≅ C_r^3 (not orbits of a normal subgroup of G). Order p r^2.
- Transitive group: the image of G_1 = N_G(R) on the cells (G itself need not act on them).
- Invocation: Theorem 1 (`thm:fourthfree`), stated for every fourth-power-free v > 1 with
  no further hypothesis.
  (Theorem numbers are those of `main.aux` for this revision.) p r^2 with p ≠ r is fourth-power-free and not p' or p'^3. The
  hypotheses match exactly. For this order the chain is short: Prop. 25 (`prop:plane`,
  r^2 ∥ v) gives O_r = 1, so F = O_p ≠ 1 with orbits of size p and r^2 blocks, against the
  quotient law. I re-checked Prop. 25 and Lemma 24 step by step; no defect.
- p = r^2+r+1: no longer an exception. It is exactly the second case. Instances exist
  (r = 5, 17, 41, 89), so the case is not vacuous as a hypothesis; r = 5, 17, 41 are also
  excluded independently by Theorem 48, which agrees.

## COVERAGE

- Circularity: none. Theorem 51 uses Lemmas 12–16, Prop. 18, Prop. 22, Lemma 28, Lemmas
  37, 38, 40, 50 and Theorem 1. Theorem 1 ← Theorem 4 ← Cor. 27 (← Prop. 25 ← Lemma 24),
  Prop. 36, Lemma 28, all in Sections 2–7. `grep` of every `\ref{thm:pr4}`,
  `\ref{lem:fixedplane}`, `\ref{lem:converse}`, `\ref{sec:singer}`: the only uses outside
  Section 8 are prose in the introduction, Remark `rem:sharp` (a forward pointer, not a
  proof step), Section 9 remarks, the census table and the AI statement.
- Satisfiability control, p = r (orders p^5, prime powers): the argument stops at once.
  Case 1 step 1 needs gcd(r^4, p) = 1; step 2 needs ν_r(v) even (it is 5); steps 3–4 and
  Lemma 40(3) use the fixed-point law, valid only for elements of order prime to p;
  Lemmas 28, 38 and Prop. 22 require r ≠ p; case 2 needs p = r^2+r+1 ≠ r. Even the last
  step is harmless: a quotient of order p^3 is allowed by Theorem 1.
- Positive control (computed): in the Paley tournaments on F_27 and F_343 with U an
  F_p-plane (orbits p^2), Q Q^T = vI − p^2 J holds, every off-diagonal entry of Q is ±p,
  and Q/p is a doubly regular tournament of order p. So the quotient mechanism is
  realized by genuine examples and is not itself contradictory; the contradiction in
  Theorem 51 comes only from Theorem 1. With U a line (orbits p) the entries are not
  constant in absolute value (1, 3 for p = 3; 1, 3, 5 for p = 7), as expected.
- Comparison (read at 09:55 CST, 2026-11-22, after steps 1–12 and the control were done):
  `DESCENT.md` (sha256 51499b04…) and `ito-lift-descent-audit.md` (sha256 927c10db…, see
  EXPOSURE). The manuscript proof is the auditor's "Simplification check" made complete:
  it keeps the regularity of E on the cells of a block and replaces the dual-plane/parity
  analysis, the rank-3 determination of E and the translation bijection by Fix(R_x) = Ux.
  It needs less than the auditor said: regularity suffices, elementary abelianness of E is
  not used. Both proofs give the same quotient on the same vertex set with the same group.
  I found no step where the short proof relies on something only the long one proves.
- Not checked: the external theorems quoted (Feit–Thompson etc.), the sections after 8,
  the census. Sections 2–7 were checked only along the dependency chain above
  (Prop. 29, Lemma 23, Lemma 35 and the case k = 2 of Prop. 36 are not load-bearing here).

## DEPENDENCIES

Discharged: Lemmas 9, 11–17, Prop. 18, Lemma 21, Prop. 22, Lemma 24, Prop. 25,
Cor. 27, Lemma 28, Lemmas 37, 38, 40(1)–(3), 50, and Theorem 1 at order p r^2. Remaining: none
internal; the standard solvable-group facts are quoted from the literature.

## ERRATA (none affects correctness)

1. Lemma 40(1) cites Lemma 38 for b_K > 1; Lemma 28 (b_K > m) already gives it, so the
   descent does not depend on Prop. 29. Optional remark.
2. In the proof of Theorem 51, "the tournament is vertex-transitive" could name the
   group: the image of G_1 on the cells. Optional.
3. The \TODO after the proof (line 818) can be removed: the short argument now has its
   own audit.
4. Theorem 1 is used at order p r^2 only through Prop. 25 and the quotient law; a
   one-line direct citation would make the dependency lighter. Optional.

## EXPOSURE

Read before forming the view: `~/.claude/skills/cold-examiner/SKILL.md`; `main.tex`
lines 41–108, 135–529, 530–612, 774–822. Read after (09:55 CST): `DESCENT.md`
(51499b04cf43c099bdac2330d9c95da507c6b61fbc2088ccbc2ba49372c0cccc) and
`ito-lift-descent-audit.md` (927c10db7f9a6ab34edef63979d1d4cd90609e6836cb2e8ef6186b49adedd4ed). No Stage 1 initial report exists for this proof in this
directory; this is a Stage 2 audit only, by one same-model reviewer. No searches.

## RESOURCES

Allocation 20 CPU-seconds, one core, nice 19. Used 0.34 CPU-seconds (one run of
`pr4_control.py`, venv Python, 27- and 343-vertex Paley matrices; script in the session
scratchpad, not kept). About 15 minutes wall. Everything else by hand.
