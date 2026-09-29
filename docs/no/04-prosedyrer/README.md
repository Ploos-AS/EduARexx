# 04 – Funksjoner og prosedyrer

Større scripts må deles opp i forståelige deler.

```rexx
say greeting('Amiga')

exit

greeting: procedure
  parse arg name
  return 'Hei,' name || '!'
```

`PROCEDURE` gir rutinen sitt eget variabelmiljø. `PARSE ARG` henter argumentene, og `RETURN` sender et resultat tilbake.

## Hvorfor dette betyr noe

En power user ender raskt med scripts for backup, filbehandling, programstyring og BBS-oppgaver. Små gjenbrukbare rutiner gjør disse lettere å teste og vedlikeholde.

## Oppgave

Lag funksjonene `banner()`, `status()` og `help()`. La hovedprogrammet velge hvilken funksjon som brukes.

Neste: [PARSE](../05-parse/README.md).
