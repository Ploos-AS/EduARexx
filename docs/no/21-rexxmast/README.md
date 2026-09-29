# 21 – RexxMast og ARexx-arkitekturen

Til nå har vi brukt ARexx ovenfra. Nå ser vi på infrastrukturen under.

## RexxMast

RexxMast er den sentrale ARexx-komponenten i klassisk AmigaOS. Script, hosts og message ports inngår i et meldingsbasert system.

En nyttig modell er:

```text
script / caller
      |
      v
   RexxMast
      |
      v
  RexxMsg
      |
      v
 host message port
      |
      v
 application
```

Dette bygger på AmigaOS Exec sitt message-port-konsept. ARexx-integrasjon er derfor tett knyttet til operativsystemets IPC-modell.

## Hvorfor lære dette?

Som bruker hjelper modellen deg å forstå hvorfor porter må eksistere og hvorfor kommandoer kan feile. Som utvikler er dette grunnlaget for å gjøre ditt eget program scriptbart.

Neste: [Exec message ports](../22-exec-message-ports/README.md).
