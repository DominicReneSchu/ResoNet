# ResoNet – Das dezentrale Resonanzfeld-Netzwerk

> Not your Key, not your Voice.

**ResoNet** ist ein P2P-Netzwerk, das jedem Menschen die Möglichkeit gibt, seine Sichtweise zu gesellschaftlichen, politischen oder philosophischen Themen **dezentral**, **verifizierbar** und **manipulationssicher** zu hinterlegen – mit einem einzigen Gerät: einem Raspberry Pi.

---

## 🎯 Zielsetzung

ResoNet möchte zentrale Abhängigkeiten überwinden und individuelle Beiträge zu einem kollektiven Resonanzfeld verbinden. Es geht nicht um Likes, Reichweite oder Kontrolle – sondern um Wahrheit, Struktur und Verantwortung im offenen Diskursraum.

- 🌐 *Keine zentrale Plattform*
- 🔐 *Fälschungssichere Inhalte durch Signaturen*
- 🧠 *Konsensabfrage via KI*
- 🌱 *Emergentes Feld statt Meinungsdiktat*

---

## 🧱 Funktionsweise

Jeder Raspy-Knoten:
- enthält die **Meinung seines Besitzers** (lokal speicherbar)
- **synchronisiert sich mit anderen Raspys** im Netzwerk
- **verifiziert** neu empfangene Inhalte durch Signaturprüfung
- speichert eine vollständige, verifizierte Kopie des gesamten Resonanzfelds

---

## 🗄️ Speicher- und Feldstruktur (systemisch)

- Die 64GB SD-Karte wird initial für das Betriebssystem (Raspbian/Raspberry Pi OS) genutzt (typisch 5–10GB, variiert durch Updates).
- **2GB sind systemisch exklusiv als maximales User-Limit für eigene Meinungen reserviert.**
    - Dieses Limit ist technisch im Feldcode (config.json, storage.py, main.py, web.py) fest verankert und kann nicht überschritten werden.
    - Überschreitung wird verhindert: Vor jedem Speichervorgang wird geprüft, ob das Limit erreicht ist.
- **Der verbleibende Speicherplatz (typisch 52–57GB, dynamisch abhängig von OS-Größe) steht automatisch für das Feld zur Verfügung.**
    - Dieser Bereich umfasst Resonanzdaten, Feldkopien, Konsens, Backups, Netzwerksynchronisation.
    - Die Feldgröße passt sich dynamisch dem Gesamtzustand an – der Userbereich bleibt invariant auf 2GB limitiert.
- Es erfolgt **keine statische Partitionierung**: Die Aufteilung ist systemisch-adaptiv, das Feld reguliert sich über die Limitlogik automatisch.
- Die Grenzen gelten feldweit, unabhängig von individueller Sichtweise (Resonanzregel).

---

## ⚙️ Installation (Raspberry Pi)

### Voraussetzungen:
- Raspberry Pi (empfohlen: 4 oder 5) 64GB
- Raspberry Pi OS (Lite oder Desktop)
- Internetzugang
- SSH (optional)

---

### **Schritt-für-Schritt-Anleitung zur Inbetriebnahme auf dem Raspberry Pi 5**

