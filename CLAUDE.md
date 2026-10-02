# CLAUDE.md – Arbeitsregeln für dieses Repo

Diese Datei lädt jeder Subagent komplett: **unter 200 Zeilen bleiben**, Details gehören in `HANDOFF.md`.

## Projekt
- Deutsche Schulungs-PDFs für Trading-Laien, gesetzt mit XeLaTeX/TikZ.
- Dokumente liegen unter `dokumente/<name>/`; Build: `scripts/build.sh`, Setup: `scripts/setup.sh`.
- Ausführlicher Stand und **alle** Vorgaben stehen in `HANDOFF.md` – **zuerst lesen**,
  aber gezielt (siehe Regel 6).

## Arbeitsweise

### 1. Rollen und Aufträge
- Der Hauptagent **koordiniert nur**; **jede** Aufgabe erledigt ein Subagent (Nutzervorgabe).
- Pro Subagent **genau eine** klar abgegrenzte Aufgabe mit **prüfbarem Ergebnis**
  (z. B. „Seite 4 gebaut, 7 Seiten, keine Überläufe").
- Der Auftrag nennt: **Ziel**, **Dateien**, was **ausdrücklich nicht** angefasst wird,
  **Prüfkommando** und **Rückgabeformat**.

### 2. Übergabe nach Tokens statt Zeilen
- Spätestens bei ca. **60–80K Tokens** Arbeitskontext oder sobald die Teilaufgabe erledigt ist,
  übergibt der Agent. (Messung: Claude Opus 4.5 als Agent 84 % richtig bei 32K, 65 % bei 64K,
  unter 50 % ab ca. 96K.)
- Nach **zwei erfolglosen Korrekturversuchen**: neuer Subagent mit besserem Auftrag,
  nicht weiterflicken.

### 3. Form der Übergabe
- Übergabe = **Commit** + kurze Datei `docs/uebergaben/<aufgabe>.md`
  (max. ca. 40 Zeilen; Vorlage `docs/uebergaben/README.md`); Ende mit `ÜBERGABE: <pfad>`.
- Der Nachfolger liest **zuerst** `CLAUDE.md`, dann die Übergabe, dann `git log -5`.

### 4. Parallelarbeit und Git
- Parallel **höchstens 3–5** Subagenten, jeder mit **eigenen Dateien**.
- Mehrere Aufgaben an derselben Datei laufen **nacheinander**, nie parallel.
- Nur **eigene Dateien explizit stagen** (kein `git add -A` / `git add .`);
  vor dem Push `git pull --rebase`.

### 5. Bilder sparsam
- Seitenübersicht: **60 dpi** (ca. 470 Tokens je A4-Seite).
- Lesbarkeit: **100 dpi** (ca. 1.260 Tokens).
- Details nur als **Ausschnitt**: `pdftoppm -r 150 -x … -y … -W … -H …` (ca. 650 Tokens)
  statt ganzer Seite bei 150 dpi (ca. 2.800 Tokens).
- Seiten als **PNG rendern**, nicht das PDF lesen.
- Bilder prüft der Subagent **selbst**; zurück an den Hauptagenten geht nur Text.

### 6. Gezielt lesen
- `grep`/Ausschnitte statt ganzer Dateien.
- Von `HANDOFF.md` nur nötige Abschnitte: `grep -n '^#' HANDOFF.md`, dann gezielt lesen.
- LaTeX-Logs nie komplett lesen, sondern greppen:
  `grep -nE '^!|Overfull|Underfull|Undefined|undefined|Rerun|Missing character' <log> | head -40`

### 7. Kurze Rückmeldung
- Maximal ca. **15 Zeilen**: Status, geänderte Dateien, Commit, höchstens 5 Probleme, Bildpfade.

### 8. Umfang dieser Datei
- `CLAUDE.md` bleibt **unter 200 Zeilen**; Ausführliches steht in `HANDOFF.md`.

### 9. Unsichere Plattform-Details
- Maße, Farben, Abläufe der Plattform **nie schätzen**: dem Nutzer einen
  **Browser-Konsolenbefehl** für den WebTrader geben.
- Dabei klar sagen, **was vorher geöffnet bzw. angeklickt sein muss**.

## Inhaltliche Grundregeln (Kurzfassung, Details in HANDOFF.md, Abschnitt 2)
- Rein **informativ/neutral**: keine Handelsempfehlung, keine Wertung
  (kein „dafür/dagegen", „sinnvoll", „Vorteil" o. Ä.).
- **Sie-Form**; gehobenes, präzises Deutsch (C1), dennoch laienverständlich;
  keine Umgangssprache.
- Nur **Begriffe der Plattform** verwenden.
- **Keine Zahlen** – Ausnahme: Hebel-Vergleich mit einfachen Zahlen (HANDOFF.md, Abschnitt 14).
- **Kein Stop-Loss** (dafür folgt später ein eigenes Dokument).
- Plattform-Elemente (Nachbauten) bleiben **original**.
- Farben und Grafikstil wie im **Pending-Orders-Guide** (PO-Farben): Lehrbuch-Grafik,
  keine UI-Optik (HANDOFF.md, Abschnitte 3 und 13).
- Alles **Vektor**, Schriften **eingebettet**.

## Nicht ins Repo
- Plattform-Schriftdateien (icomoon).
- Screenshots mit persönlichen Daten.

Quellen und Begründung: `docs/arbeitsweise-recherche.md`
