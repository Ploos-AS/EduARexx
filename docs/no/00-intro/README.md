# 00 — Introduksjon til ARexx

Velkommen til EduARexx.

Målet med kurset er ikke bare at du skal lære et programmeringsspråk. Målet er at du skal lære å bruke Amigaen som et system du kan forme, automatisere og koble sammen.

ARexx er spesielt egnet til dette fordi Amiga-programmer kan tilby egne ARexx-porter. Et script kan derfor be ett program hente data, et annet program behandle dem og et tredje program lagre resultatet — uten at du trenger å gjøre alt manuelt i brukergrensesnittet.

## Hva er ARexx?

ARexx er Amiga-versjonen av REXX. På AmigaOS fungerer språket både som et vanlig scriptspråk og som et system for kommunikasjon mellom programmer.

I begynnelsen skal vi bruke ARexx som et enkelt programmeringsspråk. Senere skal vi bruke det som et automatiseringslag over hele Amiga-miljøet.

## Før du begynner

Du trenger etter hvert:

- en Amiga eller et kvalifisert AmigaOS-miljø i emulator
- RexxMast tilgjengelig
- en teksteditor
- Shell/CLI

Kurset skal ikke distribuere Kickstart-ROM-er eller proprietære AmigaOS-filer.

## Første mentale modell

Tenk på tre nivåer:

1. **ARexx som språk** — variabler, løkker, funksjoner og tekstbehandling.
2. **ARexx som shell-automatisering** — kjøre AmigaDOS-kommandoer og automatisere filer og systemoppgaver.
3. **ARexx som lim mellom programmer** — sende kommandoer gjennom ARexx-porter og bygge komplette arbeidsflyter.

Det tredje nivået er det som gjør ARexx spesielt kraftig på Amiga.

## Første program

Opprett filen `hello.rexx`:

```rexx
/* EduARexx: first program */
SAY "Hello from ARexx!"
```

Kjør scriptet i ARexx-miljøet ditt.

Forventet resultat:

```text
Hello from ARexx!
```

Hvis dette virker, har du allerede kjørt ditt første ARexx-program.

## Hva betyr linjene?

```rexx
/* EduARexx: first program */
```

Dette er en kommentar. Den er ment for mennesker og utføres ikke som programkode.

```rexx
SAY "Hello from ARexx!"
```

`SAY` skriver en verdi som tekst.

## Første eksperiment

Endre teksten. Kjør scriptet igjen. Prøv deretter flere `SAY`-linjer.

Eksempel:

```rexx
SAY "EduARexx"
SAY "Jeg lærer ARexx."
SAY "Målet er å automatisere Amigaen."
```

## Lab 00

Fortsett til [LAB.md](LAB.md).

## Etter denne leksjonen skal du kunne

- forklare hvorfor ARexx er mer enn bare et scriptspråk
- beskrive forskjellen mellom vanlig scripting og ARexx-port-automatisering
- lage en enkel `.rexx`-fil
- bruke `SAY`
- endre og kjøre scriptet flere ganger

Neste steg er å gjøre programmet interaktivt og introdusere variabler.
