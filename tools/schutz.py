# -*- coding: utf-8 -*-
"""Erzeugt die geschützte Fassung eines Schulungs-PDFs (HANDOFF.md, Abschnitt 6.3) und prüft sie.

    python3 tools/schutz.py build/Dokument.pdf build/Dokument_GESCHUETZT.pdf

1. ToUnicode-Vergiftung über ALLE Objekte (auch Schriften in eingebetteten Grafiken/Form-XObjects):
   Die Seiten sehen gleich aus, jede Textextraktion liefert Buchstabensalat (Logik aus
   originals/scramble.py, dort unverändert abgelegt).
2. AES-256 (R6), leeres Benutzerpasswort (öffnet ohne Passwort), zufälliges Eigentümerpasswort.
   Alle Rechte verboten, auch „extract for accessibility“: P = -3904 (qpdf ignoriert dieses Bit bei
   AES-256, deshalb verschlüsselt pypdf mit direkt gesetztem P).
3. PDF-Version 2.0 (passt zu AES-256).
4. Prüfung: Seitenzahl/-größen gleich, Pixelvergleich aller Seiten = 0, Extrakt ohne echte Wörter,
   P-Wert und Header. Bei einem Fehler endet das Skript mit Code 1.
"""
import random, re, secrets, subprocess, sys, tempfile
from pathlib import Path

from PIL import Image, ImageChops
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
P_WERT = -3904  # alle Rechte verboten (auch Barrierefreiheit); vorher -3392 mit Bit 10
WOERTER = ["Pending", "Order", "Limit", "Stop", "Balance", "Margin", "Equity", "Swap", "Hebel",
           "Kurs", "Plattform", "Position", "Konto", "Sie", "die", "der", "und"]


def codes_aus(cmap):
    codes = set()
    for blk in re.findall(r"beginbfchar(.*?)endbfchar", cmap, re.S):
        for c in re.findall(r"<([0-9A-Fa-f]+)>\s*<[0-9A-Fa-f]+>", blk):
            codes.add(int(c, 16))
    for blk in re.findall(r"beginbfrange(.*?)endbfrange", cmap, re.S):
        for a, b in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<[0-9A-Fa-f]+>", blk):
            codes.update(range(int(a, 16), int(b, 16) + 1))
    return sorted(codes)


def neue_cmap(codes, zufall, bytes_je_code=2):
    """bytes_je_code=2: CID-Schriften (Identity-H); 1: einfache Schriften (Type1/TrueType)."""
    stellen = 2 * bytes_je_code
    bereich = "<00> <FF>" if bytes_je_code == 1 else "<0000> <FFFF>"
    kopf = ("/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n"
            "/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n"
            "/CMapName /Adobe-Identity-UCS def\n/CMapType 2 def\n"
            f"1 begincodespacerange\n{bereich}\nendcodespacerange\n")
    teile = []
    for i in range(0, len(codes), 100):
        gruppe = codes[i:i + 100]
        teile.append(f"{len(gruppe)} beginbfchar\n" + "".join(
            f"<{c:0{stellen}X}> <{ord(zufall.choice(ALPHABET)):04X}>\n" for c in gruppe) + "endbfchar\n")
    fuss = "endcmap\nCMapName currentdict /CMap defineresource pop\nend\nend"
    return kopf + "".join(teile) + fuss


