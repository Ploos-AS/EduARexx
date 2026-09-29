# EduARexx Curriculum

## Del I — Fundamentals

### 00. Hva er ARexx?
- hvorfor ARexx finnes
- RexxMast
- scripts og filendelser
- Shell/CLI versus Workbench
- første kjøring

### 01. Første program
- `SAY`
- kommentarer
- enkel input/output
- kjøre scripts på nytt

### 02. Variabler og uttrykk
- symboler
- tall og tekst
- operatorer
- enkel formattering

### 03. Strenger
- sammenføyning
- quoting
- innebygde strengfunksjoner
- praktisk tekstbehandling

### 04. Kontrollflyt
- `IF/THEN/ELSE`
- `SELECT`
- `DO`
- løkker
- tidlig avslutning

### 05. Procedures og functions
- labels
- `CALL`
- `RETURN`
- argumenter
- lokale variabler
- modulær struktur

### 06. PARSE
- `PARSE VALUE`
- `PARSE ARG`
- templates
- ord- og feltbehandling
- hvorfor `PARSE` er sentralt i REXX-familien

## Del II — Amiga Power User

### 07. AmigaDOS fra ARexx
- kommando-miljø
- kjøre AmigaDOS-kommandoer
- resultater og return codes
- scripts som lim mellom systemverktøy

### 08. Filer og kataloger
- lese/skrive filer
- batch-jobber
- rename/copy/archive-workflows
- sikker håndtering av brukerdata

### 09. Workbench workflows
- power-user tankegang
- launch/organize/cleanup
- automatisere repeterende oppgaver

### 10. Startup og administrasjon
- startup-relaterte scripts
- backup
- housekeeping
- konfigurasjonsdrevet automatisering

## Del III — ARexx Ports

### 11. Message ports og ARexx-modellen
- hva en port er
- host applications
- kommando-API-er
- synkron kommunikasjon

### 12. ADDRESS
- velge command environment
- sende kommandoer
- bytte mellom hosts

### 13. Resultater
- `RESULT`
- return codes
- feiltilstander
- robust dialog med applikasjoner

### 14. Orkestrering
- koble to programmer sammen
- koble flere programmer sammen
- dataflyt mellom applikasjoner
- bygge workflows som ellers ville krevd manuell GUI-bruk

## Del IV — Robust og avansert ARexx

### 15. Feilhåndtering
- `SIGNAL`
- conditions
- cleanup
- defensive scripts

### 16. TRACE og debugging
- tracing
- isolere feil
- logge beslutninger og data

### 17. Større programmer
- struktur
- navngiving
- gjenbruk
- biblioteker og inkluderingsmønstre
- testbarhet

### 18. BBS, terminal og nettverk
- terminal workflows
- ABBS-orienterte eksempler
- ARexx doors
- nettverksverktøy
- Ploos-AS-integrasjoner der det er hensiktsmessig

## Del V — Expert / Amiga internals

### 19. RexxMast under panseret
- interpreter/host-modellen
- hvordan meldinger flyter
- command environments

### 20. RexxMsg og Exec
- `RexxMsg`
- Exec message ports
- argumenter og resultater
- livssyklus for en ARexx-kommando

### 21. ARexx-port i C
- registrere en port
- motta meldinger
- parse kommandoer
- returnere resultater
- cleanup
- gjøre egne applikasjoner scriptbare

### 22. API-design for ARexx
- stabile kommandoer
- dokumenterte argumenter
- resultatformater
- backward compatibility
- scripts som offentlig grensesnitt

## Capstone

Studenten bygger en Amiga Automation Suite som demonstrerer:

- strukturert ARexx
- AmigaDOS-automatisering
- filbehandling
- minst to ARexx-hosts
- robust feilhåndtering
- logging
- konfigurasjon
- dokumentasjon
- en kort analyse av hvordan løsningen kunne utvides med en egen C-basert ARexx-port
