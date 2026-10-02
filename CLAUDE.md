# CLAUDE.md – Arbeitsregeln für dieses Repo

## Projekt
- Deutsche Schulungs-PDFs für Trading-Laien, gesetzt mit XeLaTeX/TikZ.
- Dokumente liegen unter `dokumente/<name>/`; Build: `scripts/build.sh`, Setup: `scripts/setup.sh`.
- Ausführlicher Stand und **alle** Vorgaben stehen in `HANDOFF.md` – **zuerst lesen**
  (bei Platzmangel erst das Inhaltsverzeichnis: `grep -n '^#' HANDOFF.md`).

## Arbeitsweise (Vorgaben des Nutzers)
- Der Hauptagent **koordiniert nur**; **jede** Aufgabe erledigt ein eigener Subagent.
- Subagenten als Typ **`schulung`** starten (`.claude/agents/schulung.md`): nur
  Read/Edit/Write/Bash/Grep/Glob, **Start-Kontext höchstens 20K Tokens**. Der Auftrag enthält
  nur das für die Aufgabe Nötige (Dateien, Abschnitte, Bereiche) – keine Pflichtlektüre
  ganzer Dateien. (Neue Agent-Typen lädt Claude Code erst beim Sitzungsstart.)
- **Viele kleine Agenten statt weniger großer:** Aufgaben fein aufteilen (z. B. je
  Seitenbereich) und, wo möglich, parallel laufen lassen.
- **Kontextgrenze:** Ein Agent arbeitet bis ca. **100K Tokens**. Dann
  1. schreibt er an einer sauberen Stelle eine Übergabe-Datei
     `docs/uebergaben/<aufgabe>.md` (Vorlage: `docs/uebergaben/README.md`),
  2. committet seinen Zwischenstand,
  3. beendet sich mit `ÜBERGABE: <pfad>`.
  Der Hauptagent startet sofort einen Nachfolger, der **zuerst diese Datei** liest.
- Parallel arbeitende Agenten teilen sich ein Arbeitsverzeichnis: Commits **nur per
  Pfadangabe** (`git commit -m "…" -- <pfade>`), kein `git add -A` / `git add .`,
  kein `git stash`; bei abgelehntem Push `git pull --rebase --autostash`.
- Ist etwas nicht zu 100 % sicher (Maße, Farben, Abläufe der Plattform): dem Nutzer
  einen **Browser-Konsolenbefehl** geben, den er im WebTrader ausführt – **nicht schätzen**.
- Dem Nutzer klar sagen, **was vor dem Ausführen** eines Befehls geöffnet bzw.
  angeklickt sein muss.

## Inhaltliche Grundregeln (Kurzfassung, Details in HANDOFF.md, Abschnitt 2)
- Rein **informativ**: keine Handelsempfehlung, keine Wertung
  (kein „dafür/dagegen", „sinnvoll", „Vorteil" o. Ä.).
- **Sie-Form**; gehobenes, präzises Deutsch (C1), dennoch laienverständlich;
  keine Umgangssprache.
- Nur **Begriffe der Plattform** verwenden.
- **Keine Zahlen** – Ausnahme: Hebel-Vergleich mit einfachen Zahlen (HANDOFF.md, Abschnitt 14).
- **Kein Stop-Loss** (dafür folgt später ein eigenes Dokument).
- Plattform-Elemente (Nachbauten) bleiben **original**.
- Farben und Grafikstil wie im **Pending-Orders-Guide**: Lehrbuch-Grafik, keine UI-Optik
  (HANDOFF.md, Abschnitte 3 und 13).
- Alles **Vektor**, Schriften **eingebettet**.

## Nicht ins Repo
- Plattform-Schriftdateien (icomoon).
- Screenshots mit persönlichen Daten.
