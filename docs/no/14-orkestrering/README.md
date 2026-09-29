# 14 – Orkestrering av Amiga-programmer

Nå kombinerer vi ideene.

Et workflow kan:

1. kontrollere systemet med AmigaDOS
2. sende kommando til program A
3. hente resultat
4. tolke resultatet
5. bruke det til å bestemme neste handling
6. sende kommando til program B
7. logge utfallet

## Hold integrasjonene adskilt

Lag små adapterrutiner for hvert program. Ikke spre programspecifikke kommandoer over hele scriptet.

```rexx
appstatus: procedure
  parse arg port
  options results
  address value port
  'STATUS'
  if RC ~= 0 then return ''
  return RESULT
```

## Hvorfor dette er power-user-stoff

Workbench-programmer kan bli komponenter i en større arbeidsflyt. Brukeren trenger ikke manuelt gjenta den samme sekvensen av klikk og kommandoer.

Neste: [M3-prosjekt](../15-m3-prosjekt/README.md).
