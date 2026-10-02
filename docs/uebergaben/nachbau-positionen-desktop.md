# Übergabe: nachbau-positionen-desktop
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Commit: „Nachbau: Tabelle der offenen Positionen am Desktop“

## Ergebnis (erledigt)
- `dokumente/kontogrundlagen-kosten/positionen-desktop.tex` → `positionen-desktop.pdf` (standalone, reproduzierbar, md5 bei zwei Läufen gleich). Nur Inter Regular/SemiBold eingebettet, keine Rasterbilder, Log ohne Warnungen. Vorschau (nicht eingecheckt): `build/agent-pd/positionen-desktop.png` (200 dpi). Ohne Marken: `xelatex -jobname=… '\def\ohnemarken{}\input{positionen-desktop.tex}'`.

## Für HANDOFF.md
- Messung `originals/messungen/positionen-desktop.json` (Block 1704 × 271, `#04273C`, Radius 7 px). Gezeigt als **Ausschnitt** 956,2 × 145 px: links Instrument, Type, Amount, Trade Volume; Zickzack-Bruchkante (Lücke 10 px, Fläche frei) über die volle Höhe; rechts Swap, Commission, Total Profit, Margin; Reiter Active/Pending/History oben rechts; 2 Zeilen. Spaltenabstände innerhalb der Teile wie gemessen.
- Bei `width=170mm`: 1 px = 0,178 mm, 170 × 25,8 mm, Schrift 12 px = 6,05 pt, Marken 3,0 mm.
- Köpfe Inter 400 `#A8BBBE` am gemessenen span-x; „Trade volume“ wird per capitalize als **„Trade Volume“** angezeigt (Breite 78,4 px bestätigt). Zeilen: Fläche rgba(14,80,114,.1) unter 1,6 px Rand, Grundlinien 95,0 / 124,6 (belegt durch €-span und Bildmitte), Kopf 65,4.
- Platzhalter: Instrument „Instrument“, Type „Buy“ (gemessen), Amount „Menge“, Trade Volume „Wert“, Swap „Betrag“, Commission „—“, Total Profit „Ergebnis“ (grün `#53BC51` / rot `#F94056`), Margin „Betrag“; ohne „€“ (wie `bar.tex`). Reiter ohne Zähler, Breite wie im Browser (16 + Text + 16 px), rechtsbündig am Tabellenrand.
- Marken (Stil `info-desktop.tex`, 17 px) 3 px vor dem Spaltennamen: 1 Swap, 2 Total Profit, 3 Margin.
- Weggelassen: Bild- und ID-Spalte, Open Rate, Open Time, S/L, T/P, Zahnrad- und Schließen-Spalte (Zeilenenden wieder Radius 3 px, unten Schnitt bei y145 mit Radius 7 px), Leiste New order/Search/All sides/All profits (läge außerhalb), Griff `a.hide`, Instrument-Bild und Pfeil-PNG (Fläche leer).

## Offen
1. Nicht gemessen: vertikale Ausrichtung des Reiter-Texts (mittig angenommen) und Sortierpfeile der Köpfe (padding-right 15 px; nicht gezeichnet). Konsolenbefehl am Desktop bei sichtbarer Tabelle (Reiter Active):
   `(()=>{const q=s=>document.querySelector('.maintable '+s),p=(e,w)=>{const c=getComputedStyle(e,w);return [c.content,c.fontFamily,c.fontSize,c.color].join('|')};return JSON.stringify({align:getComputedStyle(q('.nav-tabs .nav-link')).alignItems,thA:p(q('th.sort-control'),'::after'),thB:p(q('th.sort-control'),'::before'),spA:p(q('th.sort-control span'),'::after'),spB:p(q('th.sort-control span'),'::before')})})()`
2. Einbau ins Dokument – nicht Teil dieser Aufgabe.

