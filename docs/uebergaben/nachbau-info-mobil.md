# Übergabe: nachbau-info-mobil
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Ergebnis im Commit „Nachbau: Angaben eines Instruments mobil …“

## Erledigt
- `dokumente/kontogrundlagen-kosten/info-mobil.tex` → `info-mobil.pdf` (standalone, TikZ, Inter Regular/SemiBold eingebettet, keine Rasterbilder, reproduzierbar). Block 410 × 327,2 px (307,5 × 245,4 pt); bei 80 mm Breite 63,8 mm hoch, 1 px = 0,195 mm, Schrift 6,6 pt.
- Nach `originals/messungen/instrument-info-mobil.json`: Kopfzeile, Raster 3 × 4, vier Schaltflächen (Farben, Maße, 12 px/400 bzw. 600). XeTeX-Textbreiten der Schaltflächen 60,28 / 110,70 / 59,57 / 71,35 px (gemessen 60,3 / 110,7 / 59,6 / 71,4).
- Wörter statt Zahlen (wie `info-desktop.tex`): Satz long, Satz short, Wert (Spread, Gap Level, Stop Level), Stellen, „—“ (Commission), Größe, Hebel; Gold, Metals bleiben. Kopfzeile: „Kurs“ (grün) und „Kurs“ (weiß), kein Bid/Ask.
- Marken 1 Swap long, 2 Swap short, 3 Leverage: (Stil panel.pdf: weißer Kreis 22 px, Ziffer Inter 600 in #04273C), 25 px hinter dem Titel. Ohne Marken: `xelatex -jobname=info-mobil-ohne '\def\ohnemarken{}\input{info-mobil}'`.

## Weggelassen / angenommen
- Stern (`icon-star`, U+E916) und Aufklapp-Pfeil (`icon-arrow-down`, U+E910): nicht in `icons.tikz`, Plattform-Schrift nicht verfügbar. Nachholen: Font hochladen, `tools/icons_aus_font.py` um die zwei Glyphen erweitern.
- Instrument-Bild (PNG): Fläche leer.
- Seitenhintergrund nicht gemessen → wie `mobil.tex` #04273C; Kopfzeile damit rgb(5,43,65). Rahmen der Schaltflächen 0,8 px ohne Farbe in der Messung → als volle Fläche gezeichnet.
- Prüfbefehl für den Nutzer (mobile Ansicht, Quotes → Metals, Gold aufgeklappt; dann Konsole):
  `(()=>{const i=document.querySelector('.mb-quote-list .accordion-body')?.closest('.accordion-item');if(!i)return'Gold nicht aufgeklappt';let e=i.parentElement,r=[];while(e){const c=getComputedStyle(e).backgroundColor;r.push(e.tagName+'.'+[...e.classList].join('.')+' '+c);if(c.startsWith('rgb('))break;e=e.parentElement}i.querySelectorAll('a.button').forEach(a=>{const s=getComputedStyle(a);r.push(a.textContent.trim()+': '+s.borderTopStyle+' '+s.borderTopColor+' '+s.backgroundClip)});return r.join('\n')})()`

## Offen
- Nicht in `scripts/build.sh` eingetragen und nicht im Dokument eingebunden (`Kontogrundlagen-Kosten.tex` nicht angefasst).

## Für HANDOFF.md
Abschnitt 12/9: neue Datei `info-mobil.tex/.pdf` (mobile Angaben eines Instruments, Gold, 410 × 327,2 px, Marken 1–3 abschaltbar, Wörter wie oben); Stern/Pfeil/Bild fehlen (Font bzw. Raster); Seitenhintergrund und Rahmenfarbe der Schaltflächen per Prüfbefehl bestätigen. Abschnitt 3.3: neue Plattform-Farben `#F94056` (New pending order), `#062F47` (Trade Hours), `#5B6A82` (Stern, inaktiv).
