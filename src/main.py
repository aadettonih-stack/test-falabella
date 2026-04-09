import base64
import io
import pandas as pd
import functions_framework

# Importación de módulos personalizados (Arquitectura Hexagonal/Modular)
from parser import parse_mes_es
from bq_loader import load_dataframe

@functions_framework.cloud_event
def main(cloud_event):

    # 1. DECODIFICACIÓN: Los mensajes de Pub/Sub viajan en Base64.
    # Extraemos el contenido del evento y lo convertimos a bytes legibles.
    csv_bytes = base64.b64decode(
        cloud_event.data["message"]["data"]
    )

    # 2. LECTURA: Convertimos los bytes en un objeto similar a un archivo (BytesIO)
    # para que Pandas pueda leerlo como un DataFrame. 'utf-8-sig' quita el BOM de Excel.
    df = pd.read_csv(
        io.BytesIO(csv_bytes),
        encoding="utf-8-sig"
    )

    # 3. NORMALIZACIÓN DE COLUMNAS: Limpia espacios en blanco en los nombres de 
    # las columnas y las pasa a minúsculas (ej: ' Producto ' -> 'producto').
    df.columns = df.columns.str.strip().str.lower()

    # 4. TRANSFORMACIÓN DE DATOS (Punto 9 de la prueba):
    # - Aplica la lógica de parseo para convertir nombres de meses en fechas.
    df["mes"] = df["mes"].apply(parse_mes_es)
    
    # - Asegura que el monto de ventas sea un número entero (Validación de tipos).
    df["ventas_mensuales"] = df["ventas_mensuales"].astype(int)
    
    # - Agrega auditoría: Columna con la fecha y hora exacta del procesamiento.
    df["fecha_ejecucion"] = pd.Timestamp.now(tz="America/Santiago")

    # 5. CARGA: Llama a la función del adaptador de BigQuery para insertar el DataFrame.
    load_dataframe(df)