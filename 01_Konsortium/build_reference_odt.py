# -*- coding: utf-8 -*-
"""
Baut eine angepasste reference.odt fuer Pandoc-ODT-Export.
Setzt A4-Format, Segoe UI, Projekt-Farben, Fusszeile mit Kontakt + Seitenzahl.
"""
import zipfile, os, shutil, tempfile
import xml.etree.ElementTree as ET

# --- Pfade ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_ODT = os.path.join(SCRIPT_DIR, "reference.odt")
OUT_ODT = os.path.join(SCRIPT_DIR, "reference_biometh.odt")

# --- Namespaces ---
NS = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "style":  "urn:oasis:names:tc:opendocument:xmlns:style:1.0",
    "text":   "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "fo":     "urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
    "svg":    "urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0",
    "loext":  "urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0",
}
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

# Alle weiteren Namespaces aus dem Original registrieren
EXTRA_NS = {
    "table":     "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    "draw":      "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
    "xlink":     "http://www.w3.org/1999/xlink",
    "dc":        "http://purl.org/dc/elements/1.1/",
    "meta":      "urn:oasis:names:tc:opendocument:xmlns:meta:1.0",
    "number":    "urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0",
    "chart":     "urn:oasis:names:tc:opendocument:xmlns:chart:1.0",
    "dr3d":      "urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0",
    "math":      "http://www.w3.org/1998/Math/MathML",
    "form":      "urn:oasis:names:tc:opendocument:xmlns:form:1.0",
    "script":    "urn:oasis:names:tc:opendocument:xmlns:script:1.0",
    "ooo":       "http://openoffice.org/2004/office",
    "ooow":      "http://openoffice.org/2004/writer",
    "oooc":      "http://openoffice.org/2004/calc",
    "dom":       "http://www.w3.org/2001/xml-events",
    "rpt":       "http://openoffice.org/2005/report",
    "of":        "urn:oasis:names:tc:opendocument:xmlns:of:1.2",
    "xhtml":     "http://www.w3.org/1999/xhtml",
    "grddl":     "http://www.w3.org/2003/g/data-view#",
    "officeooo": "http://openoffice.org/2009/office",
    "tableooo":  "http://openoffice.org/2009/table",
    "drawooo":   "http://openoffice.org/2010/draw",
    "calcext":   "urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0",
    "css3t":     "http://www.w3.org/TR/css3-text/",
}
for prefix, uri in EXTRA_NS.items():
    ET.register_namespace(prefix, uri)


def qn(ns_prefix, local):
    """Qualified name helper."""
    return f"{{{NS[ns_prefix]}}}{local}"


