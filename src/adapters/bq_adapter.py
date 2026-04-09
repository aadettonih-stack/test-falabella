import os
from google.cloud import bigquery

def save_to_bigquery(df):
    """
    Adaptador de salida: Conecta la lógica con el almacenamiento externo (BigQuery).
    """
    project = os.environ["PROJECT_ID"]
    dataset = os.environ["DATASET"]
    table = os.environ["TABLE"]
    table_id = f"{project}.{dataset}.{table}"

    client = bigquery.Client()
    # Carga el DataFrame al destino final
    client.load_table_from_dataframe(df, table_id).result()