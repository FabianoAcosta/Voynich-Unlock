import csv
from reclassificacao import map_token_to_number, classify_ct_marker

def build_parallel_corpus(tokens):
    """
    Constrói corpus paralelo com Original / Número / Marcador.
    """
    result = []
    for t in tokens:
        num = map_token_to_number(t)
        marker = classify_ct_marker(t)
        result.append({
            "original": t,
            "numero": num if num is not None else "",
            "marcador": marker[1] if marker else "",
        })
    return result

def export_tsv(rows, path):
    """
    Exporta corpus paralelo em formato TSV.
    """
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["original","numero","marcador"], delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
