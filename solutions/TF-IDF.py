# Importaciones necesarias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

# 1. Cargar dataset (ajusta la ruta si tu CSV no está en data/tweets.csv)
tweets = pd.read_csv("tweets.csv")

# 2. Crear el vectorizador TF-IDF
vectorizer = TfidfVectorizer(lowercase=True,
                             stop_words='english',
                             min_df=2,
                             max_df=0.95)

# 3. Ajustar y transformar usando la columna 'text'
tf_dtm = vectorizer.fit_transform(tweets['text'].astype(str))

# 4. DataFrame de TF-IDF
tfidf = pd.DataFrame(tf_dtm.todense(),
                     columns=vectorizer.get_feature_names_out(),
                     index=tweets.index)

# ⚠️ Verifica que tengas la columna 'airline_sentiment'
if "airline_sentiment" not in tweets.columns:
    raise ValueError("❌ El dataset no contiene la columna 'airline_sentiment'")

# 5. Subconjuntos por sentimiento
positive_index = tweets[tweets['airline_sentiment'] == 'positive'].index
negative_index = tweets[tweets['airline_sentiment'] == 'negative'].index

# 6. Calcular medias TF-IDF y extraer top 10
pos = tfidf.loc[positive_index].mean().sort_values(ascending=False).head(10)
neg = tfidf.loc[negative_index].mean().sort_values(ascending=False).head(10)

# 7. Graficar resultados
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharex=True)

pos.sort_values().plot(kind='barh', ax=axes[0],
                       color='cornflowerblue',
                       title='Top 10 palabras (POSITIVE tweets)')

neg.sort_values().plot(kind='barh', ax=axes[1],
                       color='darksalmon',
                       title='Top 10 palabras (NEGATIVE tweets)')

plt.tight_layout()
plt.show()

