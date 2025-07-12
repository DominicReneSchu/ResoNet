# ResoNet – The Decentralized Resonance Field Network

> Your Raspy. Your Voice. Our Resonance Field.

**ResoNet** is a peer-to-peer network that enables anyone to publish their perspective on societal, political, or philosophical topics – **decentralized**, **verifiable**, and **tamper-proof** – using a single device: a Raspberry Pi.

---

## 🎯 Purpose

ResoNet aims to overcome central dependencies and connect individual contributions into a collective resonance field. It's not about likes, reach, or control – but about truth, structure, and responsibility in an open discourse space.

- 🌐 *No central platform*
- 🔐 *Tamper-proof content via signatures*
- 🧠 *Consensus queries via AI*
- 🌱 *Emergent field instead of opinion dictatorship*

---

## 🧱 How it works

Each Raspy node:
- stores the **opinion of its owner** (locally)
- **synchronizes with other Raspys** in the network
- **verifies** new content via signature checks
- holds a complete, verified copy of the entire resonance field

---

## 🗄️ Storage and Field Structure (systemic)

- The 64GB SD card is initially used for the operating system (Raspbian/Raspberry Pi OS) (typically 5–10GB, varies via updates).
- **2GB are systemically reserved as the maximum user storage limit for own opinions.**
    - This limit is technically enforced in the field code (config.json, storage.py, main.py, web.py) and cannot be exceeded.
    - Exceeding is prevented: Before every write operation, the limit is checked.
- **The remaining free space (typically 52–57GB, dynamically depending on OS size) is automatically available for the field.**
    - This area covers resonance data, field copies, consensus, backups, network synchronization.
    - The field area adapts dynamically to actual usage – the user area remains strictly capped at 2GB.
- **No static partitioning:** The allocation is systemic-adaptive, the field regulates itself via the limit logic automatically.
- These boundaries apply field-wide, regardless of individual perspective (resonance rule).

---

## ⚙️ Installation (Raspberry Pi)

### Requirements:
- Raspberry Pi (recommended: 4 or 5) 64GB
- Raspberry Pi OS (Lite or Desktop)
- Internet access
- SSH (optional)

---

### **Step-by-step guide for setup on Raspberry Pi 5**

#### 1. System: Install Raspberry Pi OS (Raspbian)
- **Download image:** [Official Website](https://www.raspberrypi.com/software/)
- **Write image to SD card:** Use Raspberry Pi Imager or balenaEtcher.
- **Insert SD card and boot Pi:** Complete basic setup (language, network, updates).
- **Enable SSH (optional):**  
  `sudo raspi-config` → Interface Options → SSH

#### 2. Update system and install Python/Git
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git
```

#### 3. Clone repository
```bash
git clone https://github.com/DominicReneSchu/ResoNet.git
cd ResoNet
```

#### 4. Install Python dependencies
```bash
python3 -m venv ~/ResoNet/env
source ~/ResoNet/env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
(If there's no `requirements.txt`, see README notes or install packages manually.)

#### 5. Initialization: Keys and configuration
```bash
source ~/ResoNet/env/bin/activate
python3 node/generate_keys.py
```
- This generates `private.pem` and `public.pem`.
- Open **config.json** for adjustment (e.g., with `nano config.json`):
  - Node name
  - Network address/field
  - Port
  - Storage paths
  - Other settings per README

#### 6. Check resonance files
- `opinions.json` and `consensus_export.json` should exist as empty arrays (`[]`).

#### 7. Start the system
```bash
python3 node/main.py
python3 ui/web.py
```
- Open the web interface: [http://localhost:5000](http://localhost:5000) or [http://raspberrypi.local:5000](http://raspberrypi.local:5000)

#### 8. Operation & field coupling
- Network participation: After startup, your node is resonance-capable and joins the field.
- Monitoring: Check logs and network connections (see README).

---

## 🌐 Architecture Overview

- **main.py**: Entry point; orchestrates loading, signing, syncing, and saving.
- **storage.py**: Opinion management, storage limit control (2GB user limit), automatic backup & versioning.
- **sync.py**: Network synchronization (P2P-ready, HTTP stub).
- **verify.py**: Cryptographic signatures for authenticity.
- **web.py**: Web UI; opinion entry & display, consensus, limit feedback.
- **viz_network.py**: Visualization of field structure and topic clusters.
- **consensus_extract.py**: GPT-compatible export of field consensus.
- **generate_keys.py**: RSA keypair generator for identity & verification.
- **install.sh**: Setup script incl. keygen, dependency installation, storage limit notice.
- **config.json**: Node configuration (name, port, topics, peers, storage limit).

---

## 🚀 Quickstart

```bash
cd ResoNet
bash setup/install.sh
python3 node/generate_keys.py
python3 node/main.py
python3 ui/web.py
```

Open [http://localhost:5000](http://localhost:5000) for the local resonance field.

---

## 🖥️ Web UI (Field Portal)

- **Submit opinion:** Directly in the browser, choose topic, enter text.
- **Field opinions:** Tabular overview of all voices, sorted by time.
- **Consensus display:** For each topic, the current field consensus is shown as a list.
- **Topic filter:** Dropdown for focused view/input per topic.
- **Storage limit display:** Current usage and user cap shown in color, input locked when limit reached.
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

Each node generates an RSA key pair (private.pem, public.pem) locally via:

```bash
python3 node/generate_keys.py
```

The public identity can optionally be published in `setup/config.json`.

---

## 🛠️ Backup & Logging

- **Backups:** Each change to opinions.json creates a timestamped backup in `data/backups/`.
- **Logging:** Actions & errors are logged in `data/resonanznet.log`.

---

## 📚 Theory & Introduction

- [Systemic Introduction ResoNet_Erklärung.md](./ResoNet_Erklärung.md)
- [English Introduction ResoNet_Theory_EN.md](./ResoNet_Theory_EN.md)

---

## 🤝 Contributors

- Systemic lead developer: Dominic-René Schu

---

## 📨 Contact & Extension

- Issues & feedback: [GitHub Issues](https://github.com/DominicReneSchu/ResoNet/issues)
- Proposals for new field features and extensions are welcome.

---

**Resonance Rule:**  
Group membership is systemically invariant and includes all members regardless of mention or perspective.