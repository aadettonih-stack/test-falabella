def normalize_columns(df):
    """
    Estandariza los nombres de las columnas de un DataFrame de Pandas.
    
    Esta función es crítica para asegurar que los encabezados del CSV 
    coincidan con el esquema de BigQuery, eliminando errores por 
    espacios accidentales o diferencias de mayúsculas.
    """
    
    # Se accede al índice de columnas del DataFrame y se aplican 
    # transformaciones de strings vectorizadas:
    df.columns = (
        df.columns
        .str.strip()  # Elimina espacios en blanco al inicio y al final (ej: " producto " -> "producto")
        .str.lower()  # Convierte todo a minúsculas (ej: "PRODUCTO" -> "producto")
    )
    
    # Retorna el DataFrame con los nombres de las columnas ya saneados
    return df