# Übergaben zwischen Agenten

Erreicht ein Agent seine Kontextgrenze (ca. 100K Tokens), hält er hier an
einer sauberen Stelle fest, was ein Nachfolger wissen muss. Ablauf:

1. Datei `docs/uebergaben/<aufgabe>.md` nach der Vorlage unten anlegen
   (`<aufgabe>` kurz, klein, mit Bindestrichen, z. B. `kontogrundlagen-seite-4.md`).
2. Nur die eigenen Dateien per Pfadangabe committen (`git commit -m "…" -- <pfade>`), pushen.
3. Mit der Zeile `ÜBERGABE: docs/uebergaben/<aufgabe>.md` beenden.

Der Nachfolger liest **zuerst** diese Datei (danach bei Bedarf `CLAUDE.md`/`HANDOFF.md`)
und ergänzt sie, statt eine neue anzulegen, falls er selbst wieder übergeben muss.

---

## Vorlage

```markdown
# Übergabe: <Aufgabe>

Stand: <Datum> · Branch: <branch> · letzter Commit: <hash>

## Auftrag (in eigenen Worten)
<Was soll am Ende erreicht sein? 2–4 Sätze.>

## Vorgaben / Rahmen
- <Relevante Nutzervorgaben, Verweise auf HANDOFF.md-Abschnitte>
- <Dateien, die nicht angefasst werden dürfen; parallel arbeitende Agenten>

## Erledigt
- <Was> – `<datei>:<zeile>` – Commit `<hash>`
- …

## Offen
1. <Nächste offene Teilaufgabe>
2. …

## Bekannte Probleme / Risiken
- <Build-Warnungen, unsichere Maße/Farben, offene Rückfragen an den Nutzer>

## Nächster konkreter Schritt
<Genau ein Schritt, mit Datei und Stelle, den der Nachfolger sofort ausführen kann.>

## Prüfkommandos
    scripts/build.sh <dokument>
    git log --oneline -5
    <weitere Kommandos zur Kontrolle des Ergebnisses>
```
