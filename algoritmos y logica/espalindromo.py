"""
/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */
"""

def es_palindromo(palabra: str) -> bool:
    palabra_limpia = palabra.lower().replace(" ", "")
    revertida = palabra_limpia[::-1]
    if palabra_limpia == revertida:
        return True
    else:
        return False

print(es_palindromo("Anita lava la tina"))

# Ejercicio de lógica sencillo