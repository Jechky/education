# Übergabe: Pending-Orders-Guide – Text- und Layout-Umbau

Stand: 02.10.2026, Branch `claude/continue-conversation-529rck`. Der Vorgänger-Agent hat wegen der Lesegrenze (ca. 1500 Zeilen) an einer sauberen Stelle aufgehört. Der Build läuft, das PDF hat 9 Seiten.

## Auftrag in eigenen Worten

Der deutsche Guide `dokumente/pending-orders/Pending-Orders-Guide.tex` bekommt einen neuen Textstil und ein neues Layout:

- Text in ganzen, verbundenen Sätzen, Lehrbuchton, laienverständlich.
- Pro Ordertyp eine eigene Seite mit großem Chart und den Abschnitten *Was es ist*, *Typischer Einsatz*, *Take-Profit* und *Beispiel*.
- Neuer Abschnitt „Eine wartende Order löschen“ (mobile Ansicht).

## Vorgaben (alle gültig, zuletzt verschärft)

Die Grundregeln stehen in `HANDOFF.md`, Abschnitt 2. Zusätzlich gilt:

1. **Sie-Form** überall (Sie/Ihr/Ihnen; Imperativ „Tippen Sie …“). Ein „Sie“ am Satzanfang darf nie die Order meinen, deshalb dort „Die Order wird …“ schreiben.
2. **C1-Register:** gehobenes, präzises Standarddeutsch wie ein Schulungsdokument einer Bank.
   - Nicht erlaubt: Umgangssprache, Slogans, Satzersatz durch „Sofort.“, „Später.“ oder „Absenden.“, Gedankenstrich-Ketten, Ausrufe, „Spickzettel“, „fürs Erste ignorieren“, „hinterherlaufen“.
   - Erwünscht: Konnektoren wie folglich, sobald, hingegen; präzise Verben wie auslösen, festlegen, hinterlegen, erteilen.
3. **Rein informativ, neutral:**
   - Nicht erlaubt: „sinnvoll“, „Vorteil“, „lohnt“, „besser“, „Gewinnchance“, jede Empfehlung.
   - Die Zwischenüberschrift heißt „Typischer Einsatz“.
   - Beispiele sind als Annahme formuliert („Sie gehen davon aus, dass …“).
   - „Günstiger kaufen / teurer verkaufen“ ist als Sachbeschreibung erlaubt.
4. **Begriffe:**
   - Nur Plattform-Begriffe: Buy Limit, Sell Limit, Buy Stop, Sell Stop, At price, Take-Profit, Buy, Sell, Type, New Pending Order, New Market Order, Place pending order, Pending, Orders, Delete, Cancel, Modify Order, T/P.
   - Für den Wert bei At price immer „Aktivierungspunkt“ schreiben.
   - Immer „ausgelöst“, nie „ausgeführt“.
   - Verboten: Ask/Bid, „Trigger“, „Marke“.
5. **Keine Zahlen** außer Schrittnummern. **Kein Stop-Loss**, keine Verlustbegrenzung. **Keine Gültigkeitsoptionen.**
6. **Roter Faden:** Instrument XY pendelt in einem engen Bereich.
   - Buy Limit: Rückfall an den unteren Rand.
   - Sell Limit: Anstieg an den oberen Rand.
   - Buy Stop: Ausbruch nach oben.
   - Sell Stop: Ausbruch nach unten.
   - Jedes Beispiel sagt auch, was passiert, wenn der Kurs nicht kommt: Die Order wartet weiter, bis er kommt oder bis sie gelöscht wird.
7. **Bilder nicht mehrfach erklären:** Die Lesehilfe steht nur einmal (Seite 3, Randspalte). Es gibt keine Anatomie-Grafik.
8. **Layout:**
   - Kicker auf allen Seiten bei 20,5 mm.
   - Gleiche Kicker im selben Kapitel („Die Limit-Typen“ / „Die Stop-Typen“).
   - In schmalen Spalten Flattersatz ohne Trennung.
   - Alles bleibt Vektor, alle Schriften eingebettet.
