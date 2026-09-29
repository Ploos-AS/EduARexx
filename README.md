# EduARexx

**Fra `SAY "Hello"` til Amiga power user.**

EduARexx er et komplett undervisningsopplegg i ARexx for Amiga. Kurset starter helt fra null og bygger steg for steg mot avansert automatisering, ARexx-porter, integrasjon mellom Amiga-programmer og utvikling av egne ARexx-vennlige programmer.

## Mål

Etter fullført kurs skal studenten kunne:

- skrive og forstå ARexx-programmer
- bruke RexxMast og ARexx fra Shell/CLI
- mestre variabler, uttrykk, kontrollflyt, funksjoner og `PARSE`
- automatisere AmigaDOS og Workbench-arbeidsflyter
- oppdage og bruke ARexx-porter
- sende kommandoer mellom programmer og håndtere resultater
- skrive robuste scripts med feilhåndtering og tracing
- automatisere BBS-, terminal- og nettverksoppgaver
- forstå hvordan ARexx integreres med AmigaOS internt
- implementere en ARexx-port i et C-program
- bygge større, vedlikeholdbare automatiseringsløsninger

## Målgruppe

Kurset krever ingen tidligere erfaring med ARexx, REXX eller programmering. Det er laget både for nye Amiga-brukere som vil bli power users og utviklere som vil gjøre egne programmer automatiserbare.

## Kursløp

Kurset er planlagt i fire deler:

1. **Fundamentals** — fra første script til strukturert ARexx
2. **Amiga Power User** — AmigaDOS, Workbench, filer og systemautomatisering
3. **Inter-application Automation** — ARexx-porter og orkestrering av programmer
4. **Expert** — robust arkitektur, debugging, RexxMsg/Exec og C-integrasjon

Se [ROADMAP.md](ROADMAP.md) og [docs/CURRICULUM.md](docs/CURRICULUM.md).

## Språk

Norsk er hovedspråk. Engelsk parallellversjon er planlagt fra samme kursstruktur.

## Praktisk læring

Hvert hovedtema skal ha:

- forklaring
- små kjørbare eksempler
- lab
- oppgaver
- kontrollspørsmål
- et konkret power-user-scenario

Kurset skal kunne kvalifiseres mot ekte m68k AmigaOS i emulator gjennom Ploos-AS sitt Amiga-runtime-miljø. Proprietære Kickstart- og AmigaOS-filer skal aldri lagres i dette repoet.

## M0

M0 etablerer kursarkitektur, progresjon, første leksjoner og lab-konvensjoner.

Start her: [docs/no/00-intro/README.md](docs/no/00-intro/README.md)

## Lisens

Kursmateriale og dokumentasjon: Creative Commons Attribution 4.0 International (`CC BY 4.0`).

Eksempelkode: MIT License, med mindre annet er angitt i den enkelte filen.
