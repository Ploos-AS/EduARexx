# Publishing EduARexx

EduARexx skal publiseres fra samme faglige kilde til flere formater.

## Førsteklasses formater

- HTML / GitHub Pages
- PDF
- EPUB
- Kindle-kompatibel e-bok
- **AmigaGuide**

AmigaGuide er et native målformat, ikke bare en arkivkopi.

## Prinsipp

Kursinnholdet vedlikeholdes i Markdown. Publiseringslaget genererer formatspesifikke representasjoner uten å lage separate faglige versjoner av kurset.

```text
Markdown course source
       |
       +--> HTML
       +--> PDF
       +--> EPUB / Kindle
       +--> AmigaGuide (.guide)
```

## AmigaGuide-mål

`EduARexx.guide` skal:

- kunne brukes offline på Amiga
- ha innholdsfortegnelse
- ha én eller flere noder per kapittel
- ha Prev/Next-navigasjon
- ha kryssreferanser til relevante kapitler og labs
- beholde kode lesbar i Amiga-miljøet
- unngå avhengighet av moderne webteknologi
- kunne kvalifiseres på m68k AmigaOS

Interaktive handlinger skal være eksplisitte og trygge. Ingen guide-knapp skal utføre destruktive systemendringer uten at brukeren forstår handlingen.

## Pipeline

Fase 1: håndlaget referanseguide som fastsetter ønsket output.

Fase 2: Markdown -> AmigaGuide-generator.

Fase 3: validator for noder, lenker, tegnsett og struktur.

Fase 4: runtime-kvalifikasjon i amiga-runtime.

Den håndlagde referansen er en golden fixture for generatoren.
