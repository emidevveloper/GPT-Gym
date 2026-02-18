"""
/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */
"""
import requests
from PIL import Image
from math import gcd
from io import BytesIO

def get_aspect_ratio(url:str):
    peticion = requests.get(url, headers={"user-agent": "Mozilla./5.0"}).content

    archivo_virtual = BytesIO(peticion)
    imagen = Image.open(archivo_virtual)
    ancho, alto = imagen.size
    division = gcd(ancho, alto)

    return f"El aspect ratio de la imagen de {url} es {ancho // division, alto // division}"

print(get_aspect_ratio("https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"))

# Ejercicio terminado