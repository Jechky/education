# Übergabe: kg-hebel-bank-broker
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Status: erledigt (ergänzt durch `kg-hebel-lehrbuch`)

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
- Nachfolger `kg-hebel-lehrbuch`: Grafik und Grün/Rot entfernt, Vergleich im Lehrbuch-Aufbau
  mit zwei Tabellen (Öffnen / Schließen der Positionen) – siehe unten.

## Für HANDOFF.md (Abschnitt 14 ersetzen; Stand nach Nachfolger `kg-hebel-lehrbuch`)
Nutzervorgaben 02.10.2026: „für die Hebel-Seite braucht es keine Illustrationen, keine Farben
Grün oder Rot“; Zahlen nach Skizze des Nutzers. **Zahlen-Ausnahme gilt jetzt für 1.000 €/1:10
und den Swap-Betrag 7 €** (nur S. 4). Aufbau wie im Lehrbuch (Opening / Closing the Positions):
Direktkauf über die Bank (Bekannter) gegen Broker mit Hebel 1:10 (Sie).
- **Entfernt:** Grafik „Ohne Hebel / Mit Hebel“ (inkl. „Trade volume“), alle `buy`/`sell`-
  Färbungen, alte Einzeltabelle, altes Fazit, Begriff „Finanzierungskosten“.
- **Aufbau:** Kicker, Titel, Lead (unverändert) · `\Htwo` „Ein Vergleich mit einfachen Zahlen“ ·
  Geschichte (3 Z.) · Tabelle „Öffnen der Positionen“ · Überleitung (1 Z.) · Tabelle „Schließen
  der Positionen“ · Schluss (3 Z.) · zwei `soft`-Kästen · Merk-Kasten (unverändert). Ende ca. 272 mm.
- Geschichte: „Angenommen, Sie und ein Bekannter verfügen über je 1.000 € und erwarten, dass der
  Kurs von Instrument XY steigt. Ihr Bekannter kauft Instrument XY für 1.000 € direkt über das
  Wertpapierdepot seiner Bank, also ohne Hebel. Sie öffnen hingegen beim Broker eine Position mit
  Hebel 1:10.“
- Spaltenköpfe (`\hdd`, zweizeilig): „Ihr Bekannter / Direktkauf über die Bank“ · „Sie / Broker,
  Hebel 1:10“; Tabellentitel (`\ttl`, fett, `ink`) in der ersten Kopfzelle.
- Öffnen: Kurs von Instrument XY 100 € | 100 € · Volumen (Wert der Position) 1.000 € | 10.000 € ·
  Margin – | 1.000 € · Geliehener Betrag – | 9.000 € · Einsatz 1.000 € | 1.000 €.
- Überleitung: „Am nächsten Tag steht Instrument XY bei 105 €, und Sie beide schließen Ihre Positionen.“
- Schließen: Kurs 105 € | 105 € · Ergebnis vor Kosten +50 € | +500 € · Kosten über Nacht: kein Swap |
  Swap: 7 € pro Nacht (darunter `muted`: „Mehr dazu auf der nächsten Seite.“) · Ergebnis nach Swap
  +50 € | +493 € · Ergebnis gemessen am Einsatz (vor Kosten) +5 % | +50 %. Keine Volumen-Zeile
  (1.050/10.500 € wären neue Zahlen).
- Schluss: „Bei einem Rückgang auf 95 € hingegen hätte der Hebel den Verlust im gleichen Verhältnis
  vergrößert: −50 € beim Direktkauf gegenüber −500 € beim Broker, jeweils vor Kosten. Fiele der Kurs
  um 10 %, entspräche Ihr Verlust dem gesamten Einsatz von 1.000 €; der Stop out schließt die
  Position in der Regel vorher.“
- Swap auf S. 4 **nicht** mit dem geliehenen Betrag begründet („Miete“ in der Skizze = Aufbewahrung,
  z. B. von Rohstoffen). ⚠ S. 5 (Lead, Grafik „Die Zinsen für den geliehenen Betrag werden als Swap
  gebucht“) und S. 7 (Swap = „Zinsen für das Halten über Nacht“) sagen noch das Gegenteil → Nachfolger.
- Zahlen nur 1.000, 10.000, 9.000, 1:10, 100, 105, 95, 50, 500, 7, 493, 5 %, 50 %, 10 %. „Spread“
  ist nicht eingeführt; „Öffnen“ statt „Eröffnen“ wie S. 3/S. 7.
- Rechnungen: 10.000 : 10 = 1.000; 10.000 − 1.000 = 9.000; 100 → 105 = +5 %: 1.000 € → +50 €,
  10.000 € → +500 €; 500 − 7 = 493; 50 bzw. 500 auf 1.000 € = 5 % bzw. 50 %; 95 €: −50/−500 €;
  −10 % von 10.000 € = −1.000 € = ganzer Einsatz.
- **Layout:** Spalten 71 / 42 / 48,53 mm (+ 2 × 2 `\tabcolsep` = 170 mm). Kopfzellen beginnen mit
  `\leavevmode` (sonst steht `\color` zuerst in der Zelle und es entsteht ca. 5 mm Lücke).
  Abstände: Lead 8 · Geschichte 6 · Tabelle 5 · Überleitung 6 · Tabelle 5 · Schluss 6 mm.
- Prüfung: 7 Seiten, Log ohne Warnung, 10 Schriften eingebettet, keine Rasterbilder, S. 1–3 und
  5–7 pixelgleich (60 dpi) mit `09b31e8`. Bild (nicht eingecheckt): `build/agent-hebel2/seite4.png`.

## Prüfkommandos
    cd dokumente/kontogrundlagen-kosten && xelatex -interaction=nonstopmode -output-directory=../../build/agent-hebel2 Kontogrundlagen-Kosten.tex
    pdftotext -f 4 -l 4 -layout ../../build/agent-hebel2/Kontogrundlagen-Kosten.pdf - | sed -n '10,50p'
