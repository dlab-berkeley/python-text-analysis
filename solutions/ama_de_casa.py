import gensim
import gensim.downloader as api
from gensim.models import KeyedVectors
wv = KeyedVectors.load_word2vec_format('../data/GoogleNews-vectors-negative300.bin', binary=True)

# pares positivos (woman + target)
positive_pair = [
    ['woman', 'chairman'],
    ['woman', 'doctor'],
    ['woman', 'computer_programmer'],
]
negative_word = 'man'

# --- Comprobación de vocabulario ---
needed = {negative_word}
for p in positive_pair:
    needed.update(p)

oov = [w for w in needed if w not in wv.key_to_index]
if oov:
    print("⚠️ Palabras fuera de vocabulario:", oov)

# --- Analogías con protección ---
for example in positive_pair:
    try:
        result = wv.most_similar(positive=example, negative=[negative_word], topn=5)
        top_word, top_score = result[0]
        print(f"man is to {example[1]} as woman is to {top_word} (score={top_score:.4f})")
        # Si quieres ver alternativas y sus puntajes:
        # for w, s in result: print("   ", w, f"{s:.4f}")
    except KeyError as e:
        print(f"❌ OOV en {example}: {e}")