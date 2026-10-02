# Übergabe: nachbau-kursliste
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Commit: „Nachbau: Kursliste am Desktop (Metals aufgeklappt) als Vektor“

## Ergebnis (erledigt)
- `dokumente/kontogrundlagen-kosten/kursliste-desktop.tex` → `kursliste-desktop.pdf` (standalone, von `scripts/build.sh` automatisch mitgebaut; md5 bei zwei Läufen gleich). Nur Inter (Regular/Medium/SemiBold) eingebettet, keine Rasterbilder, Log ohne Warnungen. Vorschau (nicht eingecheckt): `build/agent-kl/kursliste-desktop.png` (200 dpi). Ohne Marken: `xelatex -jobname=kursliste-desktop-ohne '\def\ohnemarken{}\input{kursliste-desktop}'`.

## Für HANDOFF.md
- Messung `originals/messungen/kursliste-desktop.json`: Block 304 × 410 px, Fläche `#04273C`. Kategorien `button.quotes-ttl` 304 × 28, Abstand 32 px, Inter **500** 12/14 px weiß, Text bündig links (padding-left 0). Zeilen 304 × 30, Abstand 32 px, Radius 3 px, `rgba(14,80,114,.1)` → `rgb(5,43,65)`; Name x 73,6, Kurse x 145,2 / 210,9, Inter 400, 12/18 px; Grundlinie Textbox + 12 px (wie `bar.tex`).
- Kurse → „Kurs“ (Copper weiß `color00`, Gold/Palladium grün `rgb(83,188,81)`); Namen bleiben. Info-Zeichen = Glyphe `\iconinfo` aus `icons.tikz` (U+E93A, 14 px, `rgb(34,100,134)`), **kein Ersatz nötig**.
- Maßstab 1 px = 0,75 bp, PDF 228 × 307,5 bp. Bei `width=50mm`: 1 px = 0,164 mm, 50 × 67,4 mm, Schrift 5,6 pt.
- Marke 1 (Stil `panel.pdf`, Kreis 22 px) links neben dem Info-Zeichen der Zeile Gold, Schalter `\ifmarken`.
- Weggelassen: Stern (U+E916 fehlt in `icons.tikz`; wird automatisch gezeichnet, sobald `\iconstar` existiert: Eintrag `("iconstar", 0xE916, …)` in `tools/icons_aus_font.py`), Instrument-Bilder (PNG), Richtungspfeil `span.arrow` und Pfeil auf/ab der Kategorien (beide nicht gemessen).
- Lücke: zwischen Palladium (Unterkante 286) und Commodities (350) 64 px ohne Knoten in der Messung (vermutlich Platinum, Silver) – bleibt leer.

## Offen
1. Pfeile und Lücke messen. Vorher: WebTrader am Desktop, Kursliste sichtbar, **Metals aufgeklappt**; F12 → Console, einfügen, Enter (Ergebnis liegt in der Zwischenablage):
   `(()=>{const L=document.querySelector('.quote-list').getBoundingClientRect(),R=e=>{const b=e.getBoundingClientRect();return[+(b.x-L.x).toFixed(1),+(b.y-L.y).toFixed(1),+b.width.toFixed(1),+b.height.toFixed(1)]},P=(e,p)=>{const s=getComputedStyle(e,p);return{c:s.content,font:s.fontFamily,fs:s.fontSize,col:s.color,pos:s.position,r:s.right,t:s.top,w:s.width,h:s.height,tr:s.transform,bd:s.borderRight+'|'+s.borderBottom,bg:s.backgroundImage}};const o={knopf:[...document.querySelectorAll('.quote-list button.quotes-ttl')].slice(4,7).map(b=>({txt:b.textContent.trim(),box:R(b),after:P(b,'::after'),before:P(b,'::before'),kinder:[...b.querySelectorAll('*')].map(k=>[k.className,R(k),P(k,'::before')])})),zeilen:[...document.querySelectorAll('.quote-list li > a')].map(a=>({name:a.querySelector('.symbol')?.textContent.trim(),box:R(a),pfeil:[...a.querySelectorAll('.arrow')].map(p=>[p.className,R(p),P(p),P(p,'::before')])}))};copy(JSON.stringify(o));return o})()`
2. Einbau ins Dokument (`Kontogrundlagen-Kosten.tex`) – nicht Teil dieser Aufgabe.
