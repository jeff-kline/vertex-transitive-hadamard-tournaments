# Prior-art record

Claims compared: Theorems A–D, Corollaries 1–2 and Proposition 44 of the paper.

## Searches

Two bounded searches, with their query logs:

- [search-log-2026-11-21.md](search-log-2026-11-21.md): Semantic Scholar,
  OpenAlex and Crossref lists of works citing Ito (1984); zbMATH reviews of
  Ito 1984, 1988 and 1996; web, GitHub and arXiv queries.
- [search-log-2026-11-22.md](search-log-2026-11-22.md): the citing works
  again, arXiv abstract searches, five web searches, GitHub (with a positive
  control) including repositories written by AI agents, and the aiXiv search
  pages for "tournament" and "Hadamard".

Not searched: Google Scholar (automated requests are redirected to a bot
check; logged as not performed, not as "no hits") and MathSciNet
(subscription).

## Closest sources

| Source | What it proves | Relation to this paper |
|---|---|---|
| Ito, Europ. J. Combin. 5 (1984) 37–42 | $v=pt^2$; prime power when a regular or supersolvable transitive subgroup exists; $v\ne9p$ for $p>3$ | the starting point; Theorem C contains the $9p$ case; the trace lemma is close to Ito's Lemma 5 |
| Kelly, PAMS 5 (1954); Johnsen, J. Algebra 4 (1966) | prime order with a cyclic transitive group gives Paley (as quoted by Ito, p. 37; original theorem pages not openly accessible) | Corollary 2 combines Theorem B with this conclusion; the paper gives a direct proof |
| Marušič, Ann. Discrete Math. 27 (1985) | vertex-transitive digraphs of order $p^k$, $k\le3$, are Cayley (checked against the original abstract) | used in Corollary 1 |
| Mansilla, Discrete Math. 288 (2004) | non-Cayley vertex-transitive tournaments of odd prime-power order $p^k$, $k\ge4$, and lexicographic products with Paley tournaments (full text read) | none is doubly regular (Proposition 44) |
| Javier, Llano and Zuazua, Contrib. Discrete Math. 21 (2026) | state, citing Mansilla, that non-Cayley vertex-transitive doubly regular tournaments exist | not supported by Mansilla's constructions |
| Feng, JCTA 118 (2011); Muzychuk, arXiv:1012.2089 | non-Paley skew Hadamard difference sets of order $p^3$ | Remark 45: Corollary 2 does not extend to $p^3$ |
| Araujo Garcia, Australas. J. Combin. 95 (2026) | a nilpotent group with a skew Hadamard difference set is a $p$-group; Conjecture 2.9 | Conjecture 2.9 is equivalent to Ito's Theorem 2 |
| Pasechnik, Acta Appl. Math. 29 (1992); Ito, J. Algebra 131 (1990) | association schemes and binary matrices of Hadamard tournaments | no results on transitive groups |

Primary-source checks of every cited theorem are in
[reviews/CITATIONS-v9.md](reviews/CITATIONS-v9.md) and
[reviews/MANSILLA-v9.md](reviews/MANSILLA-v9.md).

## Verdict

SOURCE-NEGATIVE: no earlier proof of Theorems A–D, Corollaries 1–2 or
Proposition 44 was found in the sources examined. This is not a claim of
global priority.
