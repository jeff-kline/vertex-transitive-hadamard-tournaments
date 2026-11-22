# Novelty search: vertex-transitive doubly regular tournaments (DRT), v < 10^4

Date of search: 2026-11-21. Claim: for 3 <= v < 10^4 a vertex-transitive DRT exists iff v is a prime power = 3 mod 4.

## Label: SOURCE-NEGATIVE (with a partial-overlap caveat)

No source found that proves or states the claim for any range, and no work citing Ito 1984 extends the transitive classification. Ito 1984 (zbMATH 0538.05021) is the strongest baseline. It reduces to prime power v in "large classes" only; the general case is not found settled in the literature searched. Coverage gaps below keep this from being a proof of absence.

## Query log (all 2026-11-21)

| # | Tool | Query | Result |
|---|---|---|---|
| 1 | Semantic Scholar API (curl) | citations of DOI 10.1016/S0195-6698(84)80016-5 | HTTP 200, 7 citing works |
| 2 | OpenAlex API | works citing W2095198999 | HTTP 200, 9 works (cited_by_count 9) |
| 3 | Crossref API | is-referenced-by-count | HTTP 200, 3 |
| 4 | Google Scholar "Cited by" (curl) | title query | FAILED: HTTP 302 to sgsync/consent (bot redirect); not "no hits" |
| 5 | Semantic Scholar | citations of Ito 1996 (10.1016/0012-365X(94)00088-Z) | HTTP 200, 0 results (index gap, not evidence) |
| 6 | zbMATH API | "Ito Hadamard tournaments" | 200, 16 |
| 7 | zbMATH API | "Hadamard tournament" | 200, 20 |
| 8 | zbMATH API | "doubly regular tournament transitive" | 200, 11 |
| 9 | zbMATH API | "Ito doubly regular asymmetric digraphs" | 200, 7 |
| 10 | zbMATH API | "Pasechnik skew-symmetric association schemes" | 200, 1 |
| 11 | zbMATH API | "Hadamard design transitive automorphism group" | 200, 20 |
| 12 | zbMATH API | "doubly regular tournament automorphism group" | HTTP 200 but result field null (parse failure); not "no hits" |
| 13 | zbMATH API | "skew Hadamard difference set nonabelian" | FAILED: HTTP 404 |
| 14 | zbMATH API | "Hadamard 2-design point-transitive" | FAILED: HTTP 404 |
| 15 | zbMATH API | doc fetch 896533, 3855130, 4142078, 784689, 4079452, 98722, 3954928 | 200; reviews read where licensed |
| 16 | WebSearch | "vertex-transitive" "doubly regular tournament" | 10 results, none classifying |
| 17 | WebSearch | "transitive" "Hadamard tournament" automorphism group prime power classification | 10 results; Berggren 1972, Goldberg 1970, Ito 1982, Ito 1980 |
| 18 | WebSearch | skew Hadamard matrix transitive automorphism group prime power Paley | 10 results; Kantor, O Cathain 2012, Garcia |
| 19 | WebSearch | "point-transitive" Hadamard design skew non prime power order | 10 results; Garcia 2606.13536 |
| 20 | WebSearch | Hadamard 2-designs transitive groups Kantor Dempwolff Braic Golemac Mandic Vucicic | 10 results; Kantor only; the Braic et al. paper not found by this query |
| 21 | WebSearch | twin prime power difference set Hadamard design / Singer | 10 results |
| 22 | arXiv API | all:"doubly regular tournament" | 200, 18 |
| 23 | arXiv API | all:"Hadamard tournament" | 200, 0 |
| 24 | arXiv API | all:"skew Hadamard" AND all:transitive | 200, 0 |
| 25 | arXiv API | id:2606.13536 (Garcia) | 200, abstract read |
| 26 | gh search repos | "doubly regular tournament" | 0 |
| 27 | gh search repos | "hadamard tournament" | 0 |
| 28 | gh search repos | "skew hadamard" | 6 incl. jeff-kline/skew-hadamard-2120 (positive control PASSED) |
| 29 | gh search code | "doubly regular tournament" | hits: Lean tournament defs, Leonardini/TournamentsBeyond5Voters, no classification |
| 30 | gh search code | "vertex-transitive tournament" | hits: eliottcassidy2000/math (transfer matrix), no classification |
| 31 | aixiv.online/search?q= (curl, 2 queries) | "doubly regular tournament", "Hadamard tournament" | INCONCLUSIVE: HTTP 200 but page is a client-rendered Next.js shell; no result list in HTML. Not searched effectively. |
| 32 | Wikipedia Difference_set (curl) | Singer / twin prime sections | confirmed, see below |

Not done: Google Scholar and aixiv (blocked or unrenderable); MathSciNet; Braic-Golemac-Mandic-Vucicic and Crnkovic papers not located by name; no full-text search of Garcia PDF for "Ito" (PDF is compressed; the abstract does not mention Ito).

## Item 1: citing works of Ito 1984

