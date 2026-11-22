# Admission record

**Current state:** ADMITTED

Current verdict: ADMITTED (2026-11-22)

**Version:** 0.1.0

**Tag:** `v0.1.0` → `7e49c29e2f3235a57b74c6fc569243753504ca44`

**Version DOI:** [`10.5281/zenodo.24448853`](https://doi.org/10.5281/zenodo.24448853) · **Concept DOI:** `10.5281/zenodo.24448852` · **Record:** <https://zenodo.org/records/24448853>

**Standard:** [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html)

Admission is a project release decision. It is not peer review, a correctness
certificate, or proof of global novelty.

**Scope set by the author.** The mathematics was frozen by the author on
2026-11-22. The author approved the abstract and README introduction and the
title on 2026-11-22.

## Principal claims

1. For every $B$, only finitely many non-prime-power orders with largest
   fourth-power divisor at most $B$ carry a vertex-transitive Hadamard
   tournament (Theorem A).
2. For fourth-power-free $v>1$, a vertex-transitive Hadamard tournament of
   order $v$ exists if and only if $v=p$ or $v=p^3$ with $p\equiv3\pmod4$
   (Theorem B); it is then Cayley (Corollary 1), and Paley when $v$ is
   cube-free (Corollary 2).
3. For $v=p^{2a+1}s^2$ with $s>1$ squarefree and prime to $p$: $a\ge4$, with
   $p=3$ when $a=4$, and $p\le4a-5$ (Theorem C).
4. For $3\le v<10^5$, existence holds exactly at the prime powers congruent to
   3 modulo 4 (Theorem D).
5. The non-Cayley vertex-transitive tournaments of Mansilla (2004) are not
   doubly regular (Proposition 44).

## Gates

| Gate | Status | Evidence or residual |
|---|---|---|
| P1 prior work and credit | PASS, residual accepted | [audit/PRIOR-ART.md](audit/PRIOR-ART.md) and the search logs of 21 and 22 Nov 2026, within 7 days of the tag. Residual: Google Scholar and MathSciNet were not searched; the original theorem pages of Kelly (1954) and Johnsen (1966) were not openly accessible, and the paper proves the needed conclusion directly. The author accepted these residuals on 2026-11-22, before the tag |
| A1 claim and artifact consistency | PASS | claims-consistency audit and full cold read of 22 Nov 2026, with an independent census; earlier cold read, proof audits and primary-source citation check; dispositions in [audit/LEDGER.md](audit/LEDGER.md) |
| R1 release and stewardship | PASS | See below |

## R1 — release and stewardship

| Check | Status | Evidence or residual |
|---|---|---|
| Reproduction | PASS | fresh `git archive` extraction of `v0.1.0`: `make verify` MATCH; deterministic `make paper`, byte-identical to the committed PDF |
| Artifact integrity | PASS | `MANIFEST.sha256` covers every tracked file |
| Hygiene | PASS | README math rendered by GitHub, every span recognized; no private paths or emails |
| Stewardship | PASS | [CORRECTIONS.md](CORRECTIONS.md) |
| Immutable semantic tag | PASS | annotated `v0.1.0` (object `9c18dde`) → `7e49c29`; tagger is the GitHub noreply identity |
| Public permanent archive with provider byte identity | PASS | the pinned GitHub `zipball/v0.1.0` (downloaded twice, identical) and the Zenodo file are byte-identical: 584694 bytes, SHA-256 `90cc108ea4d58243d8022755d56f1436a11b7095a1691d004f9dcc443d9c98e2`; Zenodo MD5 `171d927428613848f3279ed43e99795d` |
| DOI resolves; living repository identifies the version | PASS | `doi.org/10.5281/zenodo.24448853` redirects to the Zenodo record; README, `CITATION.cff` and the living paper carry the version DOI |
| Archive metadata matches repository | PASS | title, creator Kline, Jeffery, version v0.1.0, publication date 2026-11-22, license `gpl-3.0` |
| Machine-readable citation | PASS | `CITATION.cff` with version DOI, concept DOI and `date-released: 2026-11-22` |

**Admission verdict:** ADMITTED (2026-11-22). The P1 residuals and the limits
stated in the README remain. No independent human expert has reviewed the
paper.

## Archive verification

- Route: Zenodo GitHub integration; no manual deposit.
- Pinned before the GitHub Release: GitHub API `zipball/v0.1.0`, downloaded
  twice, identical, 584694 bytes, SHA-256
  `90cc108ea4d58243d8022755d56f1436a11b7095a1691d004f9dcc443d9c98e2`.
- Zenodo file `jeff-kline/vertex-transitive-hadamard-tournaments-v0.1.0.zip`:
  identical to the pinned zipball.
- Separate determinism check: `git archive --format=zip v0.1.0`, generated
  twice, identical, SHA-256
  `15bf147c12021acc947d2ef49f28a99ea8118be1f54457afcfae1ba9bb0acf2d`; a
  different file from the provider zipball, not compared with it.
- Mechanical audit at the archived state, on the unchanged tagged tree:
  11 pass, 0 warnings, 0 fail.

## External actions and owners

| Action | Owner | Status |
|---|---|---|
| Private GitHub repository and push | author authorization | done 2026-11-22 |
| Public visibility, secret scanning and push protection | author authorization | done 2026-11-22 |
| Zenodo enablement before the Release | author, in the Zenodo portal | done 2026-11-22 |
| Annotated tag `v0.1.0`, GitHub Release | author authorization | done 2026-11-22 20:38 UTC: Release "Version 0.1.0" |
| Public-site listing | author authorization | landing entry at <https://jeff-kline.github.io/> (site commit `1044a26`); Pages build and live HTML checked for title, blurb, repository link and version DOI before this record was pushed |
