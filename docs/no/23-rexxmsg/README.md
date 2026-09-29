# 23 – RexxMsg

`RexxMsg` er meldingsstrukturen som brukes i ARexx-kommunikasjon.

For studenten er de viktigste konseptene først:

- meldingen identifiserer ARexx-kommunikasjon
- den bærer argumenter/kommandoinformasjon
- den har felter for returstatus
- resultatdata må håndteres etter ARexx-kontrakten
- meldingen må svares på korrekt

Vi skiller mellom **konseptuell forståelse** og **ABI-/headerdetaljer**. Eksakte strukturfelt, konstanter og bibliotekskall skal verifiseres mot SDK/headerne som brukes av buildmiljøet, ikke kopieres fra hukommelsen.

## Fra script til C

Når scriptet gjør:

```rexx
address MYHOST 'STATUS'
```

skal hosten i prinsippet:

1. motta RexxMsg
2. identifisere kommandoen
3. parse argumentene
4. utføre operasjonen
5. sette status/resultat
6. svare på meldingen

Neste: [design en ARexx-host](../24-host-design/README.md).
