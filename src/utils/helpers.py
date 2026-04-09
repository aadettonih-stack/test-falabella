def normalize_columns(df):
    """Limpia nombres de columnas de forma técnica."""
    df.columns = df.columns.str.strip().str.lower()
    return df