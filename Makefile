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

.PHONY: import-native-evidence
import-native-evidence: validate-amigaguide
	@test -n "$(RUNTIME_RESULT)" || (echo "RUNTIME_RESULT is required" >&2; exit 64)
	@test -n "$(VERIFICATION)" || (echo "VERIFICATION is required" >&2; exit 64)
	$(PYTHON) tools/import_native_evidence.py --runtime-result "$(RUNTIME_RESULT)" --verification "$(VERIFICATION)"
