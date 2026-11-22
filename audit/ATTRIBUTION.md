# Attribution and prior-work notes removed from the v9 owner boxes (22 Nov 2026)

Kept for the release repository. Corrections since v9: the metacirculant proposition is restored (prop:metacirculant, settles Mansilla); the five shortened proofs were audited VERIFIED (checks/AUDIT-v9-shortened.md); citations checked (checks/CITATIONS-v9.md, checks/MANSILLA-v9.md).

## Prior-work notes
```latex
\TODO{\textbf{Prior-work paragraph; the owner writes the final text.} Notes.
\emph{Kelly 1954, Johnsen 1966:} a Hadamard tournament with a cyclic transitive group of prime order is Paley (as quoted by Ito, p.~37; neither paper was read for this draft). Johnsen also treats abelian groups.
\emph{Lam 1980:} rank~3 automorphism group; Ito's footnote on p.~37 says Lam's tournaments are Paley by Feit--Thompson (communicated by J.~T.~Hall).
\emph{Ito 1984:} Theorems 1--4, quoted above. Our Lemma~\ref{lem:trace} is close to his Lemma~5.
\emph{Ito 1990:} binary orthogonal tournament matrices; no results on transitive groups.
\emph{Pasechnik 1992:} association schemes of Hadamard tournaments (amorphic cells, a 4-vertex condition); cites Ito 1984; no results on transitive groups.
\emph{Garcia 2026:} Conjecture~2.9, that a group with a skew Hadamard difference set is a $p$-group, is stated as open ``even for metacyclic groups''; it is Ito's Theorem~2, which Garcia does not cite.
\emph{Maru\v{s}i\v{c} 1985:} vertex-transitive digraphs of order $p^k$, $k\le3$, are Cayley; non-Cayley vertex-transitive graphs exist for $k\ge4$. The statement is taken from~\cite{MMM}; the 1985 paper was not obtained.
\emph{Feng 2011, Muzychuk 2010:} non-Paley skew Hadamard difference sets of order $p^3$ (Remark~\ref{rem:p3}).
\emph{Mansilla 2004} and \emph{Javier--Llano--Zuazua 2026:} see Section~\ref{sec:conj}.
Also to place: Berggren 1972 and Goldberg 1970 (arc-transitive), Kantor 1969 (2-transitive).
For the results added on 22 November (Sections~\ref{sec:abelian}, \ref{sec:linear} and~\ref{sec:finite}) the source notes say that historical priority was not assessed beyond a targeted source check.
Novelty log: \texttt{vt-dtr-exam-2026-11-21/novelty/NOVELTY.md}; not searched: MathSciNet, Google Scholar.}
```

## Role-of-AI notes
```latex
\section*{Role of AI}
\TODO{\textbf{The owner writes the final text.} Division of work, under the author's direction.
\emph{Found by a different AI system (Codex):} Proposition~\ref{prop:plane} (affine-plane obstruction); Proposition~\ref{prop:chiefbound} (chief-step bound) and Proposition~\ref{prop:prefix}; the earlier separate proofs of the cases $\nu_p(v)\in\{1,3\}$ of Theorem~\ref{thm:fourthfree}; Lemma~\ref{lem:fixedplane} (fixed plane); and Theorem~\ref{thm:pr4} ($pr^4$), including the descent.
\emph{Found by a different AI system, on 22 November, after the seventh draft:} the finiteness results (Theorems~\ref{thm:A} and~\ref{thm:fixedpart}); Lemma~\ref{thm:rep}; the linear bound (Theorem~\ref{thm:linear}); the abelian orbit bound (Theorem~\ref{thm:abelian}, Corollary~\ref{cor:abelianorder}, Lemma~\ref{lem:orderbound}); centre detection (Theorem~\ref{thm:center}); the strict bound (Theorem~\ref{thm:endpoint}); and the bound $\nu_p(v)\ge9$ (Theorems~\ref{thm:powers} and~\ref{thm:C}), which closed the order $54675$. Source notes and audits: \texttt{ito-general-finiteness-2026-11-22/} and \texttt{ito-strict-endpoint-2026-11-22/}.
\emph{Found by this project's agents:} the formulation of the trace lemma (Lemma~\ref{lem:trace}) and the quotient law; the exclusion of order $pr^2$ (``N2''), now a case of Theorem~\ref{thm:fourthfree}; the rank bound, now Corollary~\ref{lem:rankbound}; Theorem~\ref{thm:gate} (gate) and Proposition~\ref{thm:fittingclass}. Codex had suggested the direction of the rank bound (the Fitting subgroup). The shorter form of the descent in Theorem~\ref{thm:pr4} was proposed by the AI agent that audited the Codex proof.
\emph{Review:} Corollary~\ref{cor:cayley} and the order-27 check come from the sketch review of 22 November. The direct argument in the proof of Corollary~\ref{cor:cubefree} comes from the cold reading of the seventh draft.
\emph{This draft (v9)} was cut by an AI editing agent from the 43-page eighth draft (\texttt{main-v8-full43pp.tex}). An AI drafting agent wrote the eighth draft from the audited notes; in Sections~\ref{sec:abelian}, \ref{sec:linear} and~\ref{sec:finite} it expanded the notes into full proofs, and these expanded proofs have not themselves been audited. Removed in v9: parts (3) and (4) of Theorem~\ref{thm:C}, the divisor-gap theorem, the two-prime theorem, the Singer families, the family $p\,3^{2k}$, the remark on the limit of descent, and the proposition on metacirculants. Five arguments were shortened in v9 and have not been audited in their new form: Corollary~\ref{lem:prime-orbit}, Proposition~\ref{prop:r-structure} and the first case of Lemma~\ref{lem:rank} now use the rank bound in place of the plane lemma of the eighth draft; the first case of Theorem~\ref{thm:pr4} now uses Proposition~\ref{thm:fittingclass}; and the submodularity step in the proof of Theorem~\ref{thm:endpoint} is written out. The census of Section~\ref{sec:census} is a single script; its rule set was reduced from ten rows to seven for this draft, and it was run once.
\emph{Independent examinations:} \texttt{vt-dtr-exam-2026-11-21/}, \texttt{ito-squarefree-2026-11-21/}, \texttt{ito-p3-squarefree-2026-11-21/}, \texttt{ito-prime-exponents-2026-11-21/}, \texttt{ito-divisor-bridge-2026-11-22/} (two audits), \texttt{ito-lift-19375-2026-11-22/} (four audits), \texttt{fitting-lane-2026-11-22/admission.md} (one cold reading; verdict ``admit, bounded''); a cold reading of the whole seventh draft (\texttt{checks/COLDREAD-v7.md}, verdict ``verified'' for the internal arguments); and one proof audit for each of the notes of 22 November named above (seven audits and three addenda, all with verdict ``verified''). The examinations were made by AI agents, some of the same model family as some of the proofs. No proof has been checked by a human or formalised.}

```
