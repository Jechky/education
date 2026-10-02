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