Union of Semantic Scholar (7), OpenAlex (9), Crossref (count 3). None extends the transitive classification on its title/abstract/review:
- Ito, Even tournaments and Hadamard tournaments, Discrete Math 1996 (zbMATH 0855.05037; review: "several results and questions"; no classification).
- Ito, Doubly regular asymmetric digraphs, Discrete Math 1988 (two indexed copies); zbMATH 4079452 review: basic properties of digraphs from symmetric designs; no.
- Pasechnik, Skew-symmetric association schemes with two classes ..., Acta Appl. Math 1992 (zbMATH 98722; review unavailable, licensing). Title concerns two-class schemes; not verified to extend Ito. Residual UNRESOLVED on its content.
- Muzychuk-Tinhofer, circulant graph recognition (1998, 2001): application of association schemes; unrelated.
- Adachi et al. 2003, 2005, 2006 on group divisible designs: unrelated.

## Item 2: zbMATH reviews

- Ito 1984 review (verbatim gist): THT = Hadamard 2-(4d+3,2d+1,d) design with transitive group G; Kelly 1954 and Johnsen 1966 treated cyclic transitive subgroup (v prime); Lam 1980 rank 3; Ito shows these hypotheses imply 4d+3 is a prime power and proves it "for large classes of THT". Note: the review phrases it through the design's group, so check whether Ito's group must preserve the orientation (tournament automorphisms); this affects how directly Ito's results transfer.
- Ito 1988: no extension. Ito 1996: no extension visible. Pasechnik 1992: review unavailable.
- Other Ito items seen: 1990 J. Algebra (0697.05040, orthogonal matrices over GF(2); no overlap), Ito-Leon-Longyear 1993 (order 23, 24 inequivalent Hadamard tournaments, by classification, not a transitive result), Ito-Okamoto 1994 (Szekeres type), Ito 1980 (doubly transitive Hadamard matrices), Kantor 1985 (2-transitive symmetric designs).

## Item 3: keyword searches

No paper found stating "transitive Hadamard tournament iff prime power" for any range. Related, non-overlapping or partial:
- Berggren 1972 / Goldberg 1970: tournaments transitive on points and arcs are quadratic residue (v = p^n, p = 3 mod 4, n odd). Stronger hypothesis, partial overlap only.
- Kantor 1969 and 1985, Ito 1980: 2-transitive / doubly transitive cases give Paley.
- O Cathain 2012 (JCTA): cocyclic Hadamard from difference sets with doubly transitive actions.
- Garcia arXiv 2606.13536 (Aust. J. Combin 95 (2026)): nilpotent group with a skew-Hadamard difference set is a p-group. Regular-subgroup case only, nilpotent only; no Ito citation seen in abstract.
- Arxiv hits 2404.11560 (Terwilliger algebras of DRTs), 2502.12090 (cyclotomic nearly DRTs), 1905.08568 (critical groups of DRTs): abstracts show no transitive classification.
- No order-specific exclusion results (e.g. for particular v < 10^4) were found.

## Item 5: point-transitive Hadamard designs of non-prime-power order

Confirmed from Wikipedia Difference_set (which lists Singer and twin prime power families) and the Stanton-Sprott statement surfaced in search: twin prime powers q, q+2 give a (q^2+2q, ...) difference set in the group F_q x F_{q+2}, a regular (hence point-transitive) symmetric design. Singer difference sets in PG(n,q) give point-transitive cyclic designs. Order 15 = (2^4-1)/(2-1), k = 7, lambda = 3 (PG(3,2) points/hyperplanes) is a Hadamard 2-(15,7,3) design with a cyclic regular group, and 15 is not a prime power. Further examples v = 35, 143, ... from twin primes (my calculation of arithmetic; the (15,7,3) identification is inferred, not quoted). So non-prime-power transitivity exists for designs; the prime-power restriction comes from the skew/orientation condition. This matches Ito 1984 and the Kelly-Johnsen observation.

## Conclusion

SOURCE-NEGATIVE: no located source proves the claim below 10^4 or in general. Closest overlaps: Ito 1984 (subcases: regular subgroup, supersolvable, v = p s^2, v != 9p), Berggren/Goldberg (arc-transitive), Kantor/Ito 1980 (2-transitive), Garcia 2026 (nilpotent regular). Residual risk: Pasechnik 1992 content, Braic et al. papers, and unindexed Japanese reports (Meijo/Konan, RIMS Kokyuroku 1992 "Groups and combinatorics") not checked.

## Addendum (root session, 2026-11-21): Pasechnik 1992 read in full (PDF supplied by the owner)
D. V. Pasechnik, "Skew-symmetric association schemes with two classes and strongly regular graphs of type L_{2n−1}(4n−1)", Acta Appl. Math. 29 (1992) 129–138, doi 10.1007/BF00053382.

Contents:
- Thm 1 / Cor 1: the symmetrized tensor product of the tournament schemes of two skew Hadamard matrices of order 4n is an amorphic cell. This gives SRGs of Latin-square type L_{2n−1}(4n−1); the first new one is (225, 98, 45).
- Thm 2: those SRGs fail the 4-vertex condition for n > 1, so they are not rank 3.
- Thm 3: every DRT scheme satisfies a 4-vertex condition, with explicit e_ij.

It cites Ito 1984 only for "further study of relations of W". **No result on transitive automorphism groups of DRTs; no overlap with the classification.** Residual novelty risk reduced to: Google Scholar coverage (blocked), aiXiv (unsearchable), and unindexed Japanese reports.
