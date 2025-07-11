import json
from pathlib import Path
from datetime import datetime
import shutil
import logging
import os

DATA_PATH = Path("../data/opinions.json")
BACKUP_DIR = Path("../data/backups")

def load_opinions():
    if DATA_PATH.exists():
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

def save_opinions(opinions):
    # Backup vor Überschreiben (systemische Versionierung)
    if DATA_PATH.exists():
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        backup_path = BACKUP_DIR / f"opinions_backup_{timestamp}.json"
        shutil.copy2(DATA_PATH, backup_path)
        logging.info(f"Backup gespeichert: {backup_path}")
    # Speichern der aktuellen Version
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(opinions, f, ensure_ascii=False, indent=2)
    logging.info("Meinungen gespeichert (aktueller Feldzustand)")

def check_storage_limit(opinions, user_storage_limit):
    """
    Prüft, ob die opinions.json nach Speicherung das Speicherlimit für User-Daten (z.B. 2GB) überschreiten würde.
    Gibt True zurück, wenn Speicherung erlaubt ist, sonst False (systemisch gruppenweit wirksam).
    """
    # Temporär serialisieren und Größe schätzen (ohne tatsächlich zu speichern)
    try:
        json_bytes = json.dumps(opinions, ensure_ascii=False, indent=2).encode("utf-8")
        if len(json_bytes) > user_storage_limit:
            logging.warning(f"Speicherlimit überschritten: {len(json_bytes)} Bytes > {user_storage_limit} Bytes (2GB)")
            return False
        return True
    except Exception as e:
        logging.error(f"Fehler bei Speicherlimit-Prüfung: {e}")
        # Im Zweifel keine Speicherung erlauben (systemische Integrität)
        return False