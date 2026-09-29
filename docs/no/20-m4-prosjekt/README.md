# 20 – M4-prosjekt: RexxFlow

RexxFlow er første prosjekt som behandles som et lite produksjonsprogram, ikke bare et eksempel.

## Mål

Bygg et generelt workflow-skall med:

- argumentvalidering
- tydelig dispatch
- logging
- sentral feilbehandling
- cleanup
- adapterrutiner
- konsistente exit-koder
- valgfri tracing

## Kommandoer

```text
rx rexxflow.rexx HELP
rx rexxflow.rexx CHECK
rx rexxflow.rexx PORT MYAPP STATUS
```

`MYAPP` er fortsatt et hypotetisk eksempel. Studenten erstatter det med en dokumentert port i labmiljøet.

## Bestått M4

Studenten skal kunne diagnostisere et script, isolere feil, lese trace-output, skille workflow fra integrasjonskode og bygge en kontrollert feilvei.

Neste del går dypere inn i AmigaOS og hvordan programmer selv blir ARexx-automatiserbare.
