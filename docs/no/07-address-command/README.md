# 07 – ADDRESS COMMAND: ARexx møter AmigaDOS

Til nå har ARexx-programmene våre hovedsakelig arbeidet med egne data. Nå begynner power-user-delen.

`ADDRESS` velger hvilket kommandomiljø ARexx sender kommandoer til. AmigaDOS-kommandogrensesnittet nås med `COMMAND`.

```rexx
/* systeminfo.rexx */
address command
'INFO'
say 'RC =' RC
```

En alternativ stil er å angi miljøet på samme linje:

```rexx
address command 'DIR SYS:'
```

## RC

Etter en ekstern kommando må du ikke anta at alt gikk bra. Undersøk `RC`.

```rexx
address command 'LIST RAM:'
if RC ~= 0 then do
  say 'LIST feilet. RC =' RC
  exit RC
end
```

## Power-user-prinsipp

Automatisering skal være observerbar: scriptet skal vite om operasjonen lyktes.

## Lab

Lag `syscheck.rexx` som kjører noen ufarlige informasjonskommandoer, viser returkode og stopper kontrollert ved feil.

Neste: [filer og kataloger](../08-filer/README.md).
