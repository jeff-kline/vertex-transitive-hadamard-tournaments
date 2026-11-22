# Vertex-transitive Hadamard tournaments: Ito counterexamples need large fourth powers

Jeffery Kline

[![Version DOI: 10.5281/zenodo.24448853](https://zenodo.org/badge/DOI/10.5281/zenodo.24448853.svg)](https://doi.org/10.5281/zenodo.24448853)

**Status: version 0.1.0 admitted 2026-11-22.** The immutable release is
[`v0.1.0`](https://github.com/jeff-kline/vertex-transitive-hadamard-tournaments/releases/tag/v0.1.0), archived at version DOI
[`10.5281/zenodo.24448853`](https://doi.org/10.5281/zenodo.24448853). The concept DOI
[`10.5281/zenodo.24448852`](https://doi.org/10.5281/zenodo.24448852) resolves to the latest version; cite the
version DOI for reproducibility. Admission under the project's
[public research standard](https://jeff-kline.github.io/posts/research-program/index.html)
is a release decision, not peer review or a correctness certificate; see
[ADMISSION.md](ADMISSION.md). The tagged snapshot retains its prepublication
“release candidate” and “Draft” wording because the DOI did not exist when it
was made.

The paper is [paper/main.pdf](paper/main.pdf); its source is
[paper/main.tex](paper/main.tex).

## Introduction

A tournament is doubly regular, or a Hadamard tournament, if every vertex
beats the same number of vertices and every two vertices beat the same number
of common vertices. One on $v$ vertices exists if and only if a skew Hadamard
matrix of order $v+1$ exists. In 1984 Ito proved that if the automorphism
group of a Hadamard tournament is transitive on the vertices, then the order
is $v=pt^2$ for a prime $p\equiv3\pmod 4$, and he raised the possibility that
$v$ is always a power of $p$. We call a vertex-transitive Hadamard tournament
whose order is not a prime power an Ito counterexample. The Paley tournaments
give vertex-transitive examples at every prime power congruent to 3 modulo 4;
no Ito counterexample is known.

The paper proves that any infinite family of Ito counterexamples needs large
fourth powers: for every bound $B$, only finitely many orders of Ito
counterexamples have largest fourth-power divisor at most $B$. When no fourth
power of a prime divides $v>1$, a vertex-transitive Hadamard tournament of
order $v$ exists only for $v=p$ or $v=p^3$; it is then a Cayley tournament of
a $p$-group, and for cube-free $v$ it is the Paley tournament. If
$v=p^{2a+1}s^2$ with $s>1$ squarefree and prime to $p$, then $a\ge4$ and
$p\le4a-5$. Finally, for $3\le v<10^5$ a vertex-transitive Hadamard
tournament of order $v$ exists if and only if $v$ is a prime power congruent
to 3 modulo 4.

Ito's question itself remains open. The exclusions are necessary conditions
on an object that may not exist: if Ito's question has a positive answer,
the results about orders with a second prime factor are vacuous.

## What is new

Ito (1984) proved that the order is $pt^2$, that it is a prime power when the
automorphism group contains a regular or a supersolvable transitive subgroup,
and that it is not $9p$ for primes $p>3$. Kelly (1954) and Johnsen (1966)
showed that a Hadamard tournament of prime order with a cyclic transitive
group is Paley. Marušič (1985) proved that vertex-transitive digraphs of
order $p$, $p^2$ or $p^3$ are Cayley digraphs. New here:

1. **Principal result: finiteness** (Theorem A). For every $B$, only finitely
   many non-prime-power orders with largest fourth-power divisor at most $B$
   carry a vertex-transitive Hadamard tournament.
2. **Fourth-power-free orders** (Theorem B). If no fourth power of a prime
   divides $v>1$, a vertex-transitive Hadamard tournament of order $v$ exists
   if and only if $v=p$ or $v=p^3$ with $p\equiv3\pmod4$. With Marušič's
   theorem it is then a Cayley tournament of a $p$-group (Corollary 1); with
   the theorem of Kelly and Johnsen, for which the paper includes a short
   proof, it is Paley when $v$ is cube-free (Corollary 2).
3. **Squarefree cofactor** (Theorem C). If $v=p^{2a+1}s^2$ with $s>1$
   squarefree and prime to $p$, then $a\ge4$, with $p=3$ when $a=4$, and
   $p\le4a-5$. This contains Ito's exclusion of $9p$.
4. **Orders below $10^5$** (Theorem D). Existence holds exactly at the prime
   powers congruent to 3 modulo 4. A short script assigns each of the other
   20181 orders to a theorem that excludes it.
5. **Tools of independent use**: an affine-plane obstruction (Proposition 19),
   a bound for abelian groups of automorphisms in terms of their orbits
   (Theorem 12), and a linear bound (Theorems 35 and 37): if $v$ is not a
   power of $p$ and the Fitting subgroup of a transitive group $G$ is a
   $p$-group, then $p<2k-1$, where $p^k$ is the size of an orbit of the
   largest normal $p$-subgroup of $G$. Its proof uses the theorem of Hall and
   Higman.
6. **Mansilla's non-Cayley tournaments are not doubly regular**
   (Proposition 44 and the discussion after it). So no non-Cayley
   vertex-transitive Hadamard tournament is known; whether one exists is left
   as a question.

Not new: Ito's four theorems; the trace lemma (Lemma 10), which is close to
Ito's Lemma 5; the conclusion of Kelly and Johnsen; Marušič's theorem; and the
group-theoretic results of Hall–Higman, Aschbacher–Smith and Dixon, which are
quoted.

These statements rest on a bounded comparison recorded in
[audit/PRIOR-ART.md](audit/PRIOR-ART.md). We found no earlier proof of
Theorems A–D or Corollaries 1–2 in the sources examined. Google Scholar and
MathSciNet were not searched. This is not a claim of global priority.

## Earlier work

- **Kelly (1954)** and **Johnsen (1966)**: prime order with a cyclic
  transitive group gives the Paley tournament.
- **Reid and Brown (1972)**: Hadamard tournaments of order $v$ correspond to
  skew Hadamard matrices of order $v+1$.
- **Ito (1984)**, *Hadamard tournaments with transitive automorphism groups*:
  Theorems 1–4 and the question this paper addresses.
- **Marušič (1985)**: vertex-transitive digraphs of order $p^k$, $k\le3$, are
  Cayley.
- **Mansilla (2004)**: non-Cayley vertex-transitive tournaments of every odd
  prime-power order $p^k$, $k\ge4$, and products of them with Paley tournaments.
- **Feng (2011)** and **Muzychuk (2010)**: non-Paley skew Hadamard difference
  sets of order $p^3$.
- **Araujo Garcia (2026)**: a nilpotent group with a skew Hadamard difference
  set is a $p$-group; Conjecture 2.9 there is equivalent to Ito's Theorem 2.
- **Javier, Llano and Zuazua (2026)**: the statement, citing Mansilla, that
  non-Cayley vertex-transitive Hadamard tournaments exist; Proposition 44
  shows that Mansilla's constructions are not doubly regular.

## Evidence and limits

| Claim | Status |
|---|---|
| Theorems A–C, Corollaries 1–2 | proved on paper; conditional on the quoted theorems of Feit–Thompson, Hall–Higman, Aschbacher–Smith, Dixon and Marušič; audited by process-separated AI reviews, not human peer review |
| Theorem D | proved on paper from Ito's Theorem 1, Theorems B and C, and three exclusions in the Appendix, with existence at prime powers from the Paley tournaments; the assignment of orders to theorems is an exact computation by [code/census.py](code/census.py), re-implemented independently from the theorem statements with the same result |
| Proposition 44 (Mansilla) | proved on paper; matched against the full text of Mansilla's article |
| Order 27 (Remark 45) | computation on McKay's catalogue files, described in [audit/reviews/CITATIONS-v9.md](audit/reviews/CITATIONS-v9.md); not part of this repository's code |
| Priority | bounded search; see [audit/PRIOR-ART.md](audit/PRIOR-ART.md) |

The census checks which theorem's hypotheses each order meets; it does not
search for tournaments. No proof has been checked by a human or formalised.
The review history is in [audit/LEDGER.md](audit/LEDGER.md).

## Reproduce

The census needs Python 3 and no external packages; the paper needs pdfLaTeX.

```sh
make verify PY=/path/to/python   # under a second
make paper
```

`make verify` runs the census and compares its output with the pinned copy in
`evidence/`.

## Role of AI

AI assisted the derivations, the computer verification, the literature search
and the exposition under the author's direction. Process-separated AI reviews
checked the proofs and certificates; they are not independent expert peer
review, and no independent human expert has examined the proofs. The sources,
the reviews and their dispositions are in [audit/](audit/), and
[audit/ATTRIBUTION.md](audit/ATTRIBUTION.md) records which system found which
result.

## License

GPL-3.0-only. See [LICENSE](LICENSE).
