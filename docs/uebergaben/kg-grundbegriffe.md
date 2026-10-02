# Übergabe: kg-grundbegriffe
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Basis `76c0e61`, Ergebnis im Commit „Kontogrundlagen: Seite Grundbegriffe …“

## Ziel (erledigt)
Neue S. 2 „Grundbegriffe“ (Dokument jetzt 8 Seiten), S. 1 und S. 3–4 (bisher 2–3) nach der Fundliste angepasst, Seitenverweise.

## Erledigt
- S. 2: Tabelle Begriff | Erklärung | Seite: Instrument, Kurs, Position, Buy/Sell, Volumen, Broker, Plattform; Margin, Stop out, Leverage (Hebel, 1:10 = Margin ein Zehntel des Volumens), Swap, Commission (Provision); Merk „Zur Schreibweise“.
- Seitenverweise automatisch: `\seite{label}` („S. 4“), `\verw{label}` („→ S. 4“); Labels hinter den `\kicker`: `s:grundbegriffe, s:kontostand, s:margin, s:hebel, s:swap, s:plattform, s:ueberblick`. Bisher gab es keine Zahlenverweise; „nächste/vorherige Seite“ (S. 5/6) stimmen weiter.
- S. 1: „Leverage (Hebel)“, Satz mit Abbildung S. 7, „aktueller Kontowert“, Level-Hinweis mit (S. 4).
- S. 3: Lead (Abbildung S. 7); Balance-Kasten neu (Swap und Commission gehen beim Schließen mit dem Ergebnis in die Balance ein); Merk: Kontowert = Equity.
- S. 4: „Sicherheit für mögliche Verluste“, Kontoübersicht und Information mit (Abbildung S. 7), „Positionen mit höherem Volumen“.
- S. 8: Balance-Zeile „Bei Schließen sowie Ein- und Auszahlung“ (einzige Inhaltsänderung ab S. 5).
- Swap-Buchung geklärt durch `originals/Education_Session_1_Account_Basics_Kosten_2.pdf` (Reverse-Engineering-Fassung), Abschnitte 7.3 und 8: Swap auf der Position, im Profit enthalten, Balance erst beim Schließen. S. 6-Merk passt dazu.
- Prüfung: 8 Seiten, Log ohne Warnungen, 10 Schriften eingebettet, 0 Rasterbilder; S. 5–7 bei 60 dpi pixelgleich mit alt S. 4–6, S. 8 nur Balance-Zeile.

## Funde aus `docs/pruefung/kontogrundlagen-begriffe-bilder.md`
- Erledigt: A1, A2, A4, A5, A12, A16; Widerspruch 1 (Swap-Buchung).
- Teilweise: A3 (Broker/Direktkauf auf S. 2; Wertpapierdepot S. 5 offen), A6 (S. 1 Verweis), A7 (definiert; S. 5 „der Stop out schließt“, S. 8 fehlt), A8 (S. 1/2; S. 8 „Volumen zu Margin“ offen), A13 (nur Devisen), A15 (Commission; Kursliste, Chart, Orders → Active offen), B-Verweise (S. 1, 3, 4; S. 5 offen).
- Offen: A9, A10, A11, A14; Widerspruch 2 (S. 5 Free = 0) und 3 (S. 8 Swap = „Kosten“); Bilder B Prio 1–5.

## Offen / zu prüfen
1. Commission: Die RE-Fassung (8.3) nennt eigene Buchungstypen „Commission In/Out“ und „Broker Commission“; dass die Commission nur mit dem Ergebnis in die Balance geht, ist damit nicht ganz belegt (Konsolenprüfung).
2. „Volume“ ist im Order-Fenster (Doku 1) die Menge; Doku 2 nennt „Volumen“ den Wert der Position.
3. Fußzeile ohne Seitenzahl: Verweise „S. n“ setzen die Seitenanzeige des PDF-Viewers voraus (Nutzerentscheidung).
4. Kommentar in `mobil.tex` nennt noch „Seite 6“ (nicht angefasst).

## Für HANDOFF.md
Abschnitt 5: Doku 2 hat 8 Seiten (neue S. 2 „Grundbegriffe“, Rest +1); 5.3 Seitenliste und 13.2/13.3 um 1 verschieben; Swap-Buchung (5.4, Widerspruch 1) als geklärt eintragen (Quelle oben); neue Makros `\seite`/`\verw`.

## Prüfkommandos
    cd dokumente/kontogrundlagen-kosten && xelatex -interaction=nonstopmode -halt-on-error -output-directory=../../build/agent-gb Kontogrundlagen-Kosten.tex
    git log --oneline -5
