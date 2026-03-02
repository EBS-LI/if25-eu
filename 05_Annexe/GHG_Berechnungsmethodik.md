# GHG Emission Avoidance — Berechnungsmethodik und Plausibilitaetspruefung

**EU Innovation Fund IF25 NZT — Small-Scale**
**Projekt: Biomethan-Konsortium Bayern**

---

## 1. Ueberblick

Der GHG Emission Avoidance Calculator ist eine offizielle Excel-Vorlage von CINEA.
Er muss heruntergeladen und mit projektspezifischen Daten befuellt werden.

**Download:** https://cinea.ec.europa.eu/programmes/innovation-fund_en
(unter "Call documents" → "GHG Emission Avoidance Calculator")

Die GHG-Vermeidung wird nach drei Sub-Kriterien bewertet:
- **Absolute GHG avoidance** (max. 2 Punkte)
- **Relative GHG avoidance** (max. 5 Punkte)
- **Quality of GHG calculation** (max. 5 Punkte)
- **Gesamt: max. 12 Punkte**

---

## 2. Vermeidungspfade

Das Projekt hat zwei primaere GHG-Vermeidungspfade:

### Pfad 1: Biomethan ersetzt fossiles Erdgas

| Parameter | Wert | Einheit | Quelle/Annahme |
|---|---|---|---|
| Biomethan-Produktion (8 Anlagen) | [PLATZHALTER] | Nm3/a | Anlagendaten |
| Energiegehalt Biomethan | 10,0 | kWh/Nm3 | Standard |
| Jaehrliche Energieproduktion | [BERECHNUNG] | MWh/a | |
| Emissionsfaktor fossiles Erdgas | 0,202 | t CO2-eq/MWh | UBA 2024 / IPCC |
| Emissionsfaktor Biomethan (LCA) | 0,025-0,040 | t CO2-eq/MWh | RED III / Well-to-Wheel |
| **Netto-Vermeidung pro MWh** | **ca. 0,165** | **t CO2-eq/MWh** | |

**Beispielrechnung (mit Platzhalter-Anlagendaten):**
```
Annahme: 8 Anlagen x durchschnittlich 500 Nm3/h Biogas x 55% Methan
= 8 x 500 x 0,55 = 2.200 Nm3/h Biomethan
= 2.200 x 8.000 h/a = 17.600.000 Nm3/a Biomethan
= 17.600.000 x 10 kWh/Nm3 = 176.000 MWh/a

CO2-Vermeidung Pfad 1 = 176.000 MWh/a x 0,165 t/MWh = 29.040 t CO2-eq/a
```

### Pfad 2: Biogenes CO2 (Food-Grade) ersetzt fossiles CO2

| Parameter | Wert | Einheit | Quelle/Annahme |
|---|---|---|---|
| CO2-Gehalt im Biogas | ca. 45% | Vol.-% | Standard |
| CO2-Produktion (roh) | [BERECHNUNG] | Nm3/a | |
| Davon nutzbar (Reverion-Abscheidung) | [BERECHNUNG] | t/a | |
| Davon als Food-Grade verkauft | [BERECHNUNG] | t/a | Marktabschaetzung |
| Emissionsfaktor fossile CO2-Produktion | 0,75 | t CO2-eq/t CO2 | Industriedaten |
| Emissionsfaktor biogene CO2-Abscheidung | ca. 0,05-0,10 | t CO2-eq/t CO2 | Energiebedarf Reverion |
| **Netto-Vermeidung pro Tonne CO2** | **ca. 0,65** | **t CO2-eq/t CO2** | |

**Erlaeuterung fossile CO2-Produktion:**
- Industrielles CO2 wird ueberwiegend aus der Ammoniakproduktion oder Ethanol-Fermentation gewonnen
- Transport und Reinigung verursachen zusaetzliche Emissionen
- Europaeischer Markt hat seit 2022 wiederholt CO2-Engpaesse erlebt
- Substitution durch biogenes CO2 ist daher nicht nur klimarelevant, sondern auch versorgungssicherheitsrelevant

**Beispielrechnung:**
```
Annahme: 8 Anlagen x 500 Nm3/h Biogas x 45% CO2 = 1.800 Nm3/h CO2
CO2-Dichte bei Normalbedingungen: 1,977 kg/Nm3
= 1.800 x 1,977 = 3.559 kg/h = 3,56 t/h
= 3,56 x 8.000 h/a = 28.475 t/a CO2 (theoretisch)

Reverion-Abscheidegrad: ca. 90% → 25.628 t/a
Davon Food-Grade-Qualitaet: ca. 85% → 21.783 t/a
Davon verkauft (Marktaufbau): Jahr 1: 30%, Jahr 5+: 80%

Durchschnitt 10 Jahre: ca. 65% = 14.159 t/a

CO2-Vermeidung Pfad 2 = 14.159 t/a x 0,65 t CO2-eq/t = 9.203 t CO2-eq/a
```

