PYTHON ?= python3
VERSION ?= 0.1.0

.PHONY: amigaguide validate-amigaguide test amiga-runtime-payload native-runtime-payload import-native-evidence native-launcher

amigaguide:
	$(PYTHON) tools/build_amigaguide.py --version $(VERSION)

validate-amigaguide: amigaguide
	$(PYTHON) tools/validate_amigaguide.py build/EduARexx.guide

test:
	$(PYTHON) -m unittest discover -s tests

amiga-runtime-payload: validate-amigaguide
	$(PYTHON) tools/package_amiga_runtime.py

native-launcher:
	$(MAKE) -C qualification

native-runtime-payload: validate-amigaguide
	@test -s build/amigaguide-launcher || (echo "native launcher missing; run a qualified amiga-dev build first" >&2; exit 69)
	$(PYTHON) tools/package_amiga_runtime.py --launcher build/amigaguide-launcher

import-native-evidence: validate-amigaguide
	@test -n "$(RUNTIME_RESULT)" || (echo "RUNTIME_RESULT is required" >&2; exit 64)
	@test -n "$(VERIFICATION)" || (echo "VERIFICATION is required" >&2; exit 64)
	$(PYTHON) tools/import_native_evidence.py --runtime-result "$(RUNTIME_RESULT)" --verification "$(VERIFICATION)"
