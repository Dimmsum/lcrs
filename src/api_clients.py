import requests
from config.config import RIOT_API_KEY, MATCH_COUNT

# Base URLs
PLATFORM_BASE = "https://na1.api.riotgames.com"      # For account info
REGIONAL_BASE = "https://americas.api.riotgames.com" # For champion mastery & matches


# 1️⃣ Get PUUID by Summoner Name + Tagline (platform routing)
def get_puuid(summoner_name, tag_line):
    url = f"{REGIONAL_BASE}/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag_line}"
    response = requests.get(url + "?api_key=" + RIOT_API_KEY)
    response.raise_for_status()
    return response.json()['puuid']

# 2️⃣ Get top champion mastery entries (regional routing)
def get_top_champion_mastery(puuid, top_n=5):
    url = f"{PLATFORM_BASE}/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top?count={top_n}"
    response = requests.get(url + "&api_key=" + RIOT_API_KEY)
    response.raise_for_status()
    return response.json()

# 3️⃣ Get recent match IDs (regional routing)
def get_recent_matches(puuid, count=MATCH_COUNT):
    url = f"{REGIONAL_BASE}/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}"
    response = requests.get(url + "?api_key=" + RIOT_API_KEY)
    response.raise_for_status()
    return response.json()

# 4️⃣ Get match details (regional routing)
def get_match_details(match_id):
    url = f"{REGIONAL_BASE}/lol/match/v5/matches/{match_id}"
    response = requests.get(url + "?api_key=" + RIOT_API_KEY)
    response.raise_for_status()
    return response.json()
