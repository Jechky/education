# Plattform-Fakten aus dem DOM: Liste der offenen Positionen

Quelle: HTML-Ausschnitte, die der Nutzer am 02.10.2026 aus dem WebTrader kopiert hat (mobil: Orders, Desktop: Tabelle unten). Der Code enthielt echte Kontodaten (IDs, Beträge, Zeiten). Er ist deshalb **nicht** im Repo, hier steht nur der Aufbau.

## Mobil: Orders
- In der unteren Navigation ist **Orders** aktiv (`mobile-navigation`: Quotes, chart, Orders, My Account).
- Reiter (`mobile-orders ul.nav-tabs`): **Active (n)**, **Pending (n)**, **History**.
- Kopfzeile der Liste (`.mb-orders-head`): **Instr | Type | Amount | Total Profit**.
- Jede Zeile (`.mb-orders-list .accordion-item`) enthält:
  - Bild des Instruments und Symbol, z. B. BCHEUR,
  - Type (Buy/Sell) und Amount (Menge),
  - Total Profit mit €, grün (`color-green-main`) oder rot (`color-red-main`, mit „-“),
  - Aufklapp-Pfeil.
- **Antippen klappt die Angaben der Position auf** (Raster mit 3 Spalten, Titel `span.ttl`):
  **ID, Open Time, Open Rate, T/P, S/L, Commission, Swap, Trade volume, Margin**.
  Commission, Swap und Margin stehen mit €.
- Darunter zwei Schaltflächen: **Close ‹Kurs›** (grün) und **Modify Order**.

## Desktop: Tabelle unten (`maintable`)
- Reiter rechts: **Active (n)**, **Pending (n)**, **History**.
- Darüber: die Schaltfläche **New order**, das Suchfeld „Search“ und die Filter **All sides** und **All profits**.
- Spalten der Tabelle (`active-orders .table2 table`):
  (Bild) | **ID | Instrument | Type | Amount | Trade volume | Open Rate | Open Time | S/L | T/P | Swap | Commission | Total Profit | Margin** | (Zahnrad `icon-settings`) | (Schließen: Kurs + `icon-close`, grün „profit“ bzw. rot „loss“).
- Hinter dem Instrument steht ein kleiner Pfeil (`arrow-Buy.png`).

## Folgerungen für die Dokumente
- **Der Swap steht bei jeder offenen Position in der Spalte „Swap“**, am Desktop in der Tabelle, mobil in den aufgeklappten Angaben.
- **Total Profit enthält den Swap.** Beispiel aus dem Ausschnitt: Swap −0,05 € und Total Profit −0,10 €. Das bestätigt die Reverse-Engineering-Fassung (Abschnitt 7.3).
- Die Plattform nennt das Ergebnis einer Position **„Total Profit“**. In der Kontoleiste heißt die Summe „Profit/Losses“.
- **„Trade volume“ ist der Wert der Position**, entspricht also dem „Volumen“ im Dokument. **„Amount“ ist die Menge.** Damit ist der Prüfbefund Volume/Volumen geklärt: Im Order-Fenster ist „Volume“ die Menge.
- Pro Position werden **Margin** und **Commission** angezeigt. Die Commission steht bei null, was zur Angabe des Nutzers passt, dass es keine gibt.
- Die Spalten S/L und T/P gehören zum Plattform-Original. Das Dokument behandelt den Stop-Loss nicht.
