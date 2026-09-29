# Native qualification

Static CI validation is not native runtime qualification.

EduARexx uses `qualification/amigaguide.json` as the contract for testing the generated guide in `amiga-runtime`.

## Required flow

1. Build `build/EduARexx.guide`.
2. Static validator must pass.
3. Copy the artifact to a writable test volume available to the Amiga guest.
4. Boot the selected m68k AmigaOS profile.
5. Open the guide with the native AmigaGuide environment.
6. Execute every check from the manifest.
7. Record emulator, emulator version, AmigaOS profile, artifact hash and result.

## Status language

- `NOT_RUN` – no native test has been executed.
- `PASS` – all required checks passed on the named runtime.
- `FAIL` – at least one required check failed.
- `BLOCKED` – test could not run; reason must be recorded.

A Linux build or parser test can never change native status to PASS.

## Proprietary files

Kickstart ROMs and AmigaOS files are runtime inputs only. They must not be committed to EduARexx.
