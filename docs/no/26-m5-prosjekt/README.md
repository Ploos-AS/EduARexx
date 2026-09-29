# 26 – M5-prosjekt: EDUHOST

M5 binder sammen power-user- og utviklersiden av ARexx.

## Leveranser

- dokumentert `EDUHOST`-kommando-API
- native C-host
- ARexx-testklient
- negative tester
- cleanup-test
- buildinstruksjoner
- runtime-kvalifikasjon på m68k AmigaOS

## Testmatrise

```text
PING            -> success + PONG
VERSION         -> success + version
ECHO hello      -> success + hello
ADD 2 3         -> success + 5
UNKNOWN         -> documented error
malformed input -> documented error
shutdown/exit   -> clean resource teardown
```

## Bestått M5

Studenten skal kunne forklare hele reisen fra `ADDRESS EDUHOST` i et script til en Exec message port i et C-program og tilbake til `RC`/`RESULT`.

Dette er overgangen fra ARexx power user til ARexx-integrasjonsutvikler.
