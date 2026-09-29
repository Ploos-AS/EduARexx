PYTHON ?= python3
VERSION ?= 0.1.0

.PHONY: amigaguide validate-amigaguide test

amigaguide:
	$(PYTHON) tools/build_amigaguide.py --version $(VERSION)

validate-amigaguide: amigaguide
	$(PYTHON) tools/validate_amigaguide.py build/EduARexx.guide

test:
	$(PYTHON) -m unittest discover -s tests

.PHONY: amiga-runtime-payload

amiga-runtime-payload: validate-amigaguide
	$(PYTHON) tools/package_amiga_runtime.py
