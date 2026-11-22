# Novelty search for v9 (22 Nov 2026)

Claim checked: Theorems A–D and Corollaries 1–2 of "Ito counterexamples need large fourth powers" (no prior proof that fourth-power-free vertex-transitive Hadamard tournament orders are p or p^3, no finiteness result, no classification below 10^5). Builds on vt-dtr-exam-2026-11-21/novelty/NOVELTY.md (21 Nov), which covered Semantic Scholar, OpenAlex, Crossref and zbMATH reviews of every work citing Ito 1984.

| # | Source | Query | Result |
|---|---|---|---|
| 1 | OpenAlex | works citing Ito 1984 (W2095198999) | 9: Ito 1988 (x2), Pasechnik 1992, Ito 1996, Muzychuk et al. 1998/2001 (circulant recognition), three Japanese GDD reports 2003–06. None treats orders of transitive groups. |
| 2 | Semantic Scholar | citations of DOI 10.1016/S0195-6698(84)80016-5 | 7, subset of #1 |
| 3 | zbMATH API | `ci:3855130` | 404 (query form unsupported); citing set covered by the 21 Nov zbMATH review reads |
| 4 | arXiv API | abs "doubly regular tournament" (16), abs "skew Hadamard difference set" (15), abs "vertex-transitive tournament" (5), all "Hadamard tournament" (0) | Read abstracts of the relevant ones: 2606.13536 (Garcia, nilpotent ⇒ p-group; cited), 2301.09993 (VT tournaments of prime order, counting), 2404.11560 (Terwilliger algebras), 2607.05152 (metric dimension). None addresses the order of a VT Hadamard tournament. |
| 5 | Web search (extended + standard), 5 queries | VT doubly regular tournament prime power Ito; title of Ito 1984; point-transitive skew Hadamard design non-prime-power; SHDS non-abelian non-prime-power 2026; VT Cayley classification | Only Garcia, JLZ, Muzychuk, Feng, MMM, Kantor (Paley designs, flag-transitive) — all already cited or outside scope. |
| 6 | GitHub `gh search repos/code` (positive control: jeff-kline/symmetric-hadamard-8740 found) | "doubly regular tournament", "skew hadamard difference set", Ito "Hadamard tournament", "vertex-transitive" "doubly regular"; repo eliottcassidy2000/math for "Ito", "vertex-transitive" "Hadamard" | AI-agent repo eliottcassidy2000/math works on tournaments (path counts, circulant congruences, n | H for VT tournaments) — nothing on Ito's question; Leonardini/TournamentsBeyond5Voters (voting inducibility) — unrelated. |
| 7 | aiXiv search pages | "tournament", "Hadamard" | No paper on Hadamard tournaments or their automorphism groups; Hadamard difference set papers (Schmidt 4p², Niedbala Giraudin, OpenAI circulant) are about Menon parameters. |
| 8 | Google Scholar (curl) | title query | NOT PERFORMED: HTTP 302 bot redirect (same as 21 Nov). Not "no hits". |
| 9 | MathSciNet | — | NOT PERFORMED: subscription required. |

Verdict: SOURCE-NEGATIVE over sources 1–7 (no work found that proves any of Theorems A–D or Corollaries 1–2). Not a proof of novelty; Google Scholar and MathSciNet remain unsearched. The paper's wording "To our knowledge ... new" matches this scope.
