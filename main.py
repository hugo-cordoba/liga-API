import json
import pandas as pd

from datetime import date
from fastapi import FastAPI

app = FastAPI()


@app.get("/matches/{team}")
async def get_match(team: str) -> list[dict]:
    """
    Returns a dictionary with the team's match data provided team from
    the municipal leagues of Madrid.

    Data source: https://datos.madrid.es/portal/site/egob

    :param team: name of the team for which we want to consult its data
    """
    df = pd.read_csv("./data/matches.csv", sep=";", encoding="latin1")
    df["Fecha"] = pd.to_datetime(df["Fecha"])

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


@app.get("/position/{team}")
async def get_position(team: str) -> list[dict]:
    """
    Returns a dictionary with the team's position data provided team from
    the municipal leagues of Madrid.

    Data source: https://datos.madrid.es/portal/site/egob

    :param team: name of the team for which we want to consult its data
    """

    df = pd.read_csv("./data/position.csv", sep=";", encoding="latin1")

    team_code = df[(df["Nombre_equipo"] == team.upper())]["Codigo_grupo"]

    positions = df[df["Codigo_grupo"] == team_code.item()].sort_values(
        "Posicion", ascending=True
    )

    return json.loads(positions.to_json(orient="records", date_format="iso"))
