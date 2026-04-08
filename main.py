import base64
import functions_framework
import csv
import io
from datetime import date, datetime, timezone
import json
import pandas as pd

from google.cloud import bigquery

bq_client = bigquery.Client()

TABLE_ID = "test-falabella-ipg.falabellaplatform.ventas_2"
def parse_mes_es(mes_str: str) -> date:
    meses = {
        "enero": 1,
        "febrero": 2,
        "marzo": 3,
        "abril": 4,
        "mayo": 5,
        "junio": 6,
        "julio": 7,
        "agosto": 8,
        "septiembre": 9,
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12
    }

    nombre_mes, anio = mes_str.lower().split()

    return date(int(anio), meses[nombre_mes], 1)

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def hello_pubsub(cloud_event):

    
    csv_bytes = base64.b64decode(cloud_event.data["message"]["data"])
    
    df = pd.read_csv(
        io.BytesIO(csv_bytes),
        encoding="utf-8-sig"   # elimina BOM automáticamente
    )
    
    # normalizar nombres columnas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )
    
    # convertir mes
    df["mes"] = df["mes"].apply(lambda x: parse_mes_es(x).isoformat())
    
    # tipos
    df["ventas_mensuales"] = df["ventas_mensuales"].astype(int)
    df["execution_ts"] = pd.Timestamp.now(tz="America/Santiago")
    rows = df.to_dict(orient="records")
    
    errors = bq_client.insert_rows_json(TABLE_ID, rows)
    
    if errors:
        print(errors)

if __name__ == "__main__":
    port = 8080
    app.run(host="0.0.0.0", port=port)
