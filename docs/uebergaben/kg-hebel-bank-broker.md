# Übergabe: kg-hebel-bank-broker
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Status: erledigt

## Ziel
Kontogrundlagen S. 4: Zahlenvergleich „Ohne Hebel / Mit Hebel 1:10“ wird zu
„Direktkauf über die Bank“ (Bekannter) gegen „Handel beim Broker, Hebel 1:10“ (Sie).
Grafik, Zahlen, Rechnungen, Spaltenbreiten und Seitenzahl (7) bleiben.

## Erledigt
- Geschichte, Spaltenköpfe, Zeile „Halten über Nacht“, Fazit, zwei TeX-Kommentare –
  `dokumente/kontogrundlagen-kosten/Kontogrundlagen-Kosten.tex`
- Prüfung: 7 Seiten, Log ohne Warnung, alle Schriften eingebettet, keine Rasterbilder;
  S. 4 Zeilenlagen (pdftotext -bbox) identisch mit vorher; S. 1–3, 5, 7 pixelgleich (60 dpi).
  Bild (nicht eingecheckt): `build/agent-hebel/seite4.png`.

## Für HANDOFF.md (Abschnitt 14, Nachtrag)
Nutzerentscheidung 02.10.2026: Vergleich jetzt wie im Lehrbuch **Direktkauf über die Bank
gegen Handel beim Broker** (nur der Broker-Handel trägt Finanzierungskosten über Nacht).
Damit ist die Zeile „Halten über Nacht“ sachlich korrekt; der ⚠-Hinweis zu „kein Swap ohne
Hebel“ (Swap auf CFD-Plattformen meist auf das ganze Volumen) ist erledigt.

- Geschichte (3 Zeilen, Zeile 3 fast voll): „Angenommen, Sie und ein Bekannter setzen je 100 € ein
  und erwarten, dass Instrument XY steigt. Ihr Bekannter kauft es direkt über das
  Wertpapierdepot seiner Bank, also ohne Hebel. Sie handeln hingegen beim Broker mit
  Hebel 1:10 und bewegen 1.000 €: Ihre 100 € sind als Margin gebunden, 900 € sind geliehen.“
- Spaltenköpfe: „Direktkauf über die Bank“ · „Handel beim Broker, Hebel 1:10“ (je einzeilig).
- Halten über Nacht: „keine Finanzierungskosten“ · „Swap für die geliehenen 900 €“ (unverändert).
- Fazit (2 Zeilen, Zeile 2 voll): „Gemessen am Einsatz ergibt dieselbe Kursbewegung beim
  Direktkauf ±5 %, beim Handel mit Hebel 1:10 hingegen +50 % oder −50 %. Der Hebel vergrößert
  folglich Gewinn und Verlust im gleichen Verhältnis.“
- Nicht-Plattform-Begriffe (bewusst, nur S. 4): Bank, Wertpapierdepot, Direktkauf,
  Finanzierungskosten, Broker (Broker auch S. 5). Keine Wertung Bank/Broker.
- Übrige Stellen geprüft (Swap-Seite S. 5, Tabelle/Kernaussagen S. 7): passen weiterhin.
- Tabelle in HANDOFF Abschnitt 14 (Kopfzeile, „kein Swap“) und Zitate von Geschichte/Fazit
  entsprechend ersetzen.

## Prüfkommandos
    cd dokumente/kontogrundlagen-kosten && xelatex -interaction=nonstopmode -output-directory=../../build/agent-hebel Kontogrundlagen-Kosten.tex
    pdftotext -f 4 -l 4 -layout ../../build/agent-hebel/Kontogrundlagen-Kosten.pdf - | sed -n '28,50p'
