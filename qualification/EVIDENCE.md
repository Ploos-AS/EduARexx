# Native evidence

Native qualification evidence is produced by `amiga-runtime`, not by ordinary EduARexx CI.

A valid import requires both:

- `result.json` from the runtime backend, proving the emulator process result and classic AmigaOS profile.
- `verification.json`, proving the contract's required guest markers.

The importer also hashes the locally built `EduARexx.guide`. This keeps the reported status tied to a concrete artifact.

```sh
make import-native-evidence \
  RUNTIME_RESULT=/path/to/evidence/result.json \
  VERIFICATION=/path/to/evidence/verification.json
```

Ordinary CI does not have Kickstart or AmigaOS assets and therefore does not run this target. Absence of native evidence means `NOT_RUN`, not PASS and not FAIL.