---

## 3. Gesamte GHG-Vermeidung

### 3.1 Jaehrliche Vermeidung

| Pfad | Vermeidung (t CO2-eq/a) |
|---|---|
| Pfad 1: Biomethan ersetzt Erdgas | 29.040 |
| Pfad 2: Food-Grade CO2 ersetzt fossiles CO2 | 9.203 |
| **Gesamt jaehrlich** | **38.243** |

### 3.2 Vermeidung ueber 10 Jahre (Referenzzeitraum)

| Pfad | Vermeidung (t CO2-eq / 10 Jahre) |
|---|---|
| Pfad 1: Biomethan | 290.400 |
| Pfad 2: CO2 (mit Rampe) | 92.030 |
| **Gesamt 10 Jahre** | **382.430** |

### 3.3 Relative GHG-Vermeidung

```
Emissionen Referenz (konventionelle Biogasverstromung):
- 8 Anlagen mit BHKW-Betrieb, Waermenutzung, RTO fuer Abgas
- Keine Biomethan-Produktion, kein CO2-Verkauf
- CO2 aus Biogas wird via RTO in die Atmosphaere abgegeben

Emissionen Referenz = Emissionen des fortgesetzten BHKW-Betriebs
                    = Stromverdraengung (Netz-Emissionsfaktor) ist geringer
                    ABER: kein Ersatz von fossilem Erdgas und fossilem CO2

Relative Vermeidung = (Emissionen_Referenz - Emissionen_Projekt) / Emissionen_Referenz

HINWEIS: Die genaue Berechnung haengt davon ab, wie die Referenz definiert wird.
Zwei Ansaetze:

a) Referenz = Konventionelles Biogas-Upgrading + RTO (kein CO2-Verkauf)
   → Relative Vermeidung durch Pfad 2 allein: ca. 25-30%

b) Referenz = Fortgesetzter BHKW-Betrieb (keine Aufbereitung)
   → Relative Vermeidung deutlich hoeher, da Biomethan Erdgas ersetzt
   → Geschaetzt: 70-85%

EMPFEHLUNG: Ansatz b) verwenden, da der IF die Innovation gegenueber dem
Status Quo (nicht gegenueber einer alternativen Innovation) bewertet.
```

---

## 4. Methodik-Details fuer den GHG-Calculator

### 4.1 Systemgrenzen

```
+-------------------------------------------------------------------+
|                    PROJEKTSYSTEMGRENZE                              |
|                                                                     |
|  Substrat → Fermenter → Biogas → Membran-Upgrading → Biomethan    |
|                                    ↓                    ↓           |
|                              CO2-reiches    20 km Leitung           |
|                              Offgas              ↓                  |
|                                ↓           Erdgasnetz-              |
|                           Reverion rSOC    Einspeisung              |
|                                ↓                                    |
|                           Food-Grade CO2                            |
|                                ↓                                    |
|                           LKW-Transport                             |
|                                ↓                                    |
|                           Brauereien                                |
+-------------------------------------------------------------------+
```

### 4.2 Emissionsfaktoren (Quellen)

| Parameter | Wert | Quelle |
|---|---|---|
| Erdgas, Verbrennung | 0,202 t CO2-eq/MWh | UBA Emissionsfaktoren 2024 |
| Strom Deutschland (Netz-Mix) | 0,380 t CO2-eq/MWh | UBA 2024 |
| Diesel (LKW-Transport) | 2,64 kg CO2-eq/Liter | IPCC / UBA |
| Biomethan (LCA, Well-to-Wheel) | 0,025-0,040 t CO2-eq/MWh | RED III Annex, Pfad: Guellen-basiert am niedrigsten |
| Fossile CO2-Produktion | 0,75 t CO2-eq/t CO2 | Literatur (DECHEMA, IEA) |
| Biogene CO2-Abscheidung (Reverion) | 0,05-0,10 t CO2-eq/t CO2 | Energiebedarf abgeschaetzt |

### 4.3 Methan-Emissionen (Vorkettenemissionen)

**WICHTIG:** Der GHG-Calculator beruecksichtigt auch Methanverluste:

