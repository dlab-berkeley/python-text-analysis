import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gensim
import gensim.downloader as api
from gensim.models import KeyedVectors

wv = KeyedVectors.load_word2vec_format('../data/GoogleNews-vectors-negative300.bin', binary=True)
# Si aún no tienes 'wv' cargado, descomenta estas líneas para usar un modelo público:
# import gensim.downloader as api
# wv = api.load("glove-wiki-gigaword-100")  # o "word2vec-google-news-300"

coffee_nouns = [
    ('coffee', 'espresso'),
    ('coffee', 'cappuccino'),
    ('coffee', 'latte'),
    ('coffee', 'americano'),
    ('coffee', 'irish'),
]

results = []

for w1, w2 in coffee_nouns:
    # Compatibilidad con Gensim 4.x:
    in_vocab = getattr(wv, "key_to_index", None)
    has_w1 = (w1 in wv.key_to_index) if in_vocab is not None else (w1 in wv)
    has_w2 = (w2 in wv.key_to_index) if in_vocab is not None else (w2 in wv)

    if not (has_w1 and has_w2):
        print(f"⚠️ OOV (fuera de vocabulario): {w1 if not has_w1 else ''} {w2 if not has_w2 else ''}".strip())
        continue

    similarity = float(wv.similarity(w1, w2))
    results.append((w1, w2, similarity))
    print(f"{w1:>7s} ↔ {w2:<11s}: {similarity:.4f}")

# Mostrar el más y el menos similar
if results:
    most_similar = max(results, key=lambda t: t[2])
    least_similar = min(results, key=lambda t: t[2])
    print("\n🏆 Más similar a 'coffee':", most_similar[1], f"({most_similar[2]:.4f})")
    print("🥄 Menos similar a 'coffee':", least_similar[1], f"({least_similar[2]:.4f})")
else:
    print("No se pudieron calcular similitudes (todas las palabras OOV).")