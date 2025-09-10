import spacy

# Cargar modelo en español (instálalo con: python -m spacy download es_core_news_sm)
nlp = spacy.load("es_core_news_sm")

def remove_stopwords_spacy(text):
    """
    Elimina stopwords usando spaCy.
    - text: texto en bruto (string)
    """
    doc = nlp(text.lower())
    
    # Filtrar tokens que no sean stopwords y sean alfabéticos
    filtered = [token.text for token in doc if not token.is_stop and token.is_alpha]
    
    return filtered

# Ejemplo de uso
print(remove_stopwords_spacy("Hola, este es un ejemplo de texto para probar spaCy."))