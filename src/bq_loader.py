import os
from google.cloud import bigquery

PROJECT = os.environ["PROJECT_ID"]
DATASET = os.environ["DATASET"]
TABLE = os.environ["TABLE"]

TABLE_ID = f"{PROJECT}.{DATASET}.{TABLE}"

client = bigquery.Client()

def load_dataframe(df):
    client.load_table_from_dataframe(df, TABLE_ID).result()