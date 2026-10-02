# Übergabe: po-design-akademie
Stand: 2026-10-02 · Branch: claude/amazing-allen-xngika · letzter Commit: siehe `git log -1`

## Ziel
Pending-Orders-Guide rein gestalterisch als „Akademie-Blatt“ neu gesetzt (Serif-Fließtext,
Sans-Titel, Kopf-/Fußzeile, schlichte Kästen, booktabs-Tabellen, Bildunterschriften, weißes
Deckblatt). Texte unverändert. Erreicht: 9 Seiten, keine Overfull/Underfull, nur Vektor.

## Vorgaben
- Nur Gestaltung; kein Wort des Fließtexts ändern. Keine Seitenzahlen. Nachbauten in Inter.
- `Pending-Orders-Guide_CoverTest.tex`, `cover*` und `dokumente/kontogrundlagen-kosten/` unberührt.

## Erledigt
- Stildatei `dokumente/stil/akademie.sty` (Einbindung `\usepackage{../stil/akademie}`) – Commit `8b724c7`
- Schriften `fonts/SourceSerif4-{Regular,It,Semibold,SemiboldIt}.otf`,
  `fonts/SourceSans3-{Regular,It,Semibold,SemiboldIt,Light}.otf`, `fonts/LICENSE-Source-OFL.txt`
- Guide `dokumente/pending-orders/Pending-Orders-Guide.tex` komplett auf die Stildatei umgestellt;
  `cover-bg.pdf` wird nicht mehr eingebunden (Deckblatt weiß, Charts bleiben).
- Feinabstimmung (Abstände Chartzeile) – Folgecommit.

## Für HANDOFF.md (Abschnitt 3 ergänzen)
- Schriften: **Source Serif 4** Fließtext/Lead (9,8/14 pt, Lead 11,5/17), **Source Sans 3**
  Titel (`\hone` 20 pt), Zwischentitel (`\hthree` 11,5 pt), Labels/Kicker (`\htwo` 7,5 pt + `\ls`,
  Versalien), Tabellen (`\aktabelle` 9 pt), Grafik-Beschriftungen (`\lbl`, `\pflab`), Kopf/Fuß.
  IBM Plex nur noch im CoverTest; Nachbauten Inter.
- Seite: Ränder 22 mm seitlich, oben 29 mm, unten 22 mm; Grundlinie `\akbase` = 14 pt,
  Abstände `\akv{n}` = n/2 Grundlinien.
- Kopfzeile: `\akdokument{Titel}` links, `\kapitel{Abschnitt}` rechts (je Seite am Anfang setzen),
  Haarlinie; Fußzeile `\akfusstext` = „EDUCATION · STANDARD TIER“; Deckblatt
  `\thispagestyle{akdeckblatt}` mit `\akreihe{Trading-Grundlagen}` links.
- Makros: `\Hone`, `\Htwo`, `\lead`, `\hr`, `\mlab`/`\hd`, `\ztitel`, `\abb{…}` (Bildunterschrift
  „Abbildung: …“), `\cn{n}` Schrittmarke, `\abschnitt{Label}{Text}`, `\chartzeile`, `\beispiel`.
- Kästen: `merk`/`hinweis` (Label „MERKE“/„HINWEIS“, Linie oben dunkel, unten hell),
  `akkarte` + `\kartenkopf{Label}{Titel}`, `bsp` (Haarlinien). Keine Farbflächen, keine Pillen.
- Tabellen: `\aktoprule` … `\midrule` … `\akbottomrule`, Zeilen-Haarlinie `\akhaar`,
  Ziffern `\aktab`; `\arraystretch` je Tabelle (1,7–1,9).
- `\XeTeXgenerateactualtext=1` in der Stildatei: Bindestriche der Source-Schriften sonst als
  U+2011 extrahiert (Suche/Kopieren).
- Kontogrundlagen: gleiche Stildatei einbinden, eigene Farb-/Schriftdefinitionen entfernen,
  Breiten auf 166 mm Satzspiegel prüfen; Warnung „You have requested package ../stil/akademie“ ist harmlos.

## Offen
1. Kontogrundlagen auf `akademie.sty` umstellen (zweiter Schritt, eigener Auftrag).
2. Nutzerentscheid: Deckblatt-Kicker „TRADING-GRUNDLAGEN“ (Text beibehalten) statt „EDUCATION · STANDARD TIER“.

## Nächster Schritt
`dokumente/kontogrundlagen-kosten/*.tex`: Präambel durch `\usepackage{../stil/akademie}` ersetzen, bauen, Breiten prüfen.

## Prüfkommandos
    scripts/build.sh pending-orders
    grep -nE '^!|Overfull|Underfull' build/Pending-Orders-Guide.log
    pdffonts build/Pending-Orders-Guide.pdf
