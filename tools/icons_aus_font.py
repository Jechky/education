#!/usr/bin/env python3
"""Glyphen einer Icon-Webfont als TikZ-Pfade ausgeben (z. B. icons.tikz).

Liest eine Schriftdatei (TTF, OTF, WOFF oder WOFF2; WOFF2 braucht das Paket
brotli) und schreibt für jedes gewünschte Zeichen ein Makro, das die Glyphe als
gefüllten TikZ-Pfad zeichnet. Die Koordinaten sind CSS-px in einer Box von
GRÖSSE x ZEILENHÖHE px (Standard 24 x 24), Ursprung unten links, y nach oben –
also genau die Box des <i>-Elements im Browser. Die Glyphe sitzt darin wie im
Browser: Grundlinie = halber Durchschuss + Ascent (Chrome nimmt die
hhea-Metriken bzw. bei gesetztem USE_TYPO_METRICS die OS/2-Typo-Werte).

TrueType-Kurven (quadratisch) werden exakt in kubische Bézier-Kurven umgerechnet
(TikZ kennt nur kubische). Gefüllt wird mit der Nonzero-Regel wie im Browser;
Löcher (z. B. der Punkt im Info-Zeichen) entstehen über die Umlaufrichtung.

Verwendung im Bild (Box-Ursprung = linke untere Ecke des 24-px-Kastens):
  \\begin{scope}[shift={(261\\px,-42\\px)},x=\\px,y=\\px,color=...] \\iconbell \\end{scope}

Aufruf (aus dem Repo-Wurzelverzeichnis):
  python3 tools/icons_aus_font.py FONT.ttf
      -> dokumente/kontogrundlagen-kosten/icons.tikz mit \\iconbell (U+E938),
         \\icongear (U+E937), \\iconorders (U+E90C), \\iconinfo (U+E93A)
  python3 tools/icons_aus_font.py /usr/share/fonts/opentype/inter/Inter-Regular.otf \\
      --zeichen testA=U+0041 testg=g --aus /tmp/test.tikz
      -> Test mit einer beliebigen Schrift; Zeichen als NAME=U+XXXX oder NAME=Zeichen
Optionen: --groesse 24 (font-size px), --zeilenhoehe (line-height px, Standard =
Größe), --stellen 3 (Nachkommastellen), --herkunft "Text" (Kommentar im Kopf).
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

from fontTools.pens.basePen import BasePen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
STANDARD_AUS = ROOT / "dokumente" / "kontogrundlagen-kosten" / "icons.tikz"
STANDARD_ZEICHEN = [  # Makroname, Codepoint, Bedeutung (Klassen der Plattform)
    ("iconbell", 0xE938, "icon-notifications (Glocke)"),
    ("icongear", 0xE937, "icon-settings (Zahnrad)"),
    ("iconorders", 0xE90C, "icon-orders (Liste mit Plus)"),
    ("iconinfo", 0xE93A, "icon-information (Kreis mit i)"),
]


class TikzPen(BasePen):
    """Sammelt Konturen als TikZ-Pfad; transformiert Font-Einheiten -> px (y nach oben)."""

    def __init__(self, glyphset, skala, dy, stellen):
        super().__init__(glyphset)
        self.s, self.dy, self.stellen = skala, dy, stellen
        self.konturen, self.akt = [], None

    def zahl(self, v):
        t = f"{v:.{self.stellen}f}".rstrip("0").rstrip(".")
        return "0" if t in ("-0", "") else t

    def pkt(self, p):
        return f"({self.zahl(p[0] * self.s)},{self.zahl(p[1] * self.s + self.dy)})"

    def _moveTo(self, p):
        self.akt = [self.pkt(p)]

    def _lineTo(self, p):
        self.akt.append("-- " + self.pkt(p))

    def _curveToOne(self, c1, c2, p):
        # BasePen rechnet qCurveTo (TrueType) über _qCurveToOne exakt in kubisch um
        self.akt.append(f".. controls {self.pkt(c1)} and {self.pkt(c2)} .. {self.pkt(p)}")

    def _closePath(self):
        if self.akt:
            self.akt.append("-- cycle")
            self.konturen.append(" ".join(self.akt))
        self.akt = None

    def _endPath(self):  # offene Kontur (in Fonts unüblich) – trotzdem schließen
        self._closePath()


def metriken(font):
    """Ascent/Descent (Font-Einheiten, Descent negativ) wie Chrome sie nimmt."""
    os2, hhea = font.get("OS/2"), font["hhea"]
    if os2 is not None and os2.fsSelection & (1 << 7):  # USE_TYPO_METRICS
        return os2.sTypoAscender, os2.sTypoDescender, "OS/2 typo (USE_TYPO_METRICS)"
    if hhea.ascent or hhea.descent:
        return hhea.ascent, hhea.descent, "hhea"
    return os2.usWinAscent, -os2.usWinDescent, "OS/2 win"


def zeichen_lesen(angaben):
    liste = []
    for a in angaben:
        name, _, z = a.partition("=")
        if not re.fullmatch(r"[A-Za-z]+", name) or not z:
            sys.exit(f"Ungültige Angabe {a!r}: erwartet NAME=U+XXXX oder NAME=Zeichen "
                     "(Makronamen nur aus Buchstaben)")
        m = re.fullmatch(r"(?:U\+|0x)([0-9A-Fa-f]{2,6})", z)
        cp = int(m.group(1), 16) if m else (ord(z) if len(z) == 1 else None)
        if cp is None:
            sys.exit(f"Ungültiges Zeichen in {a!r}")
        liste.append((name, cp, ""))
    return liste


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("font", type=Path, help="TTF/OTF/WOFF/WOFF2")
    ap.add_argument("--zeichen", nargs="+", metavar="NAME=U+XXXX",
                    help="Makroname und Codepoint (Standard: die vier Plattform-Icons)")
    ap.add_argument("--aus", type=Path, default=STANDARD_AUS, help=f"Ziel (Standard: {STANDARD_AUS.relative_to(ROOT)})")
    ap.add_argument("--groesse", type=float, default=24.0, help="font-size in px")
    ap.add_argument("--zeilenhoehe", type=float, help="line-height in px (Standard: = Größe)")
    ap.add_argument("--stellen", type=int, default=3, help="Nachkommastellen")
    ap.add_argument("--herkunft", default="", help="Kommentarzeile zur Herkunft der Schrift")
    a = ap.parse_args()

    zeichen = zeichen_lesen(a.zeichen) if a.zeichen else STANDARD_ZEICHEN
    try:
        font = TTFont(a.font)  # erkennt WOFF/WOFF2 selbst (WOFF2: brotli nötig)
    except ImportError as e:
        sys.exit(f"{e} – für WOFF2: python3 -m pip install brotli")
    cmap, gs = font.getBestCmap(), font.getGlyphSet()
    upm = font["head"].unitsPerEm
    asc, desc, quelle = metriken(font)
    L = a.zeilenhoehe if a.zeilenhoehe is not None else a.groesse
    s = a.groesse / upm
    inhalt = (asc - desc) * s                  # Höhe der Inhaltsfläche in px
    grund_oben = (L - inhalt) / 2 + asc * s    # Grundlinie unter der Boxoberkante
    dy = L - grund_oben                        # Grundlinie über der Boxunterkante

    name_tab = font["name"]
    familie = name_tab.getDebugName(1) or "?"
    version = name_tab.getDebugName(5) or "?"
    sha = hashlib.sha256(a.font.read_bytes()).hexdigest()
    flavor = getattr(font, "flavor", None) or ("CFF" if "CFF " in font else "TrueType")

    kopf = [
        "% Icons als TikZ-Pfade – erzeugt von tools/icons_aus_font.py, nicht von Hand ändern.",
        f"% Schrift: {a.font.name} ({familie}, {version}, {flavor}), sha256 {sha[:16]}…",
    ]
    if a.herkunft:
        kopf.append(f"% Herkunft: {a.herkunft}")
    kopf += [
        f"% unitsPerEm {upm}; Metriken {quelle}: Ascent {asc}, Descent {desc}.",
        f"% Box wie das <i>-Element im Browser: font-size {a.groesse:g}px, line-height {L:g}px",
        f"% -> Box {a.groesse:g} x {L:g} px, Ursprung unten links, y nach oben;",
        f"%    Grundlinie {dy:.3f} px über der Boxunterkante. 1 Einheit = 1 CSS-px.",
        "% Füllregel nonzero (wie im Browser). Farbe kommt von außen (color=…).",
        "% Gebrauch: \\begin{scope}[shift={(<x>,<y>)},x=\\px,y=\\px,color=<Farbe>]\\iconbell\\end{scope}",
        "",
    ]
    makros, fehlend = [], []
    for name, cp, bedeutung in zeichen:
        g = cmap.get(cp)
        if g is None:
            fehlend.append(f"U+{cp:04X} ({name})")
            continue
        pen = TikzPen(gs, s, dy, a.stellen)
        gs[g].draw(pen)
        bp = BoundsPen(gs)
        gs[g].draw(bp)
        box = ("leer" if bp.bounds is None else
               "x {:.2f}–{:.2f}, y {:.2f}–{:.2f} px".format(
                   bp.bounds[0] * s, bp.bounds[2] * s, bp.bounds[1] * s + dy, bp.bounds[3] * s + dy))
        breite = gs[g].width * s
        makros.append(f"% U+{cp:04X} {g}{' – ' + bedeutung if bedeutung else ''}; "
                      f"Vorschub {breite:.3f} px; Umriss {box}; {len(pen.konturen)} Kontur(en)")
        if pen.konturen:
            pfad = "\n    ".join(pen.konturen)
            makros.append(f"\\newcommand\\{name}{{\\fill[nonzero rule]\n    {pfad};}}")
        else:
            makros.append(f"\\newcommand\\{name}{{}}")
        makros.append("")
    if fehlend:
        sys.exit("Nicht in der Schrift: " + ", ".join(fehlend))

    a.aus.parent.mkdir(parents=True, exist_ok=True)
    a.aus.write_text("\n".join(kopf + makros), encoding="utf-8")
    print(f"{len(zeichen)} Glyphen -> {a.aus} (Grundlinie {dy:.3f} px über der Boxunterkante, "
          f"Metriken {quelle})")


if __name__ == "__main__":
    main()