def schuetzen(quelle, ziel):
    zufall = random.Random(20260907)
    writer = PdfWriter(clone_from=quelle)
    getauscht = 0
    for obj in list(writer._objects):
        if not hasattr(obj, "get") or "/ToUnicode" not in obj:
            continue
        alt = obj["/ToUnicode"].get_object().get_data().decode("latin-1", "ignore")
        neu = DecodedStreamObject()
        neu.set_data(neue_cmap(codes_aus(alt) or list(range(1, 512)), zufall).encode("latin-1"))
        obj[NameObject("/ToUnicode")] = writer._add_object(neu)
        getauscht += 1
    # Einfache Schriften ohne ToUnicode (z. B. Helvetica mit WinAnsiEncoding): Text wäre über die
    # Kodierung lesbar -> vergiftete 1-Byte-Tabelle ergänzen (Leseprogramme ziehen ToUnicode vor)
    for obj in list(writer._objects):
        if (hasattr(obj, "get") and obj.get("/Type") == "/Font" and "/ToUnicode" not in obj
                and obj.get("/Subtype") in ("/Type1", "/TrueType", "/MMType1", "/Type3")):
            neu = DecodedStreamObject()
            neu.set_data(neue_cmap(list(range(32, 256)), zufall, 1).encode("latin-1"))
            obj[NameObject("/ToUnicode")] = writer._add_object(neu)
            getauscht += 1
    writer.pdf_header = b"%PDF-2.0"
    writer.encrypt(user_password="", owner_password=secrets.token_hex(16),
                   algorithm="AES-256", permissions_flag=P_WERT)
    with open(ziel, "wb") as fh:
        writer.write(fh)
    return getauscht


def seitenbilder(pdf, ordner, praefix):
    subprocess.run(["pdftoppm", "-r", "100", "-png", str(pdf), str(Path(ordner) / praefix)], check=True)
    return sorted(Path(ordner).glob(praefix + "-*.png"))


def pruefen(original, geschuetzt):
    fehler = []
    a, b = PdfReader(original), PdfReader(geschuetzt)
    if len(a.pages) != len(b.pages):
        fehler.append(f"Seitenzahl {len(a.pages)} != {len(b.pages)}")
    for i, (pa, pb) in enumerate(zip(a.pages, b.pages), 1):
        if [round(float(v), 2) for v in pa.mediabox] != [round(float(v), 2) for v in pb.mediabox]:
            fehler.append(f"Seitengröße S. {i}")
    with tempfile.TemporaryDirectory() as tmp:
        bilder_a, bilder_b = seitenbilder(original, tmp, "a"), seitenbilder(geschuetzt, tmp, "b")
        max_abw = 0
        for fa, fb in zip(bilder_a, bilder_b):
            diff = ImageChops.difference(Image.open(fa).convert("RGB"), Image.open(fb).convert("RGB"))
            max_abw = max(max_abw, max(hi for lo, hi in diff.getextrema()))
    if max_abw:
        fehler.append(f"Pixelabweichung {max_abw}")
    text = subprocess.run(["pdftotext", str(geschuetzt), "-"], capture_output=True, text=True).stdout
    treffer = [w for w in WOERTER if re.search(rf"\b{w}\b", text)]
    if treffer:
        fehler.append("echte Wörter im Extrakt: " + ", ".join(treffer))
    enc = subprocess.run(["qpdf", "--show-encryption", str(geschuetzt)], capture_output=True, text=True).stdout
    if f"P = {P_WERT}" not in enc:
        fehler.append("P-Wert: " + " ".join(enc.split()[:8]))
    if "allowed" in enc.replace("not allowed", ""):
        fehler.append("nicht alle Rechte verboten")
    if "AESv3" not in enc:
        fehler.append("nicht AES-256")
    if open(geschuetzt, "rb").read(8) != b"%PDF-2.0":
        fehler.append("Header nicht %PDF-2.0")
    return max_abw, text, fehler


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    quelle, ziel = sys.argv[1], sys.argv[2]
    n = schuetzen(quelle, ziel)
    max_abw, text, fehler = pruefen(quelle, ziel)
    print(f"ToUnicode-Tabellen ersetzt: {n}")
    print(f"Pixelabweichung (100 dpi, alle Seiten): {max_abw}")
    print("Extrakt-Probe: " + " ".join(text.split()[:8]))
    print("FEHLER: " + "; ".join(fehler) if fehler else "Prüfung bestanden")
    sys.exit(1 if fehler else 0)
