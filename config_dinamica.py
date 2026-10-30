import json
from pathlib import Path

RUTA_CONFIG = Path(__file__).resolve().parent / "config_dinamica.json"

def obtener_id_purgatorio():
    with RUTA_CONFIG.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    return int(datos["ID_CANAL_PURGATORIO"])
