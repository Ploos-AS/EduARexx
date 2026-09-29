# amiga-runtime integration

EduARexx consumes the existing `amiga-runtime` schema-1 qualification contract.

The generated payload contains:

```text
amiga-runtime-payload/
  amiga-runtime.json
  EduARexx.guide
  eduarexx-metadata.json
  results/
```

Prepare it with:

```sh
make amiga-runtime-payload
```

From an `amiga-runtime` environment, the contract entry point is:

```sh
bin/qualify-contract /path/to/amiga-runtime-payload --profile a500plus-os2
bin/qualify-contract /path/to/amiga-runtime-payload --profile a1200-020-os3
```

The contract deliberately targets m68k classic profiles. AROS i386 is not a substitute for this qualification.

## Important limitation

The current generic runtime contract expects an executable-style payload path. AmigaGuide is a document opened by a guest application, so the runtime side still needs a document/application qualification adapter before these commands can legitimately produce a PASS for EduARexx.

Until that adapter exists and runs, EduARexx remains `NOT_RUN`.
