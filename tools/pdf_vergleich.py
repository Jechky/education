#!/usr/bin/env python3
"""Seitenweiser Pixelvergleich zweier PDFs (Standard: Neubau gegen ORIGINAL).

Rendert beide PDFs mit pdftoppm (Standard 150 dpi) und meldet je Seite den
Anteil abweichender Pixel und die maximale Farbabweichung (0-255). Zusätzlich
werden die Inhaltsströme der Seiten verglichen (identisch / verschieden).
Exit-Code 1, wenn eine Seite die Schwelle überschreitet oder die Seitenzahl
abweicht. Mit --diff-dir werden Differenzbilder abweichender Seiten abgelegt.

Aufruf (aus dem Repo-Wurzelverzeichnis):
  python3 tools/pdf_vergleich.py [NEU.pdf] [REFERENZ.pdf] [--dpi 150]
                                 [--schwelle 0.1] [--diff-dir DIR]
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import pikepdf
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent


def rendern(pdf, dpi, ordner, praefix):
    subprocess.run(["pdftoppm", "-r", str(dpi), "-png", str(pdf), str(ordner / praefix)],
                   check=True)
    return sorted(ordner.glob(f"{praefix}-*.png"))


def inhalt(pdf):
    with pikepdf.open(pdf) as p:
        return [b"".join(c.read_bytes() for c in (s.Contents if isinstance(s.Contents, pikepdf.Array)
                                                   else [s.Contents])) for s in p.pages]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("neu", nargs="?", default=ROOT / "build" / "Pending-Orders-Guide.pdf")
    ap.add_argument("referenz", nargs="?",
                    default=ROOT / "originals" / "Pending-Orders-Guide_ORIGINAL.pdf")
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--schwelle", type=float, default=0.1, help="max. %% abweichender Pixel")
    ap.add_argument("--diff-dir", type=Path)
    a = ap.parse_args()

    ok = True
    strom_neu, strom_ref = inhalt(a.neu), inhalt(a.referenz)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        bn, br = rendern(a.neu, a.dpi, tmp, "neu"), rendern(a.referenz, a.dpi, tmp, "ref")
        if len(bn) != len(br):
            print(f"Seitenzahl verschieden: neu {len(bn)}, Referenz {len(br)}")
            ok = False
        print(f"{'Seite':>5}  {'abweichend':>10}  {'max':>4}  Inhaltsstrom")
        for i, (pn, pr) in enumerate(zip(bn, br), 1):
            x = np.asarray(Image.open(pn).convert("RGB"), dtype=np.int16)
            y = np.asarray(Image.open(pr).convert("RGB"), dtype=np.int16)
            if x.shape != y.shape:
                print(f"{i:>5}  Bildgröße verschieden {x.shape} / {y.shape}")
                ok = False
                continue
            d = np.abs(x - y).max(axis=2)
            anteil = 100.0 * np.count_nonzero(d) / d.size
            strom = "identisch" if strom_neu[i - 1] == strom_ref[i - 1] else "verschieden"
            print(f"{i:>5}  {anteil:>9.4f}%  {int(d.max()):>4}  {strom}")
            if anteil >= a.schwelle:
                ok = False
            if a.diff_dir and d.max() > 0:
                a.diff_dir.mkdir(parents=True, exist_ok=True)
                Image.fromarray(np.where(d > 0, 0, 255).astype(np.uint8)).save(
                    a.diff_dir / f"diff-{i}.png")
    print("OK" if ok else "ABWEICHUNG")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
