# 01 – ARexx-grunnleggende

## Læringsmål

Etter dette kapitlet kan du forklare forskjellen mellom instruksjoner, uttrykk og data, bruke variabler og skrive små ARexx-programmer.

## Variabler

ARexx er dynamisk. Du trenger ikke deklarere en variabel før bruk.

```rexx
/* variables.rexx */
name = 'Amiga'
year = 1985
say 'Maskin:' name
say 'Lanseringsår:' year
```

ARexx skiller ikke mellom store og små bokstaver i symbolnavn på samme måte som mange moderne språk. Velg likevel én konsekvent skrivestil.

## Uttrykk og tekst

```rexx
a = 20
b = 5
say a + b
say a * b

first = 'Amiga'
second = 'power user'
say first second
```

ARexx gjør mye automatisk konvertering mellom tekst og tall. Det er praktisk, men gjør det viktig å forstå hvilke data scriptet faktisk mottar.

## Oppgave

Lag et script som lagrer navn, favoritt-Amiga og mengde RAM i variabler og skriver en lesbar presentasjon.

Neste: [kontrollflyt](../02-kontrollflyt/README.md).
