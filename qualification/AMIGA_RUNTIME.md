# amiga-runtime integration

EduARexx consumes the existing `amiga-runtime` schema-1 document qualification contract.

## Native payload

The native payload contains the exact generated guide plus the m68k launcher and
ARexx probe used by the guest:

```text
amiga-runtime-payload/
  amiga-runtime.json
  EduARexx.guide
  amigaguide-launcher
  amigaguide-nav.rexx
  amigaguide-test
  eduarexx-metadata.json
  results/
```

The guide SHA-256 is embedded in the packaged contract. Runtime evidence must
carry the same artifact identity before EduARexx accepts a PASS.

Build the complete payload with:

```sh
make native-launcher
make native-runtime-payload
```

Normal GitHub-hosted CI builds the launcher with the pinned `amiga-dev` image,
inspects the m68k binary and publishes the artifact:

`EduARexx-native-runtime-payload-m68k`

That artifact is build evidence, not native runtime evidence.

## Classic runtime boundary

Native qualification is delegated to the `Ploos-AS/amiga-runtime` workflow
`Classic AmigaOS qualification`. It deliberately runs only on a self-hosted
runner carrying both labels:

- `self-hosted`
- `amiga-classic`

The runner administrator supplies legal Kickstart and AmigaOS files through
private host paths. ROMs and AmigaOS files must never be copied into this
repository or a GitHub Actions artifact.

Stage or download the EduARexx native payload on that runner, then qualify both
required profiles:

```sh
qualify-contract /work/payload --profile a500plus-os2
qualify-contract /work/payload --profile a1200-020-os3
```

The classic workflow may also receive an approved GitHub Actions artifact URL,
so the published EduARexx payload can be consumed without manually rebuilding
it on the private runner.

## Required native evidence

A PASS requires the exact line-oriented protocol declared by
`qualification/amiga-runtime.json`, including:

- document, launcher and ARexx probe presence;
- native AmigaGuide open;
- ARexx `LINK Main`;
- baseline ARexx navigation;
- ARexx `QUIT`;
- successful probe completion;
- qualification end marker.

The classic backend additionally requires a clean emulator exit. Partial logs,
a timeout, a crash, a different guide hash or missing helper files fail closed.

The baseline deliberately targets classic m68k AmigaOS. AROS i386 is not a
substitute.

## Current status

The launcher build, m68k inspection, payload construction and runtime contract
tests pass in CI. Native FS-UAE/AmigaOS execution remains `NOT_RUN` until the
payload is executed on the private `amiga-classic` runner with legal runtime
assets.
