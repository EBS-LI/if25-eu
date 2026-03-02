# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projekt

- **Antrag:** EU Innovation Fund IF25 — Net-Zero Technologies, Small-Scale (2,5-20 Mio. EUR)
- **Deadline: 23. April 2026**
- **Investitionsvolumen:** ~15 Mio. EUR CAPEX, Foerderquote bis 60%
- **Konzept:** 8 Biogasanlagen liefern Rohbiogas ueber ~20 km Sammelleitung an 1 zentralen Aufbereitungsstandort (Membran-Upgrading + 1 Reverion rSOC fuer CO2 Food-Grade)
- **Akronym:** BioMeth-CO2 Bavaria

## Struktur — Wichtige Klarstellungen

- **1 zentraler Aufbereitungsstandort** (nicht 8!) — dort steht Membrananlage + 1 Reverion rSOC
- 8 Betreiber gruenden NEUE **Projektgesellschaft** = alleiniger Antragsteller (1 PIC!)
- Betreiber = Gesellschafter + Rohbiogas-Lieferanten (LoI = Lieferzusage + Beitritt)
- KEIN Konsortium/Konsortialvertrag, sondern Gesellschaftsvertrag
- **1 Reverion rSOC-Einheit** (nicht 8!)
- PIC-Registrierung wird vom **Berater** durchgefuehrt (nicht von PG)
- PG-Geschaeftsfuehrer muss nur LEAR-Schritt + Account Administrator einrichten

## Nutzer / Berater

- Alexander Schwaigkofler, Energieberatung Schwaigkofler GmbH
- Energieberater, betreut Unternehmen bei EU/KfW/BAFA-Foerderantraegen
- Handelt unter Vollmacht fuer seine Kunden
- Kontaktdaten: Poststrasse 2, FL-9491 Ruggell | +49 821 567 316 77 | info@schwaigkofler.org
- **Wichtig:** Im Aussenverhaeltnis gibt es nur den Berater — Claude/KI wird nie erwaehnt

## Technologiepartner

- Reverion GmbH, z.Hd. Fabian Gohlke, Am Mittelfeld 11, 86922 Eresing

## Build-Befehle

### PDF-Generierung aus HTML
```bash
C:/CC/EU/html2pdf.bat <datei.html>              # PDF neben HTML-Datei
C:/CC/EU/html2pdf.bat <datei.html> <ausgabe.pdf> # PDF an Zielort
```
Nutzt Chrome/Edge `--headless --print-to-pdf`. Funktioniert nur mit absoluten Pfaden oder aus dem richtigen Verzeichnis.

## Sprache & Konventionen

- Sprache: Deutsch (alle Dokumente, Code-Kommentare, Commit-Messages)
- Umlaute in Dateinamen/Code als ae/oe/ue (nicht ä/ö/ü)
- Alle Dokumente referenzieren "Innovation Fund" (nicht generisch "EU-Antrag")
- Platzhalter in Dokumenten: `[PLATZHALTER — Beschreibung]`

## Architektur — Zwei Dokument-Typen

### 1. Print-Dokumente (HTML → PDF)
- Liegen in `01_Konsortium/`, `02_Technik/`, `07_Review/`, und im Root
- HTML ist das Quelldokument, PDF wird daraus per `html2pdf.bat` abgeleitet
- Design: A4-Layout (`max-width: 210mm`), Deckblatt mit `.cover`-Klasse, `page-break-before: always` fuer Abschnitte
- Gemeinsame CSS-Variablen: `--primary: #1a3a5c`, `--accent: #2980b9`, `--success: #27ae60`, `--warning: #e67e22`, `--danger: #c0392b`
- Schriftart: `'Segoe UI', 'Calibri', 'Arial', sans-serif`, Basisgroesse `10pt`
- Jede HTML-Datei ist self-contained (kein externes CSS/JS)

### 2. Web-Portal (`web/`)
- `index.html` = Startseite mit Login-Overlay (SHA-256-Hash, `sessionStorage`)
- Unterseiten (`strukturplan.html`, `phasenplan.html`, etc.) haben eigene Sticky-Navbar `.site-nav`
- Login-Hash ist hardcoded als `HASH`-Konstante im `<script>`-Block
- Countdown-Timer berechnet Tage bis Deadline (23.04.2026)
- Phasen-Highlight: automatische Markierung der aktuellen Phase anhand Kalenderwoche
- Unterseiten betten die Print-HTML-Inhalte ein, erweitert um Navigation
- Deployment geplant via Netlify Drop

### 3. Markdown-Vorlagen (`04_Antrag/`, `05_Annexe/`, `06_Unterstuetzende_Dokumente/`)
- Vorlagen/Entwuerfe fuer Antragsteile, die spaeter in HTML/PDF uebergehen
- Enthalten Platzhalter fuer Betreiber-spezifische Daten
- `Datenblatt_Biogasanlage.md` = Formular-Vorlage zum Ausfuellen durch die 8 Betreiber

## Ordnerstruktur

```
01_Konsortium/    — Kooperationsanfragen, LoI-Vorlagen, Letter of Support
02_Technik/       — Technische Vorauslegung (Dimensionierung aller Komponenten)
03_Finanzen/      — FIF-Ausfuellhilfe und Berechnungsmodell
04_Antrag/        — Part B, Machbarkeitsstudie, Business Plan
05_Annexe/        — DNSH, GHG-Methodik, Knowledge Sharing Plan
06_Unterstuetzende_Dokumente/ — Datenblatt-Vorlage + Pflicht-Zulieferungsliste fuer Betreiber
07_Review/        — Phasenplan, Konsistenzcheck, Self-Check-Leitfaden
web/              — Projekt-Portal (passwortgeschuetzt)
```
