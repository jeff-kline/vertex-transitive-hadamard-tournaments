# Mansilla 2004 against v9 (22 Nov 2026)

Source: sources/mansilla2004-dm.pdf (full article, Discrete Math. 288 (2004) 99–111, supplied by Jeff), text in sources/mansilla2004-dm.txt.

Families in the article:
1. T(p^k, p, alpha), order p^{k+1}, k >= 3 (Section 4, Theorem 9; example T(27,3,4) of order 81, Theorem 8). Metacirculant; the rotation rho: v^i_j -> v^i_{j+1}, j in Z_{p^k}, lies in Pi <= Aut T (Prop. 2 proof, Prop. 6): p cycles of length p^k. Order = 3 mod 4 needs p = 3 mod 4 and k+1 odd, so k+1 >= 5: excluded by Proposition prop:metacirculant (restored from v8; proof re-derived independently by the coordinator: trace of S on the zeta-eigenspace is h p^{(k-1)/2} sqrt(-p), h odd, vs |f_j| <= p via division by Phi_n = Phi_p(X^d)).
2. Theorem 14 and closing remark: lexicographic products P(q)[T] and (P(p^{l-1})[P(p)])[T] with T of family 1 or earlier products; outer regular tournament on a >= 3 vertices, fibres b >= 81. Two vertices of one fibre have >= b(a-1)/2 > (ab-3)/4 common out-neighbours: not doubly regular.

The article never claims double regularity (no occurrence of "doubly"). Verdict: no tournament in Mansilla is doubly regular. JLZ's attribution is unsupported by Mansilla's constructions. Question q:cayley stays a question.

Edits in main.tex (backup main-v9-post-codex.tex): Mansilla TODO replaced by Prop. prop:metacirculant + paragraph; Gorenstein 5.3.6 replaced by inline proof (Codex's argument), TODO removed; Kelly-Johnsen recast as historical credit with the direct proof, TODO removed; barrier paragraph added after Conjecture C1. Build: 30 pp, no undefined refs/overfull/missing destinations, all Type 1; census unchanged. sha256 35cf7174ccf2b985...