9. **Nicht anfassen:**
   - Deckblatt: Nur der Untertitel wurde von du auf Sie umgestellt (erledigt).
   - `fenster-bl.pdf`, `type-menu.pdf`, `charts.tikz`, `Pending-Orders-Guide_CoverTest.tex`, `cover*`.
   - `HANDOFF.md`, `scripts/`, `tools/`, `dokumente/kontogrundlagen-kosten/`: Dort arbeitet ein anderer Agent.
10. **Git:**
    - Nur eigene Dateien per Pfad stagen.
    - Vor dem Push `git pull --rebase origin claude/continue-conversation-529rck` ausführen.
    - Die Commit-Message endet mit den Co-Authored-By- und Claude-Session-Zeilen.

## Erledigt

Datei: `dokumente/pending-orders/Pending-Orders-Guide.tex`

**Präambel:**
- Die Zeile `\babelprovide[hyphenrules=english]` ist entfernt, es wird jetzt deutsch getrennt.
- Neue Bausteine: `\flatter`, Rasterlängen `\labw` (33 mm), `\gutw` (5 mm), `\colw`, Chartmaßstab `\cu` (0,6 mm pro px).
- Neue Makros: `\mlab`, `\leadfix` (Einleitung mit fester Höhe von drei Zeilen), `\typkopf`, `\chartzeile`, `\abschnitt`, Kasten `bsp` und `\beispiel`.
- Nicht mehr benutzte Farben und Makros des Fenster-Nachbaus sind entfernt.

**Seiten:**

| Seite | Inhalt |
|---|---|
| 1 | Deckblatt, unverändert bis auf „damit Sie … kombinieren“ |
| 2 | Fundament „Was eine Pending Order ist“: Market- und Pending-Kasten („Sofortige Order“ / „Vorab geplante Order“), Nullpunkt-Grafik (Text jetzt „ausgelöst wird“), Zuordnung in Sätzen, „Was eine Pending Order im Ablauf verändert“ (drei neutrale Punkte) |
| 3 | Die Limit-Typen: Buy Limit mit Lesehilfe in der Randspalte neben dem Chart |
| 4 | Die Limit-Typen: Sell Limit („Sell Limit ist das Gegenstück zu Buy Limit“) |
| 5 | Die Stop-Typen: Buy Stop |
| 6 | Die Stop-Typen: Sell Stop |
| 7 | Übersicht „Alle vier Ordertypen im Vergleich“: Chartreihe mit Unterzeilen, Tabelle, merk-Kasten „Drei Grundregeln“ |
| 8 | In der Plattform „Der Reiter New Pending Order“: Fenster und fünf Schritte in Sie-Form, Type-Menü mit Regelkästen |
| 9 | In der Plattform „Eine wartende Order löschen“: fünf Schritte (mobile Ansicht), „Zum Wortlaut der Rückfrage“ (close order), merk-Kasten „Der gesamte Ablauf“ |

**Prüfungen am Stand dieses Commits:**
- Build fehlerfrei, keine Overfull- oder Underfull-Warnungen, 9 Seiten.
- Keine Rasterbilder; alle Schriften eingebettet.
- Ziffern im Text: nur 1–5. Das sind die Schrittnummern im Fenster, der Seite 9 und das Deckblatt-Badge.
- Folgende Wörter kommen im eigenen Text nicht vor: Trigger, Marke, Ask, Bid, ausgeführt, sinnvoll, besser, Vorteil, lohnt, Spickzettel.
- „Stop-Loss“ (einmal) und „deine/dein“ (viermal) stehen nur im unveränderten Fenster-Nachbau `fenster-bl.pdf`: „Set Stop-Loss“, „deine Menge“, „dein Wert“, „dein Ziel“.
- Starthöhe: Kicker oben bei 20,3 mm laut pdftotext-bbox, auf allen Seiten gleich wie vorher.
- Ende des Inhalts auf den Seiten 3–6 bei ca. 263–272 mm.
- Bilder: `build/PO-Neu-Uebersicht.png` (60 dpi, 3 Spalten), `build/PO-Neu-BuyLimit.png` (110 dpi), `build/Pending-Orders-Guide_TEST.pdf`. Der Ordner `build/` ist ignoriert.

