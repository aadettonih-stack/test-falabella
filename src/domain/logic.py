import pandas as pd
from src.utils.helpers import normalize_columns

def process_sales_record(df, date_parser_func):
    """
    Caso de Uso: Procesa el registro de ventas.
    Aquí se aplican las reglas de negocio sin saber de dónde vienen los datos.
    """
    # 1. Limpieza de estructura
    df = normalize_columns(df)
    
    # 2. Transformaciones específicas
    df["mes"] = df["mes"].apply(date_parser_func)
    df["ventas_mensuales"] = df["ventas_mensuales"].astype(int)
    
    # 3. Enriquecimiento (Audit)
    df["fecha_ejecucion"] = pd.Timestamp.now(tz="America/Santiago")
    
    return df