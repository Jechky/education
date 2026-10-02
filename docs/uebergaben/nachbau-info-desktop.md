# Übergabe: nachbau-info-desktop
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Commit: „Nachbau: Info-Fenster eines Instruments am Desktop“

## Ergebnis (erledigt)
- `dokumente/kontogrundlagen-kosten/info-desktop.tex` → `info-desktop.pdf` (standalone, wird von `scripts/build.sh` automatisch mitgebaut; reproduzierbar, md5 bei zwei Läufen gleich).
- Nur Inter (Light/Regular/SemiBold) eingebettet, keine Rasterbilder, Log ohne Warnungen. Vorschau (nicht eingecheckt): `build/agent-info/info-desktop.png` (200 dpi).
- Ohne Marken bauen: `xelatex -jobname=… '\def\ohnemarken{}\input{info-desktop.tex}'` (Schalter `\ifmarken`, Standard an).

## Für HANDOFF.md
- Messung `originals/messungen/instrument-info-desktop.json` (Fenster 2040 × 986, wie die Leiste). Fenster `#0E3D58`, Radius 5 px, kein Rand, Schatten `rgba(0,0,0,.25) 0 0 20px 4px` (als 24 Vektor-Ringe, Gauß σ 10 px); Kopf mit „XAUUSD“ (weiß, 400) und Trennlinie 0,8 px 10 % Weiß; Raster 2 × 130 px, Labels Inter **300** `#A8BBBE`, Werte Inter 400 weiß, 12 px / 14 px, Grundlinie Zeile + 11,2 px (wie `bar.tex`).
- Label-Breiten enthalten ein Leerzeichen („Symbol: “ = 48,64 px); XeTeX trifft alle gemessenen Breiten auf ≤ 0,05 px. Bei **Leverage** steht der Doppelpunkt nicht im Label, sondern weiß (400) dahinter.
- „Floating Points“ bricht wie auf der Plattform um (Zelle 83,4 px, Text 83,7 px).
- Maßstab: 1 Einheit = 1 CSS-px = 0,75 bp. PDF 338 × 242,8 px (Fenster 290 × 194,8 px + 24 px Schattenrand je Seite). Bei `width=60mm` für das ganze PDF: 1 px = 0,1775 mm, 60 × 43,1 mm, Fenster 51,5 × 34,6 mm, Schrift 6,0 pt. Soll das Fenster selbst 60 mm breit sein: PDF mit `width=69.93mm` einbinden (Schrift 7,0 pt).
- Platzhalter statt Zahlen: Swap long „Satz long“, Swap short „Satz short“, Digits „Stellen“, Commission „—“ (wie Bonus/Credit in `bar.tex`), Leverage „Hebel“, Contract size „Größe“. Unverändert: Symbol „Gold“, Type „Metals“, Spread „Floating Points“, Kopf „XAUUSD“.
- Marken 1 Swap long, 2 Swap short, 3 Leverage: Stil der Nummern in `panel.pdf` (weißer Kreis, Ziffer Inter SemiBold `#04273C`), maßstäblich 17 statt 22 px (Zeilenabstand nur 19 px); links vor dem Label in der leeren Hälfte von Spalte 1.
- Weggelassen: Instrument-Bild (PNG, kein Vektor; Fläche bleibt leer), Schließen-Zeichen (U+E91B fehlt in `icons.tikz`, Font nicht im Repo – die .tex zeichnet es automatisch, sobald `\iconclose` existiert: Eintrag `("iconclose", 0xE91B, …)` in `tools/icons_aus_font.py`, Font hochladen), Tabelle der Handelszeiten (Schnitt an ihrer Oberkante y 194,8, unten Radius 5 px).

## Offen
1. Nicht gemessen: ob das Leerzeichen bei Leverage hinter (angenommen) oder vor dem Doppelpunkt steht (Unterschied 3,4 px). Konsolenbefehl bei offenem Info-Fenster (Gold): `JSON.stringify([...document.querySelectorAll('.quote-info-popup dl')].map(d=>d.innerHTML))`
2. Einbau ins Dokument (`Kontogrundlagen-Kosten.tex`) – nicht Teil dieser Aufgabe.
