# 08 – Filer, kataloger og assigns

Amigaens logiske navn og assigns er en viktig del av power-user-arbeidsflyten. ARexx kan kombinere sin egen logikk med AmigaDOS-verktøy.

## Undersøk før du endrer

Start med lesende operasjoner:

```rexx
address command
'LIST SYS:'
say 'RC =' RC
```

Når kurset introduserer kommandoer som kopierer, flytter eller sletter data, skal eksemplene bruke egne testområder som `RAM:` eller en eksplisitt lab-katalog.

## Assigns

Et godt script bør bruke logiske plasseringer fremfor å bake inn bestemte disk- eller volumoppsett når det er mulig. Dette gjør automatiseringen mer portabel mellom Amiga-oppsett.

## Lab: arbeidsområde i RAM:

Lag et script som oppretter et eget midlertidig arbeidsområde under `RAM:`, kontrollerer returverdier og viser innholdet. Rydd bare opp data som scriptet selv har opprettet.

Neste: [robuste systemscript](../09-robuste-systemscript/README.md).
