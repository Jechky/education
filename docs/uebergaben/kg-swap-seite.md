# Übergabe: kg-swap-seite
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Status: erledigt (Commit siehe `git log`)

## Ziel
Kontogrundlagen S. 5: Swap nach dem Modell des Nutzers (Bank: Miete für die Aufbewahrung bzw. bei
Devisen Zinsen + Risikoanteil, dazu Aufschlag des Brokers) mit Rechenbeispiel aus der Skizze
(`originals/skizze-hebel-swap.png`); Uhrzeit des Swaps; neue Fußzeile. 7 Seiten.

## Erledigt (`dokumente/kontogrundlagen-kosten/Kontogrundlagen-Kosten.tex`)
- S. 5 Lead neu: „Bleibt eine Position über Nacht offen, verlangen die Bank und der Broker dafür je
  einen Betrag. Zusammen werden sie als Swap gebucht.“
- S. 5 unter `\Htwo` „Zusammensetzung des Swaps“: Satz „Angenommen, Instrument XY aus dem Vergleich auf
  der vorherigen Seite ist der Rohstoff Crude Oil.“ · Balken maßstäblich (Margin 17 von 170 mm = 1:10),
  Maß oben „Ihre Position in Crude Oil: 10.000 €“, unten „Margin: 1.000 € bei Hebel 1:10 ein Zehntel
  der Position“ · Pfeil „pro Nacht“ · Summenzeile (`\hthree`, Klammern `greya`): Miete für die
  Aufbewahrung + Risikoanteil + Aufschlag des Brokers = Swap; darunter 3 € · 3 € · 1 € · **7 € pro
  Nacht**; zweite Klammer unter den ersten beiden: „Betrag der Bank: 6 €“. Kein Grün/Rot.
- Danach: „Die Miete für die Aufbewahrung fällt bei Rohstoffen wie Crude Oil oder Natural Gas an; bei
  Devisen treten an ihre Stelle die Zinsen für das geliehene Geld. Der Risikoanteil soll die Bank vor
  Verlusten schützen.“ Swap long/short, Zeitstrahl, Woche, Merk-Kasten unverändert.
- Zeitstrahl: links der Stufe „Tageswechsel um 23:00 Uhr (Amsterdamer Zeit)“, rechts „Swap wird
  gebucht“ (beides `sell`, fett). Sonst überall nur „Tageswechsel“ (Notiz unter der Achse, Merk-Kasten).
- S. 7 Spickzettel: Swap „Zinsen für das Halten über Nacht“ → „Kosten für das Halten über Nacht“.
- Fußzeile (S. 2–7 und Deckblatt-Fuß): „SCHULUNGSEINHEIT“ → „EDUCATION – STANDARD PACKAGE“; Oberzeile
  des Deckblatts, Lead und `pdftitle` unverändert.

## Für HANDOFF.md
- Abschnitt 5.3, Punkt 5 (Swaps) ersetzen: Modell des Nutzers wie oben; Rechenbeispiel ist umgesetzt
  (5.4 „Rechenbeispiel-Kasten“ erledigt). Zahlen-Ausnahme S. 5: 1.000, 1:10, 10.000, 3, 3, 6, 1, 7 und
  „23:00 Uhr (Amsterdamer Zeit)“ (vom Nutzer bestätigt). Abschnitt 13.3, Zeile 5: Balken jetzt
  maßstäblich 1:10 ohne „geliehen“; Formelzeile mit Beträgen und zweiter Klammer „Betrag der Bank“.
- Fußzeile aller Seiten: „KONTOGRUNDLAGEN & KOSTEN · EDUCATION – STANDARD PACKAGE“.
- Prüfung: 7 Seiten, Log ohne Warnung, 10 Schriften eingebettet, keine Rasterbilder. 60 dpi gegen
  `706317e`: S. 2–4, 6 nur Fußzeile; S. 1 nur Fuß (276–279 mm); S. 7 nur Swap-Zeile und Fußzeile.
  S. 5 unterer Teil ab „Zeitpunkt der Buchung“ 1,2 mm höher als vorher.
- Nachtrag (Aufgabe kg-liquiditaetsanbieter, 02.10.2026): Auf S. 5 heißt es statt „Bank“ jetzt
  „Liquiditätsanbieter“ (Lead, Klammer „Betrag des Liquiditätsanbieters: 6 €“, Risikoanteil-Satz); Lead erklärt
  „der Liquiditätsanbieter – das Finanzinstitut, über das der Broker seine Positionen abwickelt –“. S. 4 („Bank“
  beim Direktkauf) unverändert. S. 5 ist voll (Rest < 1 pt): Lead 132 mm, Abstände knapper (siehe Kommentar im .tex).

## Prüfkommandos
    mkdir -p build/agent-swap && cd dokumente/kontogrundlagen-kosten && xelatex -interaction=nonstopmode -output-directory=../../build/agent-swap Kontogrundlagen-Kosten.tex
    pdftotext -layout ../../build/agent-swap/Kontogrundlagen-Kosten.pdf - | grep -n -i 'zins\|geliehen'
