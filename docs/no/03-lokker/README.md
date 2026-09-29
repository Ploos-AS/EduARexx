# 03 – Løkker

ARexx bruker `DO` til både blokker og løkker.

## Telleløkke

```rexx
do i = 1 to 5
  say 'Runde' i
end
```

## WHILE

```rexx
i = 1
do while i <= 3
  say i
  i = i + 1
end
```

## UNTIL

```rexx
i = 0
do until i = 3
  i = i + 1
  say i
end
```

## Oppgave

Lag en løkke som skriver en nummerert liste over ti tenkte filer. Tenk deretter gjennom hvordan samme mønster senere kan brukes til batch-operasjoner på Amiga-filer.

Neste: [prosedyrer](../04-prosedyrer/README.md).
