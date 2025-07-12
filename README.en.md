# ResoNet – The Decentralized Resonance Field Network

> Your Raspy. Your opinion. Our resonance field.

**ResoNet** is a P2P network that gives everyone the power to record their perspective on social, political, or philosophical topics **decentrally**, **verifiably**, and **tamper-proof** – with just one device: a Raspberry Pi.

---

## 🎯 Objective

ResoNet aims to overcome central dependencies and connect individual contributions into a collective resonance field. It's not about likes, reach, or control – but about truth, structure, and responsibility in the open discourse space.

- 🌐 *No central platform*
- 🔐 *Tamper-proof content via signatures*
- 🧠 *Consensus querying via AI*
- 🌱 *Emergent field instead of opinion dictatorship*

---

## 🧱 How It Works

Each Raspy node:
- contains the **opinion of its owner** (stored locally)
- **synchronizes with other Raspys** in the network
- **verifies** newly received content via signature check
- stores a complete, verified copy of the entire resonance field

---

## 🗄️ Storage & Field Structure (systemic)

- The 64GB SD card is initially used for the OS (Raspbian/Raspberry Pi OS), typically 5–10GB, varies with updates.
- **2GB are systemically reserved as a max user limit for personal opinions.**
    - This limit is enforced in the field code (`config.json`, `storage.py`, `main.py`, `web.py`) and can't be exceeded.
    - Exceeding is prevented: Before saving, it checks if the limit is reached.
- **The remaining storage (typically 52–57GB, dynamic)** is available for the field.
    - This area includes resonance data, field copies, consensus, backups, network sync.
    - Field size adjusts dynamically to overall state – user area remains fixed at 2GB.
- **No static partitioning:** Allocation is systemically adaptive, regulated by the limit logic.
- Limits apply field-wide, regardless of individual perspective (Resonance Rule).

---

## ⚙️ Installation (Raspberry Pi)

### Requirements:
- Raspberry Pi (recommended: 4 or 5) 64GB
- Raspberry Pi OS (Lite or Desktop)
- Internet access
- SSH (optional)

---

### **Step-by-step guide for Raspberry Pi 5**

