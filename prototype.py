from engine.recommender import load_champions, recommend_champions

champions = load_champions("champion_classifications.json")

role_input = "Mid"
desired_playstyle = ["Engage", "Pick"]
team_needs = ["Teamfight"]
enemy_strengths = ["CC"]

results = recommend_champions(champions, role_input, desired_playstyle, team_needs, enemy_strengths)

print("Recommended Champions:")
for champ, score in results:
    print(f"{champ} (Score: {score})")