# 02 – Valg og kontrollflyt

Programmer blir nyttige når de kan ta beslutninger.

## IF

```rexx
ram = 8
if ram >= 4 then
  say 'Nok RAM for denne oppgaven.'
else
  say 'Lite RAM.'
```

Bruk `DO ... END` når en gren inneholder flere instruksjoner.

## SELECT

```rexx
model = 'A1200'
select
  when model = 'A500' then say '68000-klassen'
  when model = 'A1200' then say 'AGA-maskin'
  otherwise say 'Ukjent modell'
end
```

## Power-user-øvelse

Lag et script som velger en handling ut fra argumentet `BACKUP`, `INFO` eller `HELP`. Foreløpig skal handlingene bare bruke `SAY`. Senere erstatter vi dem med ekte AmigaDOS-kommandoer.

Neste: [løkker](../03-lokker/README.md).
