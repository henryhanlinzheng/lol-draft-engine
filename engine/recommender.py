import json

def load_champions(json_path = "champion_classifications.json"):
    with open("champion_classifications.json", "r") as f:
        data = json.load(f)
    champions = data["champions"]

def score_champion(champ_data, role, playstyle, team_needs, enemy_strengths):
    score = 0
    if champ_data["lanes"]["primary"] == role or role in champ_data["lanes"].get("flex", []):
        score += 3
    else:
        score -= 5
    
    for style in playstyle:
        if style in champ_data["playstyle"].get("combat_style", []):
            score += 2
    
    for needs in team_needs:
        if needs in champ_data.get("synergies", []):
            score += 2

    for counters in enemy_strengths:
        if counters in champ_data.get("counters", []):
            score -= 3
    return score

def recommended_champions(champions, role, playstyle, team_needs, enemy_strengths, top_n = 5):
    scored = []
    for champ_id, champ_data in champions.items():
        score = score_champion(champ_data, role, playstyle, team_needs, enemy_strengths)
        scored.append((champ_id["name"]), score)

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]

