# EduARexx for AmigaGuide

Denne katalogen etablerer AmigaGuide som et offisielt publiseringsformat.

## Filer

- `EduARexx.guide` – håndlaget M6-referanse/golden fixture

Referansefilen definerer ønsket struktur før generatoren implementeres.

## Neste steg

Generatoren skal lese kurskildene og produsere en komplett guide med stabile node-ID-er, Prev/Next, innholdsfortegnelse og kryssreferanser.

En validator skal minst kontrollere:

- database-header
- balanserte `@node` / `@endnode`
- unike node-ID-er
- at interne link-mål finnes
- linje-/tegnsettregler vi bestemmer for støttede AmigaGuide-versjoner

Deretter skal resultatet åpnes og navigeres i et kvalifisert m68k AmigaOS runtime-miljø.
