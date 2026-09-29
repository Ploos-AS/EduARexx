# 28 – Native kvalifikasjon

EduARexx skiller mellom at en fil **kan bygges** og at den **virker på Amiga**.

AmigaGuide-utgaven får derfor to porter:

```text
Markdown
   |
generator
   |
static validation
   |
   +---- Linux CI PASS
   |
native m68k qualification
   |
AmigaGuide runtime PASS
```

Den nederste statusen kan bare oppnås ved en faktisk test i et m68k AmigaOS-miljø.

## Hvorfor dette er en del av kurset

Det demonstrerer en viktig regel for retro-utvikling: moderne CI kan kontrollere mye, men den kan ikke automatisk erstatte målplattformens virkelige ABI, operativsystem, programvare og brukeropplevelse.

Se `qualification/README.md` for den normative prosedyren.
