import pandas as pd
import nltk, spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

print("✔ Imports OK")

# Texto de prueba
texto = "Hola, este es un ejemplo para probar NLTK y spaCy."

# --- NLTK ---
tokens = word_tokenize(texto.lower())
stop_words = set(stopwords.words('spanish'))
filtrado = [t for t in tokens if t.isalpha() and t not in stop_words]
print("Tokens NLTK:", filtrado)

# --- spaCy ---
nlp = spacy.load("es_core_news_sm")
doc = nlp(texto)
print("Lemmas spaCy:", [t.lemma_ for t in doc if not t.is_stop and t.is_alpha])
