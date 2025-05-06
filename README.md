
Dashboard de Análise de Satisfação de IPhones

Análise de Sentimento de Avaliações - iPhone (Amazon)

Descrição do Projeto

Este projeto realiza a análise de sentimentos de avaliações de produtos da Amazon, com foco em modelos de iPhone. As etapas incluem o pré-processamento de texto em Python, classificação de sentimentos com o modelo VADER e extração de palavras-chave. O resultado é um arquivo `.csv` tratado, utilizado em dashboards interativos no Power BI para explorar os níveis de satisfação dos usuários.

---

Dados

- Fonte: Kaggle – Dataset de avaliações de produtos (NLP)
- Formato: `.csv`
- Pré-processamento: Python + NLP
- Tratamento de dados no BI: Linguagem M (Power Query)
- Criação de medidas: Linguagem DAX no Power BI

---

Objetivos do Projeto

- ✅ Pré-processar os textos das avaliações (título + descrição)
- ✅ Classificar os sentimentos como positivo, negativo ou neutro com VADER
- ✅ Extrair palavras-chave relevantes de cada avaliação
- ✅ Gerar uma base final em .csv pronta para visualizações no Power BI
- ✅ Criar um dashboard interativo que facilite a leitura dos dados
---

Funcionalidades do Dashboard

- Análise Geral de Satisfação: Visão abrangente da satisfação dos produtos iPhones.
- Detalhamento por Categoria:
  - Média de notas por país
  - Volume de avaliações por ano
  - Modelos mais e menos avaliados
  - Distribuição por sentimentos
  - Palavras mais recorrentes nas avaliações
- Comparação de Resultados: Gráficos comparativos, filtros interativos e botões de navegação entre páginas.


---

Tecnologias Utilizadas

- 🐍 Python (pré-processamento, limpeza e análise de sentimento)
- 📊 Power BI (para visualização interativa dos resultados e dashboard)
- 📄 Linguagem M (tratamento de dados no Power Query)
- 📌 DAX (criação de medidas para análise dinâmica)
- 📁 Arquivos CSV (formato intermediário dos dados para importação no BI)

Estrutura do Repositório

```plaintext
ANALISE_AMAZON/
├── analise_sentimento.py          # Script principal de análise de sentimentos
├── analise_sentimento.csv         # Arquivo final com os dados analisados
├── iphone.csv                     # Dataset original com as avaliações
├── Descricao-codigo.py            # Explicação do funcionamento do script Python
├── Medidas.dax                    # Medidas DAX utilizadas no Power BI
├── README.md                      # Explicação geral do projeto
└── requirements.txt               # Bibliotecas necessárias para rodar o script
