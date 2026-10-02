# Übergabe: kg-plattform-uebersicht
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Basis `e70e62e`, Ergebnis im Commit „Kontogrundlagen: Plattform-Seite, Übersicht, Seitenzahlen …“

## Ziel (erledigt)
Kontogrundlagen S. 7 (In der Plattform) und S. 8 (Übersicht) nach den Punkten 1–12 des Koordinators, Seitenzahlen in der Fußzeile, Endprüfung aller 8 Seiten; im Pending-Orders-Guide nur `pdftitle`.

## Erledigt
- S. 7: Lead um „In beiden Abbildungen stehen anstelle der Beträge Wörter, die den jeweiligen Wert umschreiben.“ ergänzt (Wörter in den Nachbauten unverändert). Notiz rechts: „Ganz oben steht die Balance, am Ende folgen die Felder Bonus und Credit. Der Bonus ist ein Betrag, mit dem Sie handeln können; Gewinne, die Sie damit erzielen, sind gemäß den AGB des Brokers auszahlbar.“ (Credit nur genannt). Desktop-Kasten: nur „Spalte Swap“; „Chart (der grafischen Darstellung des Kursverlaufs)“; „Kursliste, der Liste der Instrumente mit ihren aktuellen Kursen“. Mobile-Kasten: „Unter Orders → Active steht die Liste Ihrer offenen Positionen; …“ (Pfeil mit `~` gebunden).
- S. 8: neue Zeilen Stop out („Schwelle des Levels, an der die Plattform Positionen selbstständig schließt“ | „Fest je Konto“) und Bonus („Betrag, mit dem Sie handeln können; Gewinne daraus sind gemäß den AGB auszahlbar“ | „Nach den AGB des Brokers“); Leverage „Verhältnis von Margin zu Volumen; bei 1:10 beträgt die Margin ein Zehntel des Volumens“; Swap „Belastung oder Gutschrift für das Halten über Nacht; bei der Position verbucht, beim Schließen in der Balance“.
- Fußzeile rechts `\thepage~/~\pageref*{s:ende}` („3 / 8“), `\micro`, `soft`, `\ls`; Label `s:ende` hinter dem letzten Merk-Kasten; S. 1 ohne (`\thispagestyle{empty}`).
- Endprüfung: S. 2 Broker „Anders als beim Direktkauf erwerben …“ („über die Bank“ gestrichen; „Bank“ jetzt nur S. 5). `pdftitle` mit `\&` (Titel zeigte „Kontogrundlagen  Kosten“; die hyperref-Warnung ist damit weg). Guide: `pdftitle={Pending Orders – Standard Tier}`.
- Prüfung: 8 Seiten (Rest S. 7 ca. 9 pt, S. 8 ca. 180 pt), Log ohne Warnungen, 10 Schriften eingebettet, 0 Rasterbilder; Guide 9 Seiten, 11 Schriften eingebettet. S. 1 pixelgleich, S. 3–6 nur Seitenzahl, S. 2 nur Broker-Zeile und Seitenzahl.

## Bitte beim Nutzer bestätigen
1. S. 8 Bonus, Spalte „Änderung“: „Nach den AGB des Brokers“ ist abgeleitet, nicht belegt (Alternative: Zeile streichen).
2. S. 8 Stop out „Fest je Konto“ (gestützt auf HANDOFF 5.3, #147: Wert je Konto verschieden).

## Noch offen (Fundliste `docs/pruefung/kontogrundlagen-begriffe-bilder.md`)
- Erledigt sind jetzt A1, A2, A4–A16 sowie Widersprüche 1–3 (A7, A8 auf S. 8, A14, A15 auf S. 7 in diesem Schritt).
- A3: „Wertpapierdepot“ (S. 5, Z. 357) ohne Erklärung.
- B Prio 1–5 (Positionsliste, Info-Fenster, Reiter Information, Warnmeldung, Desktop-Schema): keine Bilder, nicht gemessen.
- B einfach: Balance-Marke im mobilen Panel, Orders-Symbol markieren (Nachbauten, nicht angefasst).
- Sonstiges: Kommentar in `mobil.tex` nennt „Seite 6“; S. 5 Tabellenzeile „Kosten über Nacht“ (dort Belastung, also stimmig); `pdfsubject` nennt „Free Margin“ statt „Free“; „Volume“ im Order-Fenster = Menge.

## Für HANDOFF.md
~~Abschnitt 2.3: Seitenzahlen in Doku 2 wieder eingeführt (Fußzeile rechts „n / 8“, nicht auf S. 1), weil der Text auf Seiten verweist; #59 („Seitenzahlen entfernt“) damit überholt.~~ → überholt durch den Nachtrag unten. Abschnitt 5.3: S. 7/S. 8 wie oben; Bonus erklärt, Credit nur genannt; keine Commission. Abschnitt 4: Guide-`pdftitle` „Pending Orders – Standard Tier“.

**Nachtrag (Aufgabe kg-verweise-ohne-zahlen):** Abschnitt 2.3 gilt unverändert: **Seitenzahlen bleiben entfernt** (#58/#59), auch in Doku 2. Fußzeile wieder nur „KONTOGRUNDLAGEN & KOSTEN · EDUCATION – STANDARD PACKAGE“. Verweise nennen den **Seitentitel (Kicker)** statt einer Zahl: Makros `\titel{label}{Titel}` → „Titel“ (Fließtext, z. B. „(Abbildung unter „In der Plattform“)“, „mehr dazu unter „Margin““), `\verw{label}{Titel}` → „→ Titel“ (Spalte „Mehr dazu“ in den Grundbegriffen, 30 + 102 + 29,5 mm), `\pfeil` (S. 5: „Swap: 7 € pro Nacht (→ Swaps)“); jeweils unsichtbarer Link, Titel bricht nicht um. S. 8 Bonus, Spalte „Änderung“: „–“ (Angabe war nicht belegt; Punkt 1 oben damit erledigt). `pdfsubject`: „Free“ statt „Free Margin“.

## Prüfkommandos
    cd dokumente/kontogrundlagen-kosten && xelatex -interaction=nonstopmode -halt-on-error -output-directory=../../build/agent-pu Kontogrundlagen-Kosten.tex
    grep -n -i 'commission\|provision\|Bank' dokumente/kontogrundlagen-kosten/Kontogrundlagen-Kosten.tex
