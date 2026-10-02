# Übergabe: kg-hebel-swap-feinschliff
Stand: 02.10.2026 · Branch: claude/amazing-allen-xngika · Basis `5f9d129`, Ergebnis im Commit „Kontogrundlagen: Feinschliff Hebel und Swap …“

## Ziel (erledigt)
Kontogrundlagen S. 5 (Hebel) und S. 6 (Swaps) nach den Punkten 1–14 des Koordinators; dazu S. 3 (Balance-Kasten) und, nach Nutzervorgaben während der Arbeit, S. 2 (Bonus statt Commission) sowie Hinweise „Beträge fiktiv“ auf S. 5 und S. 6. Weiterhin 8 Seiten.

## Erledigt
- S. 5: je 2.000 € verfügbar; Tabelle „Öffnen“: Einsatz bzw. Margin 1.000 € | 1.000 €, Geliehener Betrag (Volumen minus Margin), neue Zeile „Auf dem Konto frei verfügbar (Free)“ – | 1.000 €. „vor/nach Swap“ statt „vor Kosten“. Letzte Zeile „Ergebnis vor Swap, gemessen an Einsatz bzw. Margin“. Swap-Zelle „Swap: 7 € pro Nacht (S. 6)“ statt Zusatzzeile. Schluss: „Fiele der Kurs um 10 %, entspräche Ihr Verlust bereits der Margin von 1.000 €. Fällt der Kurs weiter, schließt die Plattform die Position spätestens am Stop out.“ Kasten „Auswirkung auf die Margin“; Merk: „Der Hebel eines Instruments kann niedriger sein als der Hebel Ihres Kontos; …“. Unter „Schließen“: „Alle Beträge sind fiktiv und dienen ausschließlich der Veranschaulichung.“ (`\micro`, `soft`).
- S. 6: „Angenommen, Sie halten eine Position im Rohstoff Crude Oil (Rohöl) mit einem Volumen von 10.000 €.“ (XY nicht mehr = Crude Oil); Klammer „Betrag des Brokers: 1 €“; Hinweis „Die Beträge sind fiktiv …“ unter der Formel; „Natural Gas (Erdgas)“, „Devisen (Währungen, z. B. EUR/USD)“; Swap-Sätze: „In der Regel sind beide negativ, was eine Belastung bedeutet; ist ein Satz positiv, wird Ihnen der Betrag gutgeschrieben.“ (keine Einheit); Wochen-Notiz „am Mittwoch wird der Swap für das Wochenende mitgebucht“; Merk: Swap bei der offenen Position verbucht, im Profit enthalten, beim Schließen in die Balance.
- S. 3: „Der Swap einer Position geht beim Schließen mit ihrem Ergebnis in die Balance ein.“ (Commission entfernt).
- S. 2: „Commission (Provision)“ ersetzt durch „Bonus: Ein Betrag auf Ihrem Konto, mit dem Sie handeln können. Gewinne, die Sie damit erzielen, sind gemäß den AGB des Brokers auszahlbar. → S. 7“.
- Prüfung: 8 Seiten (Rest S. 5 ca. 2 pt, S. 6 ca. 1 pt), kein Over-/Underfull, nur die bekannte hyperref-Warnung, 10 Schriften eingebettet, 0 Rasterbilder; S. 1, 4, 7, 8 pixelgleich (60 dpi), S. 2 nur Bonus-Zeile, S. 3 nur Balance-Kasten.

## Offen
1. **Commission auf S. 7** (Nutzer: gibt es auf der Plattform nicht): `Kontogrundlagen-Kosten.tex` Z. 573, Desktop-Kasten „einschließlich der Spalten Swap und Commission“. S. 8: keine Fundstelle.
2. **S. 7, Z. 560 f.:** „Die Felder Bonus und Credit sind für den regulären Handel ohne Bedeutung.“ widerspricht der neuen Bonus-Erklärung auf S. 2.
3. S. 8: Swap = „Kosten“ (Widerspruch 3), Leverage „Volumen zu Margin“ (A8), Stop out (A7); Fußzeile/Seitenzahlen.
4. Fundliste: erledigt jetzt zusätzlich A9, A10, A11, A13, Widerspruch 2; A7 auf S. 5 erledigt (S. 8 offen). Weiter offen: A3 (Wertpapierdepot nur S. 2), A14, A15 (S. 7), B-Bilder Prio 1–5.
5. Kommentar `mobil.tex` nennt „Seite 6“; „Volume“ im Order-Fenster = Menge (aus `kg-grundbegriffe`).

## Für HANDOFF.md
Abschnitt 14: Zahlen um 2.000 € erweitert (1.000 € Free); Tabelle „Öffnen“ und Schlusssatz wie oben; Begriffe „Margin“ (Sie) / „Einsatz“ (Bekannter), „vor/nach Swap“; Hinweis „fiktiv“. Abschnitt 5.3 (Swaps): Crude Oil ist eine eigene Position, nicht Instrument XY; zweite Klammer „Betrag des Brokers: 1 €“; Hinweis „fiktiv“. Abschnitt 5/2.2: keine Commission auf der Plattform, dafür Bonus (Nutzer 02.10.2026).

## Prüfkommandos
    cd dokumente/kontogrundlagen-kosten && xelatex -interaction=nonstopmode -halt-on-error -output-directory=../../build/agent-hs Kontogrundlagen-Kosten.tex
    grep -n -i 'commission\|provision' dokumente/kontogrundlagen-kosten/Kontogrundlagen-Kosten.tex
