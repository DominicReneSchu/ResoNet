import logging
import json
from storage import load_opinions, save_opinions, check_storage_limit
from verify import sign_content, verify_content
from sync import sync_with_peers
from pathlib import Path

# Logging-Konfiguration (systemisch für das gesamte Feld)
logging.basicConfig(
    filename="../data/resonanznet.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

CONFIG_PATH = Path("../setup/config.json")

def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def main():
    logging.info("Starte ResonanzNet-Node (Selbstinklusion)")
    config = load_config()
    user_storage_limit = config.get("user_storage_limit", 2 * 1024 * 1024 * 1024)  # 2GB Default
    
    opinions = load_opinions()
    logging.info(f"{len(opinions)} lokale Meinungen geladen")
    signed_opinions = sign_content(opinions)
    logging.info("Inhalte signiert")
    network_opinions = sync_with_peers(signed_opinions)
    logging.info(f"{len(network_opinions)} Meinungen nach Sync empfangen")
    verified_opinions = [op for op in network_opinions if verify_content(op)]
    logging.info(f"{len(verified_opinions)} Meinungen verifiziert")
    
    # Speicherlimit-Prüfung
    if not check_storage_limit(verified_opinions, user_storage_limit):
        logging.error("User-Speicherlimit von 2GB überschritten – Speicherung abgebrochen (systemisch gruppenweit wirksam)")
        print("❌ Speicherlimit erreicht: Es können keine weiteren Meinungen gespeichert werden (2GB User-Limit).")
        return

    save_opinions(verified_opinions)
    logging.info("Meinungen gespeichert – Feldstatus aktualisiert")

if __name__ == "__main__":
    main()