import re
import json
import nltk
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
import emoji

# Descargar recursos necesarios de NLTK
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('punkt_tab')

# Función para preprocesar el texto
def preprocesar_texto(texto):
    texto = texto.lower()  # Convertir a minúsculas
    texto = re.sub(r"http\S+|www\S+", "", texto)  # Quitar URLs
    texto = emoji.demojize(texto)  # Convertir emojis a texto
    return texto.strip()

# Función para cargar palabras personalizadas desde un archivo JSON
def cargar_palabras_personalizadas(archivo):
    with open(archivo, 'r') as file:
        return json.load(file)

# Función para analizar sentimientos por frases
def analizar_por_frases(texto, sia):
    frases = sent_tokenize(texto)
    puntajes_por_frase = []
    puntajes_globales = {"pos": 0, "neg": 0, "neu": 0, "compound": 0}

    for frase in frases:
        puntajes = sia.polarity_scores(frase)
        puntajes_por_frase.append({"frase": frase, "puntajes": puntajes})
        for key in puntajes:
            puntajes_globales[key] += puntajes[key]

    # Promedio de puntajes
    n = len(frases)
    puntajes_promedio = {key: value / n for key, value in puntajes_globales.items()}

    # Sentimiento global
    sentimiento_global = "Neutral"
    if puntajes_promedio['compound'] > 0.1:  # Ajuste de umbral para ser más permisivo
        sentimiento_global = "Positivo"
    elif puntajes_promedio['compound'] < -0.1:
        sentimiento_global = "Negativo"

    return sentimiento_global, puntajes_promedio, puntajes_por_frase

# Función para graficar los resultados
def graficar_puntajes(puntajes):
    etiquetas = ["Positivo", "Negativo", "Neutral"]
    valores = [puntajes['pos'], puntajes['neg'], puntajes['neu']]
    plt.bar(etiquetas, valores, color=["green", "red", "gray"])
    plt.title("Análisis de Sentimientos")
    plt.ylabel("Proporción")
    plt.show()

# Programa principal
def main():
    # Inicializar el analizador de sentimientos
    sia = SentimentIntensityAnalyzer()

    # Ampliar el lexicón con un vocabulario personalizado
    palabras_personalizadas = cargar_palabras_personalizadas('C:\prueba\lexicon.json')
    sia.lexicon.update(palabras_personalizadas)

    print("Bienvenido al Analizador de Sentimientos Mejorado")
    texto_usuario = input("Ingrese un texto para analizar: ")

    # Preprocesar el texto
    texto_procesado = preprocesar_texto(texto_usuario)

    # Analizar sentimientos
    sentimiento_global, puntajes_globales, puntajes_por_frase = analizar_por_frases(texto_procesado, sia)

    # Mostrar resultados globales
    print(f"\nSentimiento global: {sentimiento_global}")
    print("Detalles del análisis global:")
    print(f" - Positivo: {puntajes_globales['pos']:.2f}")
    print(f" - Negativo: {puntajes_globales['neg']:.2f}")
    print(f" - Neutral: {puntajes_globales['neu']:.2f}")
    print(f" - Compound (global): {puntajes_globales['compound']:.2f}")

    # Mostrar análisis por frases
    print("\nAnálisis por frases:")
    for item in puntajes_por_frase:
        print(f"Frase: {item['frase']}")
        print(f"  - Positivo: {item['puntajes']['pos']:.2f}")
        print(f"  - Negativo: {item['puntajes']['neg']:.2f}")
        print(f"  - Neutral: {item['puntajes']['neu']:.2f}")
        print(f"  - Compound: {item['puntajes']['compound']:.2f}")

    # Graficar resultados globales
    graficar_puntajes(puntajes_globales)


main()
