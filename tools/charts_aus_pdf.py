#!/usr/bin/env python3
r"""Rekonstruiert charts.tikz aus den Vektorpfaden des ORIGINAL-PDFs.

Hintergrund
-----------
Die vier Plattform-Chartbilder (bl = Buy Limit, sl = Sell Limit, bs = Buy Stop,
ss = Sell Stop; Original 174 x 96 px) wurden im alten Projekt in Grundformen
zerlegt: je 37 Rechtecke (Balken und Stiele), 2 Kreise (Kugeln) und 1 Dreieck
(Richtung danach). charts.tikz definiert dafür die Makros \chartbl, \chartsl,
\chartbs, \chartss und die Mini-Fassungen \chart..mini.  Die Datei selbst ist
verloren, ihre Wirkung steckt aber unverändert im ORIGINAL-PDF:

* Seite 3: \chartbl, \chartsl   (tikzpicture mit x = y = 0.44660 mm)
* Seite 4: \chartbs, \chartss   (x = y = 0.44660 mm)
* Seite 5: alle vier Mini-Fassungen (x = y = 0.21839 mm)
* Seite 1: alle vier Mini-Fassungen (x = y = 1 mm, scope shift + scale=0.26437)

Jede Form ist im Inhaltsstrom ein eigener Block ``q <Farbe> <Pfad> f Q``:
  TikZ ``\fill (a) rectangle (b);``  ->  m m l l l h m f
  TikZ ``\fill (c) circle (r);``     ->  m m c c c c h m f
  TikZ ``\fill (a) -- (b) -- (c) -- cycle;`` -> m l l h f
Je Chartbild entsteht so eine ununterbrochene Folge von 40 Blöcken.

Rückrechnung
------------
pgf rechnet eine Koordinate v (in Einheiten) so in PDF-Punkte um:
  sp = v * \pgf@xx  (TeX-Festkomma),  bp = 0.99627 * sp  (pgfsys-xetex)
und schreibt das Ergebnis mit TeX' print_scaled.  Das Skript bildet genau diese
Festkomma-Arithmetik nach und sucht zu jeder Zahl im PDF den kürzesten
Dezimalwert (höchstens 3 Nachkommastellen), der *bitgenau* dieselbe Zahl
ergibt.  Dadurch sind die Werte keine Näherung, sondern die Quellwerte.

Die Mini-Fassungen (Seiten 1 und 5) werden mit den großen verglichen.  Sind sie
geometrisch und farblich identisch, werden die Mini-Makros als Verweis auf die
großen geschrieben; sonst erhalten sie eigene Daten.

Aufruf (aus dem Repo-Wurzelverzeichnis):
  python3 tools/charts_aus_pdf.py [ORIGINAL.pdf] [Ziel/charts.tikz]
"""
import sys
from decimal import Decimal
from pathlib import Path

import pikepdf

ROOT = Path(__file__).resolve().parent.parent
QUELLE = ROOT / "originals" / "Pending-Orders-Guide_ORIGINAL.pdf"
ZIEL = ROOT / "dokumente" / "pending-orders" / "charts.tikz"

EINHEIT_GROSS = "0.44660"   # mm, Seiten 3 und 4
EINHEIT_MINI = "0.21839"    # mm, Seite 5
DECKBLATT_SCALE = 0.26437   # Seite 1: scope scale in einer x=y=1mm-Zeichnung
DECKBLATT_SHIFT = {"bs": (19.50, 95.38), "sl": (104.50, 95.38),
                   "bl": (19.50, 10.00), "ss": (104.50, 10.00)}

# Füllfarben im PDF (xdvipdfmx rundet auf 3 Stellen) -> \definecolor-Namen
FARBEN = {
    (0.698, 0.227, 0.18): "pfrot",     # B23A2E
    (0.592, 0.647, 0.706): "pfgrau",   # 97A5B4
    (0.055, 0.478, 0.306): "pfgruen",  # 0E7A4E
}
GRUEN, ROT = "pfgruen", "pfrot"

# ---------------------------------------------------------------------------
# TeX-Festkomma-Arithmetik (tex.web: round_decimals, xn_over_d, print_scaled)
UNITY = 1 << 16


