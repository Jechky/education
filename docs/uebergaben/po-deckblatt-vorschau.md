# Übergabe: po-deckblatt-vorschau
Stand: 2026-10-02 · Branch: claude/amazing-allen-xngika · Basis-Commit: 8b7d82e

## Ziel
Vorschau für das SVG-Deckblatt der Testvariante (`Pending-Orders-Guide_CoverTest.tex`):
Charts bündig mit dem Text, verwaiste Mittellinie weg, Lücke um „KURS JETZT“ schmaler.
Der eigentliche Guide (`Pending-Orders-Guide.tex`) bleibt unverändert.

## Erledigt
- Charts: linke Kante des Chart-Inhalts liegt jetzt genau auf der Textkante
  (x = 20 mm bzw. 117,5 mm; gemessen 19,995 / 117,503 mm). Maßstab unverändert (72,5/174).
  – `Pending-Orders-Guide_CoverTest.tex` (nur `shift` der vier Chart-Scopes)
- Senkrechter Stummel `center-rule-top` (x = 105, y 98–111) unter dem Navy-Band entfernt.
  – `cover.svg`, `cover-bg.svg`, `cover-bg.pdf`
- Achse „Kurs jetzt“: Linie links bis 92,6 statt 87, rechts ab 117,4 statt 123 mm
  (Luft zum Schriftbild ca. 3,3 mm, wie im Haupt-Guide). Platzhalter `ph-axis-label`
  auf x = 95, Breite 20 angepasst. – `cover.svg`, `cover-bg.svg`, `cover-bg.pdf`
- Vorschau: `build/agent-deckblatt/deckblatt-vorher.png`, `…/deckblatt-nachher.png` (100 dpi).

## Offen
1. Rückfrage an den Nutzer: Sollen die Charts zusätzlich die volle Spaltenbreite füllen
   (rechte Kante auf 92,5 bzw. 190 mm, bündig mit Achsenende und Fußzeile)? Dann werden sie
   ca. 14–15 % größer; die unteren Charts kämen „günstiger kaufen“ bis auf ca. 2 mm nahe, die
   senkrechten Positionen müssten neu verteilt werden. Derzeit enden sie bei ca. 83 / 181 mm.
2. ~~Übernahme des Deckblatts in den Haupt-Guide (HANDOFF 16, Punkt c)~~ – erledigt
   (Nutzer: „Deckblatt ja, mach“), siehe Abschnitt „Übernahme“.

## Übernahme (Aufgabe po-deckblatt-uebernahme, 02.10.2026)
- `Pending-Orders-Guide.tex`: altes Deckblatt (Fließsatz mit Titellinie, Badge, 46-mm-Charts,
  Achse mit Mittellinie, Fußlinie) durch das SVG-Deckblatt der Testvariante ersetzt
  (`remember picture,overlay`, Hintergrund `cover-bg.pdf`, Inhalte absolut in mm; Charts
  72,5/174, bündig mit der Textkante, **nicht** auf volle Spaltenbreite vergrößert).
- Präambel: nur die vier Deckblatt-Farben `cvkicker`, `cvsub`, `cvpill`, `cvpilltext`
  ergänzt. Alle anderen Makros (`\display`, `\leadf`, `\micro`, `\lbl`, `\hthree`, `\ls`,
  `\chart..mini` aus `charts.tikz`) waren schon vorhanden. **Nicht** übernommen:
  `\babelprovide[hyphenrules=english]{ngerman}` und die Fenster-Farben/-Makros der Testvariante
  (betreffen nur deren alte Innenseiten).
- Text angepasst (Sie-Form, wie bisheriges Guide-Deckblatt): Untertitel „… damit du Einstieg,
  Auslösepreis und Richtung richtig kombinierst.“ → „… damit Sie Einstieg, Auslösepreis und
  Richtung richtig kombinieren.“ (Zeilenfall gleich). Alle übrigen Deckblatt-Texte waren in
  beiden Fassungen identisch (Badge, „Ausbruch nach oben/unten“ usw. bleiben offene Rückfragen
  laut HANDOFF 8.2).
- `Pending-Orders-Guide_CoverTest.tex`, `cover.svg`, `cover-bg.svg`, `cover-bg.pdf` unverändert.
- Prüfung: 9 Seiten, Log ohne Fehler/Overfull/Underfull, alle Schriften eingebettet (gleiche
  Schriftliste wie vorher), keine Rasterbilder. S. 1 bei 60 dpi gleich der Testvariante bis auf
  den Untertitel; S. 2–9 bei 60 dpi pixelgleich mit dem Stand vor der Übernahme.
  Vorschau (nicht eingecheckt): `build/agent-cover/deckblatt.png` (100 dpi).
- Build braucht wegen `remember picture` **zwei** XeLaTeX-Läufe (beim ersten Lauf steht der
  Inhalt falsch).

## Für HANDOFF.md
- Cover-Testvariante: `cover-bg.pdf` entsteht mit `rsvg-convert -f pdf -o cover-bg.pdf cover-bg.svg`
  (im Ordner `dokumente/pending-orders/`; Ergebnis byte-gleich bis auf die Datei-ID).
- Mittellinie des SVG-Layouts (`grid-connection`) ist vollständig entfernt.
- Achse „Kurs jetzt“ im Cover: Lücke 92,6–117,4 mm; Label-Schriftbild 96,0–114,1 mm.
- **Übernahme erledigt (02.10.2026):** Das SVG-Deckblatt ist S. 1 von `Pending-Orders-Guide.tex`
  (HANDOFF 16 Punkt c und Rückfrage 8.2 „Deckblatt übernehmen?“ erledigt; offen bleibt nur
  „Charts auf volle Spaltenbreite?“). Untertitel in Sie-Form; S. 2–9 unverändert. Der Guide
  benötigt jetzt `cover-bg.pdf` im Ordner und zwei XeLaTeX-Läufe. Die Testvariante bleibt als
  Referenz liegen (Innenseiten veraltet, Du-Form).
- Charts im Cover: linke Inhaltskante bündig mit der Textkante. Die Verschiebung nutzt die
  linke Inhaltskante aus `charts.tikz` (bs/sl: 11,373 px, bl/ss: 14 px); ändert sich
  `charts.tikz`, müssen diese Werte in der Testvariante und im Guide angepasst werden.

## Prüfkommandos
    cd dokumente/pending-orders && xelatex -interaction=nonstopmode -halt-on-error \
      -output-directory=../../build/agent-deckblatt Pending-Orders-Guide_CoverTest.tex
    pdffonts -f 1 -l 1 build/agent-deckblatt/Pending-Orders-Guide_CoverTest.pdf