def modify_styles(styles_xml_path):
    tree = ET.parse(styles_xml_path)
    root = tree.getroot()

    # ==========================================
    # 1. Font-Deklarationen: Segoe UI hinzufuegen
    # ==========================================
    font_decls = root.find(f".//{qn('office','font-face-decls')}")
    if font_decls is None:
        font_decls = ET.SubElement(root, qn("office", "font-face-decls"))

    # Pruefen ob Segoe UI schon da
    has_segoe = False
    for ff in font_decls.findall(qn("style", "font-face")):
        if ff.get(qn("style", "name")) == "Segoe UI":
            has_segoe = True
            break
    if not has_segoe:
        segoe = ET.SubElement(font_decls, qn("style", "font-face"))
        segoe.set(qn("style", "name"), "Segoe UI")
        segoe.set(qn("svg", "font-family"), "'Segoe UI'")

    # ==========================================
    # 2. Alle Text-Styles auf Segoe UI umstellen
    # ==========================================
    for elem in root.iter():
        tag = elem.tag
        # text-properties
        if tag == qn("style", "text-properties"):
            if elem.get(qn("style", "font-name")):
                elem.set(qn("style", "font-name"), "Segoe UI")
            if elem.get(qn("fo", "font-family")):
                elem.set(qn("fo", "font-family"), "'Segoe UI'")

    # ==========================================
    # 3. Page-Layout: A4, Raender 20mm
    # ==========================================
    for pl in root.iter(qn("style", "page-layout")):
        for plp in pl.findall(qn("style", "page-layout-properties")):
            plp.set(qn("fo", "page-width"), "210mm")
            plp.set(qn("fo", "page-height"), "297mm")
            plp.set(qn("fo", "margin-top"), "20mm")
            plp.set(qn("fo", "margin-bottom"), "20mm")
            plp.set(qn("fo", "margin-left"), "25mm")
            plp.set(qn("fo", "margin-right"), "20mm")

        # Footer-Style: Mindesthoehe setzen
        fs = pl.find(qn("style", "footer-style"))
        if fs is not None:
            # Bestehende Properties entfernen und neu setzen
            for child in list(fs):
                fs.remove(child)
            fsp = ET.SubElement(fs, qn("style", "header-footer-properties"))
            fsp.set(qn("fo", "min-height"), "8mm")
            fsp.set(qn("fo", "margin-top"), "4mm")
            fsp.set(qn("fo", "border-top"), "0.5pt solid #1a3a5c")
            fsp.set(qn("fo", "padding-top"), "2mm")

    # ==========================================
    # 4. Master-Page: Footer mit Kontakt + Seitenzahl
    # ==========================================
    for mp in root.iter(qn("style", "master-page")):
        if mp.get(qn("style", "name")) == "Standard":
            # Bestehenden Footer entfernen
            for old_footer in mp.findall(qn("style", "footer")):
                mp.remove(old_footer)

            # Neuen Footer bauen — eine Zeile: Firma | Adresse | Mail ... Tab ... Seite X
            footer = ET.SubElement(mp, qn("style", "footer"))

            p1 = ET.SubElement(footer, qn("text", "p"))
            p1.set(qn("text", "style-name"), "Footer")

            # Links: Firma fett
            span_firma = ET.SubElement(p1, qn("text", "span"))
            span_firma.set(qn("text", "style-name"), "FooterBold")
            span_firma.text = "Energieberatung Schwaigkofler GmbH"
            span_firma.tail = "  |  Poststrasse 2, FL-9491 Ruggell  |  info@schwaigkofler.org"

            # Tab rechts
            tab = ET.SubElement(p1, qn("text", "tab"))
            tab.tail = "Seite "

            # Seitenzahl
            page_num = ET.SubElement(p1, qn("text", "page-number"))
            page_num.set(qn("text", "select-page"), "current")
            page_num.text = "1"

    # ==========================================
    # 5. Footer-Textstyles anlegen
    # ==========================================
    auto_styles = root.find(qn("office", "automatic-styles"))
    if auto_styles is None:
        auto_styles = root.find(f".//{qn('office','styles')}")

    # "Footer" paragraph style — linksbuendig mit Tab rechts bei 165mm
    footer_para = ET.SubElement(auto_styles, qn("style", "style"))
    footer_para.set(qn("style", "name"), "Footer")
    footer_para.set(qn("style", "family"), "paragraph")
    fpp = ET.SubElement(footer_para, qn("style", "paragraph-properties"))
    fpp.set(qn("fo", "text-align"), "start")
    # Tab-Stopp rechts
    tab_stops = ET.SubElement(fpp, qn("style", "tab-stops"))
    tab_stop = ET.SubElement(tab_stops, qn("style", "tab-stop"))
    tab_stop.set(qn("style", "position"), "165mm")
    tab_stop.set(qn("style", "type"), "right")
    ftp = ET.SubElement(footer_para, qn("style", "text-properties"))
    ftp.set(qn("fo", "font-size"), "7.5pt")
    ftp.set(qn("fo", "color"), "#5d6d7e")
    ftp.set(qn("style", "font-name"), "Segoe UI")

    # "FooterBold" text style
    footer_bold = ET.SubElement(auto_styles, qn("style", "style"))
    footer_bold.set(qn("style", "name"), "FooterBold")
    footer_bold.set(qn("style", "family"), "text")
    fbtp = ET.SubElement(footer_bold, qn("style", "text-properties"))
    fbtp.set(qn("fo", "font-weight"), "bold")
    fbtp.set(qn("fo", "font-size"), "7.5pt")
    fbtp.set(qn("fo", "color"), "#1a3a5c")
    fbtp.set(qn("style", "font-name"), "Segoe UI")

    # ==========================================
    # 6. Heading-Styles: Farbe #1a3a5c
    # ==========================================
    for style_el in root.iter(qn("style", "style")):
        name = style_el.get(qn("style", "name"), "")
        if name.startswith("Heading"):
            tp = style_el.find(qn("style", "text-properties"))
            if tp is not None:
                tp.set(qn("fo", "color"), "#1a3a5c")
                tp.set(qn("style", "font-name"), "Segoe UI")
            else:
                tp = ET.SubElement(style_el, qn("style", "text-properties"))
                tp.set(qn("fo", "color"), "#1a3a5c")
                tp.set(qn("style", "font-name"), "Segoe UI")

    # ==========================================
    # 7. Default-Text-Properties: Segoe UI 11pt, Blocksatz
    # ==========================================
    for dp in root.iter(qn("style", "default-style")):
        fam = dp.get(qn("style", "family"), "")
        if fam == "paragraph":
            tp = dp.find(qn("style", "text-properties"))
            if tp is not None:
                tp.set(qn("style", "font-name"), "Segoe UI")
                tp.set(qn("fo", "font-size"), "11pt")
                tp.set(qn("fo", "color"), "#2c3e50")
            pp = dp.find(qn("style", "paragraph-properties"))
            if pp is not None:
                pp.set(qn("fo", "text-align"), "justify")
            else:
                pp = ET.SubElement(dp, qn("style", "paragraph-properties"))
                pp.set(qn("fo", "text-align"), "justify")

    tree.write(styles_xml_path, xml_declaration=True, encoding="utf-8")


def build_reference_odt():
    """Entpackt, modifiziert, repackt die reference.odt."""
    tmpdir = tempfile.mkdtemp(prefix="odt_ref_")

    try:
        # Entpacken
        with zipfile.ZipFile(SRC_ODT, "r") as z:
            z.extractall(tmpdir)

        # styles.xml modifizieren
        styles_path = os.path.join(tmpdir, "styles.xml")
        modify_styles(styles_path)

        # Neu verpacken (mimetype muss ERSTE Datei sein, unkomprimiert)
        if os.path.exists(OUT_ODT):
            os.remove(OUT_ODT)

        with zipfile.ZipFile(OUT_ODT, "w") as zout:
            # mimetype zuerst, stored (nicht komprimiert)
            mimetype_path = os.path.join(tmpdir, "mimetype")
            zout.write(mimetype_path, "mimetype", compress_type=zipfile.ZIP_STORED)

            # Alle anderen Dateien
            for dirpath, dirnames, filenames in os.walk(tmpdir):
                for fn in filenames:
                    if fn == "mimetype":
                        continue
                    full = os.path.join(dirpath, fn)
                    arcname = os.path.relpath(full, tmpdir)
                    zout.write(full, arcname, compress_type=zipfile.ZIP_DEFLATED)

        print(f"Reference-ODT erstellt: {OUT_ODT}")

    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    build_reference_odt()
