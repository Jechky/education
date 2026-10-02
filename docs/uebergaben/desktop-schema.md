# Übergabe: desktop-schema
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Ergebnis im Commit „Grafik: Desktop-Bildschirm als Lehrbuch-Schema …“

## Erledigt
- `dokumente/kontogrundlagen-kosten/desktop-schema.tex` → `desktop-schema.pdf` (standalone, TikZ, 170 × 82,4 mm, IBM Plex Sans Regular/SemiBold eingebettet, keine Rasterbilder, keine Ziffern, Log ohne Warnungen, Build reproduzierbar).
- Schema statt Nachbau: weiße Bereiche, Teilungslinien `greya`, Details `rule`, Kopfleiste und unterste Leiste `paper`, Kurslinie `pfgrey`, SELL/BUY in `selltint`/`sell` bzw. `buytint`/`buy` (Rollen HANDOFF 13.1).
- Bereiche (fett, `ink`): **Kursliste** (Reiter All Quotes/Favorite, acht Kategorien, Metals aufgeklappt mit Platzhalter-Zeilen und „i“, Hinweis „Info-Zeichen“), **Chart** (SELL, BUY), **Tabelle der Positionen** (Reiter Active/Pending/History; Spalten Instrument, Type, Amount, Swap, Total Profit, Margin – ohne S/L, T/P), **Unterste Leiste** (Balance … Credit, ohne Werte). Kopfleiste nur als Fläche.
- Proportionen nach dem Screenshot des Nutzers (2000 × 969 px, 1 px = 0,085 mm; nicht im Repo); unterste Leiste etwas höher (52 statt 40 px).
- Kennbuchstaben A–D (Kreise wie `\cn`) per Schalter, Standard aus: `xelatex '\def\mitkennung{}\input{desktop-schema.tex}'`.

## Offen
1. Noch nicht in `Kontogrundlagen-Kosten.tex` eingebunden (Vorschlag: `\includegraphics[width=170mm]{desktop-schema.pdf}`, S. 7 „In der Plattform“).
2. Ob die Seite eine Legende A–D bekommt, entscheidet der Nutzer.

## Für HANDOFF.md
Abschnitt 9 „Bereits im Repo“: `desktop-schema.tex/.pdf` (Lehrbuch-Schema des Desktop-Bildschirms, 170 × 82,4 mm). Abschnitt 13.3: neue Grafik im Lehrbuch-Stil, Farbrollen wie oben. Bezeichnungen: „Kursliste“, „Chart“, „Tabelle der Positionen“, „Unterste Leiste“.
