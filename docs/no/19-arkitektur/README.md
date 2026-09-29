# 19 – Arkitektur for større ARexx-programmer

Et stort script bør ikke være én lang sekvens.

## Lagdeling

Vi bruker fire mentale lag:

1. **CLI/input** – parse og valider brukerens ønske.
2. **Workflow** – bestem rekkefølgen på operasjonene.
3. **Adapters** – snakk med AmigaDOS eller bestemte ARexx-porter.
4. **Utilities** – logging, validering og felles hjelpefunksjoner.

Denne strukturen gjør det lettere å bytte et program eller portgrensesnitt uten å skrive om hele workflowet.

## Kontrakter

En rutine bør ha et tydelig ansvar:

```text
input -> routine -> result/status
```

Dokumenter hva rutinen forventer og hva den returnerer.

## State

Unngå unødvendig global tilstand. `PROCEDURE` og eksplisitte argumenter gjør avhengigheter lettere å forstå.

## Oppgave

Tegn kallgrafen for et workflow som:

- validerer input
- undersøker systemet
- kontakter to ARexx-porter
- logger resultatet
- rydder opp

Neste: [M4-prosjekt](../20-m4-prosjekt/README.md).
