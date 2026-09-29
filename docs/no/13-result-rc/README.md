# 13 – RESULT, RC og OPTIONS RESULTS

Automatisering blir langt kraftigere når scriptet kan bruke data programmet returnerer.

## Be om resultat

```rexx
options results
port = 'MYAPP'
address value port
'STATUS'

if RC ~= 0 then do
  say 'STATUS feilet. RC =' RC
  exit RC
end

say 'Svar:' RESULT
```

`RC` beskriver status. Når verten støtter resultatdata og de blir forespurt, kan `RESULT` inneholde svaret.

## Ikke bland status og data

Et robust script behandler dem separat:

1. send kommando
2. kontroller `RC`
3. bruk `RESULT` når kommandoen lyktes
4. parse resultatet dersom formatet krever det

## Oppgave

Lag en generell rutine som sender en kommando til et portnavn og rapporterer både status og resultat.

Neste: [orkestrering](../14-orkestrering/README.md).
