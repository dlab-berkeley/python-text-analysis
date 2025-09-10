from utils import placeholder
import re   # 👈 asegúrate de importarlo arriba

blankspace_pattern = r'\s+'
blankspace_repl = ' '

def preprocess(text):
    '''Create a preprocess pipeline that cleans the tweet data.'''

    # Paso 1: Convertir a minúsculas
    text = text.lower()

    # Paso 2: Reemplazar patrones con marcadores de posición
    # - URLs -> URL
    # - Dígitos -> DIGIT
    # - Hashtags -> HASHTAG
    # - Usuarios de Twitter -> USER
    text = placeholder(text)

    # Paso 3: Eliminar espacios en blanco adicionales
    text = re.sub(blankspace_pattern, blankspace_repl, text)
    text = text.strip()
    
    return text

# Prueba
example_tweet = "Check this out! https://huggingface.co #NLP @openai 2025"
print(preprocess(example_tweet))
