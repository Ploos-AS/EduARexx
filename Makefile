PYTHON ?= python3

.PHONY: amigaguide validate-amigaguide test

amigaguide:
	$(PYTHON) tools/build_amigaguide.py

validate-amigaguide: amigaguide
	$(PYTHON) tools/validate_amigaguide.py build/EduARexx.guide

test:
	$(PYTHON) -m unittest discover -s tests
