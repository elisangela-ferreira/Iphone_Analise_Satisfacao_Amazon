import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

Baixar recursos do nltk (apenas 1ª vez)
nltk.download('punkt')
nltk.download('stopwords')

Carregar stopwords em inglês
stop_words = set(stopwords.words('english'))

Analisador de sentimentos
analyzer = SentimentIntensityAnalyzer()

1. Carregar CSV ===
df = pd.read_csv("iphone.csv")

2. texto_completo ===
df['texto_completo'] = df['reviewTitle'].fillna('') + ' ' + df['reviewDescription'].fillna('')

3. texto_limpo ===
def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto

df['texto_limpo'] = df['texto_completo'].apply(limpar_texto)

4. sentimento (com VADER) ===
def classificar_sentimento(texto):
    score = analyzer.polarity_scores(texto)['compound']
    if score >= 0.05:
        return 'positivo'
    elif score <= -0.05:
        return 'negativo'
    else:
        return 'neutro'

df['sentimento'] = df['texto_limpo'].apply(classificar_sentimento)

5. palavra_chave ===
def extrair_palavras_chave(texto):
    tokens = word_tokenize(texto)
    palavras = [palavra for palavra in tokens if palavra not in stop_words and palavra.isalpha()]
    return ', '.join(palavras)

df['palavra_chave'] = df['texto_limpo'].apply(extrair_palavras_chave)

6. Exportar apenas as colunas desejadas ===
colunas_finais = ['date', 'ratingScore', 'reviewTitle', 'reviewDescription',
                  'texto_completo', 'texto_limpo', 'sentimento',
                  'palavra_chave', 'variant', 'country']

df[colunas_finais].to_csv("analise_sentimento.csv", index=False)

print("✅ Arquivo exportado com sucesso: analise_sentimento.csv")