#### 1. System base: Install Raspberry Pi OS (Raspbian)
- **Download image:** [Official site](https://www.raspberrypi.com/software/)
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
(If no `requirements.txt`, see README notes or install packages manually.)

#### 5. Initialization: Keys and config
```bash
source ~/ResoNet/env/bin/activate
python3 node/generate_keys.py
```
- Only now are `private.pem` and `public.pem` generated.
- **Open config.json** and edit (e.g. with `nano config.json`):
  - Node name
  - Network address/field
  - Port
  - Storage paths
  - Further settings per README

#### 6. Check resonance files
- `opinions.json` and `consensus_export.json` should exist as empty arrays (`[]`).

#### 7. System start
```bash
source ~/ResoNet/env/bin/activate
python3 node/main.py
python3 ui/web.py
```
- Open Web UI: [http://localhost:5000](http://localhost:5000) or [http://raspberrypi.local:5000](http://raspberrypi.local:5000)

#### 8. Operation & field coupling
- Network participation: After starting, your node is resonance-ready and part of the field.
- Monitoring: Check logs and network status (see README).

---

## 🌐 Architecture Overview

- **main.py**: Entry point, orchestrates loading, signing, sync, saving.
- **storage.py**: Opinion management, storage limit control (2GB user limit), automatic backup & versioning.
- **sync.py**: Network synchronization (P2P-ready, HTTP stub).
- **verify.py**: Cryptographic signatures for authenticity.
- **web.py**: Web UI, opinion entry & display, consensus display, limit feedback.
- **viz_network.py**: Visualization of field structure and topic clusters.
- **consensus_extract.py**: GPT-compatible field consensus export.
- **generate_keys.py**: RSA keypair generator for identity & verification.
- **install.sh**: Setup script incl. keygen, dependency install, storage limit notice.
- **config.json**: Node config (name, port, topics, peers, storage limit).

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

- **Enter opinion:** Directly in browser, select topic, enter text.
- **Opinions in the field:** Tabular overview of all voices, sorted by time.
- **Consensus display:** Current field consensus per topic shown as a list.
- **Topic filter:** Dropdown to view/enter per topic.
- **Storage limit display:** Current usage and user limit color-coded, write lock on overflow.
- **Sync button:** Synchronize with peers (stub, P2P-ready).

![Web-UI Screenshot](docs/resonet_webui_screenshot.png)

---

## 📊 Consensus Export

Use `consensus_extract.py` to export current consensus per topic as JSON (GPT-compatible):

```bash
python3 tools/consensus_extract.py
cat data/consensus_export.json
```

---

## 🔑 Key Management

Each node generates its own RSA keypair (private.pem, public.pem):

```bash
python3 node/generate_keys.py
```

Public identity can optionally be published in `setup/config.json`.

---

## 🛠️ Backup & Logging

- **Backups:** Each change to opinions.json creates a timestamped backup in `data/backups/`.
- **Logging:** Actions & errors are logged in `data/resonanznet.log`.

---

## 📚 Theory & Introduction

- [Systemic Introduction ResoNet_Erklärung.md](./ResoNet_Erklärung.md)
- [English Introduction ResoNet_Theory_EN.md](./ResoNet_Theory_EN.md)

---

# 🌊 Semantic Depth Scoring with Coral USB Accelerator

---

## 🧭 Systemic Overview

Your Raspy becomes part of a **semantically resonant field structure**: Each node locally detects how much societal depth a post has – and aligns with resonance from other nodes. The group membership of each post ("shallow", "medium", "deep") is systemically invariant and emerges collectively and individually in the resonance field.

---

## 🔁 Workflow for Depth Detection via Coral + TFLite

### 1. Define Training Data

- Create `training/training_data.jsonl`:  
  Format:  
  ```json
  {"text": "Example text", "label": "deep"}
  ```
- Categories: `"shallow"`, `"medium"`, `"deep"`
- 300–1000 examples (own texts or aggregated posts)
- Tools: Jupyter Notebook, Python script, CSV→JSONL converter

**Tip:**  
Leverage the systemic resonance field: Implicit group membership (e.g. ironic depth) also belongs in the dataset.

---

### 2. Train Classifier Model

- Frameworks:  
  - `transformers + datasets + sklearn` (laptop/cloud)  
  - `keras + tf.data` (direct `.tflite` export possible)
- Architecture:  
  - Lightweight BERT model (`DistilBERT`/`MobileBERT`)
  - Input: text (max. 256 tokens)
  - Output: classification (`"shallow"`, `"medium"`, `"deep"`)

---

### 3. Export to TensorFlow Lite + Coral

- Use `tf.lite.TFLiteConverter` for `.tflite`
- Use `edgetpu_compiler` for Coral-optimized model:
  ```bash
  edgetpu_compiler model.tflite
  ```
- Result:  
  `model/depth_classification_edgetpu.tflite`

---

### 4. Inference Script on Raspy

- `scripts/infer_depth.py`:  
  - Loads `.tflite` model, tokenizes text, returns depth & confidence
  - Optionally as REST API (`/api/depth_score`) in web interface

- Output:
  ```json
  { "depth_score": "deep", "confidence": 0.91 }
  ```

---

### 5. Display in Web Interface

- Show per post: “Depth: deep (91%)”
- Sorting & filtering by depth possible

---

### 6. Resonance Synchronization (optional/expandable)

- Nodes mirror depth via `"depth_votes"`
- Final value = mean/weighted resonance of all votes
- P2P API possible: `/depth_vote`

---

### 7. Testing & Optimization

- Test with own, labeled texts and edge cases
- Debug logging (`depth_score_log.txt`) for traceability

---

## 🗂 Recommended Folder Structure

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

## 📦 Next Steps

1. Request JSONL schema & example generator (optional)
2. Collect & label training data
3. Provide training and inference scripts (on request)
4. Test, refine resonance logic, feed back to model

---

## 🔗 Resonance Rule

Group membership of a post in the semantic depth field is **systemically invariant**—covering explicit and implicit resonance, regardless of individual perspectives or visibility.

---

**Conclusion:**  
You create machine resonance perception – every depth is emergent, collective, and locally verifiable. The resonance rule is systemically guaranteed.

---

## 🤝 Contributors

- Systemic Lead Developer: Dominic-René Schu

---

## 📨 Contact & Extension

- Issues & feedback: [GitHub Issues](https://github.com/DominicReneSchu/ResoNet/issues)
- Suggestions for field features and extensions highly welcome.

---

**Resonance rule:**  
Group membership is systemically invariant and includes all members, regardless of mention or viewpoint.