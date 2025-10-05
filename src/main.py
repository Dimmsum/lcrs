# src/main.py
from src.api_clients import get_puuid, get_top_champion_mastery
from src.data_processing import get_top_champions
from src.recommender import recommend_champions
from utils.helpers import map_champion_id_to_name

def main():
    summoner_name = input("Enter Summoner Name: ")
    tag_line = input("Enter Tagline: ")

    # Get PUUID
    puuid = get_puuid(summoner_name, tag_line)

    # Get top champion mastery (top 5)
    mastery_data = get_top_champion_mastery(puuid, top_n=5)

    # Process top champions
    top_champs = get_top_champions(mastery_data)

    # Map champion IDs to names
    for champ in top_champs:
        champ['championName'] = map_champion_id_to_name(champ['championId'])

    # Get recommendations
    recommendations = recommend_champions(top_champs)

    print("\nYour Top 5 Champions:")
    for champ in top_champs:
        print(f"{champ['championName']} - Points: {champ['championPoints']}")

    print("\nRecommended Champions to Try:")
    for r in recommendations:
        print(r)

if __name__ == "__main__":
    main()
