# HANDOFF – Trading-Schulungs-PDFs (Stand: Ende des claude.ai-Chats, 07.09.2026; Nachträge bis 02.10.2026)

> **Für Claude Code.** Diese Datei fasst den kompletten Chat-Verlauf (`docs/chat-verlauf.txt`, Nachrichten #0–#159, 04.–07.09.2026) zusammen, damit du genau dort weitermachen kannst, wo der Chat aufgehört hat.
> Quelle ist **nur der Textexport**: Tool-Aufrufe, Bilder, Screenshots, Konsolen-Ausgaben und die erzeugten Dateien fehlen. Alles, was hier steht, ist im Verlauf belegt (Nachrichtennummer in Klammern, z. B. „(#103)“). Was nicht sicher belegt ist, ist mit **⚠ unsicher** markiert.
> Die erzeugten Dateien (.tex, .pdf, Skripte) lagen nur in der Sandbox des alten Chats und sind **hier nicht vorhanden** – siehe Abschnitt 9.

---

## Inhalt

1. [Kurzüberblick](#1-kurzüberblick)
2. [Harte Vorgaben des Nutzers (Checkliste)](#2-harte-vorgaben-des-nutzers-checkliste)
3. [Design-System](#3-design-system)
4. [Dokument 1 – „Pending Orders“](#4-dokument-1--pending-orders-kurz-guide-6-seiten)
5. [Dokument 2 – „Schulungseinheit 1: Kontogrundlagen & Kosten“](#5-dokument-2--schulungseinheit-1-kontogrundlagen--kosten-9-seiten)
6. [Technik](#6-technik)
7. [Konsolenbefehle (JS) aus dem Verlauf](#7-konsolenbefehle-js-aus-dem-verlauf)
8. [Offene Punkte / nächste Schritte](#8-offene-punkte--nächste-schritte)
9. [Fehlende Dateien](#9-fehlende-dateien)
10. [Unklarheiten und Widersprüche im Verlauf](#10-unklarheiten-und-widersprüche-im-verlauf)
11. [Stand Wiederherstellung](#11-stand-wiederherstellung)
12. [Wiederherstellung Kontogrundlagen](#12-wiederherstellung-kontogrundlagen)
13. [Farbrollen Kontogrundlagen](#13-farbrollen-kontogrundlagen)
14. [Hebel-Vergleich mit Zahlen (Kontogrundlagen S. 5)](#14-hebel-vergleich-mit-zahlen-kontogrundlagen-s-5)
15. [Sprachdurchgang Kontogrundlagen: Sie-Form, C1, neutral](#15-sprachdurchgang-kontogrundlagen-sie-form-c1-neutral-02102026)
16. [Pending-Orders-Guide: Neufassung (Sie-Form, C1, neutral)](#16-pending-orders-guide-neufassung-sie-form-c1-neutral)
17. [Nachtrag 2 (02.10.2026): Kontogrundlagen auf 8 Seiten](#17-nachtrag-2-02102026-kontogrundlagen-auf-8-seiten)
18. [Nachtrag 3 (02.10.2026): Instrumente, Positionen, Nachbauten](#18-nachtrag-3-02102026-instrumente-positionen-nachbauten)

---

## 1. Kurzüberblick

| | |
|---|---|
| **Projekt** | Deutschsprachige Schulungs-PDFs zum Trading, gesetzt mit XeLaTeX + TikZ |
| **Zielgruppe** | Laien/Einsteiger, auch Ältere (#20). Der Text muss für Laien verständlich sein (#106). |
| **Plattform** | Ein **WebTrader** (Desktop-Browser + Mobile) mit **englischer Oberfläche** (#16, #133). Begriffe im Dokument = Begriffe der Plattform. Der Name der Plattform/Firma steht nirgends im Verlauf. |
| **Format** | Helles **A4-Hochformat** (#102). Eine dunkle Querformat-Variante (BnkPro-Stil, #35) wurde nur als Demo gebaut und **nicht** übernommen; die Blattfarbe soll unverändert bleiben (#50). |
| **Dokument 1** | „**Pending Orders**“ – Kurz-Guide, 6 Seiten, fertig inkl. geschützter Fassung (#125). |
| **Dokument 2** | „**Schulungseinheit 1: Kontogrundlagen & Kosten**“ – **9 Seiten** (seit 02.10.2026; neue S. 2 „Grundbegriffe“, neue S. 8 „Instrumente und Positionen“), gebaut. Stand: Abschnitte 5.3, 17 und 18. |
| **Ausgabe je Dokument** | Zwei Fassungen: **ORIGINAL** (zum Weiterarbeiten) und **GESCHÜTZT** (zum Weitergeben) (#119). |

**Stand beim Abbruch (#157 → #158):** In Dokument 2 waren gerade die mobile Kontoübersicht (Vektor-Nachbau mit gemessenen Werten) und die Desktop-Leiste (im **blauen** Design, teils geschätzt) auf der Seite „In der Plattform“ eingebaut. Offen waren zwei weitere Messläufe mit dem Konsolenbefehl aus #153 (Desktop-Leiste im blauen Design und Instrument-Info-Feld). Danach bat der Nutzer um diese Übergabedatei (#158); die Antwort #159 ist leer.

**Stand 02.10.2026 (Repo):** Maßgeblich für Doku 2 sind die Abschnitte 12–15 (u. a. S. 5 Hebel-Vergleich, S. 6 Swap-Modell mit Rechenbeispiel – Zählung mit 8 Seiten, siehe Abschnitt 17 –, Fußzeile „KONTOGRUNDLAGEN & KOSTEN · EDUCATION – STANDARD PACKAGE“), für Doku 1 Abschnitt 16 (9 Seiten, Fußzeile „PENDING ORDERS · STANDARD TIER“, Deckblatt-Testvariante). Entscheidungen vom 02.10.2026 (Begriff „Liquiditätsanbieter“, Gutschrift-Satz, Deckblatt): Abschnitt 8.2; die neuen Rückfragen aus diesem Stand sind beantwortet.

**Nachtrag 2 (02.10.2026, `git log 4163359..3b34934`):** Doku 2 hat jetzt **8 Seiten** (neue S. 2 „Grundbegriffe“, alle folgenden Seiten +1; Zählung und Commits: Abschnitt 17). Auf der Plattform gibt es **keine Commission**, dafür einen **Bonus** (Nutzer, 02.10.2026). Neue Quelle: `originals/Education_Session_1_Account_Basics_Kosten_2.pdf` (Reverse-Engineering-Fassung des Nutzers, Abschnitt 5.1). **Seitenzahlen bleiben entfernt**, Verweise nennen den Seitentitel (Abschnitt 2.3, 5.3). Doku 1: Deckblatt (SVG) übernommen, `pdftitle` „Pending Orders – Standard Tier“ (Abschnitt 16). Offene Funde der Prüfung (Plattform-Bilder u. a.): Abschnitt 8.4.

**Nachtrag 3 (02.10.2026, `git log bee5507..5455781`):** Doku 2 hat jetzt **9 Seiten** (neue S. 8 „Instrumente und Positionen“, „Auf einen Blick“ wird S. 9). Neu: DOM-Messungen des Nutzers zu Info-Fenster, mobilen Angaben, Kursliste und Positionstabelle, daraus fünf Vektor-Nachbauten und ein Lehrbuch-Schema des Desktops; eingebunden sind nur die Angaben des Instruments (Desktop und mobil). Begriff **Total Profit** für das Ergebnis einer Position; Bid/Ask wieder entfernt. Commits, Dateien, offene Messungen: Abschnitt 18.

---

## 2. Harte Vorgaben des Nutzers (Checkliste)

Diese Regeln gelten für **beide** Dokumente, sofern nicht anders vermerkt. Vor jeder Änderung prüfen.

### 2.1 Arbeitsweise

- [ ] **Lieber fragen als raten.** „mir ist lieber [du] fragst, statt dass du Sachen machst, die nicht 100 % [sicher] sind“ (#20). Rückfragen sind ausdrücklich erwünscht (#106).
- [ ] **Wenn du dir nicht zu 110 % sicher bist → dem Nutzer einen Browser-Konsolenbefehl geben**, den er in der Plattform ausführt (F12 → Console → einfügen → Enter), und er schickt dir die Ausgabe (#40). Siehe Abschnitt 7.
- [ ] Wenn der Nutzer sagt „erkläre es mir nicht, mach es einfach“ (#106): umsetzen, nicht lange erklären.
- [ ] Ergebnisse **nachmessen statt behaupten** (Rasterbilder zählen, Schriften prüfen, Pixelvergleich, Starthöhe messen) – so wurde im Chat durchgehend gearbeitet.

### 2.2 Sprache und Begriffe

- [ ] **Nur Begriffe, die auf der Plattform stehen** – „das ist mir wichtig“ (#22). Kein erfundenes Ersatzwort.
- [ ] Order-Namen englisch wie im Fenster: **Buy Limit, Sell Limit, Buy Stop, Sell Stop**; **Buy / Sell** statt „Kauf/Verkauf“ (#16, #17).
- [ ] Feldnamen: **At price**, **Take-Profit**, **Type**, **Symbol**, **Volume**, **New Market Order**, **New Pending Order**, **Place pending order** (#29).
- [ ] **Kein „Trigger“, keine „Marke“** (#20, #23). Auch „Auslösekurs“ wurde verworfen (#21 → #22).
- [ ] **Kein Ask/Bid**; stattdessen „über / unter dem aktuellen Kurs“ (#14, #15). Gilt für **beide** Dokumente: In Doku 2 standen Bid/Ask kurz in „Grundbegriffe“ und „In der Plattform“ (`25049f5`) und sind wieder entfernt (`c1e2878`). Kurse heißen in den Nachbauten „Kurs“; der Spread ist „der Unterschied zwischen dem Kurs für Buy und dem Kurs für Sell“ (Übergabe `kg-instrument-info-wege.md`, Nachtrag).
- [ ] **Stop-Loss bekommt später ein eigenes Dokument** (Nutzerwunsch, 02.10.2026) – in den bestehenden Guides **nicht erwähnen**.
- [ ] „Market Buy / Market Sell“ gibt es auf der Plattform nicht (#21) → Reiter heißt „New Market Order“.
- [ ] **„Aktivierungspunkt“** für den Wert bei At price (#118). Vorgegebene Ersetzungen:
  - „Du trägst bei At price einen Kurs ein.“ → „Du trägst bei At price deinen Aktivierungspunkt ein.“
  - „Der Wert, bei dem die Order auslösen soll.“ → „Dein Aktivierungspunkt: der Wert, bei dem die Pending Order ausgelöst wird.“
  - „Der Kurs muss erst dorthin laufen – dann löst die Order aus.“ → „Erreicht der Markt deinen Aktivierungspunkt, wird die Order ausgelöst.“
- [ ] **„ausgelöst“ statt „ausgeführt“** – überall (#118, #119). (Begründung des Nutzers: Der Aktivierungspunkt löst aus, die Ausführung ist ein zweiter Schritt; seine Nachricht bricht danach ab.)
- [ ] Im Order-Fenster **„Instrument XY“ statt Crude Oil** (#20).
- [ ] Erklärtexte bleiben deutsch (#17).
- [ ] Doku 2: Plattform-Begriffe wie in den Screenshots: Balance, Equity, Profit/Losses, Margin, Free, Level, Stop out, Swap long, Swap short, Contract size, Leverage, Information, Orders (#147, #151, #153).
- [ ] Doku 2: **Keine Commission.** Sie gibt es auf der Plattform nicht (Nutzer, 02.10.2026); das Wort steht nirgends im Dokument. Stattdessen der **Bonus**: ein Betrag, mit dem man handeln kann; Gewinne daraus sind gemäß den AGB des Brokers auszahlbar (Nutzer, 02.10.2026). **Credit** wird nur als Feldname genannt, nicht erklärt. ⚠ Seit `0850815` steht „Commission“ als **Feldname in den eingebundenen Nachbauten** auf „Instrumente und Positionen“ (Wert „—“; Plattform-Original, laut DOM steht der Wert bei null, `docs/plattform/dom-positionsliste.md`); im Text weiterhin nicht (8.4).
- [ ] Doku 2 (seit `0850815`): **Total Profit** heißt das Ergebnis einer offenen Position einschließlich ihres Swaps (Grundbegriffe, Kontostand, Swaps, Instrumente und Positionen, Auf einen Blick); **Profit/Losses** bleibt die Summe in der Kontoübersicht (belegt: `834863a`). Im Text „**Angaben des Instruments**“ statt „Info-Fenster“; „**Forex (Devisen)**“ beim ersten Auftreten, danach „Forex“ (`25049f5`). Weitere Plattform-Begriffe: Quotes, die Kategorien Forex, Stocks, Cryptos, Indices, Energies, Metals, Commodities, ETFs, Reiter Active/Pending/History, Amount, Trade volume, Spread (5.2, 5.3).
- [ ] Doku 2: **Verweise zwischen Seiten nur per Seitentitel**, nie per Zahl: „→ Margin“, „(Abbildung unter „In der Plattform“)“ (Abschnitt 2.3, 5.3).

### 2.3 Inhalt

- [ ] **Kein Stop Loss** im Dokument – verwirrt Laien. Take-Profit bleibt genau so (#10, #12).
  ⚠ unsicher: Im Fenster-Nachbau war der Stop-Loss-Schalter anfangs ausgeschaltet sichtbar; Claude bot an, ihn zu entfernen (#15). Eine Antwort darauf fehlt.
- [ ] **Keine Zahlen im Dokument** – „generell keine Zahlen“, sie verwirren Laien (#58). Entfernt wurden Preise, Kapitelnummern, „Typ 1–4“, Datum und Seitenzahlen (#59).
  - **Seitenzahlen bleiben entfernt, auch in Doku 2** (Fußzeile ohne Seitenzahl). Verweise nennen den **Seitentitel** („→ Margin“, „mehr dazu unter „Margin““, „(Abbildung unter „In der Plattform“)“), im Dokument kein „S. n“ (Abschnitt 5.3, 17). Der Zwischenstand mit Zahlenverweisen und „n / 8“ in der Fußzeile (Commits `5f9d129`, `145c398`) ist damit überholt (`3b34934`).
  - Ausnahme 1: **Schrittnummern 1–5** (Wegweiser, keine Preise) (#59, #67). Ebenso die **Markennummern 1–5 im mobilen Nachbau** (Doku 2, S. 7 „In der Plattform“) als Wegweiser, und die **Nummern 1–3 auf S. 8 „Instrumente und Positionen“** (Marken an Swap long, Swap short, Leverage in `info-desktop.pdf`/`info-mobil.pdf` und ihre Legende; seit `0850815`). Die noch nicht eingebundenen Nachbauten tragen Marken 1 bzw. 1–3, abschaltbar mit `\ohnemarken` (Abschnitt 18).
  - Ausnahme 2: **Badge auf dem Deckblatt** „4 Ordertypen. 1 klare Entscheidungslogik.“ – vom Nutzer selbst vorgegeben (#102); Claude hat auf den Konflikt hingewiesen (#103), keine Antwort.
  - Ausnahme 3 (nur Doku 2, **S. 5** „Hebel“; bis `5f9d129` S. 4): **Hebel-Vergleich** „Direktkauf über die Bank“ gegen „Broker, Hebel 1:10“ mit einfachen Zahlen (je **2.000 €** verfügbar, 1.000 € Einsatz bzw. Margin, 10.000 €, 9.000 €, Free 1.000 € als eigene Zeile sichtbar, 1:10, Kurs 100 → 105 €, 95 €, ±50 €/±500 €, Swap 7 € pro Nacht, 5 %/50 %/10 %) – ausdrücklicher Wunsch des Nutzers (02.10.2026), Abschnitt 14. Die Zahl 2.000 € kam mit dem Feinschliff `e70e62e` hinzu. Unter der zweiten Tabelle steht (Nutzerwunsch): „Alle Beträge sind fiktiv und dienen ausschließlich der Veranschaulichung.“
  - Ausnahme 4 (nur Doku 2, **S. 6** „Swaps“; bis `5f9d129` S. 5): **Swap-Beispiel** (eigene Position in Crude Oil) mit 1.000 €, 10.000 €, 1:10, 3 €, 3 €, 6 €, 1 €, 7 € pro Nacht und „Tageswechsel um 23:00 Uhr (Amsterdamer Zeit)“ – ausdrücklich vom Nutzer (Skizze `originals/skizze-hebel-swap.png`; Uhrzeit Nutzerangabe), Abschnitt 5.3. Auch hier der Hinweis, dass die Beträge fiktiv sind (Nutzerwunsch). Die Reverse-Engineering-Fassung nennt den Rollover „üblicherweise 22:00 UTC bzw. 0:00 Serverzeit“; im Dokument gilt die Angabe des Nutzers. Sonst gilt das Zahlenverbot weiter.
  - Im Fenster stehen statt Werten „deine Menge“, „dein Wert“, „dein Ziel“ (#59); in der Kontoübersicht „Konto jetzt“ statt einer Summe (#151). Die „dein/deine“-Platzhalter in den Plattform-Nachbauten **bleiben** (Nutzerentscheidung 02.10.2026, endgültig; Abschnitt 8.2).
- [ ] **Take-Profit-Regel bei jedem Typ nennen**: bei Buy **über**, bei Sell **unter** dem At price (#48, #49).
- [ ] Kein **historischer Trade / Hebel-Rechenbeispiel** im Guide. Claude riet ab (Zahlen, Hebel ohne Absicherung, falsche Erwartungen, Größen- statt Richtungsfrage) und bot ein separates Anhangsblatt „Rechenbeispiel“ an (#65). ⚠ Der Nutzer hat nicht geantwortet.
- [ ] **Keine Doppelungen** auf einer Seite oder zwischen Seiten (#66, #68): jedes Element hat genau eine Aufgabe.
- [ ] Linien und Pfeile in Charts müssen **immer richtig** sein (#8) → datengetriebene Prüfung mit Build-Abbruch (Abschnitt 6).
- [ ] Keine aggressiven Gewinnversprechen (#102); Vor- und Nachteile gleichwertig (#147).
- [ ] Doku 1 muss die **vier Lernziele** abdecken (#114, Abschnitt 4.1).
- [ ] Doku 2 muss die **Themenliste** des Nutzers abdecken (#126, Abschnitt 5.1).

### 2.4 Gestaltung

- [ ] **Kein typischer KI-/Standard-GUI-Look** (#4).
- [ ] Design nach Claudes eigenem Best-Practice-Urteil, auch die Schrift (#30) → IBM Plex (Abschnitt 3).
- [ ] Charts = **die echten Plattform-Chartbilder als 1:1-Vektor**, keine eigenen Zeichnungen (#72, #80).
- [ ] **Charts ohne dunklen Hintergrund** (#82). Take-Profit-Linie und Gewinnzone erlaubt, aber **passend zur Plattform-Optik** (#82).
- [ ] **Kein Neongrün**; nur das Grün aus dem zweiten Bild des Nutzers (#88, #89).
- [ ] Fenster- und Kontoübersicht-Nachbauten **in Plattform-Optik**, mit gemessenen Werten (#20, #39, #153).
- [ ] **Titel des Deckblatts: „Pending Orders“** – nicht „At Price“, nicht „Pending Orders verstehen“ (#60, #62).
- [ ] Seite 6 (Doku 1): „**New Pending Order**“ statt „New Order“ (#64).
- [ ] Order-Namen auf dem Deckblatt **nicht umbrechen** (#90).
- [ ] Deckblatt: **oben kein unnötiger Weißraum**, Titelblock weit oben; etwas Weißraum unten ist ok (#96). Weißraum zwischen Text und Visual soll bleiben (#94/#95). ⚠ siehe Abschnitt 10.
- [ ] **Gleiche Starthöhe auf allen Seiten: 20,5 mm** vom oberen Rand bis zur ersten Schrift (#98, #99).
- [ ] **Flattersatz in schmalen Spalten** und in Einleitungen, dort keine Worttrennung (#122, #123).
- [ ] **Kein Schatten ums Blatt** (#56). Blattfarbe nicht ändern (#50). Erlaubt/übrig: feine helle Umrandung um Grafiken (#59).
- [ ] Deckblatt-Vorgaben aus #102 (komplett in Abschnitt 4.3): keine Fotos, keine Trader-Bilder, Weltkarten, Laptops, echten Chart-Screenshots, Neonfarben oder Gold-Effekte, keine überladene Deko; max. zwei Schriftgewichte zusätzlich zum Titel; lesbar auf A4 **und** Smartphone.
- [ ] Doku 2: **im Stil des Pending-Orders-Guides**, **nicht** im Stil des vom Nutzer hochgeladenen Dokuments (Reverse-Engineering-Fassung mit Code-Formeln) (#126, #129). Diese Fassung liegt seit 02.10.2026 im Repo (`originals/Education_Session_1_Account_Basics_Kosten_2.pdf`) und dient als **Quelle für Plattform-Fakten**, nicht als Stilvorlage (Abschnitt 5.1).

### 2.5 Qualität und Schutz

- [ ] **Druckqualität**: alles **Vektor**, **null Rasterbilder**, **alle Schriften eingebettet**, Dateigröße egal (#44, #54, #58).
- [ ] Geschützte Fassung (#118, #120, #124): kein Kopieren (auch nicht „Content copying for accessibility“), kein Drucken, .txt/Word → leer bzw. Salat, Google Translate → Salat, Design **pixelidentisch**.

---

## 3. Design-System

### 3.1 Schriften

| Schrift | Einsatz | Quelle |
|---|---|---|
| **IBM Plex Sans** | gesamter Dokumenttext. Titel in **Light**, Fließtext **Regular**, Auszeichnung **SemiBold** (Deckblatt: nur diese drei Schnitte) | #33, #103 |
| **IBM Plex Mono** | ursprünglich für alle Zahlen (bündige Preise) | #33 – ⚠ seit „keine Zahlen“ (#58) vermutlich kaum noch in Gebrauch |
| **Inter** | nur Plattform-Nachbauten (Order-Fenster, Type-Menü, Kontoübersicht), Originalschrift der Plattform, per npm geholt | #41, #151 |

Verworfen: Liberation Sans (Nutzer-Vorgabe #18, ersetzt durch #30/#33), Carlito/Excel-Look (#7), Futura (BnkPro-Referenz, nicht vorhanden, #35).

### 3.2 Größenskala

- Modulare Skala (#33): **30 / 19 / 12 / 9,4 / 7,6 / 6,4 pt**, Zeilenabstand **1,45**.
- Kleinschrift wurde später „eine Stufe größer“ gesetzt, damit sie auf dem Handy lesbar bleibt (#117). ⚠ Der genaue neue Wert steht nicht im Verlauf.
- „Pending Orders“ ist der größte Text auf dem Deckblatt (#102).

### 3.3 Farben

**Plattform-Farben (gemessen per Konsole, gelten für alle Nachbauten):**

| Hex | Bedeutung | Quelle |
|---|---|---|
| `#04273C` | Fensterhintergrund (Order-Fenster); auch Hintergrund der mobilen Kontoübersicht (blaues Design) | #39, #41, #155 |
| `#001328` | Eingabefelder im Order-Fenster; mobile Reiterleiste (`ul.nav-tabs`) | #39, #41, `…/mobil-kopf-reiter.json` |
| `#0E5072` | aktiver Reiter; Hintergrund des aufgeklappten Type-Menüs; Kasten hinter „Equity“ in der Desktop-Leiste (`.item-bg`, gemessen 02.10.2026) | #41, #47, #157, `originals/messungen/kontoleiste-desktop.json` |
| `#051B3A` | Desktop-Kontoleiste (`<footer>`, blaues Design) – **nicht** `#04273C`; auch mobile Kopfleiste (`<header>`) | `originals/messungen/kontoleiste-desktop.json`, `…/mobil-kopf-reiter.json` |
| `#226486` | Symbole der mobilen Kopfleiste (Normalzustand; aktiv weiß) | `originals/messungen/mobil-kopf-reiter.json` |
| `#53BC51` | Plattform-Grün (Button, „Estimated Profit“-Zahl, Balance-Wert mobil; Kurs in der Kursliste, positives Total Profit) | #39, #41, #155, `…/kursliste-desktop.json`, `…/positionen-desktop.json` |
| `#A8BBBE` | Labels/Bezeichnungen (Order-Fenster, mobile Kontoübersicht, Desktop-Leiste; Info-Fenster mit Inter **300**, Spaltenköpfe der Positionstabelle) | #41, #155, `…/instrument-info-desktop.json`, `…/positionen-desktop.json` |
| `#64747F` | Preis-Badges im Order-Fenster | #41 |
| `rgba(255,255,255,.1)` | Trennlinien im Type-Menü; Trennlinien (0,8 px, 10 % Weiß) in der Kontoübersicht; Trennlinie unter dem Kopf des Info-Fensters | #47, #155, `…/instrument-info-desktop.json` |
| `#0E3D58` | Info-Fenster eines Instruments am Desktop (Radius 5 px, Schatten `rgba(0,0,0,.25) 0 0 20px 4px`) | `originals/messungen/instrument-info-desktop.json` |
| `rgba(14,80,114,.1)` → `rgb(5,43,65)` | Zeilen der Kursliste und der Positionstabelle (Desktop, auf `#04273C`); Kopfzeile der mobilen Angaben (dort Hintergrund `#04273C` nur angenommen, 8.4) | `…/kursliste-desktop.json`, `…/positionen-desktop.json` |
| `#F94056` | Schaltfläche „New pending order“ (mobile Angaben); negatives Total Profit in der Positionstabelle | `…/instrument-info-mobil.json`, `…/positionen-desktop.json` |
| `#062F47` | Schaltfläche „Trade Hours“ (mobile Angaben) | `…/instrument-info-mobil.json` |
| `#5B6A82` | Stern, inaktiv (mobile Angaben; nicht gezeichnet, Glyphe fehlt) | `…/instrument-info-mobil.json` |
| `rgb(34,100,134)` = `#226486` | auch Info-Zeichen am Zeilenende der Kursliste | `…/kursliste-desktop.json` |
| `#181818` | Desktop-Leiste im **grauen** Design (Screenshot des Nutzers) – wurde **nicht** verwendet | #157 |
| ~~`#1F1F1F`~~, ~~`#7A8384`~~ | **falsch** aus dem Handy-Screenshot gepipettet, durch `#04273C` / `#A8BBBE` ersetzt | #155 |

**Dokument-Farben:**

- Grün für Buy, Rot für Sell, schwarze/dunkelgraue Typografie, dezente graue Linien, viel Weißraum (#102).
- **Grün**: das „gedämpfte“ dunklere Grün aus dem zweiten Bild des Nutzers, mit dem „BUY LIMIT“ gesetzt ist – **eine** Grüntönung im ganzen Dokument (#89). ⚠ Hex-Wert steht nicht im Verlauf. ⚠ Ob `#53BC51` das verworfene „Neongrün“ ist, ist unklar (#83: „Rot und Grün sind unverändert die Originalfarben“, danach #88 „Neongrün weg“).
- **Rot**: dasselbe Rot wie in den Überschriften statt des grellen Pink-Rots der Plattform (#89). ⚠ Hex unbekannt. Claude bot an, das Original-Rot zurückzuholen – keine Antwort.
- Graue Kerzen der Plattformbilder sind für dunklen Grund gemacht → auf Weiß **etwas abgedunkelt** (#83).
- Kurslinie und Hilfselemente neutral grau/dunkelgrau (#102).
- **Doku 2 seit 02.10.2026:** eigene Erklärgrafiken und Kästen nur noch in den Farben und Rollen von Doku 1 (Margin-Flächen Chart-Grau statt Schwarz, weiße Flächen mit `greya`-Rand, keine eigene Akzentfarbe). Das kurzzeitig eingeführte Plattform-Blau ist wieder entfernt (Nutzerwunsch, Abschnitt 13).

### 3.4 Chart-Bildsprache (Plattform-Chartbilder)

Herkunft: Die Plattform zeigt im Order-Fenster pro Type ein festes Bild `assets/images/img-pending-order-{bl|sl|bs|ss}.png`, **174 × 96 px** (#39, #41). Die vier PNGs wurden aus der HAR des Nutzers extrahiert (#41); vom Server gibt es nur diese Größe, die Dateien sind byte-identisch (md5) mit den Uploads (#71).

**Kürzel** (#77, #79): **bl** = Buy Limit · **sl** = Sell Limit · **bs** = Buy Stop · **ss** = Sell Stop.

**Lesart** (gemessen, #75):

- Das Bild liest sich von links nach rechts wie eine Zeitachse.
- **Linke Kugel = aktueller Kurs**, **rechte Kugel = At price**. Rechte Kugel immer grün, linke immer rot (reine Färbung, keine Bedeutung).
- Rechte Kugel **höher** → At price über dem Kurs → Sell Limit oder Buy Stop. **Tiefer** → Buy Limit oder Sell Stop.
- **Dreieck oben rechts** = Richtung nach der Auslösung: grün nach oben bei Buy-Typen, rot nach unten bei Sell-Typen.
- Beispiel `ss`: rote Kugel oben, rotes Dreieck nach unten, grüne Kugel tiefer → Sell Stop. Bei `sl` liegt die grüne Kugel oben (#79).

**Vektorisierung (Endstand, #101):** jedes Bild in Grundformen zerlegt: **37 Rechtecke** (Balken und Stiele), **2 Kreise** (Kugeln), **1 Dreieck**. Kanten subpixelgenau aus der Randdeckung berechnet. Stiele unter den Kugeln vorhanden, kein überlappender Balken.

**Zusätze im Dokument (Endstand nach #83, #85, #89):**

- **Kein dunkler Hintergrund**, Kerzen direkt auf dem Papier (#82, #83).
- **Take-Profit-Linie**: gestrichelt in der Farbe der Order, Strich etwa doppelt so lang wie die Lücke, Text **links über** der Linie (#73, #83). Liegt außerhalb des Kerzenbereichs, also bei Buy oben und bei Sell unten sichtbar (#83).
- **At-price-Linie** im gleichen gestrichelten Stil (#83).
- **Kurs jetzt**: dünne graue Linie; Beschriftung „Kurs jetzt“ **rechts neben** der Linie (#85).
  - ⚠ Die abgerundete graue **Pille** am rechten Rand (Plattform-Optik, #73/#83) wurde in #85 **wieder entfernt**, weil sie das Dreieck wie einen Teil der Kurslinie aussehen ließ.
- **Gewinnzone**: leichte Tönung in der Order-Farbe, beginnt **an der grünen Kugel** (erst ab Auslösung) und reicht bis zur Take-Profit-Linie (#83).
- Am Dreieck steht **„Richtung danach“** (#85).
- **Keine Nummernkreise** mehr im Chart; jede Linie trägt ihren Namen (#85).
- Alle Beschriftungen haben einen **weißen Untergrund**, damit keine Kerze den Text überdeckt (#89).
- Rechte Textspalte neben großen Charts mit denselben drei Überschriften: **Kurs jetzt · At price · Richtung danach** (#85).

### 3.5 Maße des Order-Fensters (Doku 1, gemessen per Konsole #39/#41/#47)

- Schrift Inter: Felder **12 px**, Überschrift **16 px**, Button **13 px / 600**.
- Reiter **221,5 px** breit; Felder **213,5 × 30 px**; Zähler-Buttons (+/−, gestapelt) **23 × 15 px** mit Trennlinie dazwischen; Chartbild **174 × 96 px**; Trennlinie bei **y = 361,6 px**.
- Type-Menü: Zeilenhöhe **34,4 px**, Hintergrund `#0E5072`, Trennlinien `rgba(255,255,255,.1)` (#47).
- Details: „Estimated Profit“ mit grüner Zahl, Schalter „By price / by points“, Chevrons statt gefüllter Dreiecke in den Auswahlfeldern (#41, #49), € direkt ohne Leerzeichen (#41).
- Bewusste Abweichungen: Button **aktiv** dargestellt (im DOM `disabled`, 55 % Deckkraft) (#41). Preis-Badge-Positionen aus dem Buy-Limit-Zustand für alle vier Typen übernommen – bei Sell Limit/Buy Stop eventuell leicht daneben (#41). ⚠ ungeprüft.
- Das **×** links von „Instrument XY“ ist entfernt (#46, #49).
- Variante **A „Exakt“** (flache Farben) wird verwendet, nicht Variante B „Aufgewertet“ (#43, #45).
- Ziffern **1–5** direkt im Fenster (#45).

### 3.6 Maße der Kontoübersicht (Doku 2, gemessen per Konsole #150/#154/#155)

- Schrift Inter; Zeilenhöhe **40,8 px** mit **12 px** Innenabstand; Trennlinien **0,8 px**, 10 % Weiß.
- Labels und Werte **14 px**; Überschrift **18 px**, Wert in **700** und Plattform-Grün; Spaltenbreite exakt hälftig.
- Hintergrund `#04273C`, Labels `#A8BBBE`.
- Fünf Nummern **links neben den Bezeichnungen**: Equity, Profit/Losses, Margin, Free, Level (#151).
- Desktop-Leiste: im **blauen** Design nachgebaut, breiter gemacht, weil „Balance“ links abgeschnitten war (#157). ~~Geschätzt: Kastenfarbe hinter „Equity“, Gruppenabstände~~ – seit 02.10.2026 **gemessen** und neu gebaut (Abschnitt 12).

---

## 4. Dokument 1 – „Pending Orders“ (Kurz-Guide, 6 Seiten)

### 4.1 Die vier Lernziele (vom Nutzer, #114)

1. What pending orders are.
2. Difference between market orders and pending orders.
3. Types of pending orders and when they may be used.
4. Advantages of planning entries in advance.

Laut #117 sind alle vier abgedeckt (vorher fehlten zwei fast ganz).

### 4.2 Fachlicher Kern

| Type | At price liegt | Take-Profit liegt | Kurzform (Deckblatt, #102) |
|---|---|---|---|
| **Buy Limit** | unter dem aktuellen Kurs | über dem At price | günstiger kaufen |
| **Sell Limit** | über dem aktuellen Kurs | unter dem At price | teurer verkaufen |
| **Buy Stop** | über dem aktuellen Kurs | über dem At price | Ausbruch nach oben |
| **Sell Stop** | unter dem aktuellen Kurs | unter dem At price | Ausbruch nach unten |

Die Ausgangstabelle des Nutzers (#0) enthielt zusätzlich Value 1–4 und Ideen wie „Ich will billig kaufen“. Die Nummern sind wegen „keine Zahlen“ entfernt (#59).

### 4.3 Seite für Seite (letzter bekannter Stand)

Alle Seiten beginnen bei **20,5 mm** (#99). Kopfzeilen/Kapitelzeilen laut #99: Deckblatt („Trading-Grundlagen“), **Fundament**, **Limit-Typen**, **Stop-Typen**, **Spickzettel**, **Plattform**. ⚠ Ob „Fundament“ nach dem Umbau von Seite 2 (#117) noch so heißt, ist unklar.

**Seite 1 – Deckblatt** (Endstand #103, nach dem Brief des Nutzers #102)

- Oben links klein: **TRADING-GRUNDLAGEN** (auf derselben Höhe wie die Kapitelzeilen der Innenseiten).
- Groß: **Pending Orders** (Light, einzeilig, größter Text), darunter eine kurze Akzentlinie.
- Untertitel (Wortlaut des Nutzers): *„Die vier Ordertypen auf einen Blick – damit du Einstieg, Auslösepreis und Richtung richtig kombinierst.“*
- Badge als dezente Pille mit Haarlinie: *„4 Ordertypen. 1 klare Entscheidungslogik.“*
- **Hero-Visual: 2×2-Entscheidungslogik**, zentral:
  ```
                         AT PRICE ÜBER DEM AKTUELLEN KURS
                BUY STOP                         SELL LIMIT
            Ausbruch nach oben               teurer verkaufen
  ────────────────────────── KURS JETZT ──────────────────────────
                BUY LIMIT                        SELL STOP
            günstiger kaufen                Ausbruch nach unten
                         AT PRICE UNTER DEM AKTUELLEN KURS
  ```
  - Die Linie „Kurs jetzt“ ist die Achse, ihre Beschriftung unterbricht die Linie mittig.
  - Links immer Grün (Buy), rechts immer Rot (Sell).
  - Zu jedem Type ein kleiner Chart (Grundform-Vektor der Plattformbilder), oben und unten **spiegelbildlich nach außen**, Name und Nutzenzeile **zur Linie hin**.
  - Die vier Elemente sind gleichwertig, sauber ausgerichtet und großzügig getrennt; Name plus kurze Nutzenzeile, keine langen Texte.
- Footer: links „Pending Orders“, rechts „Kurz-Guide“ (Versalien-Stil). **Kein Logo**, weil keins vorhanden (#103). ⚠ Überholt: seit 02.10.2026 „PENDING ORDERS · STANDARD TIER“ statt „KURZ-GUIDE“ (Guide und CoverTest-Variante, Abschnitt 16).
- Weitere Vorgaben aus #102: wirkt wie ein FinTech-/Broker-Onboarding-Guide, minimalistisch, vertrauenswürdig, ruhig; Stil der Innenseiten beibehalten; Ziel-Eindruck: *„Moderne Finanzplattform erklärt eine komplexe Funktion in einer klaren, ruhigen und professionellen Sprache.“*
- Frühere Deckblatt-Fassungen (Preis-Leiter, Charts in Reihe, versetzte 2-Spalten-Diagonale #93) sind **ersetzt**.

**Seite 2 – „Was eine Pending Order ist“** (Endstand #117, #123)

- **Market Order vs. Pending Order** nebeneinander als „**Sofort.**“ und „**Später.**“.
- Danach der **Nullpunkt**: Grafik mit genau zwei Seiten – oben muss der Kurs steigen, unten fallen; **keine Order-Namen** in der Grafik (#69); „Kurs jetzt“ sitzt **direkt auf der Trennlinie** (#69).
- Darunter die Zuordnung in **zwei Zeilen** (die frühere Auswahltafel ist aufs Deckblatt gewandert) (#117).
- Abschluss: **„Warum im Voraus planen“** mit drei Gründen (#117). ⚠ Die drei Gründe stehen nicht im Verlauf.
- Schmale Kästen im Flattersatz, ohne Worttrennung („Aktivierungspunkt“ in einem Stück) (#123).
- Entfernt: Abschnitt „So liest du die Grafiken“ (Doppelung mit Seite 3, #66/#67); Legende A–G.

**Seite 3 – Limit-Typen (Buy Limit, Sell Limit)** und **Seite 4 – Stop-Typen (Buy Stop, Sell Stop)** (#81, #83, #85, #117)

- Pro Type eine Karte: Kartenkopf mit Order-Name (ohne „Typ 1/2“, #59) – laut #117 stehen dort auch die Nutzenzeilen wie „Ausbruch nach oben“.
- Großer Plattform-Chart (Vektor) mit At-price-Linie, Take-Profit-Linie, Gewinnzone, „Kurs jetzt“, „Richtung danach“ (Abschnitt 3.4).
- Rechts die Textspalte mit **Kurs jetzt · At price · Richtung danach** (#85).
- Schritte mit Schrittmarken **Eintragen → Warten → Ausgelöst** (#59). Schritt 3 nennt die Take-Profit-Regel, z. B. „Dein BUY läuft. Take-Profit über den At price“ (#49, früher mit Zahl).
- Vierter Punkt je Type: **„Wann sinnvoll“** (#117).
- Merke-/Fehler-Kästen aus der Frühphase (#1): ⚠ ob noch vorhanden, ist unklar.

**Seite 5 – Spickzettel** (#49, #67, #93, #119)

- Alle vier Charts **nebeneinander in einer Reihe** (der direkte Vergleich ist der Zweck), mit Zusatzzeilen wie „At price unter dem aktuellen Kurs“ (#93: dort bleiben sie).
- **Tabelle**, letzte Spalte „Take-Profit liegt“ („über dem At price“) (#49). Laut #119 wurde „deine Tabelle aus der CSV“ übernommen, mit einer Spalte **„Auslöser“** mit Kurzformen. ⚠ Die CSV ist nicht im Export, und es ist unklar, ob sie die Spickzettel-Tabelle ersetzt hat.
- **Faustregeln** im Merkkasten, darunter als dritte die Take-Profit-Regel (#49). Merkkasten im Blocksatz mit reduzierter Trennneigung (#123).

**Seite 6 – Plattform** (#45, #49, #65)

- Überschrift: **„Der Reiter „New Pending Order““** (Claude schrieb „Der Reiter“ statt „Das Fenster“, weil das Fenster oben „NEW ORDER“ heißt) (#65).
- **Vektor-Nachbau des Order-Fensters** (Variante A „Exakt“, Inter, Maße aus 3.5), Ziffern 1–5 im Fenster, zahlenfreie Felder („deine Menge“, „dein Wert“, „dein Ziel“), Chartbild als Vektor.
- Fünf nummerierte Punkte; laut #15 gehören dazu der Reiter „New Pending Order“, das Type-Dropdown, das At-price-Feld, der Take-Profit-Schalter und der grüne Button. ⚠ Die genaue Zuordnung im Endstand ist nicht belegt.
- **Regelkästen**: z. B. „At price unter dem Kurs · Take-Profit über At price“ (#49).
- Abschnitt **„Das Type-Menü und die Regel dahinter“**: links der Ausschnitt des aufgeklappten Type-Menüs (eigener Ausschnitt, nicht im Hauptfenster, weil er das At-price-Feld verdecken würde), rechts für jeden Type, wohin At price und Take-Profit gehören (#49).
- ⚠ Der Nutzer nennt diese Seite einmal „Seite 5“ (#44, #46); Claude hat sie als Seite 6 geführt (#45).

### 4.4 Geschützte Fassung

Fertig (#121, #123, #125): ToUnicode vergiftet (11 von 11 Tabellen), AES-256, alle neun Rechte gesperrt, P = −3904, PDF-Version 2.0, Pixelabweichung 0, 112 kB. Details in Abschnitt 6.3.

---

## 5. Dokument 2 – „Schulungseinheit 1: Kontogrundlagen & Kosten“ (9 Seiten)

> **Seitenzählung (seit 02.10.2026, Commit `5f9d129`):** 8 Seiten. Neu ist S. 2 „Grundbegriffe“; alle Seiten ab „Kontostand“ rücken um 1 (alt 2 → neu 3 … alt 7 → neu 8; Tabelle in Abschnitt 17). Angepasst sind die Seitenangaben in 2.3, 5.3, 8, 13.2, 13.3, 14 und 16. Die Abschnitte **12** und **15** sowie alle mit „alte Zählung“ gekennzeichneten Prüfzeilen beschreiben den Stand mit 7 Seiten. Im Dokument selbst gibt es keine Seitenzahlen (2.3); dort heißen die Seiten nach ihrem Titel (Kicker).
>
> **Seit `0850815`: 9 Seiten.** Neu ist S. 8 „Instrumente und Positionen“; „Auf einen Blick“ wird S. 9 (Tabelle in Abschnitt 18). S. 1–7 behalten ihre Nummer. „S. 8“ für „Auf einen Blick“ in den Abschnitten 13.3 und 17 meint die 8-Seiten-Zählung.

### 5.1 Themenliste des Nutzers (#126, wörtlich)

> **Schulungseinheit 1 – Kontogrundlagen & Kosten**
> Ziel: Dem Kunden ein solides Verständnis der Kontokennzahlen, des Handelskapitalmanagements und der handelsbezogenen Kosten vermitteln.
>
> 1. **Kontostand** – Was der Kontostand darstellt. Unterschied zwischen eingezahltem Guthaben und aktuellem Kontowert.
> 2. **Gewinn & Verlust (GuV)** – Verständnis von variablen (unrealisierten) Gewinnen/Verlusten. Verständnis von realisierten (geschlossenen) Gewinnen/Verlusten. Wie sich die GuV auf die Gesamtperformance des Kontos auswirkt.
> 3. **Margin** – Definition der Margin. Warum eine Margin zum Eröffnen von Positionen erforderlich ist. Zusammenhang zwischen Positionsgröße und Margin-Anforderung.
> 4. **Freie Margin** – Definition der freien Margin. Wie die freie Margin die verfügbare Handelskapazität bestimmt. Bedeutung einer ausreichenden freien Margin.
> 5. **Hebelwirkung** – Erklärung der Hebelwirkung und ihrer Funktionsweise. Vorteile und Risiken der Hebelwirkung. Auswirkungen der Hebelwirkung auf Exposure und Risiko.
> 6. **Swaps** – Berechnung von Swap-Gebühren bzw. -Gutschriften.

Stil: wie der Pending-Orders-Guide (gleiche Schrift, Seitenlogik, Farben, keine Zahlen), **nicht** wie das hochgeladene Referenzdokument (#126, #129, #147).
Plattform-Fakten aus dem Referenzdokument: Balance, Equity, Free Margin, Margin Level, **dreifacher Swap am Mittwoch** (#129).

**Neue Quelle (02.10.2026, Commit `848378e`):** `originals/Education_Session_1_Account_Basics_Kosten_2.pdf` ist die **Reverse-Engineering-Fassung** des Nutzers („Education Session 1: Account Basics & Costs – Komplett erklärt“; Plattform-Fakten mit „rekonstruiertem Plattform-Code“ und Formeln). Genutzt: Abschnitt 7.3 und 8 (Swap-Buchung, siehe 5.3 und 5.4) und 8.3 (Buchungsarten). Der Stil bleibt der des Pending-Orders-Guides (2.4). ⚠ Dort steht der Rollover „üblicherweise 22:00 UTC bzw. 0:00 Serverzeit“; im Dokument gilt die Angabe des Nutzers: **23:00 Uhr Amsterdamer Zeit**.

### 5.2 Wo die Werte auf der Plattform stehen (Angaben des Nutzers, #134)

- **Desktop:** Kontowerte in der **untersten Leiste ganz unten rechts**. Die Positionen stehen direkt auf dem ersten Bildschirm. Instrument-Infos (Swap, Hebel …) über das **Info-Zeichen beim Instrument**.
- **Mobile:** **Info-Zeichen oben rechts** → „Information“ erscheint → oben rechts **Balance** → dort steht alles. Im Reiter **Information** stehen Leverage und Stop out (#153).
- Claudes Zusammenfassung (#147): „Desktop unterste Leiste und Info-Zeichen beim Instrument, Mobile Info-Zeichen oben rechts, dann Balance beziehungsweise Information, Positionen unter Orders.“
- **Belegt per DOM (02.10.2026, `docs/plattform/dom-kursliste-instrument-info.md`, `dom-positionsliste.md`):**
  - **Angaben eines Instruments** (Swap long, Swap short, Spread, Leverage u. a.): Desktop über das **Info-Zeichen am Ende der Zeile in der Kursliste** (öffnet ein Fenster), mobil **Quotes → Kategorie → Instrument antippen** (Angaben klappen auf). Kategorien: Forex, Stocks, Cryptos, Indices, Energies, Metals, Commodities, ETFs (am Desktop in der Kursliste, mobil als Reiter unter Quotes).
  - **Liste der offenen Positionen:** Desktop Tabelle unter dem Chart mit den Reitern Active/Pending/History, mobil dieselben Reiter unter Orders; Antippen einer Position klappt ihre Angaben auf. Spalten am Desktop u. a. Amount (Menge), Trade volume (Wert), Swap, Commission, Total Profit, Margin.
  - Übergaben: `kg-instrument-info-wege.md`, `kg-seite-instrumente.md`. Bid/Ask werden nicht genannt (2.2).

### 5.3 Seite für Seite (Stand #151/#157, nachgeführt bis 02.10.2026; Zählung mit 9 Seiten)

1. **Deckblatt** – Konto-Anatomie als Bild: Balance + Profit/Losses ergibt Equity; Equity teilt sich in Margin und Free; darunter Level als Verhältnis (#147). Seit 02.10.2026 (`5f9d129`): „Leverage (Hebel)“, ein Satz mit Verweis auf die Abbildung unter „In der Plattform“, „aktueller Kontowert“, Level-Hinweis mit „mehr dazu unter „Margin““.
2. **Grundbegriffe** (neu 02.10.2026, Commit `5f9d129`, Übergabe `docs/uebergaben/kg-grundbegriffe.md`) – Tabelle **Begriff | Erklärung | Mehr dazu**. Zeilen: Instrument, Kurs, Position, Buy/Sell, Volumen, Broker, Plattform; Margin, Stop out, Leverage (Hebel; „1:10 bedeutet: Die Margin beträgt ein Zehntel des Volumens“), Swap und **Bonus** („Ein Betrag auf Ihrem Konto, mit dem Sie handeln können. Gewinne, die Sie damit erzielen, sind gemäß den AGB des Brokers auszahlbar.“). Die Zeile hieß zuerst „Commission (Provision)“ und wurde mit `e70e62e` ersetzt (keine Commission auf der Plattform). Dazu ein Merk-Kasten „Zur Schreibweise“. Spalte „Mehr dazu“ = Seitentitel mit Pfeil („→ Kontostand“, „→ Margin“, „→ Hebel“, „→ Swaps“, „→ In der Plattform“; Spaltenbreiten 30 + 102 + 29,5 mm). Broker-Zeile: „Anders als beim Direktkauf erwerben Sie das Instrument dabei nicht selbst.“ (ohne „Bank“; „Bank“ steht nur noch auf der Hebel-Seite). „Wertpapierdepot“ wird nirgends erklärt (8.4). Nachtrag 3: Instrument „… aus der Kategorie Forex (Devisen)“ (`25049f5`); Zeile **Spread** „Der Unterschied zwischen dem Kurs für Buy und dem Kurs für Sell; er steht in den Angaben des Instruments.“ (`c1e2878`, ersetzt die kurzzeitige Zeile Bid / Ask), Verweis → Instrumente und Positionen; Leverage und Swap mit je einem zweiten Verweis dorthin; Swap „in ihrem Total Profit enthalten“ (`0850815`).
3. **Kontostand** (alt S. 2; deckt Themen 1 und 2 ab) – Balance („was fest ist“) gegen Equity („was jetzt gilt“) als zwei Kästen; Grafik mit Position im Plus und im Minus; unten der Weg von schwebend zu fest: öffnen → Kurs bewegt sich → schließen (#147). Seit 02.10.2026: Lead mit „(Abbildung unter „In der Plattform“)“; Balance-Kasten „Der Swap einer Position geht beim Schließen mit ihrem Ergebnis in die Balance ein.“ (zuerst mit Commission, mit `e70e62e` bereinigt); Merk: Kontowert = Equity. Seit `0850815`: Die Plattform „weist ihn bei der Position unter Total Profit aus, das Ergebnis aller offenen Positionen zusammen unter Profit/Losses. Er fließt in die Equity ein …“.
4. **Margin** (alt S. 3; Themen 3 und 4) – Margin, Free, Level nebeneinander; Balken in drei Zuständen (eine Position, mehrere, Positionen im Minus); Level-Skala „Normalbereich“ → Warnbereich → Stop out (Wortwahl seit Abschnitt 15). **Stop-out-Wert bewusst nicht genannt**, Verweis auf das Feld unter „Information“ („siehe „In der Plattform““), weil er je Konto anders sein kann (#147). Seit 02.10.2026: „Sicherheit für mögliche Verluste“, Verweise per Titel, „Positionen mit höherem Volumen“.
5. **Hebel** (alt S. 4; Thema 5) – Stand 02.10.2026 (Abschnitt 14, Feinschliff `e70e62e`): Direktkauf über die Bank gegen Broker mit Hebel 1:10 in zwei Tabellen „Öffnen/Schließen der Positionen“, darunter zwei neutrale `soft`-Kästen („Auswirkung auf die Margin“ / „Auswirkung auf Kursbewegungen“) und der Merk-Kasten „Wo der Hebel steht“; ohne Grafik, ohne Grün/Rot. Feinschliff: **je 2.000 € verfügbar**, **je 1.000 € eingesetzt** (Einsatz bzw. Margin), neue Zeile „Auf dem Konto frei verfügbar (Free)“ (– | 1.000 €), „Geliehener Betrag (Volumen minus Margin)“, „vor/nach Swap“ statt „vor Kosten“, Swap-Zelle „Swap: 7 € pro Nacht (→ Swaps)“, Hinweis „Alle Beträge sind fiktiv und dienen ausschließlich der Veranschaulichung.“. ⚠ Überholt: die Fassung nach #147 („ohne“/„mit“ als Grafik, Vor- und Nachteil als zwei Kästen; Grafik „ohne Hebel“ bewusst winzig). Merk-Kasten seit `25049f5`/`0850815`: Der Hebel eines Instruments steht in dessen Angaben „(Abbildung unter „Instrumente und Positionen“)“.
6. **Swaps** (alt S. 5; Thema 6) – seit 02.10.2026 nach dem **Modell des Nutzers** und seiner Skizze `originals/skizze-hebel-swap.png` (ersetzt die Fassung nach #148/#151 mit „geliehen“ und Geldmarkt-Zins):
   - Lead (Stand `ac919eb`): „Bleibt eine Position über Nacht offen, verlangen der Liquiditätsanbieter – das Finanzinstitut, über das der Broker seine Positionen abwickelt – und der Broker dafür je einen Betrag. Zusammen werden sie als Swap gebucht.“ **Begriff entschieden (Nutzer, 02.10.2026) und umgesetzt:** Auf dieser Seite heißt es **„Liquiditätsanbieter“** statt „Bank“ (Lead, Erläuterungsabsatz, Klammer „Betrag des Liquiditätsanbieters: 6 €“). Auf der **Hebel-Seite** bleibt „Bank“ (Direktkauf des Bekannten über das Wertpapierdepot seiner Bank).
   - Das Modell: Der **Liquiditätsanbieter** berechnet bei Rohstoffen (z. B. Crude Oil, Natural Gas) eine **Miete für die Aufbewahrung**; bei Devisen treten an ihre Stelle die **Zinsen für das geliehene Geld**. Dazu kommen ein **Risikoanteil** (soll den Liquiditätsanbieter vor Verlusten schützen) und der **Aufschlag des Brokers**.
   - **Rechenbeispiel** unter `\Htwo` „Zusammensetzung des Swaps“: „Angenommen, Sie halten eine Position im Rohstoff **Crude Oil (Rohöl)** mit einem Volumen von 10.000 €.“ – seit `e70e62e` eine **eigene Position**, nicht mehr das Instrument XY der Hebel-Seite (dessen Bekannter kauft XY über sein Wertpapierdepot). Balken maßstäblich (Margin 17 von 170 mm = 1:10), Maß oben „Ihre Position in Crude Oil: 10.000 €“, unten „Margin: 1.000 € bei Hebel 1:10 ein Zehntel der Position“; Pfeil „pro Nacht“; Summenzeile (`\hthree`, Klammern `greya`) Miete für die Aufbewahrung + Risikoanteil + Aufschlag des Brokers = Swap, darunter **3 € · 3 € · 1 € · 7 € pro Nacht**; zweite Stufe: Klammer **„Betrag des Liquiditätsanbieters: 6 €“** unter den ersten beiden, Klammer **„Betrag des Brokers: 1 €“** unter dem Aufschlag. Unter der Formel: „Die Beträge sind fiktiv und dienen ausschließlich der Veranschaulichung.“ Kein Grün/Rot. Danach ein Absatz zu Miete (Rohstoffe wie Crude Oil, „Natural Gas (Erdgas)“) bzw. Zinsen (Devisen, „Devisen (Währungen, z. B. EUR/USD)“) und Risikoanteil.
   - Der Moment der Buchung: den ganzen Tag nichts, zum **Tageswechsel** alles auf einmal; wer eine Minute vorher schließt, zahlt nichts. Der Zeitstrahl nennt links der Stufe „**Tageswechsel um 23:00 Uhr (Amsterdamer Zeit)**“ (Angabe des Nutzers; die Reverse-Engineering-Fassung nennt 22:00 UTC / 0:00 Serverzeit, siehe 5.1), rechts „Swap wird gebucht“ (beides `sell`, fett); sonst überall nur „Tageswechsel“.
   - **Wohin der Swap gebucht wird** (geklärt 02.10.2026, Quelle 5.1, Abschnitt 7.3/8): Er wird **bei der offenen Position verbucht**, in der Spalte **Swap** ausgewiesen und ist in ihrem **angezeigten Profit enthalten**; beim **Schließen** geht er mit dem Ergebnis der Position in die **Balance** ein. Merk-Kasten der Seite und die Texte auf „Kontostand“ und „Auf einen Blick“ sind darauf abgestimmt. Seit `0850815` heißt der angezeigte Profit **Total Profit** (Merk „in ihrem Total Profit enthalten“; belegt `834863a`, 2.2). Devisen-Beispiel seit `25049f5`: „bei Forex (Währungen, z. B. EUR/USD)“.
   - Wochen- und Satztexte: Woche mit einem Punkt pro Nacht, **am Mittwoch drei** (Notiz „am Mittwoch wird der Swap für das Wochenende mitgebucht“); **Swap long** (für Buy) und **Swap short** (für Sell) stehen bei jedem Instrument (seit `0850815`: „Die tatsächlichen Sätze stehen bei jedem Instrument (→ Instrumente und Positionen)“; im Text nicht mehr „Info-Fenster“, 2.2); „In der Regel sind beide negativ, was eine Belastung bedeutet; ist ein Satz positiv, wird Ihnen der Betrag gutgeschrieben.“ (**negativ = Belastung, positiv = Gutschrift**; keine Einheit genannt; der Satz **bleibt**, Nutzerentscheidung 02.10.2026). ⚠ Die frühere Abweichung von der Skizze („Beträge weggelassen“) entfällt.
7. **In der Plattform** (alt S. 6) – oben die **mobile Kontoübersicht** als Vektor-Nachbau (blaues Design, Maße 3.6) mit fünf Nummern (Equity, Profit/Losses, Margin, Free, Level) und „Konto jetzt“ statt einer Summe; darunter dieselben Werte als **Desktop-Leiste** (blaues Design, teils geschätzt). Unter der Leiste der Hinweis, dass **Level am Desktop fehlt** (#151, #157). ⚠ **Falsch** laut DOM-Messung vom 02.10.2026: Level steht auch am Desktop; Leiste und Hinweis sind korrigiert (Abschnitt 12). Seit 02.10.2026 zeigt die mobile Ansicht auch Kopf- und Reiterleiste mit den Marken A (Info-Zeichen) und B (Reiter Balance) (Abschnitt 12). Die **Markennummern 1–5** gelten als Wegweiser (Ausnahme 1, Abschnitt 2.3). Nachbauten und ihre Wörter statt Beträge sind unverändert.
   - Seit `145c398`: Lead um „In beiden Abbildungen stehen anstelle der Beträge Wörter, die den jeweiligen Wert umschreiben.“ ergänzt. Notiz rechts: „Ganz oben steht die Balance, am Ende folgen die Felder Bonus und Credit. Der Bonus ist ein Betrag, mit dem Sie handeln können; Gewinne, die Sie damit erzielen, sind gemäß den AGB des Brokers auszahlbar.“ (Credit nur genannt; der frühere Satz „… ohne Bedeutung“ ist entfallen). Desktop-Kasten: nur „Spalte Swap“ (keine Commission), „Chart (der grafischen Darstellung des Kursverlaufs)“, „Kursliste, der Liste der Instrumente mit ihren aktuellen Kursen“. Mobile-Kasten: „Unter Orders → Active steht die Liste Ihrer offenen Positionen; …“.
   - Nachtrag 3 (`25049f5`, `c1e2878`, `0850815`; Übergaben `kg-instrument-info-wege.md`, `kg-seite-instrumente.md`): Desktop-Kasten nennt die Kursliste mit den acht Kategorien, „Jede Zeile zeigt die aktuellen Kurse des Instruments; das Info-Zeichen am Ende der Zeile öffnet seine Angaben.“; Leistennotiz ohne die Doppelung „dieselben Werte wie die mobile Ansicht“. Mobile-Kasten: „Das Info-Zeichen oben rechts öffnet zunächst den Reiter Information mit Leverage und Stop out.“, Quotes mit denselben Kategorien als Reiter, Antippen klappt die Angaben auf. Doppelungen zur neuen S. 8 (Spalte Swap, Swap/Margin, Feldliste) gekürzt, je ein Verweis → Instrumente und Positionen. Rest ca. 9,4 pt.
8. **Instrumente und Positionen** (neu, `0850815`, Label `s:instrumente`; Übergabe `docs/uebergaben/kg-seite-instrumente.md`) – Titel „Die Angaben der Instrumente und Ihrer Positionen“, Lead mit Verweis auf die Wörter statt Beträge wie unter „In der Plattform“. Oben `info-desktop.pdf` und `info-mobil.pdf` im selben Maßstab (1 px = 0,225 mm, Schrift 7,7 pt; Desktop-Fenster 65,3 × 43,8 mm, Schatten als Overlay über den Satzrand; mobil 92,3 × 73,6 mm), Überschriften DESKTOP/MOBILE mit je einem Satz zum Weg, Legende 1–3 (Swap long „Satz des Swaps für Buy“, Swap short „… für Sell“, Leverage „Hebel des Instruments“). Unten „Die Liste der offenen Positionen“ als Text: Reiter Active/Pending/History (Desktop unter dem Chart, mobil unter Orders) und Tabelle Angabe | Bedeutung | Mehr dazu mit Amount (Menge), Trade volume (Wert = Volumen), Swap (in Total Profit enthalten), Total Profit (Ergebnis inkl. Swap; alle zusammen unter Profit/Losses), Margin; kein S/L, keine Commission. Rest ca. 79 pt (28 mm) für einen späteren Nachbau der Positionsliste (8.4).
9. **Auf einen Blick** (alt S. 7, bis `0850815` S. 8; in #151 „Spickzettel“, seit Abschnitt 15 „Auf einen Blick“) mit allen Begriffen. Er bekam eine eigene Seite, weil die Plattform-Seite sonst überladen war (#151). Seit 02.10.2026: Balance-Zeile „Bei Schließen sowie Ein- und Auszahlung“ (`5f9d129`); neue Zeilen **Stop out** („Schwelle des Levels, an der die Plattform Positionen selbstständig schließt“ | „Fest je Konto“) und **Bonus** („Betrag, mit dem Sie handeln können; Gewinne daraus sind gemäß den AGB auszahlbar“ | Spalte „Änderung“: „–“, die erste Angabe „Nach den AGB des Brokers“ war nicht belegt); Leverage „Verhältnis von Margin zu Volumen; bei 1:10 beträgt die Margin ein Zehntel des Volumens“; Swap „Belastung oder Gutschrift für das Halten über Nacht; bei der Position verbucht, beim Schließen in der Balance“ (vorher „Kosten für das Halten über Nacht“, davor „Zinsen für …“). ⚠ Stop out „Fest je Konto“ stützt sich auf 5.3/#147 (Wert je Konto verschieden), vom Nutzer nicht bestätigt (8.4). Seit `0850815` neue Zeile **Total Profit** („Ergebnis einer offenen Position einschließlich ihres Swaps“ | „Mit jeder Kursbewegung und jedem Swap“).

Fußzeile (seit 02.10.2026, S. 2–9 und Fuß des Deckblatts): „KONTOGRUNDLAGEN & KOSTEN · EDUCATION – STANDARD PACKAGE“ (vorher „… · SCHULUNGSEINHEIT“), **ohne Seitenzahl** (2.3). Die Oberzeile des Deckblatts „SCHULUNGSEINHEIT“, der Lead und der `pdftitle` bleiben. PDF-Metadaten (`145c398`, `3b34934`): `pdftitle={Kontogrundlagen \& Kosten – Schulungseinheit}` (das `\&` ist nötig, sonst zeigte der Titel „Kontogrundlagen  Kosten“), `pdfsubject={Balance, Equity, Margin, Free, Leverage, Swap}` („Free“ statt „Free Margin“).

**Verweise zwischen den Seiten (Stand `0850815`):** keine Seitenzahlen, sondern der Seitentitel (Kicker). Makros in `Kontogrundlagen-Kosten.tex`, Labels `s:grundbegriffe`, `s:kontostand`, `s:margin`, `s:hebel`, `s:swap`, `s:plattform`, `s:instrumente` (seit `0850815`), `s:ueberblick` jeweils hinter dem `\kicker`: `\titel{label}{Titel}` → „Titel“ im Fließtext (z. B. „(Abbildung unter „In der Plattform“)“, „mehr dazu unter „Margin““); `\pfeil{label}{Titel}` → „→ Titel“ (Hebel-Seite: „Swap: 7 € pro Nacht (→ Swaps)“); `\verw{label}{Titel}` wie `\pfeil`, aber in `muted` (Spalte „Mehr dazu“ der Grundbegriffe). Alle sind unsichtbare Links (`hidelinks`), der Titel bricht nicht um (`\mbox`). Die Zwischenstufe `\seite`/`\verw` mit „S. n“ (`5f9d129`) und die Fußzeile „n / 8“ (`145c398`) sind entfernt. Bei neuen Verweisen den Titel nennen, nie eine Zahl; wird eine Seite umbenannt, sind die Verweistexte nachzuziehen.

Geprüft (#147): null Rasterbilder, alle Schriften eingebettet; die geschützte Fassung liefert null echte Wörter, neun Rechte gesperrt. ⚠ Ob nach den Änderungen in #151–#157 die geschützte Fassung neu erzeugt wurde, steht nicht im Text.

### 5.4 Offene Fragen in Dokument 2

- **Blaues vs. graues Design:** Der Handy-Screenshot zeigte zuerst dunkelgrau, der Konsolenbericht Dunkelblau `#04273C` (#155). Ein weiterer Screenshot des Nutzers bestätigte Blau für Mobile (#156, #157). Die Desktop-Leiste im Screenshot ist **grau `#181818`** (#157) → die Plattform hat offenbar zwei Designs. Claude hat **beides im blauen Design** gebaut, damit es zum Order-Fenster passt. Falls Kunden hauptsächlich Grau sehen: „eine Zeile Änderung“ (#155). Der Nutzer fragte „wollen wir lieber die von Desktop nehmen??? die Leiste“ (#156); Claude nahm beide. ⚠ Keine abschließende Entscheidung des Nutzers.
- ~~**Geschätzte Werte in der Desktop-Leiste**~~ → erledigt: gemessen (02.10.2026, `originals/messungen/kontoleiste-desktop.json`), Leiste neu gebaut (Abschnitt 12).
- ~~**Level fehlt am Desktop**~~ → **falsch**: Die Desktop-Leiste zeigt alle acht Felder (Balance, Equity, Profit/Losses, Margin, Free, Level, Bonus, Credit). Der Hinweis unter der Leiste ist korrigiert.
- ~~**Instrument-Info-Feld** (Swap long, Swap short, Contract size, Leverage) noch nicht gemessen~~ → **erledigt (02.10.2026):** Desktop und mobil gemessen (`originals/messungen/instrument-info-desktop.json`, `…/instrument-info-mobil.json`), nachgebaut und auf „Instrumente und Positionen“ eingebunden; Hebel- und Swap-Seite verweisen dorthin (5.3, Abschnitt 18). Das Desktop-Fenster zeigt Symbol, Swap long, Type, Swap short, Spread (bei Gold „Floating Points“), Digits, Commission, Leverage, Contract size (`docs/plattform/dom-kursliste-instrument-info.md`); mobil kommen u. a. Gap Level und Stop Level hinzu (`info-mobil.tex`). Damit ist auch Rückfrage 2 aus `kg-instrument-info-wege.md` beantwortet.
- ~~**Total Profit = Summe in Profit/Losses**~~ (offen in `kg-seite-instrumente.md`) → **belegt** (`834863a`, Abgleich am Screenshot des Nutzers ohne Kontodaten, `docs/plattform/dom-positionsliste.md`): Profit/Losses ist die Summe der Total-Profit-Werte, Total Profit enthält den Swap.
- **Mobile, Reiter Information** (Leverage, Stop out): optional, ein Screenshot existiert schon (#153). Bild Prio 3 in 8.4 (Desktop-Weg unbekannt).
- ~~**Wohin der Swap gebucht wird**~~ (Widerspruch 1 der Prüfung `docs/pruefung/kontogrundlagen-begriffe-bilder.md`) → **geklärt (02.10.2026):** Beleg ist die Reverse-Engineering-Fassung (Abschnitt 7.3 und 8; Quelle in 5.1): Der Swap wird beim Rollover auf die offene Position geschrieben und ist im angezeigten Profit enthalten; in die Balance geht er beim Schließen ein. Eine eigene Messung liegt im Repo nicht vor. Texte siehe 5.3 (Swaps).
- ~~**Commission**~~ → gestrichen: Auf der Plattform gibt es keine Commission (Nutzer, 02.10.2026). Die Reverse-Engineering-Fassung nennt (8.3) eigene Buchungsarten „Commission In/Out“ und „Broker Commission“; im Dokument werden sie nicht verwendet. Die frühere Rückfrage, ob die Commission nur mit dem Ergebnis in die Balance geht, ist damit hinfällig.
- ~~**Seitenzahlen in Doku 2**~~ → bleiben entfernt, Verweise per Seitentitel (2.3, 5.3).
- ~~**Rechenbeispiel-Kasten** zur Swap-Skizze~~ → erledigt (02.10.2026): Rechenbeispiel 3 € + 3 € + 1 € = 7 € pro Nacht steht auf S. 6 (Abschnitt 5.3).
- **Textfarbe:** Claude merkte in #153 an, dass der Bericht aus #150 Schwarz meldete, der Screenshot aber Weiß zeigt. Deshalb ermittelt der neue Befehl die effektive Hintergrundfarbe.

---

## 6. Technik

### 6.1 Build-Pipeline

- **XeLaTeX** + **TikZ** + **tcolorbox** + **fontspec** (#25). Charts und Nachbauten als TikZ/Vektor.
- Generatoren in **Python**: Im Verlauf werden Module/Dateien `gen`, `design`, `demo.py` und `chart.tex` erwähnt (#35). Charts entstehen **datengetrieben** aus einer Tabelle (#13). ⚠ Die genaue Dateistruktur ist nicht im Export.
- **Datengetriebene Prüfung mit Build-Abbruch** (#13, #49): Vor jedem Bau wird geprüft, dass
  1. der At price auf der richtigen Seite des Kurses liegt (Buy Limit/Sell Stop darunter, Sell Limit/Buy Stop darüber),
  2. der Pfeil bzw. Weg zum At price in die richtige Richtung zeigt,
  3. der Pfeil bzw. die Richtung danach stimmt (Buy hoch, Sell runter),
  4. der **Take-Profit bei Buy über und bei Sell unter dem At price** liegt.
  Schlägt eine Prüfung fehl, bricht der Build ab.
  ⚠ Seit die Charts die Plattformbilder sind (#81), betrifft die Prüfung vor allem die ergänzten At-price-/Take-Profit-Linien und die Texte; wie sie genau angepasst wurde, steht nicht im Text.
- **Vektorisierung der Plattform-Chartbilder:**
  - Version 1: Konturverfolgung (38 Formen, später 304 Vektorpfade, #43, #81). **Verworfen**, weil die Kanten bei 600 dpi wellig waren (#100, #101).
  - **Endstand:** Zerlegung in Grundformen, pro Bild **37 Rechtecke, 2 Kreise, 1 Dreieck**; Kanten aus der Randdeckung subpixelgenau. Behobene Fehler: zu viele Balken als Marker erkannt; oberste Kugelzeilen als Stiel gewertet; Balken, der den Stiel überlappt (#101). Die Datei wurde dadurch kleiner.
  - Auch die ×-Zeichen im Fenster sind gezeichnete Formen statt Glyphen (#43); im Fenster-PDF steckt nur Inter.
- **Druck-Prüfungen** (#45, #59): `pdfimages` findet **null** Rasterbilder; alle Schriften eingebettet; Rendering bei 600 dpi und Zoom; **Stream-Kompression abgeschaltet** (für ältere Druck-RIPs); **keine Transparenz** (weiche Schatten entfernt); feine helle Umrandung um die Grafiken bleibt.
- **Layout-Prüfungen:** keine Überlängen/Seitenüberläufe (sonst entstehen zusätzliche Seiten, z. B. 8 statt 6 in #85, 7 statt 6 in #149); Starthöhe **20,5 mm** auf jeder Seite nachgemessen (#99).
- Dateigrößen (Doku 1): 319 kB (#45) → 428 kB mit Konturpfaden (#81) → kleiner mit Grundformen (#101); geschützt 112 kB (#121).

### 6.2 Bekannte Fallstricke

- **fontspec + PGF-Rekursion** (`\pgf@selectfontorig` → TeX capacity exceeded) bei `font=\lbl` in TikZ-Nodes, wobei `\lbl` = `\fontsize{7.4}{9}\selectfont`, kombiniert mit `\bfseries` im Node-Inhalt (#35). Lösung: **kein Größenmakro in `font=`**, sondern direkte `\fontsize`-Angaben bzw. Schrift im Node-Inhalt setzen. Mitursache damals: durch String-Replace kaputtes TeX (doppeltes `\end{tikzpicture}`, verschachtelte tikzpicture-Umgebungen).
- **Escaping**: TeX in Python-Strings – `sed`/Replace griffen wegen falscher Backslash-Ebenen nicht (#35, #85). Lieber Dateien sauber neu schreiben.
- **`pdfcrop` fehlte** in der alten Sandbox (Exit 127) (#35).
- **Blocksatz-Dehnung** in schmalen Spalten → gedehnte Wortabstände und Trennungen wie „Ak-tivierungspunkt“. Lösung: Flattersatz (`\raggedright`) und keine Worttrennung in schmalen Kästen und Einleitungen; Blocksatz nur bei voller Breite, mit gesenkter Trennneigung (#123).
- **Deckblatt sitzt tiefer**: Ein erzwungener Leerraum am Seitenanfang verschob es um ca. 4 mm; er wurde entfernt (#99).
- Labels in Charts können Kerzen überlappen → weißer Untergrund unter allen Beschriftungen (#89).
- Ein Menü, das über dem At-price-Feld aufklappt, verdeckt Schritt 3 → Menü als separater Ausschnitt (#49).
- **Hinweis für Agenten (Stand 02.10.2026):** In der aktuellen Umgebung erzeugt `scripts/build.sh` beim Neubau von `bar.pdf`/`mobil.pdf` leicht abweichende Dateien (vermutlich andere Schrift-/TeX-Versionen). Für Einzelprüfungen deshalb direkt mit `xelatex -output-directory=build/<ordner>` bauen und die eingecheckten Grafik-PDFs (`bar.pdf`, `mobil.pdf`) **nicht versehentlich mitcommitten** (nur eigene Dateien explizit stagen).

### 6.3 Schutz-Fassung (`*_GESCHUETZT.pdf`)

Vorgabe des Nutzers (#118, #120):

| Anforderung | Umsetzung laut Nutzer-Tabelle (#120) |
|---|---|
| Kopieren blockiert | AES-256, Extraktions-Flag „verboten“ |
| Drucken verhindert | Druck-Flags (niedrig + hoch) „verboten“ |
| Google Translate → Salat | ToUnicode-Maps ersetzt (Nutzer-Tabelle spricht von 27 Fonts) |
| Word/.txt → leer/unbrauchbar | kein gültiger Textlayer |

**Umsetzung (Endstand #121, #123, #125):**

1. Verworfener erster Ansatz (#119): Ghostscript, Text in Kurven → OCR hätte trotzdem viel erkannt, ca. 1 % Pixelabweichung durch Kantenglättung.
2. **ToUnicode-Vergiftung**: Die ToUnicode-Tabellen **aller** Schriften werden ersetzt – über **alle Objekte des Dokuments**, nicht nur über die Seitenressourcen. Wichtig: Die Inter-Schriften des Order-Fensters liegen in einer verschachtelten Grafik (eingebettetes PDF, Form-XObject) auf Seite 6; im ersten Durchlauf rutschten dort „Pending“, „Order“, „Kurs“, „price“ und „Profit“ durch (#121). Ergebnis: **11 von 11** Tabellen ersetzt, Extrakt z. B. `MqZdahd I dqfhdz Zdhh cawuwwr…`, null echte Wörter (pdftotext + pypdf).
3. **AES-256**-Verschlüsselung; Drucken (beide Flags) und Kopieren „not allowed“.
4. **„Content copying for accessibility“ aus**: qpdf ignoriert dieses Flag („is ignored for modern encryption formats“) → Berechtigungswert **P direkt gesetzt: von −3392 auf −3904** (Differenz = Barrierefreiheits-Bit). Alle neun Rechte stehen auf „verboten“ (#125).
5. **PDF-Version von 1.3 auf 2.0** korrigiert (1.3 passte nicht zu AES-256) (#125).
6. **Pixelvergleich** Original vs. geschützt: maximale Farbabweichung **0** auf allen Seiten (#121, #123, #125).
7. Das Skript (laut Aufgabenstellung `scramble.py`, ⚠ Name nicht im Export) soll **nach jeder Textänderung erneut über die frische PDF** laufen (#121).
8. **Werkzeug seit 02.10.2026:** `python3 tools/schutz.py build/<Name>.pdf build/<Name>_GESCHUETZT.pdf` setzt 2.–5. um (ToUnicode über alle Objekte, AES-256 R6 mit leerem Benutzerpasswort, P = −3904 direkt per pypdf, PDF 2.0) und prüft selbst (Seitenzahl/-größen, Pixelvergleich 100 dpi = 0, Extrakt ohne echte Wörter, `qpdf --show-encryption`, Header). Endet bei einem Fehler mit Code 1. Die PDFs in `build/` werden nicht eingecheckt.

**Grenzen** (vom Nutzer zur Kenntnis genommen): Berechtigungen sind nur eine Bitte an den Reader, der echte Schutz ist der vergiftete Textlayer; „Saving a copy“ lässt sich prinzipiell nicht abschalten; Vorlesesoftware für Sehbehinderte ist ausgesperrt, was je nach Land rechtlich relevant sein kann (#119, #121, #125).

---

## 7. Konsolenbefehle (JS) aus dem Verlauf

**Ablauf für den Nutzer:** In der Plattform die gewünschte Ansicht öffnen → **F12** → Reiter **Console** → Befehl einfügen → **Enter** → Ergebnis liegt in der Zwischenablage (`copy(...)`) → im Chat mit Strg+V einfügen (bei großer Ausgabe als .txt hochladen).
⚠ Die **Ausgaben** der Läufe (#36/#37, #41, #150, #154) sind nicht im Export; die daraus gewonnenen Werte stehen in Abschnitt 3.

### 7.1 Universeller Messbefehl (#153) – **als Nächstes verwenden**

Erkennt selbst, welcher Bereich offen ist (`kontoleiste-desktop`, `instrument-info`, `konto-mobil`, `reiterleiste`), misst Positionen, Größen, Farben und Schriften relativ zum Block und ermittelt die **effektive Hintergrundfarbe** (läuft nach oben, bis eine deckende Farbe kommt). Er soll **dreimal** laufen:

1. **Desktop, unterste Leiste** – im normalen Handelsfenster, **im blauen Design** (um die geschätzten Werte aus #157 zu ersetzen).
2. **Instrument-Info** – beim Instrument auf das Info-Zeichen klicken (Feld mit Swap long, Swap short, Contract size, Leverage offen), dann ausführen → Swap-Seite und Hebel-Seite.
3. **Mobile, Reiter Information** (Leverage, Stop out) – optional, falls am Handy keine Konsole verfügbar ist.

Am Anfang jeder Ausgabe steht `bereich`, also welcher Bereich erkannt wurde. ⚠ Die Selektoren sind geraten; wenn „Nichts gefunden“ kommt oder der falsche Bereich erkannt wird, die Liste `KAND` anpassen.

```js
(() => {
  const D = [document].concat([...document.querySelectorAll('iframe')].map(f => { try { return f.contentDocument } catch (e) { return null } }).filter(Boolean));
  const KAND = [
    ['kontoleiste-desktop', '.footer-balance, footer .balance, .bottom-bar, .status-bar'],
    ['instrument-info',     '.symbol-info, .instrument-info, .quote-details, .ngb-popover-body, .popover-body'],
    ['konto-mobil',         '.tab-pane.active.show, .dl-item'],
    ['reiterleiste',        '.nav-tabs, .mat-tab-labels']
  ];
  let root = null, was = null;
  for (const d of D) for (const [name, sel] of KAND) {
    const el = d.querySelector(sel);
    if (el && el.getBoundingClientRect().width > 60) { root = el; was = name; break; }
    if (root) break;
  }
  if (!root) { console.warn('Nichts gefunden. Bitte die gewünschte Ansicht öffnen und erneut ausführen.'); return; }

  // echte Hintergrundfarbe: nach oben laufen, bis eine deckende Farbe kommt
  const echterBg = el => { let n = el; while (n && n !== document.documentElement) { const c = getComputedStyle(n).backgroundColor; if (c && !/rgba\(0, 0, 0, 0\)|transparent/.test(c)) return c; n = n.parentElement; } return 'rgb(255,255,255)'; };

  const R = root.getBoundingClientRect(), r = n => Math.round(n * 10) / 10;
  const props = ['color','backgroundColor','borderTopColor','borderTopWidth','borderBottomColor','borderBottomWidth','borderLeftColor','borderLeftWidth','borderRadius','fontFamily','fontSize','fontWeight','letterSpacing','textTransform','opacity','textAlign','display','padding','margin','gap','width','height'];
  const nodes = [];
  (function go(el, tiefe) {
    if (tiefe > 12) return;
    const b = el.getBoundingClientRect();
    if (b.width >= 1 && b.height >= 1) {
      const s = getComputedStyle(el);
      const txt = [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).filter(Boolean).join(' ');
      const cls = el.getAttribute('class') || '';
      const eigenerBg = s.backgroundColor && !/rgba\(0, 0, 0, 0\)|transparent/.test(s.backgroundColor);
      if (txt || eigenerBg || parseFloat(s.borderTopWidth) > 0 || parseFloat(s.borderBottomWidth) > 0 || parseFloat(s.borderLeftWidth) > 0 || ['SVG','PATH','IMG','BUTTON','A','INPUT'].includes(el.tagName)) {
        const o = { t: el.tagName.toLowerCase(), c: cls.slice(0, 70), x: r(b.left - R.left), y: r(b.top - R.top), w: r(b.width), h: r(b.height) };
        if (txt) o.txt = txt.slice(0, 60);
        if (!eigenerBg) o.bgEffektiv = echterBg(el);
        props.forEach(p => { const v = s[p]; if (v && !['none','normal','0px','rgba(0, 0, 0, 0)','auto','start','row','0px 0px 0px'].includes(v)) o[p] = v; });
        nodes.push(o);
      }
    }
    [...el.children].forEach(k => go(k, tiefe + 1));
  })(root, 0);

  const out = JSON.stringify({ bereich: was, block: { w: r(R.width), h: r(R.height) }, seitenBg: echterBg(root), font: getComputedStyle(root).fontFamily, nodes }, null, 1);
  try { copy(out); console.log('✔', was, '—', nodes.length, 'Elemente kopiert'); } catch (e) { console.log(out); }
})();
```

### 7.2 Messbefehl Order-Fenster (#39)

Für das Fenster „New Order“, Reiter „New pending order“. Sucht `popup-new-order` bzw. `.modal-content` (auch in iframes) und liefert Modalgröße, Schrift und alle relevanten Elemente mit Position (x/y/w/h relativ zum Fenster), Text, Input-Wert, Bild-`src` und Styles. Daraus stammen alle Maße in 3.5.

```js
(() => {
  const docs = [document].concat([...document.querySelectorAll('iframe')].map(f => { try { return f.contentDocument } catch (e) { return null } }).filter(Boolean));
  let root = null;
  for (const d of docs) { root = d.querySelector('popup-new-order') || d.querySelector('.modal-content'); if (root) break; }
  if (!root) { console.warn('Nicht gefunden – bitte das Fenster offen lassen.'); return; }
  const R = root.getBoundingClientRect(), r1 = n => Math.round(n * 10) / 10;
  const props = ['backgroundColor','color','borderTopColor','borderTopWidth','borderRadius','fontFamily','fontSize','fontWeight','letterSpacing','textTransform','opacity','textAlign'];
  const nodes = [];
  (function walk(el) {
    const b = el.getBoundingClientRect();
    if (b.width >= 1 && b.height >= 1) {
      const s = getComputedStyle(el);
      const txt = [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).filter(Boolean).join(' ');
      const cls = el.getAttribute('class') || '';
      const keep = txt || ['INPUT','IMG','A','BUTTON'].includes(el.tagName)
        || (s.backgroundColor !== 'rgba(0, 0, 0, 0)' && s.backgroundColor !== 'transparent')
        || parseFloat(s.borderTopWidth) > 0 || /toggle|thumb|bar|price|line|arrow|counter/i.test(cls);
      if (keep) {
        const o = { t: el.tagName.toLowerCase(), c: cls.slice(0, 60), x: r1(b.left - R.left), y: r1(b.top - R.top), w: r1(b.width), h: r1(b.height) };
        if (txt) o.txt = txt.slice(0, 50);
        if (el.tagName === 'IMG') o.src = el.getAttribute('src');
        if (el.tagName === 'INPUT') o.val = el.value;
        props.forEach(p => { const v = s[p]; if (v && !['none','normal','0px','rgba(0, 0, 0, 0)','auto','start'].includes(v)) o[p] = v; });
        nodes.push(o);
      }
    }
    [...el.children].forEach(walk);
  })(root);
  const out = JSON.stringify({ modal: { w: r1(R.width), h: r1(R.height) }, font: getComputedStyle(root).fontFamily, nodes });
  try { copy(out); console.log('✔ Kopiert:', out.length, 'Zeichen /', nodes.length, 'Elemente'); } catch (e) { console.log(out); }
})();
```

### 7.3 Variante für die mobile Kontoübersicht (#150, vom Nutzer gesendet)

Angepasste Fassung von #39, die der Nutzer ausgeführt und als Befehl in den Chat gestellt hat („das ist für mobil“). Sucht `.tab-pane.active.show`, `.dl-item` oder `.user-balance`. Die Ausgabe (Werte in 3.6) kam in #154. Sie meldete die Textfarbe teils als Schwarz → deshalb wurde #153 mit effektiver Hintergrundfarbe gebaut.

```js
(() => {
  const docs = [document].concat([...document.querySelectorAll('iframe')].map(f => { try { return f.contentDocument } catch (e) { return null } }).filter(Boolean));
  let root = null;
  
  // Suche gezielt nach dem Balance-Block
  for (const d of docs) { 
    root = d.querySelector('.tab-pane.active.show') || d.querySelector('.dl-item') || d.querySelector('.user-balance');
    if (root) break; 
  }
  
  if (!root) { console.warn('Balance-Block nicht gefunden – bitte stelle sicher, dass der Balance-Tab offen ist.'); return; }
  
  const R = root.getBoundingClientRect(), r1 = n => Math.round(n * 10) / 10;
  const props = ['backgroundColor','color','borderTopColor','borderTopWidth','borderBottomColor','borderBottomWidth','borderRadius','fontFamily','fontSize','fontWeight','letterSpacing','textTransform','opacity','textAlign','display','flexDirection','justifyContent','alignItems','padding','margin'];
  const nodes = [];
  
  (function walk(el) {
    const b = el.getBoundingClientRect();
    if (b.width >= 1 && b.height >= 1) {
      const s = getComputedStyle(el);
      const txt = [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).filter(Boolean).join(' ');
      const cls = el.getAttribute('class') || '';
      
      // Filter: Nur Elemente mit Text, Background oder Border behalten
      const keep = txt || ['INPUT','IMG','A','BUTTON','DL','DT','DD','STRONG','SPAN'].includes(el.tagName)
        || (s.backgroundColor !== 'rgba(0, 0, 0, 0)' && s.backgroundColor !== 'transparent')
        || parseFloat(s.borderTopWidth) > 0 || parseFloat(s.borderBottomWidth) > 0 
        || /balance|dl-item|color-green|tab-pane|custom-scroll/i.test(cls);
        
      if (keep) {
        const o = { t: el.tagName.toLowerCase(), c: cls.slice(0, 60), x: r1(b.left - R.left), y: r1(b.top - R.top), w: r1(b.width), h: r1(b.height) };
        if (txt) o.txt = txt.slice(0, 50);
        props.forEach(p => { const v = s[p]; if (v && !['none','normal','0px','rgba(0, 0, 0, 0)','auto','start','row'].includes(v)) o[p] = v; });
        nodes.push(o);
      }
    }
    [...el.children].forEach(walk);
  })(root);
  
  const out = JSON.stringify({ block: { w: r1(R.width), h: r1(R.height), x: r1(R.left), y: r1(R.top) }, font: getComputedStyle(root).fontFamily, nodes }, null, 2);
  
  try { 
    copy(out); 
    console.log('✔ Kopiert:', out.length, 'Zeichen /', nodes.length, 'Elemente'); 
  } catch (e) { 
    console.log(out); 
  }
})();
```

### 7.4 Suche nach höher aufgelösten Chartbildern / SVGs (#71)

Probiert für die vier Bilder `img-pending-order-{bl,sl,bs,ss}` die Endungen `.svg`, `@2x.png`, `@3x.png`, `-2x.png`, `_2x.png`, `.webp`, `.png` und durchsucht den JS-Code der Seite nach Erwähnungen und SVG-Pfaden. ⚠ Ob der Nutzer ihn ausgeführt hat, steht nicht im Verlauf (er wollte danach stattdessen die 1:1-Vektoren, #72/#80). Laut Claude würde ein Server-SVG optisch nichts mehr ändern.

```js
(async () => {
  const base = location.origin + '/assets/images/';
  const names = ['img-pending-order-bl','img-pending-order-sl','img-pending-order-bs','img-pending-order-ss'];
  const exts = ['.svg','@2x.png','@3x.png','-2x.png','_2x.png','.webp','.png'];
  const found = [];
  for (const n of names) for (const e of exts) {
    const u = base + n + e;
    try {
      const r = await fetch(u, { cache: 'reload' });
      if (!r.ok) continue;
      const b = await r.blob();
      let dim = '-';
      if (b.type.includes('svg')) dim = 'VEKTOR';
      else if (b.type.startsWith('image')) dim = await new Promise(ok => { const i = new Image(); i.onload = () => ok(i.naturalWidth + 'x' + i.naturalHeight); i.onerror = () => ok('?'); i.src = URL.createObjectURL(b); });
      found.push({ datei: n + e, typ: b.type, bytes: b.size, groesse: dim });
    } catch (_) {}
  }
  console.table(found);
  const srcs = [...document.scripts].map(s => s.src).filter(s => s && s.startsWith(location.origin));
  const treffer = new Set(), svgs = new Set();
  for (const s of srcs) {
    try {
      const t = await (await fetch(s)).text();
      (t.match(/[\w\-./@]*pending-order[\w\-./@]*/g) || []).forEach(x => treffer.add(x));
      (t.match(/assets\/[\w\-./]+\.svg/g) || []).forEach(x => svgs.add(x));
    } catch (_) {}
  }
  console.log('Im Code erwähnt:', [...treffer]);
  console.log('SVG-Dateien der App:', [...svgs].slice(0, 60));
  copy(JSON.stringify({ found, treffer: [...treffer], svgs: [...svgs].slice(0, 60) }, null, 1));
  console.log('✔ Ergebnis kopiert — hier im Chat einfügen.');
})();
```

### 7.5 Erster Fenster-Befehl (#21) – überholt

Erste, gröbere Fassung (Suche über den Text „NEW ORDER“ + „Place pending order“, HTML-Klon + Styles). Durch #39 ersetzt; nur der Vollständigkeit halber.

```js
(() => {
  const docs = [document, ...[...document.querySelectorAll('iframe')].map(f => { try { return f.contentDocument } catch (e) { return null } }).filter(Boolean)];
  let root = null;
  for (const d of docs) {
    const hit = [...d.querySelectorAll('body *')].filter(e => /NEW ORDER/.test(e.textContent || '') && /Place pending order/i.test(e.textContent || ''));
    if (hit.length) { root = hit[hit.length - 1]; break; }
  }
  if (!root) { console.warn('Fenster nicht gefunden – ist "New Pending Order" offen?'); return; }
  const cs = e => { const s = getComputedStyle(e), r = e.getBoundingClientRect(); return { tag: e.tagName.toLowerCase(), text: (e.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40), bg: s.backgroundColor, color: s.color, border: s.borderColor, font: s.fontFamily.split(',')[0], size: s.fontSize, weight: s.fontWeight, radius: s.borderRadius, w: Math.round(r.width), h: Math.round(r.height) }; };
  const clone = root.cloneNode(true);
  clone.querySelectorAll('svg, canvas, script, style').forEach(n => n.remove());
  const list = [cs(root), ...[...root.querySelectorAll('*')].filter(e => e.getBoundingClientRect().width > 0).map(cs)].slice(0, 200);
  copy(JSON.stringify({ html: clone.outerHTML.slice(0, 30000), styles: list }));
  console.log('Kopiert. Jetzt im Chat einfügen. Elemente:', list.length);
})();
```

### 7.6 Weitere Hinweise zu Plattform-Assets

- Chartbilder: `location.origin + '/assets/images/img-pending-order-bl.png'` (bzw. `sl`, `bs`, `ss`). Im Fenster: Rechtsklick → „Bild in neuem Tab öffnen“ (#39).
- Der Nutzer hatte außerdem eine **.har-Datei** (Netzwerk-Tab) geliefert, in der alle vier Originalbilder steckten (#40, #41).

---

## 8. Offene Punkte / nächste Schritte

### 8.1 Unmittelbar (dort hat der Chat aufgehört)

1. **Dateien zurückholen** (Abschnitt 9). Ohne `.tex`/Skripte kann nichts gebaut werden. Fehlen sie, mit dem Nutzer klären, ob neu aufgebaut werden soll (dann diese Datei als Spezifikation nutzen).
2. ~~**Doku 2: Desktop-Leiste im blauen Design messen**~~ → erledigt 02.10.2026 (Abschnitt 12).
3. ~~**Doku 2: Instrument-Info-Feld messen**~~ → erledigt 02.10.2026: Desktop und mobil gemessen, nachgebaut, auf „Instrumente und Positionen“ eingebunden (5.4, Abschnitt 18).
4. Optional: **Mobile, Reiter Information** (Lauf 3).
5. Nach jeder Textänderung: Druck-Prüfungen (6.1) und **Schutz neu aufspielen** (6.3), Pixelvergleich = 0, Extrakt ohne echte Wörter. ✓ Stand `fe8c471`: Beide geschützten Fassungen sind mit `tools/schutz.py` neu erzeugt und geprüft (Abschnitt 19).
6. **Offene Funde der Prüfung Kontogrundlagen** (Plattform-Bilder Prio 1–5, „Wertpapierdepot“, Kommentar in `mobil.tex`) sowie Einbau der gebauten Nachbauten und offene Messbefehle: Abschnitt 8.4 und 18.

### 8.2 Entscheidungen, die beim Nutzer liegen (offen)

- [ ] **Blaues oder graues Design** für die Nachbauten in Doku 2 (und welches die Kunden hauptsächlich sehen) (#155–#157).
- [x] ~~**Swap-Rechenbeispiel** als eigener Kasten – ja/nein (#151)~~ → erledigt 02.10.2026: Rechenbeispiel (3 € + 3 € + 1 € = 7 € pro Nacht) steht auf S. 6, Zahlen-Ausnahme 4 (Abschnitt 2.3, 5.3).
- [ ] **Absender/Logo** für den Footer – gibt es einen Firmennamen oder ein Logo? (#102, #103, #117)
- [ ] **„Ausbruch nach oben/unten“** auf dem Deckblatt und in den Kartenköpfen ersetzen (z. B. „wenn der Kurs nach oben durchbricht“) oder behalten, weil der Begriff später gebraucht wird? (#117) – Achtung: Der Wortlaut stammt aus der Vorgabe des Nutzers (#102).
- [ ] **Lernreihe?** Wurden Market Orders vorher schon erklärt, oder ist Doku 1 der allererste Kontakt? Davon hängt ab, wie viel Seite 2 voraussetzen darf (#117). (Doku 2 heißt „Schulungseinheit 1“ – das spricht für eine Reihe; ⚠ die Reihenfolge der beiden Dokumente ist unklar.)
- [ ] **Badge mit „4“ und „1“** auf dem Deckblatt behalten? (#103)
- [ ] **Rot**: Dokument-Rot (wie Überschriften) behalten oder Original-Rot der Plattform? (#89)
- [ ] **Stop-Loss-Zeile** im Fenster-Nachbau ganz entfernen? (#15)
- [ ] **Historischer Trade** als separates Anhangsblatt „Rechenbeispiel“? (#65)
- [ ] ~~„Ohne Hebel“-Grafik auf der Hebel-Seite größer? (Claude rät ab, #147)~~ → gegenstandslos: Die Grafik ist seit 02.10.2026 entfernt (Nutzervorgabe, Abschnitt 14).
- [x] ~~**„dein/deine“-Platzhalter** in den Plattform-Nachbauten (`fenster-bl.pdf`: „deine Menge/dein Wert/dein Ziel“; `panel.pdf`/`mobil.tex`/`bar.tex`: „dein Guthaben“)~~ → **erledigt, endgültig:** Sie **bleiben wie sie sind** (Nutzerentscheidung 02.10.2026). Nicht erneut fragen, nicht auf „Ihre …“ umstellen.
- [x] ~~**„die Bank“ auf der Swap-Seite** (damals S. 5, jetzt S. 6) näher bestimmen~~ → **entschieden (Nutzer, 02.10.2026):** Auf der Swap-Seite heißt es **„Liquiditätsanbieter“** statt „Bank“ (laut Nutzer der richtige Begriff); **umgesetzt in `ac919eb`.** Auf der Hebel-Seite (jetzt S. 5) bleibt „Bank“ (Direktkauf über das Wertpapierdepot der Bank). Swap-Modell: Der Liquiditätsanbieter verlangt Miete für die Aufbewahrung (Rohstoffe) bzw. Zinsen (Devisen) und einen Risikoanteil; dazu kommt der Aufschlag des Brokers.
- [x] ~~**Satz zur Gutschrift auf der Swap-Seite** (damals S. 5) („In der Regel sind beide negativ; ist ein Satz positiv, wird Ihnen der Betrag gutgeschrieben.“)~~ → **entschieden: bleibt** (Nutzer, 02.10.2026).
- [x] ~~**Deckblatt von Pending Orders übernehmen?**~~ → **entschieden (Nutzer, 02.10.2026):** Das SVG-Deckblatt (`Pending-Orders-Guide_CoverTest.tex`, mit den drei Korrekturen, Abschnitt 16) wird in den Guide übernommen; **umgesetzt in `a86882f`** (S. 1 des Guides; Untertitel bleibt in Sie-Form). Die Charts werden **nicht** auf die volle Spaltenbreite gezogen (nicht beauftragt); sie bleiben bündig mit der Textkante, rechts bei ca. 83 bzw. 181 mm. Die Rückfrage „Charts auf volle Spaltenbreite?“ ist damit erledigt.
- [x] ~~**Commission** in Doku 2~~ → **entschieden (Nutzer, 02.10.2026):** Es gibt auf der Plattform keine Commission; sie ist gestrichen. Stattdessen ist der **Bonus** erklärt (Abschnitt 2.2, 5.3).
- [x] ~~**Seitenzahlen in Doku 2** (Fußzeile „n / 8“, „S. n“-Verweise)~~ → bleiben **entfernt** (Regel „keine Zahlen“, #58/#59); Verweise nennen den Seitentitel (2.3, 5.3).
- [x] ~~**Wohin der Swap gebucht wird**~~ → geklärt (Quelle 5.1; Abschnitt 5.3 und 5.4). Rollover-Zeit: Angabe des Nutzers (23:00 Uhr Amsterdamer Zeit) gilt.

### 8.3 Erledigt bzw. überholt (nicht erneut fragen)

- Chart-Stil A/B/C (#73) → erledigt durch „1:1-Vektor der Plattformbilder, ohne dunklen Hintergrund“ (#80, #82).
- Eigene Seite „So zeigt es deine Plattform“ (#75) → überholt, weil die Plattformbilder jetzt überall die Charts sind (#81).
- Kompletter Guide im dunklen Querformat (#35, #39, #43) → nein, helles A4 (#50, #102).
- Fenster-Variante A/B (#43) → A „Exakt“ (#45).
- Gewinnzone als Fläche/Klammer (#21) → überholt durch die Tönung ab der grünen Kugel (#83).
- Du-Platzhalter in den Plattform-Nachbauten → bleiben (Nutzerentscheidung 02.10.2026, endgültig).
- Swap-Rechenbeispiel auf der Swap-Seite → umgesetzt (02.10.2026).
- „Bank“ auf der Swap-Seite → „Liquiditätsanbieter“ (Nutzerentscheidung 02.10.2026, umgesetzt in `ac919eb`); Gutschrift-Satz auf der Swap-Seite bleibt; Deckblatt übernommen (`a86882f`), Charts nicht auf volle Breite (Abschnitt 8.2).
- Commission in Doku 2 → gestrichen, Bonus erklärt; Seitenzahlen bleiben entfernt, Verweise per Seitentitel; Swap-Buchung geklärt (Abschnitt 8.2, 5.4).
- Funde der Prüfung `docs/pruefung/kontogrundlagen-begriffe-bilder.md`: erledigt A1, A2, A4–A16 und die Widersprüche 1–3 (Stand `145c398`); der Rest steht in 8.4.

### 8.4 Offene Funde aus der Prüfung Kontogrundlagen (Stand 02.10.2026, nach `5455781`; Seitenangaben mit 9 Seiten)

Quellen (hier nur verwiesen, nicht abgeschrieben): `docs/pruefung/kontogrundlagen-begriffe-bilder.md` (Funde A1–A16, drei fachliche Widersprüche, Teil B „Plattform-Bilder“; Seitenangaben dort = alte Zählung, Stand `ac919eb`) und `docs/pruefung/handbuch-abgleich.md` (Abgleich der Funde mit dem englischen CFD-Handbuch des Nutzers; das Handbuch ist allgemein und belegt **kein** Plattformverhalten, siehe Vorbehalt dort).

**Erledigt:** A1, A2, A4–A16; Widerspruch 1 (Swap-Buchung), 2 (Free = 0 auf der Hebel-Seite → je 2.000 €, Free 1.000 €) und 3 (Swap = „Kosten“ auf „Auf einen Blick“ → „Belastung oder Gutschrift“). Übergaben: `kg-grundbegriffe`, `kg-hebel-swap-feinschliff`, `kg-plattform-uebersicht`.

**Offen:**

- [ ] **Plattform-Bilder, Teil B.** Sie brauchen **Konsolenbefehle vom Nutzer** (nicht schätzen; Messbefehl 7.1). Dem Nutzer jeweils sagen, was vorher geöffnet sein muss (Regel 2.1; Wege nach 5.2: Desktop erster Bildschirm bzw. Info-Zeichen beim Instrument, mobil Info-Zeichen oben rechts bzw. Orders). Priorität, Element, gebraucht auf (Seitentitel statt Zahl):
  1. ~~**Positionsliste**~~ → **Desktop gemessen und nachgebaut** (02.10.2026, `originals/messungen/positionen-desktop.json`): `positionen-desktop.pdf` (Ausschnitt mit Bruchkante, für 170 mm) und `positionen-desktop-voll.pdf` (alle Spalten, für eine Querformat-Seite mit 257 mm). **Noch nicht eingebunden.** Auf „Instrumente und Positionen“ (S. 8) steht die Liste bisher als Text; Rest unten ca. 79 pt (28 mm), der Ausschnitt ist bei 170 mm 25,8 mm hoch. Mobile Liste (Orders → Active) nicht gemessen, nur als DOM-Fakt (`docs/plattform/dom-positionsliste.md`).
  2. ~~**Info-Fenster des Instruments**~~ → **gemessen, nachgebaut und eingebunden** (Desktop `info-desktop.pdf` und mobil `info-mobil.pdf` auf „Instrumente und Positionen“, S. 8). Hebel, Swaps und In der Plattform verweisen dorthin.
  3. **Reiter „Information“** der Kontoübersicht (Leverage, Stop out) – Margin, Hebel. Mobil nur als Text; **Desktop-Weg unbekannt**.
  4. **Warnmeldung** der Plattform beim niedrigen Level – Margin. Unbekannt.
  5. ~~**Desktop-Schema**~~ → **gebaut** als Lehrbuch-Schema `desktop-schema.pdf` (170 × 82,4 mm; Kursliste, Chart, Tabelle der Positionen, Unterste Leiste), **noch nicht eingebunden** (Vorschlag der Übergabe: „In der Plattform“, S. 7; ob eine Legende A–D dazukommt, entscheidet der Nutzer). Ebenso gebaut, nicht eingebunden: `kursliste-desktop.pdf` (Kursliste, Metals aufgeklappt).
  Platz laut Übergaben (Stand `0850815`): „Grundbegriffe“ (S. 2) ca. 8 pt, „Kontostand“ (S. 3) ca. 18 pt, „Hebel“ (S. 5) ca. 0,3 pt, „Swaps“ (S. 6) ca. 0,9 pt, „In der Plattform“ (S. 7) ca. 9,4 pt, „Instrumente und Positionen“ (S. 8) ca. 79 pt; „Auf einen Blick“ (S. 9) hatte vor der neuen Zeile Total Profit ca. 180 pt (nicht neu gemessen). Weitere Bilder brauchen Umbau oder eine zusätzliche Seite (für `positionen-desktop-voll.pdf` eine Querformat-Seite).
- [ ] **Offene Messbefehle zu den Nachbauten** (Konsolenbefehle stehen in den Übergaben, hier nicht abgeschrieben; Liste in Abschnitt 18).
- [ ] **Fehlende Icon-Glyphen** (Plattform-Schrift nicht im Repo, Regel: nicht einchecken): Schließen U+E91B, Stern U+E916, Aufklapp-Pfeil U+E910, Plus U+E91A, Lupe U+E915, Griff U+E90E. Die Nachbauten lassen die Flächen leer; `info-desktop`, `kursliste-desktop` und `positionen-desktop-voll` zeichnen Schließen, Stern bzw. Plus und Lupe automatisch, sobald `\iconclose`, `\iconstar`, `\iconplus`, `\iconsearch` in `icons.tikz` stehen (Einträge in `tools/icons_aus_font.py`, Font lokal bereitstellen); in `info-mobil` müssen Stern und Pfeil nachgetragen werden. Instrument-Bilder (PNG) bleiben weggelassen.
- [ ] **Spalten S/L und T/P** in `positionen-desktop-voll.pdf` (Plattform-Original, Wert „—“): vor einem Einbau mit der Regel „kein Stop-Loss“ (2.2) abgleichen; Ausschnitt und Desktop-Schema zeigen sie nicht.
- [ ] **„Commission“ als Feldname** in den eingebundenen Nachbauten (Wert „—“) und in der Positionstabelle, obwohl der Text die Commission nicht nennt (2.2): Plattform-Original, vom Nutzer nicht ausdrücklich bestätigt.
- [ ] **„Trade volume“ gegen „Trade Volume“:** Das Dokument (S. 8) schreibt den DOM-Text „Trade volume“; die Plattform zeigt per CSS „Trade Volume“ (Übergabe `nachbau-positionen-desktop.md`). Schreibweise im Text ggf. angleichen (Regel: Begriffe wie auf der Plattform).
- [ ] **„Wertpapierdepot“** (Hebel-Seite, Geschichte des Bekannten) wird nirgends erklärt (Rest von A3; „Broker“ und „Direktkauf“ stehen in „Grundbegriffe“). Lösungsweg laut Prüfung: ein Halbsatz.
- [x] ~~**„Volume“ gegen „Volumen“:** Im Order-Fenster (Doku 1, Plattform-Originaltext) bedeutet **Volume** die Menge; Doku 2 nennt **Volumen** den Wert der Position („Grundbegriffe“, „Hebel“). Begriffsklärung beim Nutzer.~~ → per DOM geklärt (`docs/plattform/dom-positionsliste.md`): In der Positionsliste ist **Amount** die Menge und **Trade volume** der Wert (= Volumen im Dokument); im Order-Fenster ist „Volume“ die Menge. S. 8 erklärt Amount und Trade volume entsprechend.
- [ ] **Kommentar in `mobil.tex`** (Z. 5) nennt noch „Seite 6“ (heute „In der Plattform“, S. 7); nur ein Kommentar, nicht angefasst.
- [ ] **Stop out „Fest je Konto“** (Zeile in „Auf einen Blick“): abgeleitet aus 5.3/#147, vom Nutzer nicht bestätigt (Alternative: Spalte streichen).
- [ ] Einfache Ergänzungen der Prüfung ohne Messung, noch offen: **Balance-Marke** im mobilen Panel, **Orders-Symbol** im mobilen Kopf markieren (Nachbauten, nicht angefasst). Die Verweise „(Abbildung …)“ sind erledigt (per Seitentitel).

---

## 9. Fehlende Dateien

Diese Dateien lagen nur in der Sandbox des alten claude.ai-Chats. Der Nutzer sollte sie **aus dem Chat auf claude.ai herunterladen** und ins Repo legen. Vorschlag: Ordner **`originals/`** (Eingangsmaterial vom Nutzer in `originals/inputs/`).

### Bereits im Repo vorhanden (geprüft am 02.10.2026)

- **`originals/pending_orders_DE.pdf`** (112 440 Bytes): geschützte Fassung von Doku 1. 6 Seiten, A4, `CreationDate` 07.09.2026 00:38 UTC, Metadaten-Titel „Pending Orders – Kurz-Guide“, AES-256 (R = 6), Text-Extrakt ist Salat (`MqZdahd I dqfhdz Zdhh …`), keine Rasterbilder.
  ⚠ Das ist **nicht der Endstand**, sondern der Stand von #121/#123: **P = −3392** („extract for accessibility: allowed“) und Header **PDF-1.7**. Der Endstand aus #125 (P = −3904, PDF 2.0) fehlt. Eine ungeschützte Fassung oder `.tex` ist nicht vorhanden. Bauen lässt sich aus dieser Datei nichts.
- **Neu seit Nachtrag 3 (02.10.2026)** in `dokumente/kontogrundlagen-kosten/` (jeweils `.tex` und `.pdf`, standalone): `info-desktop`, `info-mobil`, `kursliste-desktop`, `positionen-desktop`, `positionen-desktop-voll` (Nachbauten) und `desktop-schema` (Lehrbuch-Schema des Desktop-Bildschirms, 170 × 82,4 mm). Messungen in `originals/messungen/`: `instrument-info-desktop.json`, `instrument-info-mobil.json`, `kursliste-desktop.json`, `positionen-desktop.json`. Plattform-Fakten: `docs/plattform/dom-kursliste-instrument-info.md`, `dom-positionsliste.md`. Übersicht: Abschnitt 18.

### Noch fehlend

⚠ Die folgenden Dateinamen stehen **nicht** im Textexport (dort fehlen die Tool-Aufrufe). Sie stammen aus der Aufgabenstellung bzw. der Erinnerung des Nutzers und sollten beim Herunterladen mit den tatsächlichen Namen abgeglichen werden.

| Datei | Inhalt | Ziel |
|---|---|---|
| `Pending-Orders-Guide_ORIGINAL.tex` | LaTeX-Quelle Doku 1 | `originals/` |
| `Pending-Orders-Guide_ORIGINAL.pdf` | Doku 1, ungeschützt, Druckqualität | `originals/` |
| `Pending-Orders-Guide_GESCHUETZT.pdf` | Doku 1, geschützt (6.3) | `originals/` |
| `Kontogrundlagen-Kosten_ORIGINAL.tex` | LaTeX-Quelle Doku 2 | `originals/` |
| `Kontogrundlagen-Kosten_ORIGINAL.pdf` | Doku 2, ungeschützt | `originals/` |
| `Kontogrundlagen-Kosten_GESCHUETZT.pdf` | Doku 2, geschützt | `originals/` |
| `scramble.py` | Schutz-Skript (ToUnicode-Vergiftung, AES-256, P = −3904, PDF 2.0) | `originals/` |
| `charts.tikz` | TikZ-Grundformen der vier Plattform-Chartbilder | `originals/` |
| `fenster-bl.pdf` | Vektor-Nachbau Order-Fenster (Buy Limit), wird in Seite 6 eingebettet | `originals/` |
| `type-menu.pdf` | Vektor-Ausschnitt des aufgeklappten Type-Menüs | `originals/` |
| `Fenster_exakt_BuyLimit_VEKTOR.pdf` | Fenster-Nachbau Variante A „Exakt“ | `originals/` |

**Zusätzlich hilfreich, falls noch verfügbar** (im Verlauf erwähnt, ⚠ Namen größtenteils unbekannt):

- Python-Generatoren (`gen`, `design`, `demo.py`, `chart.tex`) bzw. deren Nachfolger (#35).
- Die vier Original-PNGs `img-pending-order-{bl,sl,bs,ss}.png` (174 × 96 px) und die **.har**-Datei (#40, #41).
- Inter-Schriftdateien (per npm geholt, #41); IBM Plex muss lokal installiert sein.
- Eingaben des Nutzers: Screenshots (Order-Fenster, Type-Menü, Take-Profit/Kurslinie, Mobile-/Desktop-Kontoübersicht), die **Swap-Skizze** (#148), die **CSV-Tabelle** (#119), das Referenzdokument zu Doku 2 (#126/#129), die Konsolen-Ausgaben (JSON) aus #41, #150, #154, die BnkPro-Referenz-PDF (#34) und `Stil-Demo_dunkel (1).pdf` (#50).

**Werkzeuge, die die alte Sandbox hatte** (für den Neuaufbau prüfen): xelatex, TikZ/PGF, tcolorbox, fontspec, IBM Plex Sans/Mono, Inter, Ghostscript, qpdf, poppler-utils (pdftotext, pdfimages), pypdf. Kein pdfcrop.
Im Repo liegt dafür bereits **`scripts/setup.sh`** (Commit `ecc5820`). Laut Commit-Nachricht installiert es idempotent XeLaTeX (TikZ, tcolorbox, fontspec, ngerman), qpdf, Ghostscript, poppler-utils, pikepdf/pypdf/fonttools sowie IBM Plex Sans/Mono und Inter, und prüft am Ende alles.

---

## 10. Unklarheiten und Widersprüche im Verlauf

- **Weißraum auf dem Deckblatt:** #94 „der Weißraum oben darf nicht weggehen“ vs. #96 „bisschen Weißraum unten ist ok, aber oben auf keinen Fall“. Claude deutete #94 als Abstand zwischen Textblock und Charts (bleibt) und #96 als „Titelblock nach oben“. Danach kam die 20,5-mm-Regel (#99) und später das neue Deckblatt (#103). Im Zweifel: Titel bei 20,5 mm, Luft zwischen Text und Hero-Visual, Rest unten.
- **Seitennummerierung:** Der Nutzer nennt die Plattform-Seite „Seite 5“ (#44, #46), Claude führt sie als Seite 6 (#45).
- **„Auslösepreis“** im vom Nutzer vorgegebenen Untertitel (#102) ist kein Plattform-Begriff; Ähnliches gilt für „Ausbruch“ (#117). Wortlaut ist vom Nutzer, daher nicht eigenmächtig ändern.
- **Badge mit Ziffern** widerspricht der Regel „keine Zahlen“, kommt aber vom Nutzer (#102/#103).
- **Grün:** `#53BC51` ist das gemessene Plattform-Grün; im Dokument soll aber das „gedämpfte“ Grün aus dem zweiten Bild stehen (#89). Hex-Werte für Dokument-Grün und -Rot fehlen im Export.
- **„Kurs jetzt“-Pille:** in #83 eingeführt, in #85 entfernt.
- **Desktop-Design:** grau (`#181818`) im Screenshot, gebaut in Blau; Desktop-Werte teils geschätzt (#157). Seit 02.10.2026 im blauen Design gemessen (`body.blue-theme`, Leiste `#051B3A`) und danach gebaut.
- **Swaps:** Thema 6 verlangt die „Berechnung“, das Dokument ist aber zahlenfrei → Erklärung in Worten, Rechenbeispiel nur optional. ⚠ Überholt: Der Nutzer wünschte das Rechenbeispiel (02.10.2026), Zahlen-Ausnahme 4 (Abschnitt 2.3).
- **Nutzer-Nachricht #118** ist abgeschnitten („die konkrete Ausführung kann bei …“).
- **CSV-Tabelle mit Spalte „Auslöser“** (#119): Herkunft und genaue Position im Dokument sind im Export nicht sichtbar.
- **Mehrfach leere Antworten** (#11, #27, #31, #53, #57, #105–#115, #135–#145, #159): Dort fehlen Inhalte im Export oder die Antworten sind abgebrochen. Der Nutzer hat Nachrichten deshalb mehrfach wiederholt.
- **Zeitsprung:** Der Chat endet inhaltlich am 07.09.2026 (#157); die Übergabe-Bitte (#158) ist vom 01.10.2026.

---

## 11. Stand Wiederherstellung

Stand 02.10.2026: Dokument 1 („Pending Orders“) ist aus `Pending-Orders-Guide_ORIGINAL.tex` wieder baubar und **optisch identisch** mit dem ORIGINAL-PDF. Dokument 2 ist inzwischen ebenfalls wiederhergestellt (Abschnitt 12).

**Struktur**

| Pfad | Inhalt |
|---|---|
| `dokumente/pending-orders/Pending-Orders-Guide.tex` | Quelle; gegenüber `originals/…_ORIGINAL.tex` nur `Path=../../fonts/` und eine Zeile `\babelprovide[hyphenrules=english]{ngerman}` (siehe unten) |
| `dokumente/pending-orders/charts.tikz` | `\chartbl/sl/bs/ss` (+ `…mini`), erzeugt von `tools/charts_aus_pdf.py` |
| `dokumente/pending-orders/fenster-bl.pdf`, `type-menu.pdf` | aus Seite 6 des ORIGINAL-PDFs extrahierte Form-XObjects (`tools/grafiken_aus_pdf.py`), Inter eingebettet |
| `fonts/` | IBM Plex Sans (Regular, SemiBold, Italic, SemiBoldItalic, Light, LightItalic) und Mono (Regular, SemiBold) als OTF, GitHub-Release IBM/plex 1.1.0, OFL-Lizenz |
| `originals/` | unveränderte Uploads: `Pending-Orders-Guide_ORIGINAL.pdf/.tex`, `…_GESCHUETZT_3.pdf`, `Order-Trigger-Guide_2.tex` (ältere Fassung), `scramble.py` (nur abgelegt, nicht im Build), `pending_orders_DE.pdf` |
| `originals/messungen/new-order-fenster.json` | DOM-Messung des Plattform-Fensters „NEW ORDER“ (Reiter New Pending Order, Buy Limit; Modal 475 × 573,3 px, Inter) – Messgrundlage, aus der `fenster-bl.pdf` im alten Chat gebaut wurde. Nur Referenz; maßgeblich bleibt das aus dem ORIGINAL-PDF extrahierte `fenster-bl.pdf` |
| `scripts/build.sh` | Build; `tools/pdf_vergleich.py` Pixel-/Inhaltsstrom-Vergleich |

**Build:** `scripts/build.sh` (oder `scripts/build.sh pending-orders`) → `build/Pending-Orders-Guide.pdf` (`build/` ist ignoriert). Prüfen: `python3 tools/pdf_vergleich.py` (Standard: Neubau gegen `originals/Pending-Orders-Guide_ORIGINAL.pdf`, 150 dpi).

**Vergleichsergebnis:** 6 Seiten; auf allen Seiten 0,0000 % abweichende Pixel (max. Abweichung 0) bei 150 und 600 dpi; die Inhaltsströme aller sechs Seiten sind bytegleich. 11 Schriften, alle eingebettet (IBM Plex Sans Light/Regular/SemiBold, Inter im Fenster und Menü); `pdfimages` findet keine Rasterbilder.

**Erkenntnisse aus der Rekonstruktion**

- **Charts:** Je Bild 37 Rechtecke, 2 Kreise, 1 Dreieck (TikZ `rectangle`, `circle`, `-- cycle`), Werte mit höchstens 3 Nachkommastellen, bitgenau zurückgerechnet. Farben `pfrot`, `pfgrau` (#97A5B4), `pfgruen`. Die **Mini-Fassungen sind im Original identisch** mit den großen (gleiche Geometrie, gleiche Farben, kein gröberer Detailgrad) – nur kleiner skaliert. In `charts.tikz` sind sie daher Verweise.
- **Silbentrennung:** Der Original-Build lief ohne deutsche Trennmuster (babel fiel auf Englisch zurück). Mit deutschen Mustern trennt TeX auf Seite 2 „Verkau-fen“ und alle Folgezeilen verschieben sich. Die Zeile `hyphenrules=english` stellt das alte Verhalten her. ⚠ Bei neuen Texten auf deutsche Muster umstellen (Zeile entfernen) und die Umbrüche prüfen.
- Die Plex-OTFs aus `fonts/` erzeugen exakt dieselben Glyphen und Metriken wie im Original (CFF-Version 3.5).

**Offen:** keine Abweichungen. Die geschützte Fassung wurde nicht neu erzeugt (`scramble.py` liegt nur in `originals/`).

---

## 12. Wiederherstellung Kontogrundlagen

> Seitenangaben in diesem Abschnitt gelten für die **alte Zählung** (7 Seiten, vor `5f9d129`): „Seite 6“ ist heute „In der Plattform“ (S. 7), „Seite 5“ heute „Swaps“ (S. 6). Ebenso „7 Seiten“ in den Vergleichsergebnissen.

Stand 02.10.2026: Dokument 2 („Kontogrundlagen & Kosten“) ist aus `Kontogrundlagen-Kosten_ORIGINAL.tex` wieder baubar und **optisch identisch** mit dem ORIGINAL-PDF. Vorgehen wie in Abschnitt 11.

| Pfad | Inhalt |
|---|---|
| `dokumente/kontogrundlagen-kosten/Kontogrundlagen-Kosten.tex` | Quelle; gegenüber dem Original nur `Path=../../fonts/` und `\babelprovide[hyphenrules=english]{ngerman}` (ohne die Zeile trennt Seite 5 „zwi-schen“ statt „zwis-chen“) |
| `…/panel.pdf` | mobile Kontoübersicht, Form-XObject `/Fm16` von Seite 6, 339,12 × 300 pt, gesetzt 78 mm |
| `…/bar.pdf` | Desktop-Kontoleiste, gesetzt 170 mm. Ursprünglich Form-XObject `/Fm17` von Seite 6 (594 × 35,04 pt); seit 02.10.2026 aus `bar.tex` gebaut (siehe unten) |
| `…/mobil.tex/.pdf`, `…/icons.tikz` | mobile Ansicht Kopf + Reiter + `panel.pdf`; Icons aus der Plattform-Font (siehe unten). `panel.pdf` wird seitdem nur noch über `mobil.pdf` eingebunden |
| `originals/Kontogrundlagen-Kosten_ORIGINAL.tex/.pdf` | unveränderte Uploads |

**Befehle:** `scripts/build.sh kontogrundlagen-kosten` · `python3 tools/grafiken_aus_pdf.py kontogrundlagen-kosten` (ohne Argument: Pending Orders) · `python3 tools/pdf_vergleich.py --dokument kontogrundlagen-kosten`.

⚠ **Pixeltreue zum ORIGINAL-PDF ab 02.10.2026 bewusst aufgegeben** (Farbänderung auf Nutzerwunsch, Abschnitt 13): `tools/pdf_vergleich.py --dokument kontogrundlagen-kosten` meldet seitdem auf allen Seiten Abweichungen – das ist gewollt. Der folgende Befund beschreibt den Stand davor.

**Vergleichsergebnis:** 7 Seiten; alle Seiten 0,0000 % abweichende Pixel (max. 0) bei 150 und 600 dpi; Inhaltsströme der Seiten und der beiden Formen bytegleich. 10 Schriften, alle eingebettet (IBM Plex Sans Light/Regular/SemiBold, Inter in Panel und Leiste); keine Rasterbilder.

**Aufbau des alten `bar.pdf`** (bis 02.10.2026, überholt): Koordinaten in CSS-px, 1 px = 0,75 pt; im Dokument 1 px = 0,2146 mm.

- Seite 792 × 46,72 px; Leiste 792 × 46 px (594 × 34,5 pt, im Dokument 170 × 9,87 mm), Radius 5 px, Fläche `#04273C`.
- Schrift Inter Regular (4.001), 12,5 px (im Dokument 7,6 pt), Grundlinie 28 px unter der Oberkante, Glyphen auf ganze px gesetzt. Labels `#A8BBBE`, Werte Weiß.
- Kasten hinter Equity: `#0E5072`, x 215–343, y 11–36 px (128 × 25 px), Radius 3 px – **geschätzt** (Abschnitt 3.6).
- Felder (x Label / x Wert in px): Balance: 51 / 106 „dein Guthaben“ · Equity: 224 / 270 „Konto jetzt“ · Profit/Losses: 367 / 457 „schwebend“ · Margin: 549 / 599 „gebunden“ · Free: 682 / 717 „verfügbar“. Gruppenabstand ca. 24 px (**geschätzt**), rechter Rand ca. 16 px. Level fehlte (⚠ falsch, auf der Plattform steht es).

**Neubau der Desktop-Leiste nach DOM-Messung (02.10.2026)**

- Messung: `originals/messungen/kontoleiste-desktop.json` (vom Nutzer, gekürzt um Default-Styles; Fenster 2040 × 986 px, dpr 1,25, `body.blue-theme`).
- Gemessen: `<footer>` 34 px hoch, padding 8px 16px, Fläche `#051B3A` (nicht `#04273C`), eckig; Feldgruppe rechts (16 px vor dem Rand), gap 18 px; acht Felder **Balance, Equity, Profit/Losses, Margin, Free, Level, Bonus, Credit** – **Level ist am Desktop vorhanden**. Feld 18 px hoch, padding 2px 5px, Radius 3 px; nur Equity mit Fläche `#0E5072`. Inter 400, 12 px, line-height 14 px; Label `#A8BBBE`, Wert weiß; keine Trenner, Schatten oder Pseudo-Elemente.
- Kein Leerzeichen zwischen Label und Wert: „Balance:“ ist ohne Leerzeichen 48,63 px breit (gemessen 48,6), mit Leerzeichen wären es 52,0 px. Der Betrag folgt direkt („Balance:€163,831.85“), Luft gibt nur das €. Nur beim Level-Text steckt ein Leerzeichen im Wert (93,4 + 3,4 = 96,8 px).
- `dokumente/kontogrundlagen-kosten/bar.tex` (standalone, TikZ, Inter 4.0 aus `fonts-inter`) rechnet wie der Browser: Feldbreite = Label + Wert (XeTeX-Boxbreite, HarfBuzz wie Chrome) + 2 × 5 px, gap 18 px, Grundlinie 21,2 px unter der Oberkante (8 + 1,2 + 12). Probe mit den gemessenen Beträgen: Feldbreiten auf ≤ 0,2 px, Gruppe 993,7 statt 993,1 px.
- Werte als Wörter wie in `panel.pdf`: dein Guthaben · Konto jetzt · schwebend · gebunden · verfügbar · Puffer · — · —, jeweils mit einem Wortleerzeichen nach dem Doppelpunkt (ohne € würde das Wort sonst am Doppelpunkt kleben).
- Ausschnitt: 16 px Leiste links vor der Gruppe (Original: 1030,9 px), rechts 16 px; Bild 992,9 × 34 px. Im Dokument 170 × 5,82 mm, 1 px = 0,1712 mm, Schrift **5,8 pt** (ohne linken Rand wären es höchstens 5,9 pt).
- `scripts/build.sh` baut Standalone-Quellen zuerst und legt `bar.pdf` neben die `.tex` (reproduzierbar, `SOURCE_DATE_EPOCH=0`; die Datei wird nur bei geändertem Inhalt ersetzt). `tools/grafiken_aus_pdf.py kontogrundlagen-kosten` extrahiert nur noch `panel.pdf`.
- Text Seite 6: „Unterste Leiste, rechts – dauerhaft sichtbar. Dieselben Werte wie mobil, die **Balance** steht hier vorn mit in der Reihe.“ (vorher: „**Level** fehlt dort; es steht nur in der mobilen Ansicht.“).
- Vergleich mit dem ORIGINAL-PDF: Seiten 1–5 und 7 pixelgleich (0,0000 %, Inhaltsströme identisch); Seite 6 weicht erwartungsgemäß ab. Seite 6 bricht ohne Trennungen um; die Zeile `hyphenrules=english` bleibt vorerst.

**Mobiler Weg zur Kontoübersicht (02.10.2026)**

- Messung: `originals/messungen/mobil-kopf-reiter.json` (Konsolenmessung des Nutzers, zusammengefasst; Viewport 440 × 956 px, dpr 3, blaues Design): `<header>` 60 px `#051B3A`, vier Symbol-Buttons 40 × 40 (Icons 24 px, `#226486`, Webfont „icomoon“), Logo links (im Dokument **weggelassen**, Wunsch des Nutzers); `ul.nav-tabs` 40 px `#001328`, Radius 3 px, margin-bottom 16 px, Reiter Information / Balance je 220 px, aktiv `#0E5072`, Inter 14 px weiß.
- `dokumente/kontogrundlagen-kosten/mobil.tex` (standalone, wird von `build.sh` gebaut) → `mobil.pdf`, 440 × 516 px: Kopf + Reiter nach Messung, darunter `panel.pdf` unverändert 1:1 (y 116). Zustand **nach** dem Antippen: Balance aktiv, Info-Zeichen weiß, die anderen drei `#226486`. XeTeX-Breiten der Reitertexte 75,45 / 52,71 px (gemessen 75,5 / 52,7).
- ⚠ `panel.pdf` ist 452 px breit, seine Zeilen 400 px ab x 15 (ältere Messung, vermutlich 430-px-Viewport). Bei 440 px abgeschnitten (rechts nur leere Fläche); rechts bleiben 25 px statt 15 px Rand. Für exakte 410-px-Zeilen müsste die Kontoübersicht bei 440 px neu gemessen werden.
- Icons: `icons.tikz` (`\iconbell`, `\icongear`, `\iconorders`, `\iconinfo`) mit den **echten Glyphen** aus der Plattform-Font, erzeugt von `tools/icons_aus_font.py` (TTF/OTF/WOFF/WOFF2, fontTools + brotli; Box wie das `<i>` im Browser: 24 px, Grundlinie 1,5 px über der Unterkante, nonzero). Geprüft: Pfade decken sich mit dem XeTeX-Rendering der Font auf < 0,05 px. Die Fontdateien (`icomoon.b9abfeda36b81d3e.ttf`, `icomoon.47a83e5a26e26197.woff`, inhaltlich identisch) liegen **nicht** im Repo (Lizenz unklar). Neu erzeugen: `python3 tools/icons_aus_font.py <font>`.
- Seite 6: Bild im Maßstab des alten Panels (78 mm / 452 px → 75,9 × 89,0 mm). Marken: weißer Ring um das Info-Zeichen und weißer Rahmen um den Reiter Balance, Linie nach rechts zu **A** / **B** (Kreis wie `\pfn`, in der Spalte der Nummern 1–5) mit „Info-Zeichen antippen – oben rechts“ / „Balance antippen – zuerst ist Information offen“. Liste 1–5 darunter (20 mm tiefer). Mobile-Box: „Tippe oben rechts auf das Info-Zeichen. Es öffnet sich zuerst Information – tippe dann auf Balance: die Ansicht oben. Reiter Information zeigt Leverage und Stop out. …“; Desktop- und Mobile-Box gleich hoch (`soft` hat ein optionales Argument, hier `equal height group`).
- Prüfung: 7 Seiten, Seiten 1–5 und 7 pixelgleich (150 und 600 dpi, Inhaltsströme identisch), alle Schriften eingebettet, keine Rasterbilder; Seite 6 passt ohne Kürzungen und ohne Trennungen.

**Weitere Nachbauten (Nachtrag 3, 02.10.2026; Seitenangaben 9-Seiten-Zählung)**

- Gleiches Verfahren wie `bar.tex`/`mobil.tex`: standalone, TikZ, Koordinaten in CSS-px (1 px = 0,75 bp), Inter eingebettet, keine Rasterbilder, Textbreiten per XeTeX gegen die Messung geprüft, Wörter statt Zahlen, Marken 1–3 per `\ohnemarken` abschaltbar. `scripts/build.sh` baut sie ohne Eintrag mit (Erkennung `^\documentclass…{standalone}`). Dateien, Messungen und Maße: Tabelle in Abschnitt 18.
- `info-mobil.tex/.pdf` (mobile Angaben eines Instruments, Gold aufgeklappt, 410 × 327,2 px): Stern, Aufklapp-Pfeil (Font) und Instrument-Bild (Raster) fehlen; Seitenhintergrund (angenommen `#04273C` wie `mobil.tex`) und Rahmenfarbe der Schaltflächen per Prüfbefehl bestätigen (Übergabe `nachbau-info-mobil.md`).
- Fehlende Icon-Glyphen aller neuen Nachbauten: 8.4.

**Offen:** Geschützte Fassung nicht neu erzeugt. Kontoübersicht mobil bei 440 px nachmessen (siehe ⚠ oben).

---

## 13. Farbrollen Kontogrundlagen

Verlauf (02.10.2026):

1. Nutzer: „Kannst du eine andere Akzentfarbe benutzen? Z. B. bei ‚Hebel' sieht man das Weiße nicht, und das Schwarze passt nicht rein.“ Präzisierung: „Alles, was mit Plattform-Elementen zu tun hat, bleibt original.“ → Commit `dc384c3`: Plattform-Blau `#0E5072` als Akzent (`akzent`/`akzenttint`/`akzentrand`).
2. Nutzer: „Guck mal, welche Farben bei Pending Orders benutzt wurden, benutze dieselben auch hier.“ → Plattform-Blau wieder entfernt, `akzent*` gelöscht. Doku 2 nutzt für eigene Grafiken und Kästen **nur noch die Farben und Rollen von Doku 1**.

**Pixeltreue zum ORIGINAL-PDF ist seit Schritt 1 bewusst aufgegeben.** `tools/pdf_vergleich.py --dokument kontogrundlagen-kosten` meldet Abweichungen – gewollt.

### 13.1 Farbrollen im Pending-Orders-Guide (Doku 1)

| Rolle | Farbe |
|---|---|
| Überschriften, starke Labels | `ink` `#14161A` |
| Fließtext | `body` `#3C4249` |
| Unterzeilen, Kicker | `muted` `#6D757E` |
| Fußzeile, Tabellenköpfe, Kleinst-Hinweise | `soft` `#9AA1AA` |
| Trennlinien, Rahmen der Regelkästen (`prule`), Badge-Rand | `rule` `#E2E5E9` |
| gestrichelte Hilfspfeile (Nullpunkt-Grafik) | `greya` `#A8AEB6` |
| Buy / Sell (Text, Kugeln, Kerzen, TP-/At-price-Linien gestrichelt) | `buy`=`pfgruen` `#0E7A4E` / `sell`=`pfrot` `#B23A2E` |
| Zonen | `buytint` `#E9F4EE` / `selltint` `#FAEDEB` (Nullpunkt, 55 %); Gewinnzone in den Charts `pfgruen`/`pfrot` 8 % |
| neutrale Kerzen (Fläche) | `pfgrau` `#97A5B4` |
| Kurslinie „Kurs jetzt“ | `pfgrey` `#6A6A6A` |
| Kästen `soft`, `merk` | `paper` `#F7F8F9` |
| kleine schwarze Akzente: Titellinie, Nullpunkt-Achse, Merk-Kante, Nummernkreise | `ink` |

Sichtbarkeit heller Flächen auf Weiß: Tönung in der Order-Farbe statt Grau, Zonen von (gestrichelten) Linien in Order-Farbe begrenzt, Kästen über Kanten/Rahmen (Merk-Kante `ink`, `prule` mit `rule`-Rahmen und farbiger linker Kante), Linien statt Vollflächen. Keine großen dunklen Flächen.

### 13.2 Zuordnung in Doku 2

(Seitenangaben seit `5f9d129` mit 8-Seiten-Zählung. Inhalt Stand Schritt 2/3; Hebel-Grafik und „geliehen“ sind inzwischen entfernt, Abschnitt 14.)

| Element | Farbe |
|---|---|
| Margin-Flächen (Deckblatt, Margin-Balken S. 4, Hebel-Quadrate S. 5, Swap-Block S. 6) | `pfgrau`, Beschriftung `ink` (vorher Weiß auf Schwarz bzw. Blau) |
| Free-Teile, Balance-/Equity-Balken, Trade volume, „Der Rest ist geliehen“, Kästen Balance/Profit-Losses/Equity und Zins/Aufschlag/Swap, Warnbereich der Level-Skala | Weiß mit `greya`-Rand (0,35–0,5 pt) |
| Gewinn / Verlust | `buytint`/`selltint`; Verlustteil S. 3 jetzt gestrichelt `sell` (wie S. 4); Hebel S. 5: äußere Kante der Gewinn-/Verlustzone gestrichelt `buy`/`sell` (wie TP-Linien) |
| Punkte der Zeitleisten S. 3 und Wochentage S. 6 | `ink` (kleiner Akzent, wie ORIGINAL) |
| Verlaufslinie „Wann gebucht wird“ S. 6 | `pfgrey` 1,2 pt (Kurslinien-Rolle) |
| Titellinie Deckblatt | `ink` (wie Doku 1) |
| Badge „Sechs Begriffe“ | Rand `rule` (wie Doku 1) |
| `merk` | `paper` + Kante `ink` (identisch mit Doku 1) |
| `soft` | in Schritt 2 (Commit `c615842`) Weiß mit `greya`-Rand; seit Schritt 3 wieder **identisch mit Doku 1**: `paper` ohne Rand (13.3) |

Unverändert: alle Textfarben (außer Text auf den Margin-Flächen: Weiß → `ink`), `greya`-Hilfslinien und Pfeile, `rule`-Trennlinien, Plattform-Nachbauten (`bar.*`, `mobil.*`, `panel.pdf`, `icons.tikz`) und alles daran auf Seite 7 (Ring, Rahmen, Linien, Marken A/B, `\pfn` 1–5).

**Kontraste:** `ink` auf `pfgrau` 7,21:1 (Weiß wäre 2,51, `body` 4,04 – deshalb `ink`) · `muted` auf Weiß 4,67:1 (vorher auf `akzenttint` 4,02, auf `paper` 4,39) · `buy` auf `buytint` 4,76:1 · `sell` auf `selltint` 5,19:1 · `body` auf `paper` 9,55:1. Ränder gegen Weiß: `greya` 2,24:1, `pfgrau` 2,51:1 (`rule` nur 1,26:1, `paper` 1,06:1). ⚠ `soft` als Textfarbe (Kleinst-Hinweise) hat auf Weiß nur ~2,5:1 – in beiden Dokumenten so, nicht Teil dieses Auftrags.

**Prüfung** (alte Zählung; „Seite 6“ = heute „In der Plattform“): 7 Seiten; Textpositionen aller 1448 Wörter identisch mit `dc384c3` (`pdftotext -bbox`); einzige Warnung Overfull \hbox 1,24 pt in der Spickzettel-Tabelle (schon vorher); 10 Schriften eingebettet; keine Rasterbilder. Seite 6 bei 150 und 300 dpi gegen `dc384c3`: Handy-Ausschnitt mit Marken und Liste (y 58–160 mm) und Desktop-Leiste (y 186–200 mm) **0 abweichende Pixel**; die Seite weicht nur in y 214,5–253,2 mm ab (`soft`-Kästen). Bilder (nicht eingecheckt, `build/` ist ignoriert): `build/Farben-Vergleich.png` (7 Seiten, oben `dc384c3`, unten neu, 70 dpi), `build/Farben-Hebel.png` (S. 4 vorher|nachher, 110 dpi), `build/Farben-Reihe.png` (Doku 1 S. 3 neben Doku 2 S. 3, 80 dpi).

### 13.3 Grafiken im Lehrbuch-Stil (Schritt 3)

Nutzer: „Im Pending-Orders-Dokument ist das Gute, dass alle Grafiken wie LaTeX-Grafiken und wie Schulungsdokumente aussehen. Im Kontogrundlagen-Dokument sieht vieles wie AI-generierte GUI aus – das nervt mich.“

**Was die Grafiken in Doku 1 ausmacht:** Achsen und Linien statt Karten (Nullpunkt-Achse `ink`, Kurslinie `pfgrey`); Beschriftung direkt an der Linie, auf weißem Grund, die Linie unterbrechend („Kurs jetzt“ in `\hthree`); Zonen als zarte Tönung zwischen Linien, begrenzt von gestrichelten Linien in Order-Farbe (1,5 pt, Muster 7/4 pt); Hilfspfeile `greya` mit Stealth-Spitze; keine abgerundeten Kästen mit Unterzeile, keine dunklen Vollflächen mit weißer Schrift; Labels klein (`\pflab`/`\lbl`), Versalien nur für Achsen-Überschriften.

**Neue Bausteine** in `Kontogrundlagen-Kosten.tex`: `\mass[farbe]{x1}{x2}{y}{Label}` (Maßlinie, Haarlinie 0,4 pt mit Stealth-Spitzen, Label mit `\strut` auf Weiß unterbricht die Linie), `\masslinie` (ohne Label), Stile `hilfslinie` (Maßhilfslinie `greya` 0,3 pt) und `zone` (wie At-price-/Take-Profit-Linie: 1,5 pt, 7/4 pt). TikZ-Bibliothek `decorations.pathreplacing` für die Klammern.

| Seite (neue Zählung) | vorher (AI-GUI-Muster) | jetzt |
|---|---|---|
| 1 Deckblatt | drei abgerundete Karten „Balance + Profit/Losses = Equity“, darunter Segmentbalken Margin/Free | **ein** eckiger Mengenbalken (Margin `pfgrau`, Free weiß, Haarlinien-Rahmen) mit Maßketten: oben Gesamtmaß „Equity“ (`body`) und Kette „Balance | Profit/Losses“, unten „Margin | Free“; Labels in `\hthree` gemischt geschrieben (vorher Versalien), Unterzeilen `\lbl` muted; Level-Linie und Hinweis unverändert |
| 3 Kontostand | Balken mit farbiger Markierungslinie | eckige Balken (Haarlinie), Ende der Balance als gestrichelte Bezugslinie, Differenz als Maßlinie in `buy`/`sell` mit „+ Profit“ / „– Losses“; Zeitleiste: Achse `body` 0,7 pt mit Pfeil, Ereignispunkte `ink`, „UNREALISIERT“ als Maßlinie von „öffnen“ bis „schließen“ |
| 4 Margin | Segmentbalken mit Text im Balken (Speicheranzeige-Optik) | drei Mengenbalken (6 mm) mit Maßketten „Margin | Free“ darüber; Verlust als getönte Zone mit gestricheltem `sell`-Rand außerhalb der Equity; Level als Achse (`body`, Pfeil) mit getönten Zonen ohne Rahmen, Stop-out-Schwelle im `zone`-Stil `sell`, Grenze zum Puffer gestrichelt `greya` |
| 5 Hebel | Quadrate und Kästen, Text in zwei Spalten | maßstäblicher Vergleich: Margin 7,5 mm in beiden Spalten, Trade volume 7,5 mm bzw. 75 mm (= 1 : 10, passend zur geplanten Tabelle „Ohne Hebel / Mit Hebel 1:10“); Gewinn/Verlust: gleiche Bewegung = gleiche Höhe (± 6 mm), Breite = Volumen, Zonen `buytint`/`selltint` zwischen gestrichelten `buy`/`sell`-Linien, Beschriftung über bzw. unter der Linie wie „Take-Profit“. Grafik 51 statt 64 mm hoch → unter dem Text ca. 80 mm frei. ⚠ Überholt 02.10.2026: Grafik entfernt, Seite ohne Illustration und ohne Grün/Rot (Abschnitt 14) |
| 6 Swaps | abgerundete Blöcke „Margin“/„Der Rest ist geliehen“; Kette aus drei Karten mit + und = | Position als **ein** Balken, seit 02.10.2026 **maßstäblich 1 : 10** (Margin 17 von 170 mm) und ohne „geliehen“: Gesamtmaß „Ihre Position in Crude Oil: 10.000 €“, Maß „Margin: 1.000 € bei Hebel 1:10 ein Zehntel der Position“; Herleitung als **Formelzeile** „Miete für die Aufbewahrung + Risikoanteil + Aufschlag des Brokers = Swap“ (`\hthree`, zentriert) mit geschweiften Klammern `greya`, darunter die Beträge 3 € · 3 € · 1 € · 7 € pro Nacht und eine zweite Klammer „Betrag des Liquiditätsanbieters: 6 €“ unter den ersten beiden (Begriff seit `ac919eb`) und „Betrag des Brokers: 1 €“ unter dem Aufschlag (`e70e62e`); Tageslinie und Woche: Zeitachse mit Pfeil (Tag `greya`, Woche `body`) |
| 7, 8, 9 (seit `0850815`) | – | nur `soft`-Kästen (wie Doku 1); Plattform-Elemente unverändert. S. 8 „Instrumente und Positionen“: Plattform-Nachbauten `info-desktop`/`info-mobil` (original) mit Legende `\pfn` 1–3, darunter Text und Tabelle |

`soft`-Kästen wieder genau wie in Doku 1 (`paper`, ohne Rand). ⚠ Ihre `muted`-Kicker (8 pt fett, Versalien) haben darauf 4,39:1 – wie in Doku 1. Merk-Kasten und Badge unverändert wie Doku 1.

**Neue Grafik im Lehrbuch-Stil (Nachtrag 3):** `desktop-schema.tex/.pdf` (170 × 82,4 mm, IBM Plex Sans, noch nicht eingebunden; Übergabe `docs/uebergaben/desktop-schema.md`) – Schema statt Nachbau: weiße Bereiche, Teilungslinien `greya`, Details `rule`, Kopfleiste und unterste Leiste `paper`, Kurslinie `pfgrey`, SELL/BUY in `selltint`/`sell` bzw. `buytint`/`buy` (Rollen 13.1). Bezeichnungen fett in `ink`: „Kursliste“, „Chart“, „Tabelle der Positionen“, „Unterste Leiste“. Kennbuchstaben A–D (Kreise wie `\cn`) per `\mitkennung`, Standard aus.

**Prüfung** (alte Zählung): 7 Seiten; einzige Warnung Overfull \hbox 1,24 pt in der Spickzettel-Tabelle (alt); 10 Schriften eingebettet; keine Rasterbilder. Fließtext an derselben Stelle wie in `c615842` (Seiten 1–3, 5–7; nur Grafik-Beschriftungen bewegt), Seite 4 rückt unter der kleineren Hebel-Grafik nach oben. Seite 6 bei 300 dpi gegen `dc384c3` und `c615842`: Handy-Ausschnitt mit Marken und Liste (y 58–160 mm), Desktop-Leiste (y 186–200 mm) und alles oberhalb der Kästen (y 0–214 mm) **0 abweichende Pixel**. Bilder (nicht eingecheckt): `build/Grafik-Vergleich.png` (7 Seiten, oben `c615842`, unten neu, 70 dpi), `build/Grafik-Reihe.png` (Doku 1 S. 2 und 3 neben Doku 2 S. 3 und 4, 80 dpi).

---

## 14. Hebel-Vergleich mit Zahlen (Kontogrundlagen S. 5)

Stand 02.10.2026 (Commits `09b31e8`, `706317e`; Feinschliff `e70e62e`, Übergabe `docs/uebergaben/kg-hebel-swap-feinschliff.md`). **Seit `5f9d129` ist es S. 5** (vorher S. 4; „Swaps“ ist S. 6). Nutzerwunsch: ein Vergleich wie im englischen Lehrbuchbeispiel „you vs. your friend“ (CFD mit Hebel gegen direkten Kauf, Tabellen „Opening the Positions / Closing the Positions“), aber mit **einfachen Zahlen**. Ersetzt die frühere Fassung (Einzeltabelle „Ohne Hebel / Mit Hebel 1:10“ mit 100 €, Fazit und Grafik).

**Nutzervorgaben 02.10.2026:** „für die Hebel-Seite braucht es keine Illustrationen, keine Farben Grün oder Rot“; Zahlen nach der Skizze des Nutzers (`originals/skizze-hebel-swap.png`).

⚠ **Zahlen-Ausnahme 3** (Abschnitt 2.3), nur S. 5: 1.000 €, **2.000 €** (seit `e70e62e`), 10.000 €, 9.000 €, 1:10 und der Swap-Betrag 7 € pro Nacht samt der Kurswerte. Nicht als Freigabe für weitere Beträge im Dokument verstehen. Das Swap-Beispiel auf S. 6 ist eine eigene, ebenfalls vom Nutzer gewünschte Ausnahme (Ausnahme 4, Abschnitt 5.3).

**Vorgaben aus derselben Runde (über den Koordinator weitergegeben):**

- Register: gehobenes, präzises Standarddeutsch (C1, seriöses Schulungsdokument einer Bank), ganze Sätze mit klarer Logik (folglich, demnach, hingegen, sofern), keine saloppen Bilder („fressen“, „wird es eng“, „kostet dich“), keine Slogans, keine Gedankenstrich-Ketten; für Laien verständlich.
- **Anrede „Sie“** (Entscheidung des Nutzers); der Durchgang ist erledigt (Abschnitt 15).
- **Rein informativ:** keine Handelsentscheidung nahelegen oder bewerten. Keine Wertungen wie „Vorteil/Nachteil“, „was dafür/dagegen spricht“, „lohnt sich“, „sinnvoll“, „Gewinnverstärker“. **Kein Grün/Rot** auf dieser Seite (auch nicht für Gewinn/Verlust).

**Entfernt:** Grafik „Ohne Hebel / Mit Hebel“ (inkl. „Trade volume“), alle `buy`/`sell`-Färbungen, alte Einzeltabelle, altes Fazit und der Begriff „Finanzierungskosten“.

**Aufbau der Seite (von oben, Lehrbuch-Aufbau):** Kicker, Titel, Lead (unverändert) · `\Htwo` „Ein Vergleich mit einfachen Zahlen“ · Geschichte (3 Zeilen) · Tabelle „Öffnen der Positionen“ · Überleitung (1 Zeile) · Tabelle „Schließen der Positionen“ · Schluss (3 Zeilen) · zwei `soft`-Kästen (gleich hoch, `equal height group=hebel`; seit `e70e62e` „AUSWIRKUNG AUF DIE MARGIN“ – „Ein großes Volumen erfordert nur eine geringe Margin. Folglich bleibt ein größerer Teil der Equity frei.“ – und „AUSWIRKUNG AUF KURSBEWEGUNGEN“; vorher „… AUF DEN KAPITALEINSATZ“) · Merk-Kasten „Wo der Hebel steht“ (Information → Leverage; seit `e70e62e` mit dem Satz „Der Hebel eines Instruments kann niedriger sein als der Hebel Ihres Kontos; maßgeblich ist stets der Wert des Instruments.“). Unter der zweiten Tabelle der Hinweis „Alle Beträge sind fiktiv und dienen ausschließlich der Veranschaulichung.“ (`\micro`, `soft`). Die Seite ist voll (Rest ca. 2 pt).

**Direktkauf über die Bank (Bekannter) gegen Broker mit Hebel 1:10 (Sie).**

Geschichte: „Angenommen, Sie und ein Bekannter verfügen über je 2.000 € und erwarten, dass der Kurs von Instrument XY steigt. Ihr Bekannter kauft Instrument XY für 1.000 € direkt über das Wertpapierdepot seiner Bank, also ohne Hebel. Sie öffnen hingegen beim Broker eine Position mit Hebel 1:10.“

Spaltenköpfe (`\hdd`, zweizeilig): „Ihr Bekannter / Direktkauf über die Bank“ · „Sie / Broker, Hebel 1:10“; der Tabellentitel (`\ttl`, fett, `ink`) steht in der ersten Kopfzelle.

| Öffnen der Positionen | Ihr Bekannter (Direktkauf über die Bank) | Sie (Broker, Hebel 1:10) |
|---|---|---|
| Kurs von Instrument XY | 100 € | 100 € |
| Volumen (Wert der Position) | 1.000 € | 10.000 € |
| Einsatz bzw. Margin | 1.000 € | 1.000 € |
| Geliehener Betrag (Volumen minus Margin) | – | 9.000 € |
| Auf dem Konto frei verfügbar (Free) | – | 1.000 € |

Überleitung: „Am nächsten Tag steht Instrument XY bei 105 €, und Sie beide schließen Ihre Positionen.“

| Schließen der Positionen | Ihr Bekannter | Sie |
|---|---|---|
| Kurs von Instrument XY | 105 € | 105 € |
| Ergebnis vor Swap | +50 € | +500 € |
| Kosten über Nacht | kein Swap | Swap: 7 € pro Nacht (→ Swaps) |
| Ergebnis nach Swap | +50 € | +493 € |
| Ergebnis vor Swap, gemessen an Einsatz bzw. Margin | +5 % | +50 % |

Keine Volumen-Zeile beim Schließen (1.050/10.500 € wären neue Zahlen). Darunter: „Alle Beträge sind fiktiv und dienen ausschließlich der Veranschaulichung.“ (Stand `e70e62e`; Tabellen der Fassung davor: „Margin“, „Geliehener Betrag“, „Einsatz“, „vor Kosten“.)

Schluss (seit `e70e62e`): „Bei einem Rückgang auf 95 € hätte der Hebel den Verlust ebenso vergrößert: −50 € beim Direktkauf gegenüber −500 € beim Broker, jeweils vor Swap. Fiele der Kurs um 10 %, entspräche Ihr Verlust bereits der Margin von 1.000 €. Fällt der Kurs weiter, schließt die Plattform die Position spätestens am Stop out.“

**Rechnungen geprüft:** 10.000 : 10 = 1.000; 10.000 − 1.000 = 9.000; 2.000 − 1.000 = 1.000 (Free); 100 → 105 = +5 %: 1.000 € → +50 €, 10.000 € → +500 €; 500 − 7 = 493; 50 bzw. 500 auf 1.000 € = 5 % bzw. 50 %; bei 95 €: −50 €/−500 €; −10 % von 10.000 € = −1.000 € = ganzer Einsatz. Zahlen im Abschnitt nur: 1.000, 2.000, 10.000, 9.000, 1:10, 100, 105, 95, 50, 500, 7, 493, 5 %, 50 %, 10 %. „Spread“ ist nicht eingeführt; „Öffnen“ statt „Eröffnen“ wie auf „Margin“ und „Auf einen Blick“ (alt S. 3/S. 7).

**Stop-out-Aussage** (Begründung der Fassung vor `e70e62e`; der Schluss lautet seitdem wie oben unter „Schluss“, ohne „in der Regel“): Liegt der Stop-out-Wert des Kontos über null, schließt die Plattform, bevor die Equity null erreicht – also vor dem Verlust des gesamten Einsatzes. „In der Regel“, weil der Wert je Konto verschieden ist und Kurssprünge möglich sind; **keine Prozentschwelle genannt** (wie S. 3). ⚠ Je nach Stop-out-Wert kann schon bei 95 € der Stop out greifen; die Rechnung −500 € bleibt davon unberührt. Der Widerspruch 2 der Prüfung (Margin = ganzes Guthaben, Free = 0, Level sofort am Stop out) ist durch die je 2.000 € mit Free 1.000 € behoben.

**Swap auf der Hebel-Seite:** Der Swap wird hier **nicht** mit dem geliehenen Betrag begründet („Miete“ in der Skizze = Aufbewahrung, z. B. von Rohstoffen); die Erklärung steht auf S. 6 (Abschnitt 5.3). Die Zeile „kein Swap“ gilt für den Direktkauf über das Wertpapierdepot der Bank, nicht für eine Position beim Broker. ⚠ Überholt ist damit die frühere Notiz „kein Swap ohne Hebel“ (Swap = Zins für geliehenes Geld) samt dem Hinweis auf CFD-Plattformen; zur Rückfrage in Abschnitt 16 (b) siehe dort.

**Layout:** Spalten 71 / 42 / 48,53 mm (+ 2 × 2 `\tabcolsep` = 170 mm). Kopfzellen beginnen mit `\leavevmode` (sonst steht `\color` zuerst in der Zelle und es entsteht ca. 5 mm Lücke). Abstände: Lead 8 · Geschichte 6 · Tabelle 5 · Überleitung 6 · Tabelle 5 mm; seit `e70e62e` danach Hinweis „fiktiv“ 1 mm und Schluss 3,5 mm (vorher Schluss 6 mm). Zahlen in IBM Plex Sans (nicht Mono), schmales Leerzeichen `\,` vor € und %, Minus U+2212, Tausenderpunkt; `Hebel~1:10`, `Instrument~XY` gegen Umbrüche. Der Satzspiegel endet bei 279 mm: **Jede zusätzliche Zeile auf S. 5 kann den Merk-Kasten auf eine neue Seite schieben** (Rest seit `e70e62e` ca. 2 pt) – nach Textänderungen Seitenzahl prüfen.

**Prüfung** (Stand `706317e`, alte Zählung: dort S. 4 = heute S. 5): 7 Seiten; Log ohne Warnung; 10 Schriften eingebettet; keine Rasterbilder; S. 1–3 und 5–7 pixelgleich (60 dpi) mit `09b31e8`. Stand `e70e62e` (neue Zählung): 8 Seiten, Rest S. 5 ca. 2 pt und S. 6 ca. 1 pt, kein Over-/Underfull, 10 Schriften eingebettet, 0 Rasterbilder; S. 1, 4, 7, 8 bei 60 dpi pixelgleich zum Stand davor. Bild (nicht eingecheckt): `build/agent-hebel2/seite4.png`. Prüfkommandos: `cd dokumente/kontogrundlagen-kosten && xelatex -interaction=nonstopmode -output-directory=../../build/agent-hebel2 Kontogrundlagen-Kosten.tex`, danach (heute) `pdftotext -f 5 -l 5 -layout …`.

**Übergaben:** `docs/uebergaben/kg-hebel-bank-broker.md` (Stand nach Nachfolger `kg-hebel-lehrbuch`) und `docs/uebergaben/kg-swap-seite.md` sind erledigt, ebenso `docs/uebergaben/kg-hebel-swap-feinschliff.md` (Feinschliff `e70e62e`).

## 15. Sprachdurchgang Kontogrundlagen: Sie-Form, C1, neutral (02.10.2026)

(Seitenangaben in diesem Abschnitt: alte Zählung, 7 Seiten.) Alle Texte von `Kontogrundlagen-Kosten.tex` (S. 1–7: Lead, Überschriften, Kästen, Grafik-Beschriftungen, Tabelle S. 7, Merk-Kästen, Texte neben den Plattform-Grafiken auf S. 6) auf **Sie-Form, gehobenes Deutsch (C1), rein informativ** umgestellt. Keine Umgangssprache, keine Slogans, keine Wertungen („Gesundheitsanzeige“, „genug Puffer“, „ehrliche Zahl“, „fressen“ … entfernt). „Spickzettel“ → „Auf einen Blick“, „Drei Faustregeln“ → „Kernaussagen“, „Margin Call“ → „Warnbereich“ (kein Plattform-Begriff), Skala S. 3 „GENUG PUFFER“ → „NORMALBEREICH“. Hebel-Tabelle und -Zahlen S. 4 unverändert; nur Lead und Merk-Kasten dort umformuliert (Länge gleich). ⚠ Die Hebel-Tabelle wurde danach ersetzt (Abschnitt 14). Plattform-Elemente (`bar.*`, `mobil.*`, `panel.pdf`, Marken A/B/1–5) unverändert – sie enthalten weiterhin den Platzhalter **„dein Guthaben“** (einzige du-Form im PDF; Nutzerentscheidung 02.10.2026: bleibt, endgültig – Abschnitt 8.2).
Nebenbei: Tabelle S. 7 im Flattersatz, letzte Spalte 62 → 61,5 mm (alter Overfull 1,24 pt weg); Kästen S. 2 gleich hoch (`equal height group=konto`). Prüfung: 7 Seiten, kein Overfull, keine Ziffern außer S. 4-Vergleich und Schrittmarken, kein Stop-Loss. Übersicht (nicht eingecheckt): `build/KG-Text-Uebersicht.png`.

## 16. Pending-Orders-Guide: Neufassung (Sie-Form, C1, neutral)

Ersetzt den Seitenplan in Abschnitt 4.3 (dort Stand des alten Chats, 6 Seiten). Datei: `dokumente/pending-orders/Pending-Orders-Guide.tex`.

**Seiten (jetzt 9):**

| Seite | Inhalt |
|---|---|
| S1 | Deckblatt: seit `a86882f` das SVG-Deckblatt aus der Testvariante (siehe (c)); Untertitel in Sie-Form |
| S2 | „Was eine Pending Order ist“: Market vs. Pending, Nullpunkt, „Was eine Pending Order im Ablauf verändert“ |
| S3–S6 | je ein Ordertyp: Chart + Randspalte „Was es ist“, „Typischer Einsatz“, „Take-Profit“, „Beispiel“ (Instrument XY); Lesehilfe nur einmal auf S3 |
| S7 | „Übersicht“ (früher Spickzettel): Chartreihe, Tabelle, „Drei Grundregeln“ |
| S8 | Order-Fenster: fünf Schritte + Type-Menü |
| S9 | „Eine wartende Order löschen“ (mobile Ansicht): Orders → Pending → Order antippen → Delete → Rückfrage „close order“ mit Delete bestätigen; Cancel bricht ab |

**Text:** Sie-Form, gehobenes C1-Deutsch, rein informativ (keine Wertungen; „Wann sinnvoll“ → „Typischer Einsatz“). Keine Zahlen außer Schrittnummern und Badge. Kein Stop-Loss im Text.

**Technik:**
- Zeile `hyphenrules=english` entfernt → deutsche Silbentrennung aktiv. Pixeltreue zum alten Original damit bewusst aufgegeben.
- Neue Makros: `\abschnitt`, `\beispiel`, `\chartzeile`, `\leadfix`. Linke Spalte `\labw` = 37 mm; `\abschnitt` setzt Label und Text per `\leavevmode` auf dieselbe Grundlinie.
- Abstandsparameter für S7/S9 in der Präambel: `\SPICKCHART`, `\SPICKTAB`, `\TROW`, `\TABMERK`, `\MERKPAR`, `\LOESCHSEP`.
- S7 endet wie S3–S6 bei ca. 264 mm; S9 im Flattersatz, 140 mm breit, endet bei ca. 238 mm.
- **Fußzeile** (02.10.2026, Commit `87a95f9`): „PENDING ORDERS · STANDARD TIER“ statt „… · KURZ-GUIDE“, im Guide und in der CoverTest-Variante (dort auch der Fuß des SVG-Deckblatts: „STANDARD TIER“ rechts).
- **PDF-Metadaten** (02.10.2026, Commit `145c398`): `pdftitle={Pending Orders – Standard Tier}` (vorher „Pending Orders – Kurz-Guide“); `pdfsubject` unverändert. Die CoverTest-Variante trägt noch „Kurz-Guide“.

**Entscheidungen beim Nutzer (Stand 02.10.2026):**
- (a) ~~Du-Platzhalter in Plattform-Nachbauten~~ („deine Menge / dein Wert / dein Ziel“ in `fenster-bl.pdf`, „dein Guthaben“ in `panel.pdf`/`mobil.tex`/`bar.tex`) → **erledigt: bleiben wie sie sind** (Nutzerentscheidung, endgültig). Nicht auf „Ihre …“ umbauen. „Set Stop-Loss“ im Fenster ist Plattform-Originaltext und bleibt.
- (b) ~~Swap ohne Hebel~~ → überholt: Kontogrundlagen S. 5 vergleicht seit 02.10.2026 den Direktkauf über die Bank (ohne Hebel, ohne Swap) mit dem Broker bei Hebel 1:10 (Abschnitt 14); die Swap-Erklärung steht nach dem Modell des Nutzers auf S. 6 (Abschnitt 5.3). Eine ausdrückliche Antwort des Nutzers zur CFD-Praxis (Swap oft auch bei 1:1) gab es nicht.
- (c) Cover-Testvariante `Pending-Orders-Guide_CoverTest.tex` (SVG-Cover): **Entscheidung des Nutzers (02.10.2026): Das SVG-Deckblatt wird in den Guide übernommen**; **umgesetzt in `a86882f`**: S. 1 von `Pending-Orders-Guide.tex` ist das SVG-Deckblatt (Navy-Band aus `cover-bg.pdf`, Inhalte absolut in mm, Charts bündig mit der Textkante, Mittellinie entfernt, Lücke um „KURS JETZT“ schmaler, Fuß „PENDING ORDERS · STANDARD TIER“); der Untertitel bleibt in Sie-Form („… damit Sie Einstieg, Auslösepreis und Richtung richtig kombinieren.“, die Testvariante hat noch die Du-Form); die Präambel bekam nur die Deckblatt-Farben `cvkicker`, `cvsub`, `cvpill`, `cvpilltext`. Prüfung: 9 Seiten, S. 2–9 bei 60 dpi pixelgleich zum Stand davor, Schriften eingebettet, keine Rasterbilder; Testvariante und `cover*`-Dateien unverändert. Die Innenseiten der Testvariante sind veraltet und werden nicht übernommen. Die drei Korrekturen sind in der Testvariante umgesetzt (siehe unten). Die Charts werden **nicht** auf volle Spaltenbreite gezogen (nicht beauftragt).
- Entscheidungen zu Kontogrundlagen S. 6 (Begriff „Liquiditätsanbieter“ statt „Bank“, umgesetzt in `ac919eb`; Gutschrift-Satz bleibt): Abschnitt 8.2.

**Deckblatt-Testvariante (02.10.2026, Commit `d55ca00`, Übergabe `docs/uebergaben/po-deckblatt-vorschau.md`):** Nur `Pending-Orders-Guide_CoverTest.tex`, `cover.svg`, `cover-bg.svg`, `cover-bg.pdf` geändert; der Guide selbst blieb dabei unverändert (Übernahme in den Guide: s. (c)).
- Charts bündig mit dem Text: linke Inhaltskante bei x = 20 mm bzw. 117,5 mm (gemessen 19,995 / 117,503 mm), Maßstab unverändert (72,5/174). Die Verschiebung (`shift` der vier Chart-Scopes) nutzt die linke Inhaltskante aus `charts.tikz` (bs/sl: 11,373 px, bl/ss: 14 px); **ändert sich `charts.tikz`, müssen diese Werte in der Testvariante angepasst werden**.
- Verwaiste Mittellinie (`center-rule-top`/`grid-connection`, x = 105, y 98–111) unter dem Navy-Band entfernt.
- Achse „Kurs jetzt“: Lücke 92,6–117,4 mm (vorher 87–123 mm), Label-Schriftbild 96,0–114,1 mm, Luft zum Schriftbild ca. 3,3 mm wie im Haupt-Guide; Platzhalter `ph-axis-label` auf x = 95, Breite 20.
- `cover-bg.pdf` entsteht mit `rsvg-convert -f pdf -o cover-bg.pdf cover-bg.svg` (Ordner `dokumente/pending-orders/`).
- Prüfung: `cd dokumente/pending-orders && xelatex -interaction=nonstopmode -halt-on-error -output-directory=../../build/agent-deckblatt Pending-Orders-Guide_CoverTest.tex`, dann `pdffonts -f 1 -l 1 …`. Vorschau (nicht eingecheckt): `build/agent-deckblatt/deckblatt-vorher.png`, `…/deckblatt-nachher.png` (100 dpi).

**Übergaben:** `docs/uebergaben/pending-orders-text.md`, `docs/uebergaben/kontogrundlagen-hebel.md`, `docs/uebergaben/kg-hebel-bank-broker.md` und `docs/uebergaben/kg-swap-seite.md` sind erledigt; `docs/uebergaben/po-deckblatt-vorschau.md` ist umgesetzt (Abschnitt „Übernahme“ der Übergabe), die Rückfragen dazu sind beantwortet (Abschnitt 8.2). Die Übergaben `kg-grundbegriffe.md`, `kg-hebel-swap-feinschliff.md` und `kg-plattform-uebersicht.md` (Doku 2) sind erledigt und in Abschnitt 17 eingearbeitet.

## 17. Nachtrag 2 (02.10.2026): Kontogrundlagen auf 8 Seiten

Umfang: `git log --oneline 4163359..3b34934` (Basis `4163359` = HANDOFF mit den Nutzerentscheidungen vom 02.10.). Die Inhalte stehen in den Abschnitten 2.2, 2.3, 5, 8, 13, 14 und 16; hier nur Übersicht und Umrechnung. Die Übergaben `docs/uebergaben/kg-grundbegriffe.md`, `kg-hebel-swap-feinschliff.md` und `kg-plattform-uebersicht.md` (mit dem Nachtrag „Seitenzahlen bleiben entfernt, Verweise per Seitentitel“) sind erledigt; ihre Abschnitte „Für HANDOFF.md“ sind hier eingearbeitet.

**Commits (älteste zuerst):**

| Commit | Inhalt |
|---|---|
| `a86882f` | Pending Orders: SVG-Deckblatt aus der Testvariante in den Guide übernommen (16) |
| `ac919eb` | Doku 2, „Swaps“: Liquiditätsanbieter statt Bank (5.3) |
| `750c605` | Prüfung `docs/pruefung/kontogrundlagen-begriffe-bilder.md`: unerklärte Begriffe, fehlende Plattform-Bilder (8.4) |
| `76c0e61` | Prüfung `docs/pruefung/handbuch-abgleich.md`: Abgleich der Funde mit dem CFD-Handbuch des Nutzers (8.4) |
| `848378e` | `originals/Education_Session_1_Account_Basics_Kosten_2.pdf`, Reverse-Engineering-Fassung des Nutzers (5.1) |
| `5f9d129` | Doku 2: neue Seite „Grundbegriffe“, Begriffe und Verweise auf den alten S. 1–4, Swap-Buchung nach der RE-Fassung |
| `e70e62e` | Doku 2: Feinschliff „Hebel“ und „Swaps“; Bonus statt Commission |
| `145c398` | Doku 2: „In der Plattform“ und „Auf einen Blick“; Guide-`pdftitle` |
| `3b34934` | Doku 2: Verweise per Seitentitel statt Seitenzahl, Fußzeile ohne Seitenzahl |

**Seitenzählung Doku 2** (Seitenangaben in HANDOFF: neue Zählung, außer wo „alte Zählung“ steht; im Dokument selbst gibt es keine Seitenzahlen):

| Seitentitel (Kicker) | alt (7 Seiten) | neu (8 Seiten) |
|---|---|---|
| Deckblatt | 1 | 1 |
| Grundbegriffe | – | 2 |
| Kontostand | 2 | 3 |
| Margin | 3 | 4 |
| Hebel | 4 | 5 |
| Swaps | 5 | 6 |
| In der Plattform | 6 | 7 |
| Auf einen Blick (früher „Spickzettel“) | 7 | 8 |

**Nutzerangaben und Quellen (02.10.2026):**

- Auf der Plattform gibt es **keine Commission**; es gibt einen **Bonus** (handelbar, Gewinne daraus gemäß den AGB auszahlbar). Credit wird nur genannt (2.2, 5.3).
- **Swap-Buchung** (Quelle `originals/Education_Session_1_Account_Basics_Kosten_2.pdf`, Abschnitt 7.3 und 8): bei der offenen Position verbucht, im angezeigten Profit enthalten, beim Schließen in der Balance (5.3, 5.4).
- **Rollover:** die RE-Fassung nennt „üblicherweise 22:00 UTC bzw. 0:00 Serverzeit“; der Nutzer gab **23:00 Uhr Amsterdamer Zeit** an (im Dokument verwendet; 2.3, 5.3).
- Hinweis „Alle Beträge sind fiktiv und dienen ausschließlich der Veranschaulichung.“ auf „Hebel“ und „Swaps“ (Nutzerwunsch; 2.3).
- **Seitenzahlen bleiben entfernt** (#58/#59); Verweise per Seitentitel, Markennummern 1–5 im mobilen Nachbau sind Wegweiser (Ausnahme 1; 2.3, 5.3).
- Guide: `pdftitle` „Pending Orders – Standard Tier“ (16).

**Prüfdateien (Verweis, nicht abgeschrieben):** `docs/pruefung/kontogrundlagen-begriffe-bilder.md` (Funde A1–A16, Widersprüche, Bilder; Stand `ac919eb`, alte Zählung) und `docs/pruefung/handbuch-abgleich.md` (Handbuch belegt kein Plattformverhalten). Status der Funde und offene Punkte: 8.4.

**Prüfstand:** Bei `145c398` (Übergabe `kg-plattform-uebersicht`): Doku 2 mit 8 Seiten, Rest „In der Plattform“ ca. 9 pt und „Auf einen Blick“ ca. 180 pt, Log ohne Warnungen, 10 Schriften eingebettet, 0 Rasterbilder; Guide 9 Seiten, 11 Schriften eingebettet. Für diesen Nachtrag neu gebaut (Stand `3b34934`, in einen Ordner außerhalb des Repos gebaut, kein Dokument geändert): 8 Seiten in der Reihenfolge der Tabelle oben, 10 Schriften eingebettet, 0 Rasterbilder, kein Over-/Underfull, im Text weder „Commission“ noch eine Seitenzahl, `pdftitle` „Kontogrundlagen & Kosten – Schulungseinheit“. Die geschützten Fassungen wurden nach diesen Änderungen nicht neu erzeugt (6.3).

---

## 18. Nachtrag 3 (02.10.2026): Instrumente, Positionen, Nachbauten

Umfang: `git log --oneline 3b34934..5455781` (18 Commits; der erste, `bee5507`, ist Nachtrag 2). Die Inhalte stehen in den Abschnitten 2.2, 2.3, 3.3, 5.2–5.4, 8.1, 8.4, 9, 12 und 13.3; hier nur Übersicht, Zählung und Dateien. Die Abschnitte „Für HANDOFF.md“ der Übergaben `docs/uebergaben/kg-instrument-info-wege.md`, `kg-seite-instrumente.md`, `nachbau-info-desktop.md`, `nachbau-info-mobil.md`, `nachbau-kursliste.md`, `nachbau-positionen-desktop.md` (mit „Vollständige Fassung“) und `desktop-schema.md` sind eingearbeitet; Einzelheiten (Maße, Breitenproben, Platzhalter) stehen nur dort.

**Commits (älteste zuerst):**

| Commit | Inhalt |
|---|---|
| `bee5507` | HANDOFF: Nachtrag 2 (17) |
| `3cc4418` | Plattform-Fakten Kursliste (Desktop) und Instrument-Info (mobil) aus dem DOM, `docs/plattform/dom-kursliste-instrument-info.md` (5.2) |
| `4b39f4c` | Plattform-Fakten Info-Fenster eines Instruments am Desktop (5.4) |
| `989a638` | Messung `originals/messungen/instrument-info-desktop.json` |
| `25049f5` | Doku 2: Wege zu den Angaben eines Instruments, Kursliste, Forex; Bid/Ask (2.2, 5.3; Übergabe `kg-instrument-info-wege.md`) |
| `6d09ff6` | Messung `originals/messungen/instrument-info-mobil.json` |
| `c1e2878` | Doku 2: Bid/Ask wieder entfernt, Zeile Spread (2.2, 5.3) |
| `3471ec7` | Nachbau `info-desktop` (Übergabe `nachbau-info-desktop.md`) |
| `0e9655e` | Nachbau `info-mobil` (Übergabe `nachbau-info-mobil.md`) |
| `c3ec368` | Plattform-Fakten Liste der offenen Positionen, mobil und Desktop, `docs/plattform/dom-positionsliste.md` (5.2, 8.4) |
| `6562d87` | Messungen `kursliste-desktop.json` und `positionen-desktop.json` (anonymisiert) |
| `3956ea7` | Lehrbuch-Schema `desktop-schema` (13.3; Übergabe `desktop-schema.md`) |
| `4c39571` | Nachbau `kursliste-desktop` (Übergabe `nachbau-kursliste.md`) |
| `d231c27` | Kursliste: Platinum und Silver nach dem Zeilenmuster ergänzt (nicht gemessen) |
| `0850815` | Doku 2: neue S. 8 „Instrumente und Positionen“, Begriff Total Profit (2.2, 2.3, 5.3; Übergabe `kg-seite-instrumente.md`) |
| `834863a` | Plattform-Fakten: Profit/Losses = Summe von Total Profit (5.4) |
| `8ff840a` | Nachbau `positionen-desktop` als Ausschnitt (Übergabe `nachbau-positionen-desktop.md`) |
| `5455781` | Nachbau `positionen-desktop-voll` für Querformat (ebd., „Vollständige Fassung“) |

**Seitenzählung Doku 2** (seit `0850815`; im Dokument keine Seitenzahlen):

| Seitentitel (Kicker) | 8 Seiten (Abschnitt 17) | neu (9 Seiten) |
|---|---|---|
| Deckblatt | 1 | 1 |
| Grundbegriffe | 2 | 2 |
| Kontostand | 3 | 3 |
| Margin | 4 | 4 |
| Hebel | 5 | 5 |
| Swaps | 6 | 6 |
| In der Plattform | 7 | 7 |
| Instrumente und Positionen | – | 8 |
| Auf einen Blick | 8 | 9 |

**Neue Dateien in `dokumente/kontogrundlagen-kosten/`** (alle standalone, Vektor, reproduzierbar, Log ohne Warnungen; Messungen in `originals/messungen/`):

| Datei (`.tex`/`.pdf`) | Inhalt | Messung | Maße / Maßstab | eingebunden |
|---|---|---|---|---|
| `info-desktop` | Info-Fenster eines Instruments am Desktop (Gold, Kopf „XAUUSD“, Raster der Angaben; ohne Handelszeiten), Marken 1–3 | `instrument-info-desktop.json` | PDF 338 × 242,8 px (Fenster 290 × 194,8 px + 24 px Schattenrand), 1 px = 0,75 bp; im Dokument 1 px = 0,225 mm, Fenster 65,3 × 43,8 mm, Schrift 7,7 pt | **ja**, S. 8 |
| `info-mobil` | Angaben eines Instruments mobil (Quotes, Gold aufgeklappt; Kopfzeile, Raster 3 × 4, vier Schaltflächen), Marken 1–3 | `instrument-info-mobil.json` | 410 × 327,2 px (307,5 × 245,4 pt); im Dokument 92,3 × 73,6 mm, Schrift 7,7 pt | **ja**, S. 8 |
| `kursliste-desktop` | Kursliste am Desktop, Metals aufgeklappt (Platinum, Silver nur nach Zeilenmuster), Info-Zeichen, Marke 1 an Gold | `kursliste-desktop.json` | 304 × 410 px = 228 × 307,5 bp; bei 50 mm: 1 px = 0,164 mm, 50 × 67,4 mm, Schrift 5,6 pt | nein |
| `positionen-desktop` | Tabelle der offenen Positionen als Ausschnitt mit Bruchkante (links Instrument, Type, Amount, Trade Volume; rechts Swap, Commission, Total Profit, Margin; Reiter; 2 Zeilen), Marken 1–3 | `positionen-desktop.json` | 956,2 × 145 px; bei 170 mm: 1 px = 0,178 mm, 170 × 25,8 mm, Schrift 6,05 pt | nein |
| `positionen-desktop-voll` | dieselbe Tabelle vollständig ohne Bruchkante (13 Spalten ID … Margin, Leiste New order/Search/All sides/All profits), Marken 1–3 | `positionen-desktop.json` | 1484 × 145 px; bei 257 mm (Querformat): 1 px = 0,173 mm, 257 × 25,1 mm, Schrift 5,9 pt | nein |
| `desktop-schema` | Lehrbuch-Schema des Desktop-Bildschirms (Kursliste, Chart, Tabelle der Positionen, Unterste Leiste), IBM Plex Sans, A–D per `\mitkennung` | keine; Proportionen nach Screenshot des Nutzers (nicht im Repo) | 170 × 82,4 mm | nein (Vorschlag: S. 7) |

**Offene Konsolenbefehle** (nur Verweis; Befehl und „was vorher geöffnet sein muss“ stehen in der Übergabe):

- `nachbau-info-desktop.md`, „Offen“ 1: Leerzeichen bei Leverage vor oder hinter dem Doppelpunkt.
- `nachbau-info-mobil.md`, „Weggelassen / angenommen“: Prüfbefehl für Seitenhintergrund und Rahmenfarbe der Schaltflächen.
- `nachbau-kursliste.md`, „Offen“ 1: Pfeil auf/ab der Kategorien und Richtungspfeil der Zeilen.
- `nachbau-positionen-desktop.md`, „Offen“ 1: Ausrichtung des Reiter-Texts, Sortierpfeile der Köpfe.
- `nachbau-positionen-desktop.md`, „Offen (vollständige Fassung)“ 1: Farbe des Platzhalters „Search“ (vorläufig `#A8BBBE`), Auswahlpfeile von All sides / All profits.
- Ohne Befehl bisher: mobile Liste der offenen Positionen (Orders → Active), Reiter „Information“ (8.4).

**Prüfstand** (laut Übergabe `kg-seite-instrumente.md`, Stand `0850815`): 9 Seiten, Log ohne Over-/Underfull, 15 Schriften eingebettet, 0 Rasterbilder; Zahlen nur an den freigegebenen Stellen, Nummern auf S. 7 und 8; S. 1 und 4 pixelgleich. Für diesen Nachtrag nicht neu gebaut. Die geschützten Fassungen sind weiterhin nicht neu erzeugt (8.1, 6.3).

## 19. Nachtrag 4 (02.10.2026): Einbau der Querformat-Seiten, Schutz-Werkzeug

Die alte Sitzung hatte den Einbau fertig, aber nicht committet (Limit). Er ist nach ihren Screenshots neu gebaut (`fe8c471`):

| Seite | Inhalt |
|---|---|
| 7 „In der Plattform“ (hoch) | Einleitung und Notiz gekürzt (Bonus-Satz entfällt, steht in „Grundbegriffe“; neu: Reiter **Information** nennt Leverage und Stop out); `desktop-schema.pdf` (170 mm) über `bar.pdf`; Verweissatz auf S. 8/9. Kästen DESKTOP/MOBILE entfallen. |
| 8 „Angaben eines Instruments“ (quer) | Kursliste (`kursliste-desktop-ohne.pdf`, gezeigt Energies bis Commodities) → Ring um das Info-Zeichen bei Gold → Pfeil „Klick auf das **Info-Zeichen (i)**“ → `info-desktop.pdf`; rechts MOBILE `info-mobil.pdf`; Legende 1–3 in einer Zeile. Maßstab 1 px = 0,22 mm. Label `s:instrumente`. |
| 9 „Offene Positionen“ (quer) | Wege DESKTOP/MOBILE, `positionen-desktop-voll.pdf` auf 257 mm, Erklärungstabelle (Amount, Trade Volume, 1 Swap, 2 Total Profit, 3 Margin). Label `s:positionen`. |
| 10 „Auf einen Blick“ (hoch) | unverändert |

- Querformat per `\quer` / `\hoch` (Präambel): Seitengröße je Seite, Ränder und Kickerhöhe wie hochkant, Fußzeile über `\headwidth`.
- `kursliste-desktop-ohne.pdf`: Variante ohne Marke, gebaut mit `xelatex -jobname=kursliste-desktop-ohne '\def\ohnemarken{}\input{kursliste-desktop}'` (nicht in `scripts/build.sh`).
- `positionen-desktop.pdf` (Ausschnitt mit Bruchkante) ist nicht mehr eingebunden.
- Swap-Doppelungen gestrichen (Nutzer, 02.10.2026): Merk-Kasten „Zusammenfassung“ am Ende von „Swaps“ und der Satz „Der Swap einer Position geht beim Schließen … in die Balance ein“ im Kasten BALANCE auf „Kontostand“. Die Buchung (bei der Position, in Total Profit enthalten, beim Schließen in die Balance) steht weiter in „Grundbegriffe“, „Offene Positionen“ und „Auf einen Blick“. Die Swap-Zeilen der Hebel-Tabelle bleiben.
- Verweise „Instrumente und Positionen“ → „Angaben eines Instruments“ (S. 2, 5, 6); Text „Trade Volume“ wie auf der Plattform.
- **Achtung Build:** `scripts/build.sh` ersetzt die eingecheckten Nachbau-PDFs, wenn TeX Live eine andere Version hat (nur binär verschieden). Vor dem Commit mit `git checkout dokumente/kontogrundlagen-kosten/*.pdf` zurücksetzen, außer ein Nachbau wurde absichtlich geändert.

**Prüfstand `fe8c471`:** Doku 2 mit 10 Seiten (S. 8/9 quer), Log ohne Over-/Underfull, 21 Schriften eingebettet, 0 Rasterbilder, Ziffern nur Wegweiser 1–5 und 1:10. Guide mit 9 Seiten, 0 Warnungen, alles eingebettet. Schutz (`tools/schutz.py`): Doku 2 21/21 und Guide 11/11 ToUnicode ersetzt, Pixelabweichung 0, P = −3904, AES-256, PDF 2.0.
