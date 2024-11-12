import json
import pandas as pd

from datetime import date
from fastapi import FastAPI

app = FastAPI()

df = pd.read_csv("./data/partidos.csv", sep=";", encoding="latin1")
df["Fecha"] = pd.to_datetime(df["Fecha"])


@app.get("/partidos/{team}")
async def root(team: str) -> list[dict]:
    """
    Returns a dictionary with the data of the provided team from the municipal
    leagues of Madrid. Data source: https://datos.madrid.es/portal/site/egob

    :param team: name of the team for which we want to consult its data
    """

    date_today = date.today()

    team_data = df[
        (df["Equipo_local"] == team) | (df["Equipo_visitante"] == team)
    ]

    matches = pd.concat(
        [
            team_data[team_data["Fecha"].dt.date >= date_today].sort_values(
                "Fecha", ascending=True
            ),
            team_data[team_data["Fecha"].dt.date < date_today].sort_values(
                "Fecha", ascending=False
            ),
        ]
    )

    return json.loads(matches.to_json(orient="records", date_format="iso"))
