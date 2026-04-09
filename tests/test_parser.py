from src.parser import parse_mes_es

def test_parse_mes():
    assert str(parse_mes_es("Enero 2022")) == "2022-01-01"