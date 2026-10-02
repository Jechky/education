# Übergabe: kg-seite-instrumente
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Ergebnis im Commit „Kontogrundlagen: neue Seite Instrumente und Positionen …“

## Erledigt (`Kontogrundlagen-Kosten.tex`, jetzt 9 Seiten)
- Neue S. 8 „Instrumente und Positionen“ (Label `s:instrumente`), Titel „Die Angaben der Instrumente und Ihrer Positionen“, Lead mit „wie unter „In der Plattform“ … Wörter“.
- Oben `info-desktop.pdf` und `info-mobil.pdf` im selben Maßstab (1 px = 0,225 mm, Schrift 7,7 pt): Desktop-Fenster 65,3 × 43,8 mm (Schatten als overlay über den Satzrand), mobil 92,3 × 73,6 mm. Überschriften DESKTOP/MOBILE (wie S. 7) mit je einem Satz zum Weg. Legende (\pfn 1–3, kompakte Tabelle) links unter dem Desktop-Fenster: Swap long „Satz des Swaps für Buy“, Swap short „… für Sell“, Leverage „Hebel des Instruments“.
- Unten „Die Liste der offenen Positionen“: Desktop Tabelle unter dem Chart, Reiter Active/Pending/History; mobil dieselben Reiter unter Orders, Antippen klappt Angaben auf. Tabelle Angabe | Bedeutung | Mehr dazu: Amount (Menge), Trade volume (Wert = Volumen), Swap (in Total Profit enthalten), Total Profit (Ergebnis inkl. Swap; alle zusammen unter Profit/Losses), Margin. Kein S/L, keine Commission. Rest ca. 79 pt (28 mm) für einen späteren Nachbau.
- S. 2: Spread → Instrumente und Positionen (statt In der Plattform); Leverage und Swap je zweiter Verweis; Swap „in ihrem Total Profit enthalten“.
- S. 3: „weist ihn bei der Position unter Total Profit aus, das Ergebnis aller offenen Positionen zusammen unter Profit/Losses. Er fließt in die Equity ein …“
- S. 5 Merk: Weg zum Hebel des Instruments → „(Abbildung unter „Instrumente und Positionen“)“.
- S. 6: „Die tatsächlichen Sätze stehen bei jedem Instrument (→ Instrumente und Positionen)“; Merk „in ihrem Total Profit enthalten“.
- S. 7 Kästen: Doppelungen zur neuen Seite gekürzt (Spalte Swap, Swap/Margin, Feldliste), je ein Verweis → Instrumente und Positionen.
- S. 9: neue Zeile Total Profit („Ergebnis einer offenen Position einschließlich ihres Swaps“ | „Mit jeder Kursbewegung und jedem Swap“).
- `scripts/build.sh` baut `info-desktop.tex`/`info-mobil.tex` automatisch (Erkennung `^\documentclass…{standalone}`), nicht geändert.
- Prüfung: 9 Seiten, Log ohne Over-/Underfull, 15 Schriften eingebettet, 0 Rasterbilder; Zahlen nur 1:10 (S. 2, S. 9), S. 5/6 unverändert, Nummern S. 7/8. Rest je Seite: S. 2 8 pt, S. 3 18 pt, S. 5 0,3 pt, S. 6 0,9 pt, S. 7 9,4 pt. S. 1 und 4 pixelgleich.

## Offen
- Nachbau der Positionsliste (Desktop-Tabelle bzw. mobile Liste) braucht eine Messung; Platz unten auf S. 8.
- „Total Profit = Summe in Profit/Losses“ folgt aus den bisherigen Aussagen des Dokuments, ist aber nicht eigens gemessen.

## Für HANDOFF.md
Abschnitt 5.3: neue S. 8 „Instrumente und Positionen“ (oben Nachbauten Desktop/mobil mit Legende 1–3, unten Liste der offenen Positionen als Text), „Auf einen Blick“ wird S. 9; Begriff „Total Profit“ für das Ergebnis einer Position (S. 2, 3, 6, 8, 9), „Profit/Losses“ bleibt für die Kontoübersicht. Abschnitt 2.3: Ausnahme 1 um die Nummern 1–3 auf S. 8 ergänzen. Abschnitt 5.4: Instrument-Info erledigt (Nachbauten eingebunden).
