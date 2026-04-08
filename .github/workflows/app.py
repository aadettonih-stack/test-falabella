import base64
import functions_framework
import csv
import io
from datetime import date
import json

from google.cloud import bigquery

bq_client = bigquery.Client()

TABLE_ID = "test-falabella-ipg.falabellaplatform.ventas"
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
    # Print out the data from Pub/Sub, to prove that it worked
    csv_bytes= base64.b64decode(cloud_event.data["message"]["data"])
    csv_text = csv_bytes.decode("utf-8")

    # Leer CSV completo
    reader = csv.DictReader(io.StringIO(csv_text))

    rows = []

    for row in reader:
        rows.append({
            "producto": row["producto"],
            "region": row["region"],
            "mes": parse_mes_es(row["mes"]).isoformat(),
            "ventas_mensuales": int(row["ventas_mensuales"])
        })
    print (rows)
    # Insertar en BigQuery
    errors = bq_client.insert_rows_json(TABLE_ID, rows)

    if errors:
        print("BigQuery errors:", errors)
        return ("Error", 500)

    return ("OK", 200)

if __name__ == "__main__":
    port = 8080
    app.run(host="0.0.0.0", port=port)
