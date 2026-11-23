# ==================================================
# IMPORT LIBRARIES
# ==================================================

import json
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# LOAD DATA
# ==================================================

ruta = r"C:\data\matches\43\106.json"

def cargar_datos (ruta):

    with open( ruta, encoding="utf-8") as f:
        return json.load(f)

matches = cargar_datos (ruta)

# ==================================================
# VARIABLES
# ==================================================

df_matches = pd.DataFrame(matches)
estadisticas = {}
goles_l = 0
goles_v = 0
promedio= 0

# ==================================================
# DATA ANALYSIS USING PYTHON
# ==================================================

primer = matches[0]
ultimo = matches[-1]

print("FIFA World Cup Qatar 2022 - Data Analysis using Python\n")
print("Analisis de Datos\n")
print("Primer Partido:",
    primer["home_team"]["home_team_name"],
    "vs",
    primer["away_team"]["away_team_name"]
)

print("Ultimo Partido:",
    ultimo["home_team"]["home_team_name"],
    "vs",
    ultimo["away_team"]["away_team_name"]
)

# Acumular los goles marcados por locales y visitantes
# para calcular estadísticas globales del torneo

for partido in matches:

    goles_l += partido["home_score"]
    goles_v += partido["away_score"]
    
    local = partido["home_team"]["home_team_name"]
    visitante = partido["away_team"]["away_team_name"]

    gol_local = partido["home_score"]
    gol_visitante = partido["away_score"]

    estadisticas.setdefault(local, {
        "PJ": 0,
        "GF": 0,
        "GC": 0,
        "PG": 0,
        "PE": 0,
        "PP": 0,
        "PTS": 0
    })

    estadisticas.setdefault(visitante, {
        "PJ": 0,
        "GF": 0,
        "GC": 0,
        "PG": 0,
        "PE": 0,
        "PP": 0,
        "PTS": 0
    })

    estadisticas[local]["PJ"] += 1
    estadisticas[local]["GF"] += gol_local
    estadisticas[local]["GC"] += gol_visitante

    estadisticas[visitante]["PJ"] += 1
    estadisticas[visitante]["GF"] += gol_visitante
    estadisticas[visitante]["GC"] += gol_local

    if gol_local > gol_visitante:

        estadisticas[local]["PG"] += 1
        estadisticas[visitante]["PP"] += 1

    elif gol_local < gol_visitante:

        estadisticas[visitante]["PG"] += 1
        estadisticas[local]["PP"] += 1

    else:

        estadisticas[local]["PE"] += 1
        estadisticas[visitante]["PE"] += 1

for equipo in estadisticas:

    estadisticas[equipo]["PTS"] = (
        estadisticas[equipo]["PG"] * 3
        + estadisticas[equipo]["PE"]
    )    

ranking = sorted(
    estadisticas.items(),
    key=lambda x: x[1]["GF"],
    reverse=True
)

for equipo in estadisticas:

    gf = estadisticas[equipo]["GF"]
    gc = estadisticas[equipo]["GC"]

    estadisticas[equipo]["DG"] = gf - gc

ranking_df = pd.DataFrame(
ranking,
columns=["Equipo", "Goles"]
)


tabla_goles = pd.DataFrame.from_dict(
    estadisticas,
    orient="index"
)

tabla_goles = tabla_goles.reset_index()

tabla_goles = tabla_goles.rename(
    columns={"index": "Equipo"}
)

tabla_goles = tabla_goles.sort_values(
    by=["PTS", "DG", "GF"],
    ascending=False
)
tabla_goles = tabla_goles.reset_index(drop=True)

tabla_goles.index += 1

tabla_goles.index.name = "Pos"

tabla_goles["Ronda"] = "Desconocida"

tabla_goles.loc[tabla_goles["PJ"] == 3, "Ronda"] = "Fase de Grupos"

tabla_goles.loc[tabla_goles["PJ"] == 4, "Ronda"] = "Octavos"

tabla_goles.loc[tabla_goles["PJ"] == 5, "Ronda"] = "Cuartos"

tabla_goles.loc[tabla_goles["PJ"] == 7, "Ronda"] = "Semifinales+"



print("\nClasificación Final - Mas puntos - Qatar 2022\n")

print(tabla_goles)

tabla_goles.to_csv(
    "tabla_estadisticas.csv",
    index=False,
    encoding="utf-8-sig"
)

tabla_goles["PPG"] = round(
    tabla_goles["PTS"] / tabla_goles["PJ"],
    2
)

tabla_goles.to_csv(
    "ranking_ataque.csv",
    index=False,
    encoding="utf-8-sig"
)

ranking_defensa = tabla_goles.sort_values(
    by="GC"
)

ranking_defensa.to_csv(
    "ranking_defensa.csv",
    index=False,
    encoding="utf-8-sig"
)

ranking_ataque = tabla_goles.sort_values(
    by="GF",
    ascending=False
)

ranking_ataque.to_csv(
    "ranking_ataque.csv",
    index=False,
    encoding="utf-8-sig"
)

top10_puntos = tabla_goles.head(10)

def crear_grafico(df, columna, titulo, archivo):

    top10 = df.sort_values(
        by=columna,
        ascending=False
    ).head(10)

    plt.figure(figsize=(10, 6))

    plt.barh(
        top10["Equipo"],
        top10[columna]
    )

    plt.title(titulo)

    plt.xlabel(columna)

    plt.tight_layout()

    plt.savefig(archivo)

    plt.close()

graficos = [

    ("PTS", "Top 10 Teams by Points", "top10_puntos.png"),

    ("GF", "Top 10 Teams by Goals", "top10_goles.png"),

    ("DG", "Top 10 Teams by Goal Difference", "top10_dg.png")

]

for columna, titulo, archivo in graficos:

    crear_grafico(
        tabla_goles,
        columna,
        titulo,
        archivo

    )
