from datetime import date

def parse_mes_es(mes_str: str) -> date:
    """
    Convierte un string de formato 'Mes Año' (ej: 'Enero 2022') 
    en un objeto de tipo date de Python.
    """
    # 1. DICCIONARIO DE MAPEO: Relaciona el nombre del mes en español 
    # con su valor numérico correspondiente para la librería datetime.
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

    # 2. PROCESAMIENTO DE TEXTO:
    # .lower() asegura que no falle si viene como 'Enero' o 'ENERO'.
    # .split() divide el string en dos partes usando el espacio como separador.
    # Ejemplo: 'Enero 2022' -> ['enero', '2022']
    nombre_mes, anio = mes_str.lower().split()

    # 3. CONSTRUCCIÓN DE LA FECHA:
    # Retorna un objeto date(año, mes, día). 
    # Se utiliza el día 1 por defecto para representar el inicio del mes.
    return date(int(anio), meses[nombre_mes], 1)