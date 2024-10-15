# Comunidad de Madrid Municipal Leagues API

## Description

This API provides up-to-date information about matches in Madrid's municipal leagues. It allows users to query data for a specific team, including their past and upcoming matches.

## Data Source

The data is obtained from [datos.madrid.es](https://datos.madrid.es/portal/site/egob), the open data portal of the Madrid City Council.

## Endpoint

### GET /{team}

Returns match data for the specified team.

- **URL**: `/{team}`
- **Method**: GET
- **URL Parameters**:
  - `team`: Name of the team (required)

#### Successful Response

- **Code**: 200 OK
- **Content**: A JSON array with the team's matches, chronologically ordered (future matches first, followed by past matches).

#### Usage Example

GET /YOUR_TEAM_NAME

#### Response Example

```json
[
  {
    "Codigo_temporada": 2024,
    "Codigo_competicion": 8892,
    "Codigo_fase": 9790,
    "Codigo_grupo": 26060,
    "Jornada": 1,
    "Partido": 5,
    "Codigo_equipo1": 158811,
    "Codigo_equipo2": 158814,
    "Resultado1": 0,
    "Resultado2": 0,
    "Codigo_campo": 996,
    "Fecha": "2024-10-19T00:00:00.000",
    "Hora": "19:40",
    "Programado": 1,
    "Estado": "R",
    "Nombre_temporada": "2024/2025",
    "Nombre_competicion": "45 JUEGOS DEPORTIVOS MUNICIPALES",
    "Nombre_fase": "FASE GRUPO 45 JDM",
    "Nombre_grupo": "JDM MOR SAB TAR F7 SEN MAS G2",
    "Nombre_deporte": "FUTBOL 7",
    "Nombre_categoria": "SENIOR MASCULINO",
    "Nombre_jornada": 1,
    "Equipo_local": "RIVAL_TEAM_NAME",
    "Equipo_visitante": "YOUR_TEAM_NAME",
    "Campo": "Campo 2 Moratalaz",
    "Sexo_grupo": "M",
    "Distrito": "MORATALAZ",
    "Observaciones": " ",
    "SISTEMA_COMPETICION": "LIGA",
    "COORD_X_CAMPO": -3.631419,
    "COORD_Y_CAMPO": 40.398358,
    "Color_Camiseta_1": "Negro",
    "Color_Camiseta_2": "Azul claro"
  },
  {
    "..."
  },
]
```

## Installation and Execution

### 1. Clone this repository:
```
git clone https://github.com/hugo-cordoba/liga-API.git
```

```
cd liga-API
```

### 2. Create and activate a virtual environment:
- On Windows:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install dependencies:
```
pip install -r requirements.txt
```

### 4. Run the application:
```
uvicorn main:app --reload
```

The API will be available at http://localhost:8000.


## Contributions
Contributions are welcome. Please open an issue to discuss proposed changes before creating a pull request :).

## Dev Team
github: https://github.com/hugo-cordoba

linkedin: https://www.linkedin.com/in/hugocordobaleal/
