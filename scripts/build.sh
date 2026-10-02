#!/usr/bin/env bash
# Baut die Schulungs-PDFs mit XeLaTeX (zwei Durchläufe), Ausgabe nach build/.
#   scripts/build.sh                 -> alle Dokumente unter dokumente/*/
#   scripts/build.sh pending-orders  -> nur dieses Dokument
# Schriften kommen aus fonts/ (Path=../../fonts/ in der .tex), Grafiken und
# charts.tikz liegen neben der .tex. Das System braucht nur TeX Live (XeLaTeX).
set -euo pipefail

ROOT=$(cd "$(dirname "$0")/.." && pwd)
OUT="$ROOT/build"
mkdir -p "$OUT"

if [ $# -gt 0 ]; then DOCS=("$@"); else
  DOCS=(); for d in "$ROOT"/dokumente/*/; do DOCS+=("$(basename "$d")"); done
fi

for doc in "${DOCS[@]}"; do
  dir="$ROOT/dokumente/$doc"
  [ -d "$dir" ] || { echo "Unbekanntes Dokument: $doc" >&2; exit 1; }
  for tex in "$dir"/*.tex; do
    name=$(basename "$tex" .tex)
    echo "==> $doc/$name.tex"
    for lauf in 1 2; do
      ( cd "$dir" && xelatex -interaction=nonstopmode -halt-on-error \
          -output-directory="$OUT" "$name.tex" > "$OUT/$name.lauf$lauf.out" 2>&1 ) || {
        echo "FEHLER in Lauf $lauf, siehe $OUT/$name.log" >&2
        tail -n 30 "$OUT/$name.lauf$lauf.out" >&2; exit 1; }
    done
    rm -f "$OUT/$name.lauf1.out" "$OUT/$name.lauf2.out"
    seiten=$(pdfinfo "$OUT/$name.pdf" 2>/dev/null | awk '/^Pages:/{print $2}')
    echo "    -> build/$name.pdf (${seiten:-?} Seiten)"
  done
done
