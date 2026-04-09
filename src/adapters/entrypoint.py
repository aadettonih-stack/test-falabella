import base64
import io
import pandas as pd
from src.domain.logic import process_sales_record
from src.domain.parser import parse_mes_es
from src.adapters.bq_adapter import save_to_bigquery

def cloud_handler(cloud_event):
    """
    EntryPoint: Es el 'puerto' que recibe el evento de la nube.
    Traduce el evento de Pub/Sub a un formato que el dominio entiende (DataFrame).
    """
    # 1. Traducir entrada (Base64 a CSV/DataFrame)
    data_payload = base64.b64decode(cloud_event.data["message"]["data"])
    df_input = pd.read_csv(io.BytesIO(data_payload), encoding="utf-8-sig")

    # 2. Invocar lógica de negocio
    df_processed = process_sales_record(df_input, parse_mes_es)

    # 3. Invocar salida
    save_to_bigquery(df_processed)
    
    return "OK"