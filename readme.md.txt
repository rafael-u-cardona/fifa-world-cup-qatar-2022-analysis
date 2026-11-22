# fifa-world-cup-qatar-2022-analysis
Football data analysis of FIFA World Cup Qatar 2022 using Python and StatsBomb Open Data.
This project analyzes the FIFA World Cup Qatar 2022 using StatsBomb Open Data and Python.

The objective is to explore team performance throughout the tournament and generate statistical metrics such as goals scored, goals conceded, points, goal difference and tournament progression.

Project Structure
fifa-world-cup-qatar-2022-analysis

├── data
│   └── 106.json

├── src
│   └── Script3-TablaGoles.py

├── outputs
│   ├── tabla_estadisticas.csv
│   ├── ranking_ataque.csv
│   ├── ranking_defensa.csv
│   ├── top10_puntos.png
│   ├── top10_goles.png
│   └── top10_dg.png

└── README.md

## Clone the repository:

git clone https://github.com/ruceneg-cardona/fifa-world-cup-qatar-2022-analysis.git
Install dependencies:

pip install pandas matplotlib
Run the script:

python Script3-TablaGoles.py

## Dataset

Source:

StatsBomb Open Data

Competition:
FIFA World Cup Qatar 2022

Competition ID: 43

Season ID: 106

## Technologies Used

- Python
- JSON
- Pandas
- Matplotlib

## Output Files
  The script automatically generates the following outputs:
  
  CSV Files
  tabla_estadisticas.csv
  
  Complete team statistics table.
  ranking_ataque.csv
  
  Teams ranked by goals scored (GF).
  ranking_defensa.csv
  
  Teams ranked by goals conceded (GC).
  Visualizations
  top10_puntos.png
  
  Top 10 teams by points.
  top10_goles.png
  
  Top 10 teams by goals scored.
  top10_dg.png
  Top 10 teams by goal difference.

## Metrics Calculated

For each team:

- PJ (Matches Played)
- GF (Goals For)
- GC (Goals Conceded)
- DG (Goal Difference)
- PG (Wins)
- PE (Draws)
- PP (Losses)
- PTS (Points)

Additional metric:

- Tournament Round Reached
  - Group Stage
  - Round of 16
  - Quarter Finals
  - Semi Finals+

## Key Findings

- France was the highest-scoring team with 16 goals.
- England recorded the best goal difference (+9).
- France achieved the highest point total (16).
- Argentina finished second with 14 points.
- Four teams reached the Semi Finals+ stage:
  - France
  - Argentina
  - Croatia
  - Morocco

## Output Files

- tabla_estadisticas.csv
- Team rankings by points
- Team rankings by goal difference
- Top scoring teams visualization

---

## Future Improvements

- Player analysis
- xG (Expected Goals)
- Shot maps
- Passing networks
- Power BI dashboard
- Match prediction models

---

## Author - Rafael U. Cardona E.
	  - Rafael.u.cardona@gmail.com
