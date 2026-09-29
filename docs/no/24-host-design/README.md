# 24 – Design en ARexx-host

Før vi skriver C, designer vi kommandogrensesnittet.

## Eksempel: EDUHOST

```text
PING
VERSION
ECHO <text>
ADD <a> <b>
HELP
```

Et godt ARexx-interface bør være:

- stabilt
- dokumentert
- enkelt å parse
- tydelig om returstatus
- tydelig om resultatformat
- bakoverkompatibelt når mulig

## Dispatch

```text
RexxMsg
  |
parse command
  |
  +-- PING
  +-- VERSION
  +-- ECHO
  +-- ADD
  +-- HELP
  |
set RC/result
  |
ReplyMsg
```

## Power-user møter utvikler

Studenten har tidligere stått på venstre side av API-et. Nå designer studenten høyre side. Dette er nøkkelen til å lage Amiga-programmer som kan inngå i automatiserte workflows.

Neste: [C-host](../25-c-host/README.md).