def _round_decimals(ziffern):
    a = 0
    for d in reversed(ziffern[:17]):
        a = (a + d * 2 * UNITY) // 10
    return (a + 1) // 2


def _xn_over_d(x, n, d):
    r = (abs(x) * n) // d
    return -r if x < 0 else r


def tex_mult(dezimal, sp):
    """TeX: <dezimal><dimen>, z. B. 89.525\\pgf@xx"""
    neg = dezimal.startswith("-")
    ganz, _, bruch = dezimal.lstrip("-").partition(".")
    f = _round_decimals([int(c) for c in bruch])
    r = int(ganz or 0) * sp + _xn_over_d(sp, f, UNITY)
    return -r if neg else r


def tex_mm(dezimal):
    """TeX: <dezimal>mm -> sp"""
    ganz, _, bruch = dezimal.partition(".")
    f = _round_decimals([int(c) for c in bruch])
    q, rest = divmod(int(ganz) * 7227, 2540)
    f = (7227 * f + UNITY * rest) // 2540
    return (q + f // UNITY) * UNITY + f % UNITY


def tex_print_scaled(s):
    aus = "-" if s < 0 else ""
    s = abs(s)
    aus += str(s // UNITY)
    s = 10 * (s % UNITY) + 5
    if s != 5:
        aus += "."
        delta = 10
        while True:
            if delta > UNITY:
                s += 0x8000 - 50000
            aus += str(s // UNITY)
            s = 10 * (s % UNITY)
            delta *= 10
            if s <= delta:
                break
    return aus


def pgf_bp(sp):
    """pgfsys-xetex: \\pgf@sys@bp -> Zahl im Inhaltsstrom"""
    return tex_print_scaled(tex_mult("0.99627", sp))


def bp_text(x):
    t = f"{x:.5f}".rstrip("0")
    return t + "0" if t.endswith(".") else t


def zahl(t):
    """Kompakte TeX-Schreibweise: 14.0 -> 14, 89.500 -> 89.5"""
    if "." in t:
        t = t.rstrip("0").rstrip(".")
    return t or "0"


def kandidaten(naeherung):
    for stellen in range(0, 4):
        schritt = 10 ** -stellen
        basis = round(naeherung, stellen)
        for k in sorted(range(-4, 5), key=abs):
            yield f"{basis + k * schritt:.{stellen}f}"


def loese(bp_wert, einheit_sp, offset_sp=0):
    """Kürzester Dezimalwert v mit pgf_bp(offset + v*einheit) == bp_wert."""
    soll = bp_text(bp_wert)
    faktor = float(pgf_bp(1000 * einheit_sp)) / 1000
    naeherung = (bp_wert - float(pgf_bp(offset_sp))) / faktor
    for v in kandidaten(naeherung):
        if pgf_bp(offset_sp + tex_mult(v, einheit_sp)) == soll:
            return v
    raise ValueError(f"keine exakte Quelle für {soll} (≈ {naeherung:.4f})")


# ---------------------------------------------------------------------------
# PDF lesen

def fuellbloecke(seite):
    """Zerlegt den Inhaltsstrom in Läufe aufeinanderfolgender einfacher
    Füllblöcke  q [RG/rg]* (m|l|c|h)+ f [RG/rg]* Q  und liefert Läufe >= 10."""
    ops = [([float(o) if isinstance(o, (int, float, Decimal)) else o for o in a], str(op))
           for a, op in pikepdf.parse_content_stream(seite)]
    laeufe, lauf, i = [], [], 0
    while i < len(ops):
        if ops[i][1] == "q":
            j, farbe, pfad = i + 1, None, []
            while j < len(ops) and ops[j][1] in ("RG", "rg"):
                if ops[j][1] == "rg":
                    farbe = tuple(ops[j][0])
                j += 1
            while j < len(ops) and ops[j][1] in ("m", "l", "c", "h"):
                pfad.append(ops[j])
                j += 1
            if pfad and j < len(ops) and ops[j][1] == "f":
                j += 1
                while j < len(ops) and ops[j][1] in ("RG", "rg"):
                    j += 1
                if j < len(ops) and ops[j][1] == "Q":
                    lauf.append((farbe, pfad))
                    i = j + 1
                    continue
        if lauf:
            laeufe.append(lauf)
            lauf = []
        i += 1
    if lauf:
        laeufe.append(lauf)
    return [l for l in laeufe if len(l) >= 10]


def form(pfad):
    folge = [op for _, op in pfad]
    if folge == ["m", "m", "l", "l", "l", "h", "m"]:
        (x0, y0), (x1, y1) = pfad[0][0], pfad[3][0]
        return "rect", [x0, y0, x1, y1]
    if folge == ["m", "m", "c", "c", "c", "c", "h", "m"]:
        (cx, cy), (rx, _) = pfad[0][0], pfad[1][0]
        return "circle", [cx, cy, rx]          # rx = cx + r
    if folge == ["m", "l", "l", "h"]:
        return "tri", [v for p in pfad[:3] for v in p[0]]
    raise ValueError(f"unbekannte Pfadform {folge}")


def chart_exakt(lauf, einheit_mm):
    """Quellwerte (Strings) eines Chartbilds aus einer 0-basierten Zeichnung."""
    e = tex_mm(einheit_mm)
    formen = []
    for farbe, pfad in lauf:
        art, w = form(pfad)
        if farbe not in FARBEN:
            raise ValueError(f"unbekannte Farbe {farbe}")
        if art == "circle":
            cx, cy = loese(w[0], e), loese(w[1], e)
            r = loese(w[2], e, offset_sp=tex_mult(cx, e))
            werte = [cx, cy, r]
        else:
            werte = [loese(v, e) for v in w]
        formen.append((FARBEN[farbe], art, werte))
    return formen


def chart_naeherung(lauf, einheit_mm, shift_mm=(0.0, 0.0)):
    """Float-Werte in Chart-Einheiten (für den Vergleich der Mini-Fassungen)."""
    bp_mm = 72 / 25.4
    def u(v, achse):
        return (v / bp_mm - shift_mm[achse]) / einheit_mm
    formen = []
    for farbe, pfad in lauf:
        art, w = form(pfad)
        if art == "circle":
            werte = [u(w[0], 0), u(w[1], 1), (w[2] - w[0]) / bp_mm / einheit_mm]
        else:
            werte = [u(v, i % 2) for i, v in enumerate(w)]
        formen.append((FARBEN.get(farbe, str(farbe)), art, werte))
    return formen


def abweichung(a, b):
    if [(f, t, len(w)) for f, t, w in a] != [(f, t, len(w)) for f, t, w in b]:
        return float("inf")
    return max(abs(float(x) - float(y))
               for (_, _, wa), (_, _, wb) in zip(a, b) for x, y in zip(wa, wb))


def pruefe_lesart(name, formen):
    """Lesart der Plattformbilder (HANDOFF 3.4): linke Kugel rot = Kurs jetzt,
    rechte Kugel grün = At price, Dreieck grün nach oben (Buy) / rot nach unten
    (Sell)."""
    kugeln = sorted([(float(w[0]), float(w[1]), f) for f, t, w in formen if t == "circle"])
    (_, y_links, f_links), (_, y_rechts, f_rechts) = kugeln
    dreieck = [(f, [float(v) for v in w]) for f, t, w in formen if t == "tri"][0]
    hoch = dreieck[1][5] > dreieck[1][1]
    assert f_links == ROT and f_rechts == GRUEN, name
    erwartet = {  # (At price über dem Kurs?, Richtung nach oben?, Dreieckfarbe)
        "bl": (False, True, GRUEN), "sl": (True, False, ROT),
        "bs": (True, True, GRUEN), "ss": (False, False, ROT)}[name]
    assert (y_rechts > y_links, hoch, dreieck[0]) == erwartet, name
    n = {t: sum(1 for _, tt, _ in formen if tt == t) for t in ("rect", "circle", "tri")}
    assert n == {"rect": 37, "circle": 2, "tri": 1}, (name, n)


# ---------------------------------------------------------------------------
# Ausgabe

def tikz_zeile(farbe, art, w):
    w = [zahl(v) for v in w]
    if art == "rect":
        return f"\\fill[{farbe}] ({w[0]},{w[1]}) rectangle ({w[2]},{w[3]});"
    if art == "circle":
        return f"\\fill[{farbe}] ({w[0]},{w[1]}) circle ({w[2]});"
    return f"\\fill[{farbe}] ({w[0]},{w[1]}) -- ({w[2]},{w[3]}) -- ({w[4]},{w[5]}) -- cycle;"


def main():
    quelle = Path(sys.argv[1]) if len(sys.argv) > 1 else QUELLE
    ziel = Path(sys.argv[2]) if len(sys.argv) > 2 else ZIEL
    pdf = pikepdf.open(quelle)
    l1, l3, l4, l5 = (fuellbloecke(pdf.pages[i]) for i in (0, 2, 3, 4))
    for nr, l in ((1, l1), (3, l3), (4, l4), (5, l5)):
        assert all(len(x) == 40 for x in l), f"Seite {nr}: Läufe {[len(x) for x in l]}"
    assert (len(l1), len(l3), len(l4), len(l5)) == (4, 2, 2, 4)

    gross = {"bl": chart_exakt(l3[0], EINHEIT_GROSS), "sl": chart_exakt(l3[1], EINHEIT_GROSS),
             "bs": chart_exakt(l4[0], EINHEIT_GROSS), "ss": chart_exakt(l4[1], EINHEIT_GROSS)}
    mini5 = dict(zip(["bl", "sl", "bs", "ss"], (chart_exakt(l, EINHEIT_MINI) for l in l5)))
    mini1 = {n: chart_naeherung(l, DECKBLATT_SCALE, DECKBLATT_SHIFT[n])
             for n, l in zip(["bs", "sl", "bl", "ss"], l1)}

    mini_gleich = {}
    for n in ("bl", "sl", "bs", "ss"):
        pruefe_lesart(n, gross[n])
        d5 = abweichung(gross[n], mini5[n])
        d1 = abweichung(gross[n], mini1[n])
        exakt5 = mini5[n] == gross[n]
        mini_gleich[n] = exakt5 and d1 < 0.02
        print(f"\\chart{n}: 37 Rechtecke, 2 Kreise, 1 Dreieck | Mini S.5 "
              f"{'bitgenau gleich' if exakt5 else f'max. {d5:.4f} E. Abweichung'}, "
              f"Mini S.1 max. {d1:.4f} E. Abweichung")

    zeilen = [
        "% charts.tikz -- Vektor-Nachbau der vier Plattform-Chartbilder",
        "% (img-pending-order-{bl,sl,bs,ss}.png, 174 x 96 px; Ursprung unten links,",
        "% 1 Einheit = 1 px).  Je Bild 37 Rechtecke (Balken und Stiele), 2 Kreise",
        "% (Kugeln: links rot = Kurs jetzt, rechts gruen = At price), 1 Dreieck",
        "% (Richtung danach).  Farben: pfgruen, pfrot, pfgrau (abgedunkelte graue",
        "% Kerzen fuer weissen Grund), definiert in der .tex.",
        "%",
        "% AUTOMATISCH ERZEUGT von tools/charts_aus_pdf.py aus",
        "% originals/Pending-Orders-Guide_ORIGINAL.pdf (Seiten 1, 3, 4, 5).",
        "% Alle Werte sind bitgenau aus dem Inhaltsstrom zurueckgerechnet.",
        "",
    ]
    for n in ("bl", "sl", "bs", "ss"):
        zeilen.append(f"\\newcommand{{\\chart{n}}}{{%")
        zeilen += ["  " + tikz_zeile(*f) for f in gross[n]]
        zeilen.append("}")
    zeilen += ["", "% Mini-Fassungen (Spickzettel S. 5, Deckblatt)."]
    if all(mini_gleich.values()):
        zeilen += [
            "% Im ORIGINAL-PDF sind sie geometrisch und farblich identisch mit den",
            "% grossen Fassungen (nur kleiner skaliert) -> Verweis statt Kopie.",
        ]
    for n in ("bl", "sl", "bs", "ss"):
        if mini_gleich[n]:
            zeilen.append(f"\\newcommand{{\\chart{n}mini}}{{\\chart{n}}}")
        else:
            zeilen.append(f"\\newcommand{{\\chart{n}mini}}{{%")
            zeilen += ["  " + tikz_zeile(*f) for f in mini5[n]]
            zeilen.append("}")
    ziel.write_text("\n".join(zeilen) + "\n", encoding="utf-8")
    print(f"geschrieben: {ziel}")


if __name__ == "__main__":
    main()
