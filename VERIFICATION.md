# Verification record

## Environment of the pinned run (2026-11-22)

- macOS, x86_64, one core.
- Python 3, standard library only, in an isolated virtual environment.
- pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2021).

The program needs no network. Its SHA-256 hash is in
[MANIFEST.sha256](MANIFEST.sha256).

## Commands

```sh
make verify PY=/path/to/python
make paper
```

`make verify` runs [code/census.py](code/census.py), writes
`build/census.txt` and compares it byte for byte with
[evidence/census.txt](evidence/census.txt). It takes under a second.

## What the census covers

For each of the 25000 orders $v\equiv3\pmod4$ with $3\le v<10^5$, the script
factors $v$ and assigns it to the first rule whose hypotheses $v$ meets:

| Row | Rule | Orders |
|---|---|---|
| 1 | prime power (existence by the Paley tournament) | 4819 |
| 2 | Ito's Theorem 1 ($v$ not of the form $pt^2$) | 18388 |
| 3 | Theorem B (fourth-power-free) | 1622 |
| 4 | Theorem C (squarefree cofactor) | 7 |
| 5 | prefix bound (Appendix) | 29 |
| 6 | gate (Appendix) | 134 |
| 7 | orders $pr^4$ (Appendix) | 1 |

No order is left open. The census checks hypotheses in exact integer
arithmetic; it does not search for tournaments, and the exclusions rest on
the proofs in the paper. The rule set was re-implemented independently for
the seventh draft (see [audit/LEDGER.md](audit/LEDGER.md)); the ninth-draft
rules shown here were rerun, not re-implemented.

## Paper

`make paper` builds [paper/main.pdf](paper/main.pdf) in three passes with
`SOURCE_DATE_EPOCH` fixed. Two builds give identical bytes.

PDF SHA-256: `3de182fe72225d701c9f734cdfeeb50f03f2e5e8bdc953e42610c23c056e0625`
