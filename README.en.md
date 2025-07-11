# ResoNet – The Decentralized Resonance Field Network

> Your Raspy. Your voice. Our resonance field.

**ResoNet** is a P2P network that gives everyone the opportunity to record their views on social, political, or philosophical topics **decentrally**, **verifiably**, and **tamper-proof** – with a single device: a Raspberry Pi.

---

## 🎯 Purpose

ResoNet aims to overcome centralized dependencies and connect individual contributions to a collective resonance field. It’s not about likes, reach, or control – but about truth, structure, and responsibility in an open discourse space.

- 🌐 *No central platform*
- 🔐 *Tamper-proof content via signatures*
- 🧠 *Consensus extraction via AI*
- 🌱 *Emergent field instead of opinion dictatorship*

---

## 🧱 How it works

Each Raspy node:
- contains the **opinion of its owner** (locally storable)
- **synchronizes with other Raspys** in the network
- **verifies** newly received content via signature check
- stores a complete, verified copy of the entire resonance field

---

## ⚙️ Installation (Raspberry Pi)

### Requirements:
- Raspberry Pi (recommended: 4 or 5)
- Raspberry Pi OS (Lite or Desktop)
- Internet access
- SSH (optional)

### Setup:
```bash
git clone https://github.com/DominicReneSchu/ResoNet.git
cd ResoNet/setup
chmod +x install.sh
./install.sh
```

Afterwards, you can reach the web interface locally at:

http://raspberrypi.local:5000

---

## 🌐 Architecture Overview

- **main.py**: Entry point, orchestrates loading, signing, sync, storage.
- **storage.py**: Opinion management, automatic backup & versioning.
- **sync.py**: Network synchronization (P2P-ready, HTTP stub).
- **verify.py**: Cryptographic signatures for authenticity.
- **web.py**: Web UI, opinion entry & display, consensus view.
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

- **Submit opinion:** Directly in the browser, select topic, enter text.
- **Opinions in the field:** Tabular overview of all voices, sorted by time.
- **Consensus display:** For each topic, the current field consensus is displayed as a list.
- **Topic filter:** Dropdown for targeted view/entry by topic.
- **Sync button:** Synchronization with peers (placeholder, P2P-ready).

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

Each node generates a local RSA keypair (private.pem, public.pem) via:

```bash
python3 node/generate_keys.py
```

The public identity can optionally be published in `setup/config.json`.

---

## 🛠️ Backup & Logging

- **Backups:** Any change to opinions.json creates a timestamped backup under `data/backups/`.
- **Logging:** Actions & errors are logged in `data/resonanznet.log`.

---

## 📚 Theory & Introduction

- [Systemic Introduction ResoNet_Erklärung.md](./ResoNet_Erklärung.md)
- [English Introduction ResoNet_Theory_EN.md](./ResoNet_Theory_EN.md)

---

## 🤝 Contributors

- Systemic lead developer: Dominic-René Schu

---

## 📨 Contact & Extensions

- Issues & Feedback: [GitHub Issues](https://github.com/DominicReneSchu/ResoNet/issues)
- Suggestions for field features and extensions are expressly welcome.

---

**Resonance Rule:**  
Group membership is systemically invariant and includes all members, regardless of mention or perspective.