SHELL := /bin/sh
PY ?= python3

PDFLATEX ?= pdflatex
export SOURCE_DATE_EPOCH := 1795305600
export FORCE_SOURCE_DATE := 1

.PHONY: paper verify

# Three passes from a clean extraction; no inherited auxiliaries are required.
paper:
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	@! grep -E 'Warning:|Overfull|undefined references|undefined citations' paper/main.log
	@echo "paper built: paper/main.pdf"

# Assign every order v = 3 (mod 4), 3 <= v < 10^5, to an excluding rule
# (under a second on one core; Python 3, standard library only), then compare
# the output with the pinned copy in evidence/.
verify:
	@mkdir -p build
	@$(PY) code/census.py > build/census.txt
	@if cmp -s evidence/census.txt build/census.txt; then echo "MATCH census.txt"; \
	  else echo "MISMATCH census.txt"; exit 1; fi
	@echo "verify: census matches evidence/"
