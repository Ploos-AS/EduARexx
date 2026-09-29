# 12 – ADDRESS mot et program

Når du kjenner portnavnet kan `ADDRESS` bytte kommandomiljø fra AmigaDOS til programmet.

```rexx
port = 'MYAPP'
address value port
'STATUS'
say 'RC =' RC
```

`ADDRESS VALUE` lar oss velge miljø fra en variabel. Det er nyttig i gjenbrukbare scripts.

## Viktig

`MYAPP` er et undervisningseksempel, ikke et løfte om at en bestemt port finnes. Bruk portnavnet dokumentasjonen til det faktiske programmet oppgir.

## Designmønster

Et større script kan veksle mellom miljøer:

```rexx
address command 'INFO'
address value port
'STATUS'
address command 'ECHO Tilbake i AmigaDOS'
```

Dermed blir ARexx et orkestreringslag over både operativsystem og applikasjoner.

Neste: [RESULT og RC](../13-result-rc/README.md).
