# Übergabe: Kontogrundlagen & Kosten – Hebel-Seite (S. 4)

Stand 02.10.2026. Branch `claude/continue-conversation-529rck`. Ausführlich: `HANDOFF.md` Abschnitt 14.

## Auftrag (in eigenen Worten)

Auf der Hebel-Seite (S. 4) von `dokumente/kontogrundlagen-kosten/Kontogrundlagen-Kosten.tex` einen Vergleich „Ohne Hebel / Mit Hebel 1:10“ mit einfachen Zahlen einbauen. Vorbild ist das englische Lehrbuchbeispiel „you vs. your friend“ (CFD mit Hebel gegen direkten Kauf, Tabelle Opening/Closing). Dazu gehören eine kurze Geschichte, eine Tabelle im Spickzettel-Stil (booktabs, `\hd`-Köpfe, `\midrule`, + in `buy`, − in `sell`) und ein Fazit. Grafik, Merk-Kasten und Plattform-Elemente bleiben erhalten. Am Ende HANDOFF ergänzen, committen und pushen.

## Vorgaben

1. **Zahlen-Ausnahme gilt nur für diesen Hebel-Vergleich.** Sonst gilt im Dokument weiter das Zahlenverbot (HANDOFF 2.3, Ausnahme 3).
2. Deutsche Schreibweise: 1.000 €, 5 %, schmales Leerzeichen `\,` vor € und %, echtes Minus U+2212.
3. **Sie-Form, C1-Register** (seriöses Bankdokument): präzise, ganze Sätze, logische Konnektoren (folglich, hingegen …). Keine saloppen Bilder, keine Slogans, keine Gedankenstrich-Ketten. Für Laien verständlich.
4. **Rein informativ:** Nichts bewerten und keine Handelsentscheidung nahelegen. Also kein „dafür/dagegen“, „Vorteil/Nachteil“, „lohnt sich“, „sinnvoll“ oder „Gewinnverstärker“. Grün/Rot nur für Gewinn/Verlust.
5. Stop out vorsichtig formulieren („in der Regel vorher“), ohne Prozentschwelle.
6. Der Hinweis „Information → Leverage“ steht schon im Merk-Kasten. Nicht doppeln.
7. Grafiken und Farben im PO-Stil (HANDOFF 13). Plattform-Elemente (S. 6) nicht anfassen.
8. Zusammenarbeit: Nur `dokumente/kontogrundlagen-kosten/`, `HANDOFF.md` und diese Datei anfassen. Pfade einzeln stagen, vor dem Push `git pull --rebase`. In `dokumente/pending-orders/` arbeitet ein anderer Agent.

## Erledigt

- `Kontogrundlagen-Kosten.tex` Z. 314–336: Kommentar zur Ausnahme, `\Htwo{Ein Vergleich mit einfachen Zahlen}`, Geschichte (3 Zeilen), Tabelle (Z. 322–334) und Fazit (2 Zeilen), alles in Sie-Form/C1.
- Z. 338–346: Die beiden Kästen sind neutral (Überschriften `muted`): „AUSWIRKUNG AUF DEN KAPITALEINSATZ“ und „AUSWIRKUNG AUF KURSBEWEGUNGEN“. Beide sind gleich hoch (`equal height group=hebel`).
- Schlusszeile „kein Gewinnverstärker …“ entfernt. Ihre Aussage steht jetzt im Fazit; außerdem war die Zeile wertend und die Seite wäre übergelaufen.
- Abstände: Lead → Grafik 8 mm (statt 9), vor dem Merk-Kasten nur noch dessen eigene 6 mm.
- Rechnungen geprüft. 7 Seiten, keine neuen Overfulls, 10 Schriften eingebettet, keine Rasterbilder. Seiten 1–3 und 5–7 sind pixelgleich mit `86b22e4`.
- `HANDOFF.md`: Inhaltsverzeichnis, Z. 80 (Ausnahme 3), Seite 4 in 5.3, Abschnitt 14 ab Z. 870.
- Nicht eingecheckt (`build/` wird ignoriert): `build/Hebel-Neu.png` (S. 4, 110 dpi) und `build/Kontogrundlagen-Kosten_TEST.pdf`.

## Offen

1. Lead (Z. 287–288) und Merk-Kasten (Z. 348–350) auf S. 4 sind noch in der du-Form. Sie werden im eigenen Durchgang „Sie/C1“ umgestellt, wie das ganze übrige Dokument; das ist nicht Teil dieses Auftrags.
2. Nutzer bestätigen lassen: Die Tabelle sagt „kein Swap“ ohne Hebel (Modell der Swap-Seite: Swap = Zins auf geliehenes Geld). Auf CFD-Plattformen fällt Swap meist auch bei 1:1 an (siehe ⚠ in HANDOFF 14).
3. Optional: Zeile −5 % kann je nach Stop-out-Wert schon den Stop out auslösen (Level 50 %). Der Betrag stimmt trotzdem; bei Bedarf mit dem Nutzer klären.

## Bekannte Probleme

- S. 4 ist bis ca. 275 mm gefüllt (Satzspiegel bis 279 mm). **Jede zusätzliche Zeile schiebt den Merk-Kasten auf eine neue Seite.** Nach jeder Textänderung die Seitenzahl prüfen (7 erwartet).
- Die Spalte „Mit Hebel 1:10“ beginnt bei 88 mm, bündig mit „Mit Hebel“ in der Grafik. Die Spaltenbreiten 34 / 45,53 / 82 mm ergeben zusammen genau 170 mm.

## Nächster konkreter Schritt

Keiner für diesen Auftrag, er ist abgeschlossen. Wer S. 4 im Sie/C1-Durchgang überarbeitet, sollte danach `scripts/build.sh kontogrundlagen-kosten` laufen lassen, die Seitenzahl prüfen und S. 4 bei 110 dpi ansehen.