## Offen

1. **Seite 9:**
   - Die Schritte stehen im Blocksatz mit Trennungen („An-gaben“, „Bestä-tigung“). Lösung: die `enumerate` in `\flatter` setzen, am besten in einer Minipage von 140 mm.
   - Die Seite ist nur zu etwa 80 % gefüllt (Ende bei ca. 228 mm). Lösung: `itemsep` auf etwa 6 mm erhöhen.
2. **Seite 7 (Übersicht):** Die Seite endet bei ca. 191 mm, unten bleiben rund 85 mm leer. Großzügigere Abstände würden helfen: Lead→Charts 14 mm, Charts→Tabelle 18 mm, Tabellenzeilen 3,5 mm, Tabelle→merk 10 mm. Keine neuen Inhalte und keine Doppelung mit den Regelkästen auf Seite 8. Die Charts bleiben nebeneinander in einer Reihe (Nutzerwunsch).
3. **`build/PO-Neu-BuyLimit.png` ansehen** (wurde erzeugt, aber noch nicht geprüft):
   - Grundlinie des Randlabels „BEISPIEL“ gegen die erste Zeile im Kasten; der Ausgleich ist `\vspace{1.6pt}` im Makro `\beispiel`.
   - Lesbarkeit der Lesehilfe (`\fine` in der 33-mm-Spalte).
   - „TYPISCHER EINSATZ“ bricht zweizeilig um. Das ist in Ordnung oder `\labw` auf etwa 36 mm vergrößern.
4. **Fenster-Nachbau `fenster-bl.pdf`:** Er enthält weiterhin „deine Menge / dein Wert / dein Ziel“ (du-Form) und „Set Stop-Loss“. Die Datei durfte nicht angefasst werden; der Nutzer muss entscheiden. Eine Umstellung auf Sie bräuchte einen Neubau des Fensters (Inter-Glyphen „I/h/r“ fehlen im Subset).
5. Nach den Korrekturen erneut prüfen:
   - Build und Seitenzahl.
   - pdftotext: Ziffern, verbotene Wörter, du-Formen mit Wortgrenzen.
   - Overfull/Underfull im Log.
   - `pdfimages`, `pdffonts`.
   - Übersicht bei 60 dpi und Buy-Limit-Seite bei 110 dpi neu rendern und ansehen.
   - PDF nach `build/Pending-Orders-Guide_TEST.pdf` kopieren.
   - Commit und Push.
6. Notiz für `HANDOFF.md` an den Koordinator geben (nicht selbst eintragen):
   - Neue Seitenstruktur mit 9 Seiten.
   - Sie-Form, C1, neutral.
   - hyphenrules-Zeile entfernt.
   - Raster-Makros.
   - Lösch-Abschnitt auf Seite 9.
   - Offene Entscheidung zu du-Form und Stop-Loss im Fenster-Nachbau.

## Bekannte Probleme

- `scripts/build.sh pending-orders` baut auch `Pending-Orders-Guide_CoverTest.tex` mit. Das ist harmlos, die Ausgabe landet nur in `build/`.
- „Auslöser“ in der Tabelle auf Seite 7 stammt aus der CSV des Nutzers und wurde deshalb belassen. Es ist sinngemäß nah an „Trigger“; bei Bedarf in „Ausgelöst, wenn“ ändern.
- Deckblatt-Badge „4 Ordertypen. 1 klare Entscheidungslogik.“: Die Ziffern sind eine Vorgabe des Nutzers (siehe `HANDOFF.md` 2.3).

## Nächster konkreter Schritt

1. Punkt 1 (Seite 9 in Flattersatz, Abstände) und Punkt 2 (Abstände auf Seite 7) in der `.tex` umsetzen.
2. `scripts/build.sh pending-orders` ausführen.
3. Mit `pdftoppm -r 60` und `montage -tile 3x` die Datei `build/PO-Neu-Uebersicht.png` neu erzeugen und ansehen; dazu `build/PO-Neu-BuyLimit.png` ansehen.
4. Prüfungen nach Punkt 5 durchführen, dann committen und pushen.
