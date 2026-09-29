# 09 – Robuste systemscript

Et power-user-script må være tryggere enn en tilfeldig samling Shell-kommandoer.

## Regler

1. Valider argumenter før systemet endres.
2. Kontroller `RC` etter eksterne kommandoer.
3. Bruk testområder for destruktive øvelser.
4. Ikke overskriv brukerdata uten eksplisitt design.
5. Rapporter hva som feilet.
6. Returner en meningsfull exit-kode.

## Guard-rutine

```rexx
if target = '' then do
  say 'Mangler mål.'
  exit 10
end
```

## Dry-run som designmønster

Før et senere script gjør en endring, kan det først skrive kommandoen det planlegger å utføre. Dette gjør automatisering lettere å forstå og feilsøke.

## Oppgave

Design et backup-script med modusene `CHECK` og `RUN`. I dette kapitlet skal `RUN` fortsatt arbeide kun i et ufarlig labområde.

Neste: [M2-prosjektet](../10-m2-prosjekt/README.md).
