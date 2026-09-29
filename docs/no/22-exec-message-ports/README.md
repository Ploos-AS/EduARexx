# 22 – Exec message ports

AmigaOS bruker meldinger og porter som en grunnleggende IPC-mekanisme.

På konseptnivå:

1. en task oppretter en message port
2. andre finner eller kjenner porten
3. en melding sendes til porten
4. mottakeren behandler meldingen
5. meldingen svares på når protokollen krever det

## ARexx som protokoll over mekanismen

En ARexx-host bruker ikke bare vilkårlige meldinger. Den må forstå ARexx-kontrakten og håndtere RexxMsg korrekt.

## Viktig utviklerregel

Message ownership, reply og ressurslevetid må være eksplisitt forstått. Feil her er ikke bare en scriptfeil; i native Amiga-kode kan dårlig IPC-håndtering gi heng, lekkasjer eller ugyldig minnebruk.

## Lab på papir

Tegn livsløpet til en kommando fra et ARexx-script til en host og tilbake. Marker hvem som eier meldingen i hvert steg.

Neste: [RexxMsg](../23-rexxmsg/README.md).
