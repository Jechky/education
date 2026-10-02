# Plattform-Fakten aus dem DOM: Kursliste und Instrument-Info

Quelle: HTML-Ausschnitte, die der Nutzer am 02.10.2026 aus dem WebTrader kopiert hat (Desktop-Kursliste und mobile Ansicht „Quotes“). Persönliche Daten sind darin nicht enthalten. Kurse und Werte sind nur Momentaufnahmen und gehören nicht ins Dokument.

## Desktop: Kursliste
- Container `.quote-list` mit einem Akkordeon (`ngb-accordion`). Die Kategorien sind Schaltflächen `button.quotes-ttl`, in dieser Reihenfolge:
  **Forex, Stocks, Cryptos, Indices, Energies, Metals, Commodities, ETFs**.
- Eine aufgeklappte Kategorie zeigt `ul > li > a`. Jede Zeile enthält:
  1. `span.fav`: Stern (`i.icon-star`, Favorit)
  2. `span.image`: Bild des Instruments (`assets/images/instruments/<SYMBOL>.png`)
  3. `span.arrow` / `.arrow.up` / `.arrow.down`: Richtungspfeil
  4. `span.symbol`: Name, z. B. Copper, Gold, Palladium, Platinum, Silver
  5. `span.bid` und `span.ask`: Kurse, eingefärbt mit `color00`, `color-green-main` oder `color-red-main`
  6. `span.info > i.icon-information`: **Info-Zeichen**, öffnet die Angaben zum Instrument
- Wie das Fenster aussieht, das sich nach Klick auf das Info-Zeichen öffnet, ist noch nicht übermittelt.

## Mobil: Quotes
- Untere Navigation (`mobile-navigation .navigation-tabs`): **Quotes** (`icon-monetary-statement`), **chart** (`icon-chart-type04`), **Orders** (`icon-orders`), **My Account** (`icon-account`).
- Unter Quotes stehen Reiter (`.custom-tabs`): **Fav, Forex, Stocks, Cryptos, Indices, Energies, Metals, Commodities, ETFs**.
- Darunter folgen ein Suchfeld (Platzhalter „Search“) und die Kopfzeile **Instrument | Bid | Ask**.
- Liste `.mb-quote-list` (Akkordeon): Jede Zeile enthält Stern, Bild, Pfeil, Name, Bid, Ask und den Aufklapp-Pfeil (`icon-arrow-down`).
- **Antippen eines Instruments klappt seine Angaben auf** (`.accordion-body`, Raster mit 3 Spalten). Die Felder mit dem Titel (`span.ttl`) in dieser Reihenfolge:
  **Symbol, Swap long, Swap short, Type, Spread, Gap Level, Digits, Stop Level, Commission, Contract size, Leverage**
  - Beispiel Gold: Swap long −85, Swap short −65, Type Metals, Spread 175, Commission 0, Contract size 100, Leverage 1 : 100.
  - Die Einheit der Swap-Werte wird nicht angezeigt (vermutlich Punkte, nicht belegt).
  - Commission steht mit dem Wert 0 da. Das passt zur Angabe des Nutzers, dass es keine Commission gibt.
- Darunter ein Raster mit 2 Spalten und vier Schaltflächen: **New order, New pending order, New chart, Trade Hours**.

## Desktop: Info-Fenster eines Instruments (nach Klick auf das Info-Zeichen)
- Es öffnet sich ein Overlay als Kontextmenü: `.cdk-overlay-pane.ngx-contextmenu` → `.ngx-contextmenu.quote-info-popup` → `symbol-info` → `.quote-info-frame`. Es schließt sich vermutlich, sobald woanders hingeklickt wird, also auch beim Klick in die Konsole.
- Kopf (`.heading`): Bild des Instruments und das **Symbol**, z. B. „XAUUSD“.
- Angaben (`.quote-info.grid.grid-col-2`, jeweils `dl > dt + dd`), in dieser Reihenfolge:
  **Symbol, Swap long, Type, Swap short, Spread, Digits, Commission, Leverage, Contract size**
  - Beispiel Gold: Swap long −85, Swap short −65, Type Metals, **Spread „Floating Points“** (mobil steht dort ein Wert), Commission 0, Leverage 1 : 100, Contract size 100.
- Darunter die Tabelle der Handelszeiten (`trading-hours`) mit den Spalten **Day of week | Open Time | Close Time**, Montag bis Sonntag, mehrere Zeitfenster je Tag. Die Zeitzone ist nicht angegeben.
- Rechts oben eine Schaltfläche zum Schließen (`a.close > i.icon-close`).

## Folgerungen für die Dokumente
- Die Plattform nennt Devisen **„Forex“**. Rohöl und Erdgas gehören vermutlich zur Kategorie **„Energies“**; nicht belegt, weil diese Kategorie im Ausschnitt nicht aufgeklappt ist.
- Weg zu Swap long, Swap short und Leverage eines Instruments:
  - Desktop: Info-Zeichen am Ende der Zeile in der Kursliste
  - mobil: Quotes → Kategorie → Instrument antippen
- Für Nachbauten fehlen noch Maße, Farben und Schriften. Messbefehl siehe Chat bzw. HANDOFF 7.1, mit angepassten Selektoren.
