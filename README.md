# Web Scraper en Python

Este proyecto es un web scraper implementado en Python que recorre un sitio web, extrae todas las etiquetas `<a>` con sus respectivos enlaces y accede a cada página enlazada. Por cada enlace encontrado, obtiene todas las etiquetas `<h1>` y `<p>` y las almacena en un array en un archivo JSON. Si no se encuentran dichos elementos, guarda el array como vacío.

## Requisitos

- Python 3
- BeautifulSoup
- requests

## Uso

1. Clona el repositorio.
   `git clone https://github.com/MeyerHector/TLP-PY-Crawler`

2. Instala las dependencias
   `pip install beautifulsoup4 requests`.
3. Ejecuta el script
   `python main.py`

## Resultados

Los resultados se guardan en un archivo `resultados.json`, donde cada clave es un enlace encontrado y cada valor es un array de las etiquetas `<h1>` y `<p>` encontradas en esa página.
