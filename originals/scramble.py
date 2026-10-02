# -*- coding: utf-8 -*-
"""Ersetzt die ToUnicode-Tabellen aller eingebetteten Schriften durch eine
falsche Zuordnung. Die Seite sieht identisch aus, aber jede Textextraktion
liefert nur noch Buchstabensalat."""
import re, random
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
random.seed(20260907)

def codes_aus(cmap: str):
    """Liest die Zeichencodes aus einer vorhandenen ToUnicode-Tabelle."""
    codes = set()
    for blk in re.findall(r"beginbfchar(.*?)endbfchar", cmap, re.S):
        for c in re.findall(r"<([0-9A-Fa-f]+)>\s*<[0-9A-Fa-f]+>", blk):
            codes.add(int(c, 16))
    for blk in re.findall(r"beginbfrange(.*?)endbfrange", cmap, re.S):
        for a, b in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<[0-9A-Fa-f]+>", blk):
            codes.update(range(int(a,16), int(b,16)+1))
    return sorted(codes)

def neue_cmap(codes):
    kopf = ("/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n"
            "/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n"
            "/CMapName /Adobe-Identity-UCS def\n/CMapType 2 def\n"
            "1 begincodespacerange\n<0000> <FFFF>\nendcodespacerange\n")
    teile = []
    for i in range(0, len(codes), 100):
        gruppe = codes[i:i+100]
        teile.append(f"{len(gruppe)} beginbfchar\n" + "".join(
            f"<{c:04X}> <{ord(random.choice(ALPHABET)):04X}>\n" for c in gruppe) + "endbfchar\n")
    fuss = "endcmap\nCMapName currentdict /CMap defineresource pop\nend\nend"
    return kopf + "".join(teile) + fuss

def verarbeite(quelle, ziel):
    """Geht über ALLE Objekte des Dokuments - auch Schriften, die tief in
    eingebetteten Grafiken stecken."""
    writer = PdfWriter(clone_from=quelle)
    getauscht = 0
    for obj in list(writer._objects):
        try:
            if not hasattr(obj, "get") or "/ToUnicode" not in obj:
                continue
            tu = obj["/ToUnicode"]
            alt_cmap = tu.get_object().get_data().decode("latin-1", "ignore")
            codes = codes_aus(alt_cmap) or list(range(1, 512))
            neu_stream = DecodedStreamObject()
            neu_stream.set_data(neue_cmap(codes).encode("latin-1"))
            obj[NameObject("/ToUnicode")] = writer._add_object(neu_stream)
            getauscht += 1
        except Exception:
            continue
    with open(ziel, "wb") as fh:
        writer.write(fh)
    return getauscht

n = verarbeite("guide2.pdf", "salat.pdf")
print(f"ToUnicode-Tabellen ersetzt: {n}")
