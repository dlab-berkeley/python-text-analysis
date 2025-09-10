#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
lemmatize_tweets.py
Programa para lematizar texto (tweets) con spaCy.
- Lee un CSV (columna 'text' o 'text_processed')
- Crea la columna 'text_lemmatized'
- Imprime un ejemplo y guarda el resultado si se indica --out

Uso:
  python lemmatize_tweets.py --in data/tweets.csv --col text_processed --lang en --out data/tweets_lemmatized.csv
  python lemmatize_tweets.py --text "Dogs are running fast!" --lang en
"""

import argparse
import sys
import pandas as pd

def load_spacy_model(lang: str):
    import spacy
    model_map = {
        "en": "en_core_web_sm",
        "es": "es_core_news_sm",
    }
    name = model_map.get(lang.lower())
    if not name:
        raise ValueError(f"Idioma no soportado: {lang}. Usa 'en' o 'es'.")

    try:
        nlp = spacy.load(name, disable=["parser", "ner"])
        return nlp
    except OSError:
        msg = (
            f"No se encontró el modelo '{name}'.\n"
            f"Instálalo con:\n"
            f"  python -m spacy download {name}\n"
        )
        raise RuntimeError(msg)

def lemmatize_text(text: str, nlp, drop_stopwords: bool = False, only_alpha: bool = False) -> str:
    """
    Lematiza el texto. Opcionalmente elimina stopwords y tokens no alfabéticos.
    """
    if not isinstance(text, str):
        text = "" if pd.isna(text) else str(text)

    doc = nlp(text)
    lemmas = []
    for tok in doc:
        if only_alpha and not tok.is_alpha:
            continue
        if drop_stopwords and tok.is_stop:
            continue
        # .lemma_ ya devuelve la forma base
        lemmas.append(tok.lemma_)
    return " ".join(lemmas)

def main():
    parser = argparse.ArgumentParser(description="Lematizar textos/tweets con spaCy.")
    parser.add_argument("--in", dest="in_path", type=str, help="Ruta CSV de entrada (opcional si usas --text)")
    parser.add_argument("--col", dest="col_name", type=str, default=None,
                        help="Nombre de la columna a procesar (por defecto intenta 'text_processed' y luego 'text').")
    parser.add_argument("--out", dest="out_path", type=str, default=None, help="Ruta CSV de salida (opcional).")
    parser.add_argument("--lang", dest="lang", type=str, default="en", choices=["en", "es"],
                        help="Idioma del modelo spaCy: en | es (por defecto: en).")
    parser.add_argument("--text", dest="single_text", type=str, default=None,
                        help="Texto único a lematizar (si no usas CSV).")
    parser.add_argument("--drop-stopwords", action="store_true", help="Eliminar stopwords durante lematización.")
    parser.add_argument("--only-alpha", action="store_true", help="Conservar solo tokens alfabéticos.")
    args = parser.parse_args()

    # Cargar modelo
    try:
        nlp = load_spacy_model(args.lang)
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    # Caso 1: texto único
    if args.single_text is not None:
        result = lemmatize_text(args.single_text, nlp, drop_stopwords=args.drop_stopwords, only_alpha=args.only_alpha)
        print(result)
        sys.exit(0)

    # Caso 2: CSV
    if not args.in_path:
        print("Error: debes proporcionar --in <ruta.csv> o --text \"...\"", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(args.in_path)

    # Resolver columna a procesar
    col = args.col_name
    if col is None:
        if "text_processed" in df.columns:
            col = "text_processed"
        elif "text" in df.columns:
            col = "text"
        else:
            print("No se encontró columna 'text_processed' ni 'text'. Usa --col para indicar la columna.", file=sys.stderr)
            sys.exit(1)

    if col not in df.columns:
        print(f"La columna '{col}' no existe en el CSV.", file=sys.stderr)
        sys.exit(1)

    # Lematizar toda la columna
    df["text_lemmatized"] = df[col].apply(
        lambda x: lemmatize_text(x, nlp, drop_stopwords=args.drop_stopwords, only_alpha=args.only_alpha)
    )

    # Mostrar ejemplo (fila 101 si existe)
    if len(df) > 101:
        print(df[col].iloc[101])
        print("=" * 50)
        print(df["text_lemmatized"].iloc[101])

    # Guardar si se indicó salida
    if args.out_path:
        df.to_csv(args.out_path, index=False)
        print(f"✅ Archivo guardado en: {args.out_path}")
    else:
        # Muestra las primeras filas como vista previa
        print(df[[col, "text_lemmatized"]].head())

if __name__ == "__main__":
    main()
