# League of Legends Draft Engine by Henry Hanlin Zheng

A hybrid **rule-based + data-driven** assistant for League of Legends champion selection. This tool helps players choose champions that maximize **team composition, synergy, and counters** based on currently picked champions, bans, and selected roles.

---

## Features

- **Role & Lane Recommendations**  
  Suggests champions based on your selected role and lane, filling gaps in team composition.

- **Playstyle, Synergy, and Counter Tags**  
  Each champion is classified with unified tags describing:
  - **Playstyle**: What the champion can do.
  - **Synergies**: What kind of team composition benefits the champion.
  - **Counters**: What the champion is vulnerable to or should avoid.

- **Hybrid Recommendation Engine**
  - **Rule-based**: Provides overall direction, e.g., "Pick a tank", "Pick a scaling mid-laner".
  - **Data-driven**: Uses historical match and draft data to recommend specific champions.

- **Flexible JSON-based Configuration**
  - Champion attributes are defined in a JSON format, making it easy to update with new champions or patch changes.

---

## Data Sources

- [Riot Games API](https://developer.riotgames.com/docs/lol)
- Community-curated champion attributes

---

## Tenative Roadmap

- Champion pool filtering by player history
- Streamlit UI with real-time suggestions
- Add full enemy team logic
- Build a desktop interface for interactive drafting

---

For inquiries, please contact me at henry.zheng.2006@gmail.com  
Find me on [LinkedIn](https://www.linkedin.com/in/hhzheng/)

---
League of Legends Draft Engine by Henry Hanlin Zheng is not endorsed by Riot Games and does not reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games and all associated properties are trademarks or registered trademarks of Riot Games, Inc
