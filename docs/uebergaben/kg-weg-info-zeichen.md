# Übergabe: kg-weg-info-zeichen
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Ergebnis im Commit „Kontogrundlagen: Querformat-Seiten …“

## Erledigt (`Kontogrundlagen-Kosten.tex`, jetzt 10 Seiten)
- Stand des abgebrochenen Vorgängers übernommen und fertiggestellt (Pfeil kräftiger, Mess-`\message` entfernt, Variante reproduzierbar neu gebaut).
- Makros `\querformat` / `\hochformat` (Präambel): echte Seite 297 × 210 mm ohne `/Rotate`, Ränder und Fußzeile wie im Hochformat, Satz 257 × 173 mm. `\querformat` setzt das Papier über `\Gm@restore@org` (geometry-intern), da `\newgeometry` sonst A4 hoch wiederherstellt.
- S. 7 „In der Plattform“: Lead gekürzt, Kästen DESKTOP/MOBILE entfallen (Inhalt jetzt auf S. 8/9), `desktop-schema.pdf` (170 mm) über `bar.pdf`, Schlusszeile verweist per Titel auf beide neuen Seiten. Rest ca. 8,7 pt.
- S. 8 „Angaben eines Instruments“ (quer, Label `s:instrumente`): Maßstab 1 px = 0,21 mm (Schrift 7,1 pt). Links Ausschnitt `kursliste-desktop-ohne.pdf` (Energies bis Commodities) mit weißem Ring um das Info-Zeichen der Zeile Gold, Pfeil (1,2 pt) „Klick auf das Info-Zeichen (i)“ zu `info-desktop.pdf` (Schatten ganz innerhalb des Satzes); rechts `info-mobil.pdf` mit weißem Rahmen um die Kopfzeile, Weg „Quotes → Metals → Gold antippen“. Darunter Legende 1 Swap long, 2 Swap short, 3 Leverage in einer Zeile.
- S. 9 „Offene Positionen“ (quer, Label `s:positionen`): DESKTOP/MOBILE-Wege, `positionen-desktop-voll.pdf` in voller Breite (Makro `\positionstabelle`), Tabelle Amount, Trade Volume, 1 Swap, 2 Total Profit, 3 Margin mit Verweisen.
- Verweise S. 2, 5, 6 lauten jetzt „Angaben eines Instruments“. S. 10 „Auf einen Blick“ bleibt letzte Seite.
- Prüfung: Log sauber, alle Schriften eingebettet, 0 Rasterbilder, Ziffern nur Marken und 1:10; S. 1, 3, 4, 10 pixelgleich zu HEAD (alte S. 9), S. 2/5/6 nur Verweiszeilen.

## Variante (eingecheckt, `scripts/build.sh` baut sie nicht)
Im Ordner `dokumente/kontogrundlagen-kosten`:
`SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 xelatex -interaction=nonstopmode -halt-on-error -jobname=kursliste-desktop-ohne '\def\ohnemarken{}\input{kursliste-desktop}'` (md5 bei zwei Läufen gleich).

## Offen
1. `scripts/build.sh` kennt keine Varianten (`-jobname`/`\ohnemarken`); nach Änderung an `kursliste-desktop.tex` die Variante von Hand neu bauen.
2. `positionen-desktop-voll.pdf` zeigt die Spalten S/L und Commission (Original der Plattform); HANDOFF 2.2/2.3 verbieten beide Begriffe im Text. Wie bei `info-desktop`/`info-mobil` (Commission) beim Nutzer bestätigen.

## Für HANDOFF.md
Abschnitt 5.3: 10 Seiten; S. 7 mit Desktop-Schema, S. 8 „Angaben eines Instruments“ und S. 9 „Offene Positionen“ im Querformat (Makros `\querformat`/`\hochformat`), S. 10 „Auf einen Blick“. Abschnitt 2.3, Ausnahme 1: Marken 1–3 auf S. 8 und S. 9. Abschnitt 9: Variante `kursliste-desktop-ohne.pdf` (Befehl oben).
