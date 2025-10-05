# run_data_dragon.py
from src.data_dragon import fetch_champion_list, fetch_champion_info

if __name__ == "__main__":
    print("Fetching champion list...")
    fetch_champion_list()
    print("Fetching champion info...")
    fetch_champion_info()
    print("Data Dragon files created successfully!")
