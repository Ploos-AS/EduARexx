# 05 – PARSE: ARexx-verktøyet du må mestre

`PARSE` er sentralt i praktisk ARexx. Det brukes til å hente argumenter og dele opp tekst og resultater.

## Argumenter

```rexx
/* helloarg.rexx */
parse arg name
if name = '' then name = 'Amiga-bruker'
say 'Hei,' name
```

## Del opp tekst

```rexx
line = 'A1200 68020 8MB'
parse var line model cpu memory
say 'Modell:' model
say 'CPU:' cpu
say 'RAM:' memory
```

## Praktisk tankemodell

Ikke tenk på `PARSE` som bare streng-splitting. Senere skal vi bruke det til å tolke kommandolinjer, statusdata og svar fra andre Amiga-programmer.

## Lab

Skriv `machine.rexx` som tar tre argumenter: modell, CPU og RAM. Scriptet skal validere at alle finnes og deretter skrive en statusrapport.

Neste: [M1-prosjektet](../06-m1-prosjekt/README.md).
