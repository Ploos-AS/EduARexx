# 17 – SIGNAL og feilbehandling

Robuste scripts må ha en plan for feil.

ARexx kan overføre kontroll til navngitte labels. Dette brukes også i strukturert feilhåndtering.

```rexx
signal on syntax

say 'Starter'
/* arbeid */
exit 0

syntax:
  say 'Syntaksfeil oppstod.'
  exit 10
```

Ulike miljøer og feiltyper må testes mot den AmigaOS-versjonen kurset kvalifiseres på. Ikke bygg kritisk logikk på antakelser om en feiltilstand du ikke har testet.

## Cleanup-mønster

Når scriptet oppretter midlertidige ressurser, bør både normal og unormal avslutning ende i kontrollert opprydding.

```text
start
  |
work ---- error
  |         |
success     |
  \       /
   cleanup
      |
     exit
```

## Oppgave

Utvid et tidligere labscript slik at feil går gjennom én sentral feilrutine og avslutning gjennom én cleanup-rutine.

Neste: [logging](../18-logging/README.md).
