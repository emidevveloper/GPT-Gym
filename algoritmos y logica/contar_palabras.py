"""
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
"""
texto = """
Python es un lenguaje de programación. Es un lenguaje muy popular y versátil
para el desarrollo de software
"""

def contar_palabras(texto: str) -> int:
    texto_minusculas = texto.lower()
    texto_modificado = texto_minusculas.replace('.', "").replace(',', "")
    palabras = texto_modificado.split()

    frecuencia_palabras = {}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    return frecuencia_palabras

print(contar_palabras(texto))