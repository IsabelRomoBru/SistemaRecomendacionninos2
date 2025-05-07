from sentence_transformers import SentenceTransformer

def cargar_modelo():
    return SentenceTransformer("distiluse-base-multilingual-cased-v1")  # más liviano

modelo_nlp = cargar_modelo()
