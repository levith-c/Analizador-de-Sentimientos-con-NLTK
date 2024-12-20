# Nombre del Proyecto: Analizador de Sentimientos Mejorado con NLTK

# Objetivo:
Este proyecto tiene como objetivo analizar el sentimiento de un texto ingresado por el usuario y clasificarlo en tres categorías: positivo, negativo o neutral. El análisis se realiza utilizando la biblioteca NLTK (Natural Language Toolkit) para procesar el texto y el analizador de sentimientos de VADER (Valence Aware Dictionary and sEntiment Reasoner). Para mejorar la precisión, el proyecto también permite la personalización del análisis mediante un vocabulario adicional.

# Características principales:
- Análisis de Sentimiento por Frase: El texto se divide en frases individuales y se evalúa el sentimiento de cada una.
- Clasificación Global: El proyecto calcula un puntaje global promedio del sentimiento del texto completo.
- Personalización del Vocabulario: Permite la integración de un archivo JSON con un vocabulario personalizado para mejorar la precisión del análisis.
- Visualización Gráfica: Utiliza matplotlib para generar un gráfico de barras que muestra la proporción de sentimientos positivo, negativo y neutral en el texto.
- Preprocesamiento de Texto: El texto ingresado es preprocesado para eliminar URLs, emojis, asegurando que el análisis sea más preciso.

# Tecnologías utilizadas:
- Python 3.10
- NLTK (Natural Language Toolkit)
- matplotlib (para la visualización de resultados)
- JSON (para vocabulario personalizado)
- regex (para la limpieza del texto)
