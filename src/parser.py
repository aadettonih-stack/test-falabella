from datetime import date

def parse_mes_es(mes_str: str) -> date:
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

    nombre_mes, anio = mes_str.lower().split()
    return date(int(anio), meses[nombre_mes], 1)