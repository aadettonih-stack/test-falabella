import base64
import io
import pandas as pd
import functions_framework

from parser import parse_mes_es
from bq_loader import load_dataframe

@functions_framework.cloud_event
def hello_pubsub(cloud_event):

    csv_bytes = base64.b64decode(
        cloud_event.data["message"]["data"]
    )

    df = pd.read_csv(
        io.BytesIO(csv_bytes),
        encoding="utf-8-sig"
    )

    df.columns = df.columns.str.strip().str.lower()

    df["mes"] = df["mes"].apply(parse_mes_es)
    df["ventas_mensuales"] = df["ventas_mensuales"].astype(int)
    df["fecha_ejecucion"] = pd.Timestamp.now(tz="America/Santiago")

    load_dataframe(df)