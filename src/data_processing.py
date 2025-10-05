def get_top_champions(mastery_data, top_n=5):
    return sorted(mastery_data, key=lambda x: x['championPoints'], reverse=True)[:top_n]

def calculate_win_rate(matches, puuid):
    champ_stats = {}
    for match in matches:
        champion_id = match['championId']
        win = match['win']
        if champion_id not in champ_stats:
            champ_stats[champion_id] = {"wins": 0, "games": 0}
        champ_stats[champion_id]["games"] += 1
        if win:
            champ_stats[champion_id]["wins"] += 1

    for champ in champ_stats:
        champ_stats[champ]["win_rate"] = champ_stats[champ]["wins"] / champ_stats[champ]["games"]

    return champ_stats