#### 1. Systembasis: Raspberry Pi OS (Raspbian) installieren
- **Image herunterladen:** [Offizielle Website](https://www.raspberrypi.com/software/)
- **Image auf SD-Karte schreiben:** Mit Raspberry Pi Imager oder balenaEtcher.
- **SD-Karte einsetzen und Pi starten:** Grundinstallation durchführen (Sprache, Netzwerk, Updates).
- **SSH aktivieren (optional):**  
  `sudo raspi-config` → Interface Options → SSH

#### 2. System aktualisieren und Python/Git installieren
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git
```

#### 3. Repository beziehen
```bash
git clone https://github.com/DominicReneSchu/ResoNet.git
cd ResoNet
```

#### 4. Python-Abhängigkeiten installieren
```bash
python3 -m venv ~/ResoNet/env
source ~/ResoNet/env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
(Falls keine `requirements.txt`, siehe Hinweise im README oder installiere Pakete manuell.)

#### 5. Initialisierung: Schlüssel und Konfiguration
```bash
source ~/ResoNet/env/bin/activate
python3 node/generate_keys.py
```
- Erst jetzt werden `private.pem` und `public.pem` erzeugt.
- **config.json** öffnen und anpassen (z.B. mit `nano config.json`):
  - Knotenname
  - Netzwerkadresse/Feld
  - Port
  - Speicherpfade
  - Weitere Einstellungen nach README

#### 6. Resonanzdateien kontrollieren
- `opinions.json` und `consensus_export.json` sollten als leeres Array (`[]`) existieren.

#### 7. Systemstart
```bash
source ~/ResoNet/env/bin/activate
python3 node/main.py
python3 ui/web.py
```
- Webinterface öffnen: [http://localhost:5000](http://localhost:5000) oder [http://raspberrypi.local:5000](http://raspberrypi.local:5000)

#### 8. Betrieb & Feldkopplung
- Netzwerkteilnahme: Nach dem Start ist dein Knoten resonanzfähig und nimmt am Feld teil.
- Monitoring: Prüfe Logausgaben und Netzwerkverbindungen (siehe README).

---

## 🌐 Architekturüberblick

- **main.py**: Einstiegspunkt, orchestriert Laden, Signatur, Sync, Speicherung.
- **storage.py**: Meinungsverwaltung, Speicherlimitkontrolle (2GB User-Limit), automatisches Backup & Versionierung.
- **sync.py**: Netzwerk-Synchronisation (P2P-ready, HTTP-Stub).
- **verify.py**: Kryptografische Signaturen für Authentizität.
- **web.py**: Web-UI, Eintragen & Anzeigen von Meinungen, Konsensanzeige, Limit-Feedback.
- **viz_network.py**: Visualisierung der Feldstruktur und Themencluster.
- **consensus_extract.py**: GPT-kompatibler Export des Feldkonsenses.
- **generate_keys.py**: RSA-Keypair-Generator für Identität & Verifikation.
- **install.sh**: Setup-Skript inkl. Keygen, Abhängigkeitsinstallation, Speicherlimit-Hinweis.
- **config.json**: Knotenkonfiguration (Name, Port, Topics, Peers, Speicherlimit).

---

## 🚀 Schnellstart

```bash
cd ResoNet
bash setup/install.sh
python3 node/generate_keys.py
python3 node/main.py
python3 ui/web.py
```

Öffne [http://localhost:5000](http://localhost:5000) für das lokale Resonanzfeld.

---

## 🖥️ Web-UI (Feldportal)

- **Meinung eintragen:** Direkt im Browser, Thema auswählen, Text eingeben.
- **Meinungen im Feld:** Tabellarische Übersicht aller Stimmen, sortiert nach Zeit.
- **Konsensanzeige:** Für jedes Thema wird der aktuelle Feld-Konsens als Liste angezeigt.
- **Themenfilter:** Auswahlfeld zur gezielten Ansicht/Eingabe je Topic.
- **Speicherlimit-Anzeige:** Aktueller Verbrauch und User-Grenze werden farblich visualisiert, Schreibsperre bei Überschreitung.
- **Sync-Button:** Synchronisation mit Peers (Platzhalter, P2P-ready).

![Web-UI Screenshot](docs/resonet_webui_screenshot.png)

---

## 📊 Konsens-Export

Nutze `consensus_extract.py`, um den aktuellen Konsens pro Thema als JSON zu exportieren (GPT-kompatibel):

```bash
python3 tools/consensus_extract.py
cat data/consensus_export.json
```

---

## 🔑 Schlüsselverwaltung

Jeder Knoten generiert lokal ein RSA-Schlüsselpaar (private.pem, public.pem) per:

```bash
python3 node/generate_keys.py
```

Die öffentliche Identität kann optional in `setup/config.json` veröffentlicht werden.

---

## 🛠️ Backup & Logging

- **Backups:** Jede Änderung an opinions.json erzeugt ein zeitgestempeltes Backup unter `data/backups/`.
- **Logging:** Aktionen & Fehler werden in `data/resonanznet.log` protokolliert.

---

## 📚 Theorie & Einführung

- [Systemische Einführung ResoNet_Erklärung.md](https://github.com/DominicReneSchu/public/blob/main/de/fakten/docs/gesellschaft/resonet_erklärung.md)

---

# 🌊 Semantische Tiefe-Bewertung mit Coral USB Accelerator

---

## 🧭 Systemischer Überblick

Dein Raspy wird Teil einer **semantisch resonanten Feldstruktur**: Jeder Knoten erkennt lokal, wie viel gesellschaftliche Tiefe ein Beitrag besitzt – und stimmt sich über Resonanz mit anderen Knoten ab. Die Gruppenzugehörigkeit jedes Beitrags ("shallow", "medium", "deep") ist systemisch invariant und wird durch kollektive wie individuelle Bewertung im Resonanzfeld emergent bestimmt.

---

## 🔁 Ablaufplan zur Tiefe-Erkennung via Coral + TFLite

### 1. Trainingsdatenbasis definieren

- `training/training_data.jsonl` erstellen:  
  Format:  
  ```json
  {"text": "Beispieltext", "label": "deep"}
  ```
- Kategorien: `"shallow"`, `"medium"`, `"deep"`
- 300–1000 Beispiele (eigene Texte oder aggregierte Beiträge)
- Tools: Jupyter Notebook, Python-Skript, CSV→JSONL-Konverter

**Tipp:**  
Nutze das systemische Resonanzfeld: Auch implizite Gruppenzugehörigkeit (z.B. ironische Tiefe) gehört ins Datenset.

---

### 2. Klassifikator-Modell trainieren

- Frameworks:  
  - `transformers + datasets + sklearn` (Laptop/Cloud)  
  - `keras + tf.data` (direkter `.tflite`-Export möglich)
- Architektur:  
  - Leichtes BERT-Modell (`DistilBERT`/`MobileBERT`)
  - Eingabe: Text (max. 256 Tokens)
  - Ausgabe: Klassifikation (`"shallow"`, `"medium"`, `"deep"`)

---

### 3. Export nach TensorFlow Lite + Coral

- `tf.lite.TFLiteConverter` für `.tflite`
- `edgetpu_compiler` für Coral-kompatibles Modell:
  ```bash
  edgetpu_compiler model.tflite
  ```
- Ergebnis:  
  `model/depth_classification_edgetpu.tflite`

---

### 4. Inferenz-Skript auf Raspy

- `scripts/infer_depth.py`:  
  - Lädt `.tflite`-Modell, tokenisiert Text, gibt Tiefe & Confidence zurück
  - Optional als REST-API (`/api/depth_score`) im Webinterface

- Output:
  ```json
  { "depth_score": "deep", "confidence": 0.91 }
  ```

---

### 5. Anzeige im Webinterface

- Visualisierung pro Beitrag: “Tiefe: tief (91%)”
- Sortierung & Filter nach Tiefe möglich

---

### 6. Resonanz-Synchronisation (optional/ausbaubar)

- Knoten spiegeln Tiefe durch `"depth_votes"`
- Finaler Wert = Mittelwert/gewichtete Resonanz aller Stimmen
- P2P-API denkbar: `/depth_vote`

---

### 7. Testen & Optimieren

- Teste mit eigenen, markierten Texten und Grenzfällen
- Debug-Logging (`depth_score_log.txt`) zur Nachvollziehbarkeit

---

## 🗂 Empfohlene Ordnerstruktur

```bash
ResoNet/
├── requirements.txt
├── data/
│   ├── opinions.json
│   ├── consensus_export.json
│   └── resonanznet.log
├── model/
│   └── depth_classification_edgetpu.tflite
├── node/
│   ├── main.py
│   ├── sync.py
│   ├── verify.py
│   ├── generate_keys.py
│   └── storage.py
├── scripts/
│   └── infer_depth.py
├── training/
│   ├── train_depth_model.py
│   └── training_data.jsonl
├── tools/
│   ├── consensus_extract.py
│   └── viz_network.py
├── ui/
│   └── web.py
├── setup/
│   ├── install.sh
│   └── config.json
```

---

## 📦 Nächste Schritte

1. **JSONL-Schema & Beispielgenerator** anfordern (optional)
2. Trainingsdaten sammeln & labeln
3. Trainingsskript und Inferenz-Skript bereitstellen (auf Wunsch)
4. Testen, Resonanzlogik verfeinern, Feedback ins Modell rückführen

---

## 🔗 Resonanzregel

Die Gruppenzugehörigkeit eines Beitrags zum semantischen Tiefenfeld ist **systemisch invariant**—sie umfasst explizite wie implizite Schwingungen, unabhängig von Einzelperspektiven oder Sichtbarkeit.

---

**Fazit:**  
Du schaffst eine maschinelle Resonanzwahrnehmung – jede Tiefe ist emergent, kollektiv und lokal überprüfbar. Die Resonanzregel wird systemisch garantiert.

---

## 🤝 Mitwirkende

- Systemischer Hauptentwickler: Dominic-René Schu

---

## 📨 Kontakt & Erweiterung

- Issues & Feedback: [GitHub Issues](https://github.com/DominicReneSchu/ResoNet/issues)
- Vorschläge für Feld-Features und Erweiterungen sind ausdrücklich erwünscht.

---

**Resonanzregel:**  
Gruppenzugehörigkeit ist systemisch invariant und umfasst alle Mitglieder unabhängig von Nennung oder Sichtweise.