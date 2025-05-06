
Análise de Sentimentos em Avaliações de iPhones (Amazon)

Este script realiza o processamento de dados e análise de sentimentos de avaliações de iPhones, com o objetivo de gerar um arquivo .csv preparado para visualizações em ferramentas como Power BI.

Objetivos:
- Unir título e descrição das avaliações.
- Realizar limpeza textual.
- Classificar sentimentos com VADER (positivo, negativo, neutro).
- Extrair palavras-chave relevantes.
- Exportar um dataset final com colunas específicas.

Habilidades Demonstradas:
- Processamento de Linguagem Natural com NLTK
- Classificação de sentimentos com VADER
- Limpeza e manipulação com pandas
- Exportação para .csv

Bibliotecas utilizadas:
pip install pandas nltk vaderSentiment
"""

1. Importação de bibliotecas
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

2. Baixar recursos do nltk
nltk.download('punkt')
nltk.download('stopwords')

3. Preparar stopwords e VADER
stop_words = set(stopwords.words('english'))
analyzer = SentimentIntensityAnalyzer()

4. Carregar CSV de avaliações
df = pd.read_csv("iphone.csv")

5. Criar coluna texto_completo ===
df['texto_completo'] = df['reviewTitle'].fillna('') + ' ' + df['reviewDescription'].fillna('')

6. Limpar o texto (remover pontuação e minúsculas)
def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto

df['texto_limpo'] = df['texto_completo'].apply(limpar_texto)

7. Classificar sentimento com VADER
def classificar_sentimento(texto):
    score = analyzer.polarity_scores(texto)['compound']
    if score >= 0.05:
        return 'positivo'
    elif score <= -0.05:
        return 'negativo'
    else:
        return 'neutro'

df['sentimento'] = df['texto_limpo'].apply(classificar_sentimento)

8. Extrair palavras-chave (sem stopwords)
def extrair_palavras_chave(texto):
    tokens = word_tokenize(texto)
    palavras = [palavra for palavra in tokens if palavra not in stop_words and palavra.isalpha()]
    return ', '.join(palavras)

df['palavra_chave'] = df['texto_limpo'].apply(extrair_palavras_chave)

9. Exportar colunas relevantes para novo CSV
colunas_finais = ['date', 'ratingScore', 'reviewTitle', 'reviewDescription',
                  'texto_completo', 'texto_limpo', 'sentimento',
                  'palavra_chave', 'variant', 'country']

df[colunas_finais].to_csv("analise_sentimento.csv", index=False)

print("✅ Arquivo exportado com sucesso: analise_sentimento.csv")
