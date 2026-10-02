# Übergaben zwischen Agenten

Ein Agent übergibt bei ca. 60–80K Tokens Arbeitskontext oder wenn seine Teilaufgabe erledigt ist
(Regeln: `CLAUDE.md`, Regel 2 und 3). Ablauf:

1. Datei `docs/uebergaben/<aufgabe>.md` nach der Vorlage anlegen
   (`<aufgabe>` kurz, klein, mit Bindestrichen, z. B. `kontogrundlagen-seite-4`).
2. Nur eigene Dateien explizit stagen, committen, `git pull --rebase`, pushen.
3. Mit der Zeile `ÜBERGABE: docs/uebergaben/<aufgabe>.md` beenden.

Der Nachfolger liest zuerst `CLAUDE.md`, dann die Übergabe, dann `git log -5`.
Muss er selbst übergeben, ergänzt er die Datei, statt eine neue anzulegen.
Die Datei hat **höchstens ca. 40 Zeilen** – nur das, was nicht schon in `CLAUDE.md`
oder `HANDOFF.md` steht.

---

## Vorlage

```markdown
# Übergabe: <Aufgabe>
Stand: <Datum> · Branch: <branch> · letzter Commit: <hash>

## Ziel
<Was soll am Ende erreicht sein? 1–3 Sätze, prüfbar.>

## Vorgaben
<Nur Abweichendes/Aufgabenspezifisches; sonst nichts wiederholen.
Z. B. HANDOFF.md-Abschnitte, Dateien, die nicht angefasst werden dürfen.>

## Erledigt
- <Was> – `<datei>` – Commit `<hash>`

## Offen
1. <Offene Teilaufgabe, ggf. mit bekanntem Problem>
2. …

## Nächster Schritt
<Genau ein Schritt mit Datei und Stelle, sofort ausführbar.>

## Prüfkommandos
    scripts/build.sh <dokument>
    git log --oneline -5
```
