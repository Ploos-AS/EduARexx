# 16 – TRACE og systematisk debugging

Når et ARexx-script vokser, er `SAY` alene ikke nok som feilsøkingsstrategi.

## TRACE

ARexx har innebygget tracing. En enkel start er:

```rexx
trace all
```

Tracing kan vise hvordan interpretereren arbeider seg gjennom scriptet. Bruk det målrettet; full tracing kan produsere mye output.

## En reproducerbar feilrapport

Når et script feiler, noter minst:

- scriptversjon
- AmigaOS-versjon
- emulator eller maskin
- eksakt kommando
- argumenter
- RC og eventuelle resultater
- relevant trace-output

## Debugging-metode

1. Reproduser feilen med minst mulig input.
2. Finn siste kjente korrekte steg.
3. Slå på tracing rundt det mistenkte området.
4. Kontroller variabler og returverdier.
5. Reduser problemet til et lite testcase.
6. Rett årsaken, ikke bare symptomet.

Neste: [SIGNAL og feilbehandling](../17-signal-errors/README.md).
