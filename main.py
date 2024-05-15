import requests as rq
import json
from bs4 import BeautifulSoup

url = 'https://www.meteored.com.ar/tiempo-en_Formosa-America+Sur-Argentina-Formosa-SARF-1-16900.html'

# funcion para obtener las etiquetas <a> de la url proporcionada
def crawler(url):
    request = rq.get(url)# Hace la request con el metodo get a la url
    
    contents = request.text # Guarda en las variable contents el contenido html de la pagina con el .text y se guarda como string
    soup = BeautifulSoup(contents, features='html.parser') # Parsea el contenido con un estilo html pero de BeautifulSoup y lo guardo en la variable soup
    links = soup.find_all('a') # Con el metodo find_all encuentra todas las etiquetas <a> y los guarda en la variable links

    return links


# Funcion para obtener todas las etiquetas <h1> y <p> de cada url proporcionada 
def get_p_and_h1(url):
    # Misma logica que la function crawler
    request = rq.get(url)
    
    contents = request.text

    soup = BeautifulSoup(contents, features='html.parser')

    # Guarda en la variable h1_and_p todas las coincidencias que se encuentren en la url de las etitquetas <h1> y <p>
    h1_and_p = soup.find_all(['h1', 'p'])

    # La variable de arriba tiene objetos "Tag" que son propios de BeautifulSoup, para poder pasarlos a Json luego, necesito pasarlos todos a strings
    return [str(tag) for tag in h1_and_p] # Transforma a string cada tag o registro de h1_and_p y devuelve como array


links = crawler(url) # Guarda los valores que me retorna la funtion crawler en la variable links

# Defino un dict para poder trabajar posteriormente y transformarlo en Json
cosas = {}

# Por cada link que haya en la variable links
for link in links:
    # En caso de algun error ignora ese link y continua con el siguiente
    try:
        cosas.update({link['href']: get_p_and_h1(link['href'])}) # Agrega al dict definido anteriormente, como clave el link pero solamente el href de este, y como clave utilizo la function get_p_and_h1 y utilizo nuevamente el mismo href del <a>
        print(f'se guardo con exito {link['href']}')
    except KeyError:
        continue
print('Se guardaron todos los links correctamente')


# Guarda el diccionario en un archivo Json
with open('resultados.json', 'w') as f:
    json.dump(cosas, f)
