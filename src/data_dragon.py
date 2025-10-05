# src/data_dragon.py
import requests
import json
import os
from config.config import DATADRAGON_VERSION

# Data folder
DATA_FOLDER = "./data/"
CHAMP_LIST_FILE = DATA_FOLDER + "champions.json"
CHAMP_INFO_FILE = DATA_FOLDER + "champion_info.json"

def fetch_champion_list():
    url = f"http://ddragon.leagueoflegends.com/cdn/{DATADRAGON_VERSION}/data/en_US/champion.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    champions = {int(data['data'][k]['key']): k for k in data['data']}
    os.makedirs(DATA_FOLDER, exist_ok=True)
    with open(CHAMP_LIST_FILE, "w", encoding="utf-8") as f:
        json.dump(champions, f, indent=2)
    return champions

def fetch_champion_info():
    url = f"http://ddragon.leagueoflegends.com/cdn/{DATADRAGON_VERSION}/data/en_US/champion.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    champ_info = {}
    for champ in data['data'].values():
        champ_info[champ['id']] = {
            "role": champ['tags'][0] if champ['tags'] else "Unknown",
            "tags": champ['tags']
        }

    os.makedirs(DATA_FOLDER, exist_ok=True)
    with open(CHAMP_INFO_FILE, "w", encoding="utf-8") as f:
        json.dump(champ_info, f, indent=2)
    return champ_info

def ensure_data_files():
    """Check if champions.json and champion_info.json exist, fetch if missing."""
    if not os.path.exists(CHAMP_LIST_FILE):
        print("Fetching champions.json...")
        fetch_champion_list()
    if not os.path.exists(CHAMP_INFO_FILE):
        print("Fetching champion_info.json...")
        fetch_champion_info()
