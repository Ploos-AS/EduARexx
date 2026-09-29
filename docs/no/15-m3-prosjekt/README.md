# 15 – M3-prosjekt: PortCommander

Målet er å lage et generelt undervisningsverktøy for ARexx-porter.

## Grensesnitt

```text
rx portcommander.rexx PORT COMMAND
```

Eksempel med en hypotetisk port:

```text
rx portcommander.rexx MYAPP STATUS
```

## Krav

PortCommander skal:

- lese port og kommando fra argumentene
- bruke `OPTIONS RESULTS`
- bruke dynamisk `ADDRESS VALUE`
- kontrollere `RC`
- vise `RESULT` når et resultat finnes
- skille transport/status fra data
- gi forståelig hjelp
- ikke anta et bestemt tredjepartsprogram

## Bestått M3

Studenten skal kunne forklare hva en ARexx-port er, finne portnavn og kommandoer i dokumentasjon, kommunisere med en port og bruke svar fra ett program som input til videre automatisering.

Neste milepæl går videre til debugging, tracing og mer avanserte workflows.
