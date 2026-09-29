# 25 – Første ARexx-host i C

Målet er en minimal native host med portnavnet `EDUHOST`.

## Før vi kompilerer

Den konkrete implementasjonen av message port, RexxSysLib, RexxMsg-felter og resultatstrenger avhenger av Amiga-headerne og SDK-et vi bygger mot. Derfor behandles kildekoden i M5 først som et **kvalifiserbart skjelett**.

Krav til ferdig host:

1. åpne nødvendige systemressurser
2. opprette og publisere `EDUHOST`
3. vente på meldinger uten busy-loop
4. validere at mottatt melding kan behandles
5. dispatch kommando
6. sette korrekt returstatus/resultat
7. ReplyMsg nøyaktig som protokollen krever
8. rydde ned port og ressurser kontrollert

## Test fra ARexx

Når hosten er kvalifisert skal dette være mulig:

```rexx
options results
address EDUHOST 'PING'
say RC RESULT
```

Deretter tester vi `VERSION`, `ECHO`, `ADD` og ukjent kommando.

Neste: [M5-prosjektet](../26-m5-prosjekt/README.md).