| Quelle | Emissionsfaktor | Minderungsmassnahme |
|---|---|---|
| Methanschlupf Membrananlage | 0,5-2% des Methans | Nachverbrennung / Abfackelung |
| Leckagen Leitung | <0,1% | Leckageortung, Qualitaetspipeline |
| Gasspeicher-Emissionen | vernachlaessigbar | Doppelmembran, Ueberwachung |

**Empfehlung:** Methanschlupf der Membrananlage explizit adressieren, da Methan ein
25x staerkeres Treibhausgas als CO2 ist. Reverion-Technologie kann auch hier punkten,
da das Offgas (mit Restmethan) durch die rSOC geleitet wird und das Methan dort
energetisch genutzt (nicht emittiert) wird.

---

## 5. Plausibilitaetspruefung

### 5.1 Benchmark-Vergleich

| Vergleichsprojekt | CO2-Vermeidung | Quelle |
|---|---|---|
| Typische Biomethan-Anlage (1 MW) | 3.000-5.000 t CO2/a | FNR |
| Innovation Fund Projekt "W4W" | k.A. | CINEA Projektdatenbank |
| Biomethan + CCU (DBFZ-Studie) | 4.000-6.000 t CO2/a pro Anlage | DBFZ 2023 |
| **Unser Projekt (8 Anlagen)** | **38.243 t CO2/a** | **= ca. 4.780 t/Anlage → plausibel** |

### 5.2 Spezifische Vermeidungskosten

```
EUR Grant pro Tonne CO2 vermieden (10 Jahre):

Angenommen: IF-Grant = 3.000.000 EUR (konservativer Ansatz)
CO2-Vermeidung 10 Jahre = 382.430 t

EUR/t CO2 = 3.000.000 / 382.430 = 7,85 EUR/t CO2 → SEHR kosteneffizient!

Zum Vergleich:
- EU ETS-Preis (2026): ca. 60-80 EUR/t CO2
- Innovation Fund Durchschnitt: 20-60 EUR Grant/t CO2
- CCS-Projekte: >100 EUR/t CO2

→ Starkes Argument fuer Cost Efficiency (Kriterium 5)
```

### 5.3 Sensitivitaetsanalyse

| Parameter | Basis | Optimistisch | Pessimistisch |
|---|---|---|---|
| Biogasproduktion (Nm3/h gesamt) | 4.000 | 5.000 | 3.000 |
| Methangehalt | 55% | 58% | 52% |
| Reverion-Abscheidegrad | 90% | 95% | 80% |
| CO2-Verkaufsrate (Durchschnitt 10 J.) | 65% | 80% | 40% |
| **CO2-Vermeidung (t/a)** | **38.243** | **52.000** | **25.000** |

---

## 6. Ausfuellanleitung GHG-Calculator

### Schritt 1: Allgemeine Projektdaten
- Projektname, Laufzeit (10 Jahre), Referenzzeitraum
- Projekttyp: "Biogas upgrading to biomethane + CO2 capture"

### Schritt 2: Referenzszenario definieren
- "Business as usual": Fortgesetzter BHKW-Betrieb der 8 Anlagen
- Erdgasverbrauch der Endkunden, der durch Biomethan ersetzt wird
- Fossile CO2-Versorgung der Brauereien

### Schritt 3: Projektszenario definieren
- Biomethan-Einspeisung ins Erdgasnetz
- Food-Grade CO2-Produktion und -Verkauf
- Eigener Energieverbrauch des Projekts (Strom, Waerme)

### Schritt 4: Emissionsfaktoren eintragen
- Siehe Tabelle 4.2 oben
- Standardwerte aus RED III Annex fuer Biomethan verwenden
- Fuer CO2: eigene Berechnung auf Basis Energiebedarf Reverion

### Schritt 5: Berechnung pruefen
- Absolute Vermeidung: Soll >10.000 t CO2/a sein (Small-Scale)
- Relative Vermeidung: Soll >50% sein fuer hohe Punktzahl
- Plausibilitaet gegen Benchmarks pruefen

---

## 7. Naechste Schritte

1. [ ] GHG Emission Avoidance Calculator Excel von CINEA herunterladen
2. [ ] Reale Anlagendaten einpflegen (Biogasproduktion aller 8 Anlagen)
3. [ ] Emissionsfaktoren mit aktuellsten UBA/RED-III-Werten aktualisieren
4. [ ] Reverion-spezifische Daten (Energiebedarf, Abscheidegrad) eintragen
5. [ ] Referenzszenario mit Berater abstimmen
6. [ ] Plausibilitaetspruefung gegen Benchmarks durchfuehren
7. [ ] Abgleich GHG ↔ Part B ↔ Business Plan (Konsistenzcheck!)
