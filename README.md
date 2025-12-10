[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17836768.svg)](https://doi.org/10.5281/zenodo.17836768)

# Voynich Unlock 🔑

Voynich Unlock apresenta o **Método SEIS/OITO**: uma leitura numérica e estruturada do manuscrito. Onde muitos viram mistério insolúvel, mostramos um caminho claro e consistente — uma chave que começa a destravar o enigma.

## 📌 Objetivo
- Demonstrar que o Voynich pode ser lido como sequência numérica (1–10).
- Explicar a diversidade gráfica via **CT + marcadores** (H, P, K, F, Z/Q).
- Produzir corpus paralelo (Original / Numérico / PT / EN).

## 📂 Estrutura
- `docs/` → documentação detalhada (método, fluxo de trabalho, dicionário).
- `src/` → código Python para aplicar o método e exportar corpus paralelo.
- `tests/` → testes unitários.
- `corpus/` → arquivos TSV com fólios convertidos.

## 🚀 Como usar
1. Clone o repositório:
   git clone https://github.com/seuusuario/voynich-unlock.git
   cd voynich-unlock

2. Execute o script principal:
   python src/seis_oito.py

3. Os resultados estarão em `src/corpus/` como arquivos TSV.

## 📖 Método
- **SEIS/OITO:** primeira e quarta letra iguais; segunda e terceira diferentes, mas com “i” em comum.
- **CT + marcador:** variantes gráficas reclassificadas como núcleo 4 (quatre) + índice (H, P, K, F, Z/Q).


## Próximos passos

Uma proposta de validação futura do método é aplicar a mesma lógica de reclassificação e leitura em colunas a textos medievais em occitano que
contenham números por extenso. A ideia é "cifrar" esses manuscritosm conhecidos e verificar se a saída gerada apresenta padrões estatísticos
semelhantes ao Voynich. 

Esse processo de engenharia reversa permitiria comparar distribuições de tokens, entropias e matrizes de transição, fortalecendo a hipótese de que
o método SEIS/OITO reproduz características estruturais do manuscrito.
A execução dessa etapa depende da disponibilidade de corpus transcrito em occitano, e pode ser desenvolvida por colaboradores futuros.


## 📜 Licença
MIT License.
