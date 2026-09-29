# 11 – ARexx ports

ARexx-porten er broen mellom scriptet og et program som tilbyr et ARexx-kommandogrensesnitt.

## Mental modell

Et ARexx-kompatibelt program oppretter en navngitt message port. Scriptet adresserer porten og sender tekstkommandoer. Programmet tolker kommandoen og kan returnere status og resultat.

```text
ARexx script
    |
    v
RexxMast
    |
    v
PROGRAMPORT
    |
    v
Amiga application
```

Dette gjør ARexx annerledes enn et vanlig Shell-script: vi kan kontrollere programmer gjennom grensesnitt de selv eksponerer.

## Portnavn

Portnavn og kommandoer bestemmes av programmet. Ikke anta at alle programmer støtter de samme kommandoene.

## Før du automatiserer

Finn programmets ARexx-dokumentasjon og noter:

- portnavn
- kommandoer
- argumenter
- returverdier
- krav til programtilstand

Neste: [ADDRESS mot programmer](../12-address-port/README.md).
