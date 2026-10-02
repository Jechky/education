# HANDOFF – Trading-Schulungs-PDFs (Stand: Ende des claude.ai-Chats, 07.09.2026)

> **Für Claude Code.** Diese Datei fasst den kompletten Chat-Verlauf (`docs/chat-verlauf.txt`, Nachrichten #0–#159, 04.–07.09.2026) zusammen, damit du genau dort weitermachen kannst, wo der Chat aufgehört hat.
> Quelle ist **nur der Textexport**: Tool-Aufrufe, Bilder, Screenshots, Konsolen-Ausgaben und die erzeugten Dateien fehlen. Alles, was hier steht, ist im Verlauf belegt (Nachrichtennummer in Klammern, z. B. „(#103)“). Was nicht sicher belegt ist, ist mit **⚠ unsicher** markiert.
> Die erzeugten Dateien (.tex, .pdf, Skripte) lagen nur in der Sandbox des alten Chats und sind **hier nicht vorhanden** – siehe Abschnitt 9.

---

## Inhalt

1. [Kurzüberblick](#1-kurzüberblick)
2. [Harte Vorgaben des Nutzers (Checkliste)](#2-harte-vorgaben-des-nutzers-checkliste)
3. [Design-System](#3-design-system)
4. [Dokument 1 – „Pending Orders“](#4-dokument-1--pending-orders-kurz-guide-6-seiten)
5. [Dokument 2 – „Schulungseinheit 1: Kontogrundlagen & Kosten“](#5-dokument-2--schulungseinheit-1-kontogrundlagen--kosten-7-seiten)
6. [Technik](#6-technik)
7. [Konsolenbefehle (JS) aus dem Verlauf](#7-konsolenbefehle-js-aus-dem-verlauf)
8. [Offene Punkte / nächste Schritte](#8-offene-punkte--nächste-schritte)
9. [Fehlende Dateien](#9-fehlende-dateien)
10. [Unklarheiten und Widersprüche im Verlauf](#10-unklarheiten-und-widersprüche-im-verlauf)
11. [Stand Wiederherstellung](#11-stand-wiederherstellung)
12. [Wiederherstellung Kontogrundlagen](#12-wiederherstellung-kontogrundlagen)
13. [Akzentfarbe Kontogrundlagen](#13-akzentfarbe-kontogrundlagen)

---

## 1. Kurzüberblick

| | |
|---|---|
| **Projekt** | Deutschsprachige Schulungs-PDFs zum Trading, gesetzt mit XeLaTeX + TikZ |
| **Zielgruppe** | Laien/Einsteiger, auch Ältere (#20). Der Text muss für Laien verständlich sein (#106). |
| **Plattform** | Ein **WebTrader** (Desktop-Browser + Mobile) mit **englischer Oberfläche** (#16, #133). Begriffe im Dokument = Begriffe der Plattform. Der Name der Plattform/Firma steht nirgends im Verlauf. |
| **Format** | Helles **A4-Hochformat** (#102). Eine dunkle Querformat-Variante (BnkPro-Stil, #35) wurde nur als Demo gebaut und **nicht** übernommen; die Blattfarbe soll unverändert bleiben (#50). |
| **Dokument 1** | „**Pending Orders**“ – Kurz-Guide, 6 Seiten, fertig inkl. geschützter Fassung (#125). |
| **Dokument 2** | „**Schulungseinheit 1: Kontogrundlagen & Kosten**“ – 7 Seiten, gebaut, Plattform-Seite wird gerade verfeinert (#157). |
| **Ausgabe je Dokument** | Zwei Fassungen: **ORIGINAL** (zum Weiterarbeiten) und **GESCHÜTZT** (zum Weitergeben) (#119). |

**Stand beim Abbruch (#157 → #158):** In Dokument 2 waren gerade die mobile Kontoübersicht (Vektor-Nachbau mit gemessenen Werten) und die Desktop-Leiste (im **blauen** Design, teils geschätzt) auf der Seite „In der Plattform“ eingebaut. Offen waren zwei weitere Messläufe mit dem Konsolenbefehl aus #153 (Desktop-Leiste im blauen Design und Instrument-Info-Feld). Danach bat der Nutzer um diese Übergabedatei (#158); die Antwort #159 ist leer.

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
- [ ] **Kein Ask/Bid**; stattdessen „über / unter dem aktuellen Kurs“ (#14, #15).
- [ ] „Market Buy / Market Sell“ gibt es auf der Plattform nicht (#21) → Reiter heißt „New Market Order“.
- [ ] **„Aktivierungspunkt“** für den Wert bei At price (#118). Vorgegebene Ersetzungen:
  - „Du trägst bei At price einen Kurs ein.“ → „Du trägst bei At price deinen Aktivierungspunkt ein.“
  - „Der Wert, bei dem die Order auslösen soll.“ → „Dein Aktivierungspunkt: der Wert, bei dem die Pending Order ausgelöst wird.“
  - „Der Kurs muss erst dorthin laufen – dann löst die Order aus.“ → „Erreicht der Markt deinen Aktivierungspunkt, wird die Order ausgelöst.“
- [ ] **„ausgelöst“ statt „ausgeführt“** – überall (#118, #119). (Begründung des Nutzers: Der Aktivierungspunkt löst aus, die Ausführung ist ein zweiter Schritt; seine Nachricht bricht danach ab.)
- [ ] Im Order-Fenster **„Instrument XY“ statt Crude Oil** (#20).
- [ ] Erklärtexte bleiben deutsch (#17).
- [ ] Doku 2: Plattform-Begriffe wie in den Screenshots: Balance, Equity, Profit/Losses, Margin, Free, Level, Stop out, Swap long, Swap short, Contract size, Leverage, Information, Orders (#147, #151, #153).

### 2.3 Inhalt

- [ ] **Kein Stop Loss** im Dokument – verwirrt Laien. Take-Profit bleibt genau so (#10, #12).
  ⚠ unsicher: Im Fenster-Nachbau war der Stop-Loss-Schalter anfangs ausgeschaltet sichtbar; Claude bot an, ihn zu entfernen (#15). Eine Antwort darauf fehlt.
- [ ] **Keine Zahlen im Dokument** – „generell keine Zahlen“, sie verwirren Laien (#58). Entfernt wurden Preise, Kapitelnummern, „Typ 1–4“, Datum und Seitenzahlen (#59).
  - Ausnahme 1: **Schrittnummern 1–5** (Wegweiser, keine Preise) (#59, #67).
  - Ausnahme 2: **Badge auf dem Deckblatt** „4 Ordertypen. 1 klare Entscheidungslogik.“ – vom Nutzer selbst vorgegeben (#102); Claude hat auf den Konflikt hingewiesen (#103), keine Antwort.
  - Im Fenster stehen statt Werten „deine Menge“, „dein Wert“, „dein Ziel“ (#59); in der Kontoübersicht „Konto jetzt“ statt einer Summe (#151).
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
- [ ] Doku 2: **im Stil des Pending-Orders-Guides**, **nicht** im Stil des vom Nutzer hochgeladenen Dokuments (Reverse-Engineering-Fassung mit Code-Formeln) (#126, #129).

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
| `#53BC51` | Plattform-Grün (Button, „Estimated Profit“-Zahl, Balance-Wert mobil) | #39, #41, #155 |
| `#A8BBBE` | Labels/Bezeichnungen (Order-Fenster, mobile Kontoübersicht, Desktop-Leiste) | #41, #155 |
| `#64747F` | Preis-Badges im Order-Fenster | #41 |
| `rgba(255,255,255,.1)` | Trennlinien im Type-Menü; Trennlinien (0,8 px, 10 % Weiß) in der Kontoübersicht | #47, #155 |
| `#181818` | Desktop-Leiste im **grauen** Design (Screenshot des Nutzers) – wurde **nicht** verwendet | #157 |
| ~~`#1F1F1F`~~, ~~`#7A8384`~~ | **falsch** aus dem Handy-Screenshot gepipettet, durch `#04273C` / `#A8BBBE` ersetzt | #155 |

**Dokument-Farben:**

- Grün für Buy, Rot für Sell, schwarze/dunkelgraue Typografie, dezente graue Linien, viel Weißraum (#102).
- **Grün**: das „gedämpfte“ dunklere Grün aus dem zweiten Bild des Nutzers, mit dem „BUY LIMIT“ gesetzt ist – **eine** Grüntönung im ganzen Dokument (#89). ⚠ Hex-Wert steht nicht im Verlauf. ⚠ Ob `#53BC51` das verworfene „Neongrün“ ist, ist unklar (#83: „Rot und Grün sind unverändert die Originalfarben“, danach #88 „Neongrün weg“).
- **Rot**: dasselbe Rot wie in den Überschriften statt des grellen Pink-Rots der Plattform (#89). ⚠ Hex unbekannt. Claude bot an, das Original-Rot zurückzuholen – keine Antwort.
- Graue Kerzen der Plattformbilder sind für dunklen Grund gemacht → auf Weiß **etwas abgedunkelt** (#83).
- Kurslinie und Hilfselemente neutral grau/dunkelgrau (#102).
- **Doku 2 seit 02.10.2026:** Akzentfarbe Plattform-Blau statt Schwarz für die eigenen Erklärgrafiken, helle Flächen in einer Tönung davon (Nutzerwunsch, Abschnitt 13).

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
- Footer: links „Pending Orders“, rechts „Kurz-Guide“ (Versalien-Stil). **Kein Logo**, weil keins vorhanden (#103).
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

## 5. Dokument 2 – „Schulungseinheit 1: Kontogrundlagen & Kosten“ (7 Seiten)

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

### 5.2 Wo die Werte auf der Plattform stehen (Angaben des Nutzers, #134)

- **Desktop:** Kontowerte in der **untersten Leiste ganz unten rechts**. Die Positionen stehen direkt auf dem ersten Bildschirm. Instrument-Infos (Swap, Hebel …) über das **Info-Zeichen beim Instrument**.
- **Mobile:** **Info-Zeichen oben rechts** → „Information“ erscheint → oben rechts **Balance** → dort steht alles. Im Reiter **Information** stehen Leverage und Stop out (#153).
- Claudes Zusammenfassung (#147): „Desktop unterste Leiste und Info-Zeichen beim Instrument, Mobile Info-Zeichen oben rechts, dann Balance beziehungsweise Information, Positionen unter Orders.“

### 5.3 Seite für Seite (Stand #151/#157)

1. **Deckblatt** – Konto-Anatomie als Bild: Balance + Profit/Losses ergibt Equity; Equity teilt sich in Margin und Free; darunter Level als Verhältnis (#147).
2. **Kontostand** (deckt Themen 1 und 2 ab) – Balance („was fest ist“) gegen Equity („was jetzt gilt“) als zwei Kästen; Grafik mit Position im Plus und im Minus; unten der Weg von schwebend zu fest: öffnen → Kurs bewegt sich → schließen (#147).
3. **Margin** (Themen 3 und 4) – Margin, Free, Level nebeneinander; Balken in drei Zuständen (eine Position, mehrere, Positionen im Minus); Level-Skala „genug Puffer“ → Warnbereich → Stop out. **Stop-out-Wert bewusst nicht genannt**, Verweis auf das Feld unter „Information“, weil er je Konto anders sein kann (#147).
4. **Hebel** (Thema 5) – „ohne“ und „mit“ nebeneinander: gleicher Einsatz, unterschiedlich viel bewegtes Volumen; darunter symmetrisch, wie stark dieselbe Bewegung nach oben und unten wirkt; Vor- und Nachteil als zwei gleichwertige Kästen, keine Gewinnversprechen. Die Grafik „ohne Hebel“ ist **bewusst winzig** (das ist die Aussage) (#147).
5. **Swaps** (Thema 6) – neu nach der **Skizze des Nutzers** (#148, #151):
   - Das Warum: Dir gehört nur die Margin, der Rest ist geliehen, und geliehenes Geld kostet Zinsen.
   - Die Kette: **Geldmarkt-Zins + Broker-Aufschlag = dein Swap**.
   - Der Moment der Buchung: den ganzen Tag nichts, zum **Tageswechsel** alles auf einmal; wer eine Minute vorher schließt, zahlt nichts.
   - Aus der ersten Fassung (#147): Woche mit einem Punkt pro Nacht, **am Mittwoch drei**; Swap long, Swap short und wo der Swap bei der Position auftaucht. ⚠ Ob das nach dem Straffen (#149) noch alles drin ist, ist unklar.
   - Abweichung von der Skizze: **Beträge weggelassen**, stattdessen Wörter (Zahlenverbot). Rechenbeispiel als eigener Kasten auf Wunsch (#151). ⚠ Die Skizze selbst ist nicht im Export.
6. **In der Plattform** – oben die **mobile Kontoübersicht** als Vektor-Nachbau (blaues Design, Maße 3.6) mit fünf Nummern (Equity, Profit/Losses, Margin, Free, Level) und „Konto jetzt“ statt einer Summe; darunter dieselben Werte als **Desktop-Leiste** (blaues Design, teils geschätzt). Unter der Leiste der Hinweis, dass **Level am Desktop fehlt** (#151, #157). ⚠ **Falsch** laut DOM-Messung vom 02.10.2026: Level steht auch am Desktop; Leiste und Hinweis sind korrigiert (Abschnitt 12). Seit 02.10.2026 zeigt die mobile Ansicht auch Kopf- und Reiterleiste mit den Marken A (Info-Zeichen) und B (Reiter Balance) (Abschnitt 12).
7. **Spickzettel** mit allen Begriffen. Er bekam eine eigene Seite, weil die Plattform-Seite sonst überladen war (#151).

Geprüft (#147): null Rasterbilder, alle Schriften eingebettet; die geschützte Fassung liefert null echte Wörter, neun Rechte gesperrt. ⚠ Ob nach den Änderungen in #151–#157 die geschützte Fassung neu erzeugt wurde, steht nicht im Text.

### 5.4 Offene Fragen in Dokument 2

- **Blaues vs. graues Design:** Der Handy-Screenshot zeigte zuerst dunkelgrau, der Konsolenbericht Dunkelblau `#04273C` (#155). Ein weiterer Screenshot des Nutzers bestätigte Blau für Mobile (#156, #157). Die Desktop-Leiste im Screenshot ist **grau `#181818`** (#157) → die Plattform hat offenbar zwei Designs. Claude hat **beides im blauen Design** gebaut, damit es zum Order-Fenster passt. Falls Kunden hauptsächlich Grau sehen: „eine Zeile Änderung“ (#155). Der Nutzer fragte „wollen wir lieber die von Desktop nehmen??? die Leiste“ (#156); Claude nahm beide. ⚠ Keine abschließende Entscheidung des Nutzers.
- ~~**Geschätzte Werte in der Desktop-Leiste**~~ → erledigt: gemessen (02.10.2026, `originals/messungen/kontoleiste-desktop.json`), Leiste neu gebaut (Abschnitt 12).
- ~~**Level fehlt am Desktop**~~ → **falsch**: Die Desktop-Leiste zeigt alle acht Felder (Balance, Equity, Profit/Losses, Margin, Free, Level, Bonus, Credit). Der Hinweis unter der Leiste ist korrigiert.
- **Instrument-Info-Feld** (Swap long, Swap short, Contract size, Leverage) noch nicht gemessen → für echte Fenster auf der Swap- und der Hebel-Seite (#153, #155).
- **Mobile, Reiter Information** (Leverage, Stop out): optional, ein Screenshot existiert schon (#153).
- **Rechenbeispiel-Kasten** zur Swap-Skizze: optional, nur auf Wunsch (#151).
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
3. **Doku 2: Instrument-Info-Feld messen** (Befehl 7.1, Lauf 2) → echtes Fenster auf der Swap- und der Hebel-Seite (#153, #155). Zahlenverbot beachten: Beispielwerte durch Wörter bzw. neutrale Platzhalter ersetzen.
4. Optional: **Mobile, Reiter Information** (Lauf 3).
5. Nach jeder Textänderung: Druck-Prüfungen (6.1) und **Schutz neu aufspielen** (6.3), Pixelvergleich = 0, Extrakt ohne echte Wörter.

### 8.2 Entscheidungen, die beim Nutzer liegen (offen)

- [ ] **Blaues oder graues Design** für die Nachbauten in Doku 2 (und welches die Kunden hauptsächlich sehen) (#155–#157).
- [ ] **Swap-Rechenbeispiel** als eigener Kasten – ja/nein (#151). (Widerspricht dem Zahlenverbot, nur auf ausdrücklichen Wunsch.)
- [ ] **Absender/Logo** für den Footer – gibt es einen Firmennamen oder ein Logo? (#102, #103, #117)
- [ ] **„Ausbruch nach oben/unten“** auf dem Deckblatt und in den Kartenköpfen ersetzen (z. B. „wenn der Kurs nach oben durchbricht“) oder behalten, weil der Begriff später gebraucht wird? (#117) – Achtung: Der Wortlaut stammt aus der Vorgabe des Nutzers (#102).
- [ ] **Lernreihe?** Wurden Market Orders vorher schon erklärt, oder ist Doku 1 der allererste Kontakt? Davon hängt ab, wie viel Seite 2 voraussetzen darf (#117). (Doku 2 heißt „Schulungseinheit 1“ – das spricht für eine Reihe; ⚠ die Reihenfolge der beiden Dokumente ist unklar.)
- [ ] **Badge mit „4“ und „1“** auf dem Deckblatt behalten? (#103)
- [ ] **Rot**: Dokument-Rot (wie Überschriften) behalten oder Original-Rot der Plattform? (#89)
- [ ] **Stop-Loss-Zeile** im Fenster-Nachbau ganz entfernen? (#15)
- [ ] **Historischer Trade** als separates Anhangsblatt „Rechenbeispiel“? (#65)
- [ ] „Ohne Hebel“-Grafik auf der Hebel-Seite größer? (Claude rät ab, #147)

### 8.3 Erledigt bzw. überholt (nicht erneut fragen)

- Chart-Stil A/B/C (#73) → erledigt durch „1:1-Vektor der Plattformbilder, ohne dunklen Hintergrund“ (#80, #82).
- Eigene Seite „So zeigt es deine Plattform“ (#75) → überholt, weil die Plattformbilder jetzt überall die Charts sind (#81).
- Kompletter Guide im dunklen Querformat (#35, #39, #43) → nein, helles A4 (#50, #102).
- Fenster-Variante A/B (#43) → A „Exakt“ (#45).
- Gewinnzone als Fläche/Klammer (#21) → überholt durch die Tönung ab der grünen Kugel (#83).

---

## 9. Fehlende Dateien

Diese Dateien lagen nur in der Sandbox des alten claude.ai-Chats. Der Nutzer sollte sie **aus dem Chat auf claude.ai herunterladen** und ins Repo legen. Vorschlag: Ordner **`originals/`** (Eingangsmaterial vom Nutzer in `originals/inputs/`).

### Bereits im Repo vorhanden (geprüft am 02.10.2026)

- **`originals/pending_orders_DE.pdf`** (112 440 Bytes): geschützte Fassung von Doku 1. 6 Seiten, A4, `CreationDate` 07.09.2026 00:38 UTC, Metadaten-Titel „Pending Orders – Kurz-Guide“, AES-256 (R = 6), Text-Extrakt ist Salat (`MqZdahd I dqfhdz Zdhh …`), keine Rasterbilder.
  ⚠ Das ist **nicht der Endstand**, sondern der Stand von #121/#123: **P = −3392** („extract for accessibility: allowed“) und Header **PDF-1.7**. Der Endstand aus #125 (P = −3904, PDF 2.0) fehlt. Eine ungeschützte Fassung oder `.tex` ist nicht vorhanden. Bauen lässt sich aus dieser Datei nichts.

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
- **Swaps:** Thema 6 verlangt die „Berechnung“, das Dokument ist aber zahlenfrei → Erklärung in Worten, Rechenbeispiel nur optional.
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

**Offen:** Geschützte Fassung nicht neu erzeugt. Kontoübersicht mobil bei 440 px nachmessen (siehe ⚠ oben).

---

## 13. Akzentfarbe Kontogrundlagen

Stand 02.10.2026, Nutzerwunsch: „Kannst du eine andere Akzentfarbe benutzen? Z. B. bei ‚Hebel' sieht man das Weiße nicht, und das Schwarze passt nicht rein.“ Präzisierung: „Alles, was mit Plattform-Elementen zu tun hat, bleibt original.“

**Pixeltreue zum ORIGINAL-PDF ist ab hier bewusst aufgegeben.** `tools/pdf_vergleich.py --dokument kontogrundlagen-kosten` meldet auf allen sieben Seiten Abweichungen (Seiten 1–5 und 7 max. 88, Seite 6 zusätzlich durch die früheren Änderungen) – gewollt.

**Neue Farben** (zentral in `Kontogrundlagen-Kosten.tex`, `ink`/`paper`/`rule` bleiben unverändert definiert):

| Name | Hex | Rolle | Kontrast |
|---|---|---|---|
| `akzent` | `#0E5072` | Plattform-Blau (aktiver Reiter, Kasten hinter Equity). Alle bisher schwarzen Flächen, Linien und Punkte der eigenen Grafiken | Weiß darauf 8,72:1; gegen Weiß 8,72:1 |
| `akzenttint` | `#E8EFF4` | helle Flächen (vorher `paper` `#F7F8F9`) | gegen Weiß 1,16:1 (vorher 1,06:1) |
| `akzentrand` | `#C5D5E0` | Rand der hellen Flächen (vorher `rule` `#E2E5E9`) | gegen Weiß 1,50:1 (vorher 1,26:1) |

Text auf `akzenttint`: ink 15,6:1 · body 8,75:1 · buy 4,62:1 · sell 5,11:1 · **muted 4,02:1** (vorher auf `paper` 4,39:1; Textfarben bleiben laut Vorgabe, ⚠ knapp unter 4,5:1, betrifft nur Kleinschrift-Labels wie „Free“, „eingezahlt und abgeschlossen“, BALANCE/EQUITY in den soft-Kästen). Eine eigene dunklere Navy-Variante für feine Linien war nicht nötig: `akzent` ist auch als 0,5-pt-Linie klar.

**Geändert je Seite**

1. Deckblatt: Akzentlinie unter dem Titel; Kästen Balance und Profit/Losses (Tönung + Rand), Equity-Kasten (weiß, Rand); Margin-Block (`akzent`), Free-Teil (`akzenttint`, vorher weiß) mit Rahmen und Trennlinie in `akzent`; Rand des Badges „Sechs Begriffe“.
2. Kontostand: soft-Kästen Balance/Equity; Balken Balance/Equity (Tönung + Rand, auch der gestrichelte Verlustteil); drei Zeitleisten-Punkte; Merk-Kasten (Fläche + linke Kante).
3. Margin: drei Margin-Balken (`akzent`), Free-Teile (Tönung), Balkenränder; Level-Skala: Warnbereich (Tönung) und Rand.
4. Hebel: zwei Margin-Quadrate (`akzent`), Trade-volume-Quadrat und -Balken (Tönung + Rand); soft-Kästen; Merk-Kasten.
5. Swaps: Margin-Block, „Der Rest ist geliehen“ (Tönung + Rand); Kästen Zins/Aufschlag (Tönung + Rand), „Dein Swap“ (weiß, Rand); Tageslinie „Wann gebucht wird“; Wochenpunkte Mo/Di/Do/Fr; Merk-Kasten.
6. In der Plattform: **nur** die soft-Kästen Desktop/Mobile. Unverändert (Plattform): `mobil.pdf`, `bar.pdf`, Ring/Rahmen, Verbindungslinien und Marken A/B, Nummernkreise 1–5 (`\pfn`, bleibt `ink`). Pixelvergleich bei 150 dpi: Handy-Ausschnitt mit Marken und Liste (y 58–160 mm) und Desktop-Leiste (y 186–200 mm) 0 abweichende Pixel; die Seite weicht nur in y 214,5–253,2 mm ab (soft-Kästen).
7. Spickzettel: Merk-Kasten.

Nicht geändert: Text- und Überschriftenfarben, Buy/Sell und ihre Tints, `greya`-Hilfslinien und Pfeile, Trennlinien (`\kicker`, `\hr`, Fußlinie) in `rule`, Plattform-Nachbauten (`bar.*`, `mobil.*`, `panel.pdf`, `icons.tikz`). Ungenutzte Stile `cnum`/`pfnum`/`prule` unverändert.

**Prüfung:** 7 Seiten, keine Seitenüberläufe (einzige Warnung: Overfull \hbox 1,24 pt in der Spickzettel-Tabelle, schon vorher vorhanden), 10 Schriften eingebettet, keine Rasterbilder. Vergleichsbilder (nicht eingecheckt, `build/` ist ignoriert): `build/Farben-Vergleich.png` (alle Seiten, alt oben/neu unten, 70 dpi), `build/Farben-Hebel.png` (Seite 4 alt|neu, 110 dpi).
