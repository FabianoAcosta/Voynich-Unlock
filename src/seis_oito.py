from reclassificacao import map_token_to_number, classify_ct_marker
from export_tsv import build_parallel_corpus, export_tsv

def main():
    # Exemplo mínimo: processar uma lista de tokens
    tokens = ["dain", "daiin", "qokain", "shor", "cthor", "edy"]
    parallel = build_parallel_corpus(tokens)
    export_tsv(parallel, "corpus/lote_demo.tsv")

if __name__ == "__main__":
    main()
