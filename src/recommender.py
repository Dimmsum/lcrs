# src/recommender.py
import os
import json
from src.data_dragon import ensure_data_files

ensure_data_files()
DATA_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
CHAMP_INFO_FILE = os.path.join(DATA_FOLDER, "champion_info.json")

def recommend_champions(top_champs, limit=10):
    with open(CHAMP_INFO_FILE, 'r', encoding='utf-8') as f:
        champ_info = json.load(f)

    recommendations = []
    top_names = [champ['championName'] for champ in top_champs]

    for champ in top_champs:
        role = champ_info.get(champ['championName'], {}).get('role', 'Unknown')
        # Recommend champions with same role not in top champions
        similar = [c for c, info in champ_info.items() 
                   if info['role'] == role and c not in top_names]
        recommendations.extend(similar)

    # Remove duplicates and limit
    unique_recommendations = []
    for r in recommendations:
        if r not in unique_recommendations:
            unique_recommendations.append(r)
        if len(unique_recommendations) >= limit:
            break

    return unique_recommendations
