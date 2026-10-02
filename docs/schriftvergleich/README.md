# Schriftvergleich (Auswahl, noch keine Änderung an den Dokumenten)

Ausschnitt der Seite „Hebel“ in sechs Varianten, gleiche Größen, Zeilenabstände und Farben wie im Dokument.
Plattform-Nachbauten bleiben in jedem Fall Inter. Schriftdateien liegen **nicht** im Repo.

| | Schrift | Quelle, Lizenz | Installation |
|---|---|---|---|
| A | IBM Plex Sans (jetziger Stand) | Repo `fonts/`, OFL 1.1 | vorhanden |
| B | Inter 4.0 | apt `fonts-inter`, OFL 1.1 | `apt-get install fonts-inter` |
| C | Source Sans 3 (3.052) | github.com/adobe-fonts/source-sans, OFL 1.1 | `curl -L -o ss3.zip https://github.com/adobe-fonts/source-sans/releases/download/3.052R/OTF-source-sans-3.052R.zip` |
| D | Lato 2.015 | apt `fonts-lato`, OFL 1.1 | `apt-get install fonts-lato` |
| E | Fira Sans 4.203 | github.com/google/fonts (`ofl/firasans`), OFL 1.1 | `curl -L -O https://raw.githubusercontent.com/google/fonts/main/ofl/firasans/FiraSans-{Light,Regular,SemiBold,Italic}.ttf` |
| F | Source Serif 4 (4.005, „SmText“) + Source Sans 3 | github.com/adobe-fonts/source-serif, OFL 1.1 | `curl -L -o ss4.zip https://github.com/adobe-fonts/source-serif/releases/download/4.005R/source-serif-4.005_Desktop.zip` |

Heruntergeladene Dateien (OTF/TTF) nach `build/schriftvergleich/fonts/` entpacken.
Bauen: `mkdir -p build/schriftvergleich && cd build/schriftvergleich && xelatex ../../docs/schriftvergleich/schriftvergleich.tex`
Vorschau: `pdftoppm -r 100 -png -singlefile schriftvergleich.pdf schriftvergleich`
