# Independent census (from theorem statements of main.tex only)

Script: checks/census_independent.py (0.7 s, one core). Range: v = 3 mod 4, 3 <= v < 100000 (25000 values).

## Result
- open == [54675]: YES. Every v < 54675 is classified: YES.
- Order of tests (statement order in the paper, Ito first): realized 4819; Ito Thm 1 18388; Thm fourthfree 1622; Thm divisor 22; Prop prefix 6; Thm pr4 23; Thm exponent 6; Thm 729p 104; Thm twoprime 1; Thm fittingclass 1; Thm fittingintro(3) 7; open 1. Total 25000.
- Standalone exclusions per statement (ignoring order): Ito 18388; fourthfree 19825; cor cubefree 18961; exponent 1628; divisor 341; twoprime 24; prefix 358; cor chief 352; pr4 37; singer list 3; 729p 800; fittingintro(3) 1758; fittingclass 1780.
- Cumulative classification does not depend on which order is used for the union, only the per-row counts do (paper's table order gives different row counts, e.g. exponent 6 here vs rows 3-10 there; union is identical).

## Vacuous statements
None of the implemented statements is vacuous in range. Thm singer excludes 775, 19375, 88723 standalone (3), but all are caught earlier by other tests (first-applicable count 0 in this order; the paper puts singer before pr4 and gets 1, for 19375). Thm twoprime excludes 24 standalone and first-applicable only 1 here; Cor cubefree is subsumed by fourthfree.

## Ambiguities and unimplemented
- Statements that are conditional on a group G (Prop plane, Cor fitting, Prop chiefbound, Prop endgame, Thm gate, Cor ord, Lemma rankbound, Thm fittingintro(1),(2), Prop HH, Prop metacirculant) give no exclusion of v alone; not implemented as exclusions.
- Thm singer: first sentence is conditional on a plane sign function; only the stated consequence (31*5^2e, 307*17^2e, 1723*41^2e) implemented.
- Thm fittingintro(3) uses k_i=1 or ord_p(r_i) >= 4k_i; fittingclass uses the gate-witness definition (conditions (1)-(6) of Thm gate, with (j,n,N) searched exhaustively, N over divisors of v/r^(2j)). Exclusion = "a<=1 and v is not a power of p".
- Prop endgame chained after fittingclass (F(G) p-group => a>=2 when u>1) is a two-statement combination; tested informationally: it excludes nothing extra from the open list (54675 has a=3).
- Thm divisor: D(u) < p^(a+1/2) done as D(u)^2 < p^(2a+1) in exact integers; D(t) <= p exact.
- Thm exponent: hypotheses s>1 odd squarefree prime to p; conclusion a>=2 and r_i < p^(a-1) prod_{j<i} r_j; a<2 counts as excluded.
- Cor chief / Prop prefix applied with p = the unique prime of odd exponent (Ito), v not a prime power.
