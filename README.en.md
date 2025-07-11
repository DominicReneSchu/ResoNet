# ResoNet – The Decentralized Resonance Field Network

> Your Raspy. Your Opinion. Our Resonance Field.

**ResoNet** is a P2P network that enables everyone to record their perspective on social, political, or philosophical topics **decentrally**, **verifiably**, and **tamper-proof** – with a single device: a Raspberry Pi.

---

## 🎯 Purpose

ResoNet aims to overcome central dependencies and connect individual contributions to a collective resonance field. It's not about likes, reach, or control – but about truth, structure, and responsibility in an open discourse space.

- 🌐 *No central platform*
- 🔐 *Tamper-proof content via signatures*
- 🧠 *Consensus queries via AI*
- 🌱 *Emergent field, not opinion dictatorship*

---

## 🧱 How it Works

Each Raspy node:
- contains the **opinion of its owner** (stored locally)
- **synchronizes with other Raspys** in the network
- **verifies** newly received content via signature check
- stores a complete, verified copy of the entire resonance field

---

## ⚙️ Installation (Raspberry Pi)

### Requirements:
- Raspberry Pi (recommended: 4 or 5) 64GB
- Raspberry Pi OS (Lite or Desktop)
- Internet access
- SSH (optional)

---

### **Step-by-Step Guide for Setup on Raspberry Pi 5**

#### 1. System Base: Install Raspberry Pi OS (Raspbian)
- **Download the image:** [Official Website](https://www.raspberrypi.com/software/)
- **Write image to SD card:** Use Raspberry Pi Imager or balenaEtcher.
- **Insert SD card and start the Pi:** Complete initial setup (language, network, updates).
- **Enable SSH (optional):**  
  `sudo raspi-config` → Interface Options → SSH

#### 2. Update System and Install Python/Git
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git
```

#### 3. Clone Repository
```bash
git clone https://github.com/DominicReneSchu/ResoNet.git
cd ResoNet
```

#### 4. Install Python Dependencies
```bash
pip3 install -r requirements.txt
```
(If no `requirements.txt` is present, check the README or install packages manually.)

#### 5. Initialization: Keys and Configuration
```bash
python3 node/generate_keys.py
```
- Only now are `private.pem` and `public.pem` created.
- Open **config.json** and adjust (e.g., with `nano config.json`):
  - Node name
  - Network address/field
  - Port
  - Storage paths
  - Further settings as per README

#### 6. Check Resonance Files
- `opinions.json` and `consensus_export.json` should exist as empty arrays (`[]`).

#### 7. Start the System
```bash
python3 node/main.py
python3 ui/web.py
```
- Open the web interface: [http://localhost:5000](http://localhost:5000) or [http://raspberrypi.local:5000](http://raspberrypi.local:5000)

#### 8. Operation & Field Coupling
- Network participation: After starting, your node is resonance-ready and participates in the field.
- Monitoring: Check log outputs and network connections (see README).

---

## 🌐 Architecture Overview

- **main.py**: Entry point, orchestrates loading, signing, sync, storage.
- **storage.py**: Opinion management, automatic backup & versioning.
- **sync.py**: Network synchronization (P2P-ready, HTTP stub).
- **verify.py**: Cryptographic signatures for authenticity.
- **web.py**: Web UI, entering & displaying opinions, consensus display.
- **viz_network.py**: Visualization of field structure and topic clusters.
- **consensus_extract.py**: GPT-compatible export of field consensus.
- **generate_keys.py**: RSA keypair generator for identity & verification.
- **install.sh**: Setup script incl. keygen, dependency installation.
- **config.json**: Node configuration (name, port, topics, peers).

---

## 🚀 Quickstart

```bash
cd ResoNet
bash setup/install.sh
python3 node/generate_keys.py
python3 node/main.py
python3 ui/web.py
```

Open [http://localhost:5000](http://localhost:5000) for your local resonance field.

---

## 🖥️ Web UI (Field Portal)

- **Submit opinion:** Directly in the browser, select a topic, enter text.
- **Field opinions:** Tabular overview of all voices, sorted by time.
- **Consensus display:** The current field consensus for each topic is displayed as a list.
- **Topic filter:** Selection field for focused view/input by topic.
- **Sync button:** Synchronize with peers (placeholder, P2P-ready).

![Web-UI Screenshot](docs/resonet_webui_screenshot.png)

---

## 📊 Consensus Export

Use `consensus_extract.py` to export the current consensus per topic as JSON (GPT-compatible):

```bash
python3 tools/consensus_extract.py
cat data/consensus_export.json
```

---

## 🔑 Key Management

Each node generates a local RSA keypair (`private.pem`, `public.pem`) via:

```bash
python3 node/generate_keys.py
```

The public identity can optionally be published in `setup/config.json`.

---

## 🛠️ Backup & Logging

- **Backups:** Every change to opinions.json creates a timestamped backup under `data/backups/`.
- **Logging:** Actions & errors are logged in `data/resonanznet.log`.

---

## 📚 Theory & Introduction

- [Systemic Introduction ResoNet_Erklärung.md](./ResoNet_Erklärung.md)
- [English Introduction ResoNet_Theory_EN.md](./ResoNet_Theory_EN.md)

---

## 🤝 Contributors

- Systemic Lead Developer: Dominic-René Schu

---

## 📨 Contact & Extension

- Issues & Feedback: [GitHub Issues](https://github.com/DominicReneSchu/ResoNet/issues)
- Suggestions for field features and extensions are expressly welcome.

---

**Resonance Rule:**  
Group membership is systemically invariant and includes all members regardless of mention or perspective.