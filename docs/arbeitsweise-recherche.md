# Arbeitsweise mit Subagenten – Zusammenfassung der Recherche

Diese Datei begründet die Regeln in `CLAUDE.md`. Sie ist für Nicht-Entwickler geschrieben.
Jede Aussage trägt eine Kennzeichnung:

- **[belegt]** – gemessen in einer Studie oder einem Test
- **[offiziell]** – Aussage der Hersteller- bzw. Tool-Dokumentation
- **[Praxis]** / **[Praxisbericht]** / **[Beispiel]** – Erfahrung aus Projekten, nicht überprüft
- **[Einschätzung]** – unsere eigene Schlussfolgerung

## 1. Kontext: Je länger, desto fehleranfälliger

- Die Leistung sinkt **stetig** mit wachsendem Kontext; es gibt **keinen einzelnen Kipppunkt**
  (18 Modelle getestet). https://www.trychroma.com/research/context-rot [belegt]
- LOCA-bench, Claude Opus 4.5 als Agent bei mehrstufigen Aufgaben: richtig bei 8K Tokens 96 %,
  bei 16–32K 84 %, 64K 65 %, 96K 45 %, 128K 34 %, 256K 15 %. https://arxiv.org/abs/2602.07962 [belegt]
- NoLiMa (ältere Modelle): wirksam oft nur 4–16K Tokens. https://arxiv.org/abs/2502.05167 [belegt]
- Neue Modelle **finden** einzelne Angaben in sehr langen Texten viel besser
  (Opus 4.6: MRCR 76 % bei 1 Mio. Tokens). Das ist aber **kein** mehrstufiges Arbeiten.
  https://www.anthropic.com/news/claude-opus-4-6 [belegt]
- Über viele Gesprächsschritte hinweg verschlechtern sich Ergebnisse um rund 39 %.
  https://arxiv.org/abs/2505.06120 [belegt]
- Anthropic rät, den Kontext zu **kuratieren** und Rückgaben auf 1–2K Tokens zu halten.
  https://platform.claude.com/docs/en/build-with-claude/context-windows [offiziell]
- Folgerung: Übergabe bei ca. **60–80K Tokens** [Einschätzung]. Die frühere Grenze von
  1500 Zeilen LaTeX entspricht nur etwa 30–40K Tokens – das war **zu früh** und
  **das falsche Maß**.

## 2. Leitlinien von Anthropic

- In sich geschlossene Aufgaben delegieren; iterative, eng gekoppelte Arbeit eher in
  **einem** Agenten. https://code.claude.com/docs/en/sub-agents [offiziell]
- 3–5 Agenten parallel, jeder mit eigenen Dateien; „drei fokussierte schlagen fünf
  verstreute". https://code.claude.com/docs/en/agent-teams [offiziell]
- Briefing mit Ziel, Ausgabeformat und Grenzen.
  https://www.anthropic.com/engineering/multi-agent-research-system [offiziell]
- `CLAUDE.md` unter 200 Zeilen. https://code.claude.com/docs/en/memory [offiziell]
- Nach zwei Fehlkorrekturen neu anfangen. https://code.claude.com/docs/en/best-practices [offiziell]
- Fortschrittsdatei, Aufgabenliste und Commits; eine Aufgabe pro Sitzung.
  https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents [Beispiel]
- Hinweis: Ein **reiner Koordinator** ist von Anthropic nicht ausdrücklich empfohlen.
  Im Projekt gilt er als **Nutzervorgabe**.

## 3. Praxiserfahrungen

- Übergabe in drei Schichten: kurze Einstiegsdatei, Aufgabenliste, knappe Fortschrittsnotiz
  plus `git log`. [Praxis]
- Ein eigener Arbeitsordner (worktree) je Agent verschiebt Konflikte nur ans Ende.
  https://code.claude.com/docs/en/worktrees [Praxis]
- Flache Koordination über Sperren skalierte schlecht: 20 Agenten erreichten etwa den
  Durchsatz von 2–3. https://cursor.com/blog/scaling-agents [Praxisbericht]
- Prüfschleife mit ausführbarem Check; Prüfer mit frischem Kontext. [Praxis]
- Typische Fehler (MAST, 1.600 Abläufe): verfrühtes „fertig", vage Aufträge mit doppelter
  Arbeit, gegenseitiges Überschreiben, veraltete Notizen. https://arxiv.org/abs/2503.13657 [belegt]

## 4. Tokens sparen

- Bilder: A4 bei 60/100/150 dpi kosten ca. 468/1.260/2.835 Tokens
  (Formel ⌈Breite/28⌉ × ⌈Höhe/28⌉).
  https://platform.claude.com/docs/en/build-with-claude/vision [offiziell + eigene Rechnung]
- Ausschnitte statt ganzer Seiten sparen weiter (ca. 650 Tokens).
- Ein PDF direkt zu lesen kostet **zusätzlich** Text-Tokens; besser Seiten als PNG rendern.
  https://platform.claude.com/docs/en/build-with-claude/pdf-support [offiziell]
- Knappe Tool-Ausgaben: 72 statt 206 Tokens für dieselbe Information.
  https://www.anthropic.com/engineering/writing-tools-for-agents [offiziell]
- LaTeX leise bauen und das Log durchsuchen statt lesen.
  https://manpages.debian.org/testing/latexmk/latexmk.1.en.html [offiziell]
- Kontext-Bereinigung sparte in Anthropics Test 84 %.
  https://claude.com/blog/context-management [offiziell]

## 5. Was das für dieses Projekt heißt

Der Hauptagent bleibt Koordinator, und jeder Subagent bekommt genau eine kleine Aufgabe mit
prüfbarem Ergebnis. Übergeben wird nach Tokens (ca. 60–80K) oder nach erledigter Teilaufgabe,
nicht nach Zeilen. Eine kurze Übergabedatei plus Commit genügt dem Nachfolger, wenn er zuerst
`CLAUDE.md`, dann die Übergabe und `git log -5` liest. Gearbeitet wird höchstens zu fünft
parallel, jeder mit eigenen Dateien. Bilder, Logs und `HANDOFF.md` werden nur ausschnittsweise
gelesen, damit der Kontext lange brauchbar bleibt.

## Rohnotizen

Die ausführlichen Rohnotizen liegen unter
`research_notes/Subagenten Arbeitsablauf und Kontext/`.
