#!/usr/bin/env python3
"""Holt die eingebetteten Plattform-Grafiken aus einem ORIGINAL-PDF zurück.

XeTeX/xdvipdfmx legt jede per \\includegraphics eingebundene PDF-Seite als
Form-XObject ab. Dieses Skript sucht auf der angegebenen Seite die Formen über
ihre gesetzte Breite und schreibt sie als eigenständige einseitige PDFs:

  MediaBox  = BBox der Form
  Contents  = Inhaltsstrom der Form (unverändert)
  Resources = Ressourcen der Form inkl. Schriften und verschachtelter Formen

\\includegraphics[width=<Breite>]{<Datei>} ergibt damit wieder exakt dasselbe Bild.

Bekannte Dokumente (Seite, Dateiname -> gesetzte Breite):
  pending-orders          Seite 6: fenster-bl.pdf 80 mm, type-menu.pdf 46 mm
  kontogrundlagen-kosten  Seite 6: panel.pdf 78 mm
  (bar.pdf wird nicht mehr extrahiert, sondern aus bar.tex gebaut – nach DOM-Messung)

Aufruf (aus dem Repo-Wurzelverzeichnis):
  python3 tools/grafiken_aus_pdf.py [DOKUMENT] [--quelle ORIGINAL.pdf] [--ziel ORDNER]
DOKUMENT ist standardmäßig pending-orders; Quelle und Ziel ergeben sich daraus.
"""
import argparse
from pathlib import Path

import pikepdf

ROOT = Path(__file__).resolve().parent.parent
MM = 72 / 25.4
# Dokument -> (ORIGINAL-PDF in originals/, Seite (1-basiert), {Datei: Breite in mm})
DOKUMENTE = {
    "pending-orders": ("Pending-Orders-Guide_ORIGINAL.pdf", 6,
                       {"fenster-bl.pdf": 80.0, "type-menu.pdf": 46.0}),
    "kontogrundlagen-kosten": ("Kontogrundlagen-Kosten_ORIGINAL.pdf", 6,
                               {"panel.pdf": 78.0}),
}


def formen_mit_breite(seite):
    """Liefert {Name: gesetzte Breite in bp} aller Form-XObjects einer Seite."""
    xobjs = seite.Resources.XObject
    stapel, ctm, breiten = [], [1, 0, 0, 1, 0, 0], {}

    def mul(m, n):  # m * n (PDF-Konvention: neue cm links multiplizieren)
        a, b, c, d, e, f = m
        A, B, C, D, E, F = n
        return [a * A + b * C, a * B + b * D, c * A + d * C, c * B + d * D,
                e * A + f * C + E, e * B + f * D + F]

    for operanden, op in pikepdf.parse_content_stream(seite):
        op = str(op)
        if op == "q":
            stapel.append(ctm)
        elif op == "Q":
            ctm = stapel.pop()
        elif op == "cm":
            ctm = mul([float(x) for x in operanden], ctm)
        elif op == "Do":
            name = str(operanden[0])
            form = xobjs[name]
            bbox = [float(x) for x in form.BBox]
            breiten[name] = ctm[0] * (bbox[2] - bbox[0])
    return breiten


def form_als_pdf(quelle_pdf, form, ziel):
    neu = pikepdf.new()
    ressourcen = form.Resources
    if not ressourcen.is_indirect:  # copy_foreign braucht ein indirektes Objekt
        ressourcen = quelle_pdf.make_indirect(ressourcen)
    bbox = [float(x) for x in form.BBox]
    matrix = [float(x) for x in form.get("/Matrix", [1, 0, 0, 1, 0, 0])]
    if matrix != [1, 0, 0, 1, 0, 0]:
        raise SystemExit(f"{ziel.name}: Form-Matrix {matrix} nicht unterstützt")
    seite = pikepdf.Dictionary(
        Type=pikepdf.Name.Page,
        MediaBox=pikepdf.Array(bbox),
        Resources=neu.copy_foreign(ressourcen),
        Contents=neu.make_stream(form.read_bytes()),
    )
    neu.pages.append(pikepdf.Page(seite))
    neu.save(ziel, deterministic_id=True)
    return bbox


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dokument", nargs="?", default="pending-orders", choices=DOKUMENTE)
    ap.add_argument("--quelle", type=Path, help="ORIGINAL-PDF (Standard: originals/…)")
    ap.add_argument("--ziel", type=Path, help="Zielordner (Standard: dokumente/<DOKUMENT>)")
    a = ap.parse_args()

    pdf_name, seitennr, grafiken = DOKUMENTE[a.dokument]
    quelle = a.quelle or ROOT / "originals" / pdf_name
    ziel = a.ziel or ROOT / "dokumente" / a.dokument
    pdf = pikepdf.open(quelle)
    seite = pdf.pages[seitennr - 1]
    breiten = formen_mit_breite(seite)
    for datei, mm in grafiken.items():
        treffer = [n for n, b in breiten.items() if abs(b - mm * MM) < 0.5]
        if len(treffer) != 1:
            raise SystemExit(f"{datei}: keine eindeutige Form mit {mm} mm Breite ({breiten})")
        bbox = form_als_pdf(pdf, seite.Resources.XObject[treffer[0]], ziel / datei)
        print(f"{datei}: {treffer[0]} -> MediaBox {bbox}, "
              f"gesetzt {breiten[treffer[0]] / MM:.3f} mm breit")


if __name__ == "__main__":
    main()
