#!/usr/bin/env bash
# Reproduziert die Werkzeugkette fuer die LaTeX-Schulungs-PDFs (idempotent).
#   - XeLaTeX + TikZ/pgf, tcolorbox, fontspec, xcolor, geometry, ragged2e,
#     microtype, hyperref, babel (ngerman)
#   - qpdf, ghostscript, poppler-utils (pdftotext, pdffonts, pdfimages, pdftoppm)
#   - Python: pikepdf, pypdf, fonttools
#   - Schriften: IBM Plex Sans + IBM Plex Mono, Inter
#     (apt: fonts-ibm-plex, fonts-inter; Fallback: offizielle GitHub-Releases
#      nach /usr/local/share/fonts)
# Getestet auf Ubuntu 24.04 (TeX Live 2023). Ausfuehren als root (oder mit sudo).
set -euo pipefail

SUDO=""
if [ "$(id -u)" -ne 0 ]; then SUDO="sudo"; fi
export DEBIAN_FRONTEND=noninteractive

log() { printf '\n==> %s\n' "$*"; }

APT_PKGS=(
  texlive-xetex                # xelatex, fontspec-Basis
  texlive-latex-recommended    # fontspec, microtype, xcolor, hyperref, geometry
  texlive-latex-extra          # tcolorbox, ragged2e
  texlive-pictures             # pgf/TikZ
  texlive-fonts-recommended
  texlive-lang-german          # babel-german (ngerman), Trennmuster
  qpdf ghostscript poppler-utils
  fontconfig curl unzip ca-certificates
  python3-pip
)
FONT_PKGS=(fonts-ibm-plex fonts-inter)

# --- 1. apt-Pakete -----------------------------------------------------------
missing=()
for p in "${APT_PKGS[@]}"; do
  dpkg-query -W -f='${Status}' "$p" 2>/dev/null | grep -q "install ok installed" || missing+=("$p")
done
if [ ${#missing[@]} -gt 0 ]; then
  log "apt: installiere ${missing[*]}"
  $SUDO apt-get update -qq
  $SUDO apt-get install -y -q --no-install-recommends "${missing[@]}"
else
  log "apt: alle TeX-/PDF-Pakete vorhanden"
fi

# Font-Pakete einzeln (duerfen fehlen -> GitHub-Fallback unten)
for p in "${FONT_PKGS[@]}"; do
  if ! dpkg-query -W -f='${Status}' "$p" 2>/dev/null | grep -q "install ok installed"; then
    if apt-cache show "$p" >/dev/null 2>&1; then
      log "apt: installiere $p"
      $SUDO apt-get install -y -q --no-install-recommends "$p" || true
    fi
  fi
done

# --- 2. Schriften (Fallback: offizielle Releases) -----------------------------
FONTDIR=/usr/local/share/fonts
have_font() { fc-list ":postscriptname=$1" file | grep -q .; }
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

need_plex_sans=0; need_plex_mono=0; need_inter=0
for ps in IBMPlexSans-Light IBMPlexSans IBMPlexSans-SmBld IBMPlexSans-Bold; do have_font "$ps" || need_plex_sans=1; done
for ps in IBMPlexMono IBMPlexMono-Bold; do have_font "$ps" || need_plex_mono=1; done
for ps in Inter-Regular Inter-SemiBold Inter-Bold; do have_font "$ps" || need_inter=1; done

PLEX_BASE="https://github.com/IBM/plex/releases/download"
if [ $need_plex_sans = 1 ]; then
  log "Fonts: lade IBM Plex Sans (GitHub-Release)"
  curl -fsSL -o "$TMP/plex-sans.zip" "$PLEX_BASE/%40ibm%2Fplex-sans%401.1.0/ibm-plex-sans.zip"
  unzip -oq "$TMP/plex-sans.zip" -d "$TMP/plex-sans"
  $SUDO mkdir -p "$FONTDIR/ibm-plex"
  $SUDO cp "$TMP"/plex-sans/ibm-plex-sans/fonts/complete/otf/*.otf "$FONTDIR/ibm-plex/"
fi
if [ $need_plex_mono = 1 ]; then
  log "Fonts: lade IBM Plex Mono (GitHub-Release)"
  curl -fsSL -o "$TMP/plex-mono.zip" "$PLEX_BASE/%40ibm%2Fplex-mono%401.1.0/ibm-plex-mono.zip"
  unzip -oq "$TMP/plex-mono.zip" -d "$TMP/plex-mono"
  $SUDO mkdir -p "$FONTDIR/ibm-plex"
  $SUDO cp "$TMP"/plex-mono/ibm-plex-mono/fonts/complete/otf/*.otf "$FONTDIR/ibm-plex/"
fi
if [ $need_inter = 1 ]; then
  log "Fonts: lade Inter 4.1 (GitHub-Release)"
  curl -fsSL -o "$TMP/inter.zip" "https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip"
  unzip -oq "$TMP/inter.zip" -d "$TMP/inter"
  $SUDO mkdir -p "$FONTDIR/inter"
  $SUDO cp "$TMP"/inter/extras/otf/Inter-*.otf "$FONTDIR/inter/"
fi
log "fc-cache"
$SUDO fc-cache -f >/dev/null

# --- 3. Python-Pakete ----------------------------------------------------------
if python3 -c "import pikepdf, pypdf, fontTools" 2>/dev/null; then
  log "pip: pikepdf/pypdf/fonttools vorhanden"
else
  log "pip: installiere pikepdf pypdf fonttools"
  python3 -m pip install -q pikepdf pypdf fonttools 2>/dev/null \
    || python3 -m pip install -q --break-system-packages pikepdf pypdf fonttools
fi

# --- 4. Pruefung ---------------------------------------------------------------
log "Pruefung"
fail=0
for t in xelatex qpdf gs pdftotext pdffonts pdfimages pdftoppm fc-list; do
  command -v "$t" >/dev/null || { echo "FEHLT: $t"; fail=1; }
done
for s in fontspec.sty tikz.sty tcolorbox.sty xcolor.sty geometry.sty ragged2e.sty microtype.sty hyperref.sty babel.sty ngerman.ldf; do
  kpsewhich "$s" >/dev/null || { echo "FEHLT (TeX): $s"; fail=1; }
done
for ps in IBMPlexSans-Light IBMPlexSans IBMPlexSans-SmBld IBMPlexSans-Bold IBMPlexMono IBMPlexMono-Bold Inter-Regular Inter-SemiBold Inter-Bold; do
  have_font "$ps" || { echo "FEHLT (Font): $ps"; fail=1; }
done
python3 -c "import pikepdf, pypdf, fontTools" || fail=1
if [ $fail = 0 ]; then
  echo "OK: $(xelatex --version | head -1); qpdf $(qpdf --version | head -1 | awk '{print $3}'); gs $(gs --version)"
else
  echo "Setup unvollstaendig." >&2; exit 1
fi