## Vollständige Fassung (Aufgabe nachbau-positionen-voll, 02.10.2026)
- `dokumente/kontogrundlagen-kosten/positionen-desktop-voll.tex` → `positionen-desktop-voll.pdf` (standalone, reproduzierbar, md5 bei zwei Läufen gleich). Nur Inter Regular/SemiBold eingebettet, keine Rasterbilder, Log ohne Warnungen, Text ohne Ziffern außer den Marken 1–3. Vorschau (nicht eingecheckt): `build/agent-pv/positionen-desktop-voll.png` (150 dpi bei 257 mm Breite). Ohne Marken: `xelatex -jobname=… '\def\ohnemarken{}\input{positionen-desktop-voll.tex}'`.
- Für eine **Querformat-Seite** (Satzbreite 257 mm), **ohne Bruchkante**. Block 1484 × 145 px = 1704 − 70 (Bildspalte) − 150 (Zahnrad- und Schließen-Spalte); alle Spalten ab ID um −70 px verschoben, gemessene Abstände unverändert; Zeilen außen wieder Radius 3 px; unten Schnitt bei y145 wie im Ausschnitt (leere Fläche bis y271 entfällt).
- Bei `width=257mm`: 1 px = 0,173 mm, 257 × 25,1 mm, Schrift 12 px = **5,9 pt**, Marken 2,9 mm.
- Gezeigt: Leiste **New order** (Rand 0,8 px grün, Inter 600) / **Search** / **All sides** / **All profits** an ihrer gemessenen Stelle oben links; Reiter **Active / Pending / History** ohne Zähler, bündig rechts; Spalten **ID, Instrument, Type, Amount, Trade Volume, Open Rate, Open Time, S/L, T/P, Swap, Commission, Total Profit, Margin**; 2 Zeilen.
- Platzhalter wie im Ausschnitt, neu: ID „Nummer“, Open Rate „Kurs“, Open Time „Zeitpunkt“, S/L und T/P „—“. Marken 1 Swap, 2 Total Profit, 3 Margin (`\ohnemarken`).
- Textbreiten im Log (`POSITIONEN-VOLL`) stimmen mit allen gemessenen Werten auf 0,1 px überein (auch ID, Open Rate, Open Time, S/L, T/P, All sides, All profits). „New order“: Textende 97,7 aus der Zentrierung abgeleitet (Plus bei x22,3, Inhalt mittig um x60); Abstand Plus–Text ergibt 3,1 px (≈ Leerzeichen Inter 600).
- Icons: Plus (U+E91A) und Lupe (U+E915) fehlen in `icons.tikz` → Fläche leer; sie werden automatisch gezeichnet, sobald `\iconplus` bzw. `\iconsearch` existieren (Einträge in `tools/icons_aus_font.py`; Makro `\icon` mit Ersatz-Glyphe getestet). Weggelassen wie im Ausschnitt: Griff `a.hide` (Icon U+E90E fehlt), Instrument-Bild, Pfeil-PNG, Sortierpfeile.

### Offen (vollständige Fassung)
1. **Nicht gemessen, vorläufig:** Farbe des Platzhalters „Search“ (gezeichnet in `#A8BBBE` wie Köpfe und Lupe, eine Zeile `\definecolor{suchtext}`) und der Auswahlpfeil von All sides / All profits (nicht gezeichnet). Konsolenbefehl am **Desktop**, WebTrader geöffnet, Tabelle unten aufgeklappt und sichtbar, Reiter **Active** angeklickt, Suchfeld **leer** und nicht angeklickt:
   `(()=>{const m=document.querySelector('.maintable'),b=m.getBoundingClientRect(),r=e=>{const q=e.getBoundingClientRect();return [q.x-b.x,q.y-b.y,q.width,q.height].map(v=>Math.round(v*10)/10).join(',')},i=m.querySelector('input.form-control'),p=getComputedStyle(i,'::placeholder');return JSON.stringify({ph:[i.placeholder,p.color,p.opacity,p.fontWeight,p.fontSize].join('|'),pfeile:[...m.querySelectorAll('.ng-arrow-wrapper,.ng-arrow')].map(e=>{const c=getComputedStyle(e);return [e.className,r(e),c.borderTopColor,c.borderTopWidth,c.borderLeftWidth,c.borderRightWidth,c.color].join('|')})})})()`
2. Einbau ins Dokument (Querformat-Seite) – nicht Teil dieser Aufgabe.
