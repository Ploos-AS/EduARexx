# 18 – Logging og observerbarhet

Et automatiseringsscript som kjører uten at brukeren ser hvert steg, må kunne forklare hva det gjorde.

## Enkel logger

```rexx
log: procedure
  parse arg level, message
  say '['level']' message
  return
```

Bruk nivåer konsekvent, for eksempel `INFO`, `WARN` og `ERROR`.

## Hva bør logges?

Logg beslutninger og grenseflater:

- hvilken operasjon som startet
- hvilket mål som ble valgt
- kall til eksterne miljøer
- RC ved feil
- viktige resultater
- cleanup
- sluttstatus

Ikke fyll loggen med støy som gjør faktiske feil vanskeligere å finne.

## Lab

Legg logging til AmiOperator eller PortCommander uten å endre programmets eksterne oppførsel.

Neste: [programarkitektur](../19-arkitektur/README.md).
