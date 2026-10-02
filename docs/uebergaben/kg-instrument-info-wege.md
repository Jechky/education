# Übergabe: kg-instrument-info-wege
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Basis `3cc4418`, Ergebnis im Commit „Kontogrundlagen: Wege zu den Angaben eines Instruments …“

## Ziel (erledigt)
Kontogrundlagen mit `docs/plattform/dom-kursliste-instrument-info.md` in Einklang gebracht, nur Text.

## Erledigt (`Kontogrundlagen-Kosten.tex`)
- „Info-Fenster“ entfällt (Desktop-Fenster nicht belegt); neutral „Angaben des Instruments“.
- S. 2: Instrument „… eine Währung aus der Kategorie Forex (Devisen)“. Neue Zeile nach Buy / Sell: **Bid / Ask** (Spread) „Bid ist der Kurs, zu dem Sie verkaufen, Ask der Kurs, zu dem Sie kaufen. Der Unterschied zwischen beiden heißt Spread.“ → In der Plattform. Eigene Zeile „Spread“ passt nicht (Rest ca. 8 pt, nötig ca. 20 pt).
- S. 5 Merk: „… den eines Instruments in dessen Angaben (am Desktop über das Info-Zeichen in der Kursliste, mobil durch Antippen des Instruments unter Quotes).“
- S. 6: „Die tatsächlichen Sätze nennen die Angaben jedes Instruments (Kursliste bzw. Quotes): Swap long für Buy, Swap short für Sell.“ („Swap-Sätze“ passt nicht mehr); „bei Forex (Währungen, z. B. EUR/USD)“.
- S. 7 Leistennotiz: Doppelung „dieselben Werte wie die mobile Ansicht“ gestrichen. Desktop-Kasten: „untersten Leiste“ (Doppelung zur Notiz) gestrichen; Kursliste mit den acht Kategorien, „Jede Zeile zeigt Bid (Kurs für Sell) und Ask (Kurs für Buy); das Info-Zeichen am Ende der Zeile öffnet die Angaben des Instruments.“ Mobile-Kasten: A/B-Doppelung gekürzt („Das Info-Zeichen oben rechts öffnet zunächst den Reiter Information mit Leverage und Stop out.“), Orders → Active unverändert, neu „Unter Quotes stehen dieselben Kategorien als Reiter. Durch Antippen eines Instruments klappen seine Angaben auf, darunter Swap long, Swap short, Spread und Leverage.“
- Crude Oil ohne Kategorie; keine DOM-Werte übernommen.
- Prüfung: 8 Seiten (Rest S. 2 ca. 8 pt, S. 5 ca. 0,3 pt, S. 6 ca. 0,9 pt, S. 7 ca. 9,4 pt), Log sauber, 10 Schriften eingebettet, 0 Rasterbilder, Zahlen nur an den freigegebenen Stellen; S. 1, 3, 4, 8 pixelgleich.

## Bitte beim Nutzer bestätigen
1. HANDOFF 2.2 „Kein Ask/Bid“ (#14, #15) gilt laut Kopf für beide Dokumente; Bid/Ask stehen jetzt auf Anweisung in Doku 2 (S. 2, S. 7). Gilt die Regel nur für Doku 1?
2. Ob das Desktop-Info-Fenster Spread und dieselben Felder wie mobil zeigt, ist nicht belegt (Text nennt die Felder nur beim mobilen Weg).

## Für HANDOFF.md
Abschnitt 2.2: „Kein Ask/Bid“ nur Doku 1 (falls bestätigt); „Forex (Devisen)“ beim ersten Auftreten, danach „Forex“. Abschnitt 5.2/5.3: Weg zu Swap long/short, Spread, Leverage eines Instruments: Desktop Info-Zeichen am Zeilenende der Kursliste, mobil Quotes → Instrument antippen; Kategorien Forex, Stocks, Cryptos, Indices, Energies, Metals, Commodities, ETFs; Bid/Ask in der Grundbegriffe-Tabelle. Abschnitt 8.4: Fund „Info-Fenster, mobiler Weg fehlt“ erledigt.
