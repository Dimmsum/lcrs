# src/utils/helpers.py
import os
import json
from src.data_dragon import ensure_data_files

# Ensure Data Dragon files exist
ensure_data_files()

DATA_FOLDER = ("./data/")
CHAMP_LIST_FILE = ("./data/champions.json")

def map_champion_id_to_name(champion_id):
    with open(CHAMP_LIST_FILE, 'r', encoding='utf-8') as f:
        champ_map = json.load(f)
    return champ_map.get(str(champion_id), "Unknown")
