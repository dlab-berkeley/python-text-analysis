import nltk
from nltk.corpus import stopwords
from nltk.tokenize import ToktokTokenizer
toktok = ToktokTokenizer()

# Descargar recursos si no los tienes aún
nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords_nltk(text, stop_words):
    """
    Elimina stopwords usando NLTK.
    - text: texto en bruto (string)
    - stop_words: conjunto/lista de stopwords predefinidas
    """
    # Tokenización
    tokens = toktok.tokenize(text.lower())
    
    # Filtrar palabras que no están en stopwords y son alfabéticas
        
    return [t for t in tokens if t.isalpha() and t not in stop_words]

# Ejemplo de uso
stop_words_es = set(stopwords.words('spanish'))
print(remove_stopwords_nltk("Hola, este es un ejemplo de texto para probar NLTK.", stop_words_es))