import os
from google.cloud import bigquery

# --- CONFIGURACIÓN DE VARIABLES DE ENTORNO ---
# Se recomienda usar os.environ para no dejar IDs sensibles escritos en el código (Hardcoded).
# Estas variables se configuran en el panel de Cloud Run o en tu terminal.
PROJECT = os.environ["PROJECT_ID"]  # ID de tu proyecto en Google Clouda
DATASET = os.environ["DATASET"]    # Nombre del Dataset en BigQuery (ej: 'ventas_ds')
TABLE = os.environ["TABLE"]        # Nombre de la Tabla (ej: 'ventas_procesadas')

# Construimos el ID completo de la tabla con el formato: proyecto.dataset.tabla
TABLE_ID = f"{PROJECT}.{DATASET}.{TABLE}"

# --- INICIALIZACIÓN DEL CLIENTE ---
# Al no pasarle parámetros, el cliente busca automáticamente las credenciales
# de la cuenta de servicio (Service Account) en el entorno de GCP.
client = bigquery.Client()

def load_dataframe(df):
    """
    Función que recibe un DataFrame de Pandas y lo carga en BigQuery.
    """
    # .load_table_from_dataframe: Envía el bloque de datos completo a la tabla especificada.
    # .result(): Es una llamada síncrona que bloquea el script hasta que la carga 
    # termine o falle (espera a que el "Job" de BigQuery finalice).
    client.load_table_from_dataframe(df, TABLE_ID).result()