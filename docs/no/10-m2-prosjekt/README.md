# 10 – M2-prosjekt: AmiOperator

M2 avsluttes med et lite systemverktøy som kombinerer ARexx-logikk og AmigaDOS.

## Grensesnitt

```text
rx amioperator.rexx INFO
rx amioperator.rexx LIST RAM:
rx amioperator.rexx CHECK
rx amioperator.rexx HELP
```

## Krav

Programmet skal:

- bruke `PARSE ARG`
- bruke `ADDRESS COMMAND`
- kontrollere `RC`
- validere brukerinput
- ha egne prosedyrer
- unngå destruktive operasjoner
- gi forståelige feilmeldinger
- returnere fornuftige exit-koder

## Power-user checkpoint

Etter M2 skal studenten forstå skillet mellom ARexx som språk og ARexx som kontrollag over AmigaOS.

Neste milepæl er M3: **ARexx ports og inter-program automation**. Det er der én ARexx-prosess begynner å orkestrere andre Amiga-programmer.
