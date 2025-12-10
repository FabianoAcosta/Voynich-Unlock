def is_seis_oito(token: str) -> bool:
    """
    Verifica se o token segue o padrão SEIS/OITO.
    """
    return token in {"dain", "daiin", "qokain", "qokar"}

def map_token_to_number(token: str) -> int | None:
    """
    Mapeia tokens voynichianos para números (1–10).
    """
    mapa = {
        "dain": 5,
        "daiin": 6,
        "shor": 7,
        "shol": 7,
        "shey": 7,
        "qokain": 8,
        "qokar": 8,
        "qotor": 8,
        "okol": 9,
        "qokol": 9,
        "dy": 10,
        "edy": 10,
        # CT + marcador → 4
        "cthor": 4,
        "cthy": 4,
        "cthol": 4,
    }
    return mapa.get(token)

def classify_ct_marker(token: str) -> tuple[int, str] | None:
    """
    Reclassifica tokens CT em núcleo + marcador.
    """
    markers = {
        "cthor": "H",
        "cthy": "Y",
        "cthol": "L",
    }
    if token in markers:
        return (4, markers[token])
    return None
