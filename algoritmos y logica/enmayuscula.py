"""
/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""

def to_upper(string:str) -> str:
    es_mayus = True
    modified_text = ""
    for char in string:
        if char == " ":  # ¿Es un espacio?
            modified_text += char
            es_mayus = True  # ¡Prendemos el interruptor para la siguiente palabra!

        elif es_mayus == True:  # ¿Debo poner mayúscula?
            if char in mapeo_letras:
                modified_text += mapeo_letras[char]
            else:
                modified_text += char # Por si ya era mayúscula
            
            es_mayus = False  # ¡APAGAMOS el interruptor! (Ya cumplimos)

        else:
            modified_text += char # Letras normales de en medio de la palabra
    return modified_text


#print(to_upper("hola mundo"))

def to_upper(string:str) -> str:
    mapeo_letras = {
    'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 
    'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 
    'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 
    'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'
    }
    
    result = ""
    is_upper = True
    for char in string:
        if char == " ":
            result += char
            is_upper = True
        elif is_upper and char in mapeo_letras:
            result += mapeo_letras[char]
            is_upper = False
        else:
            result += char
            is_upper = False
    return result

print(to_upper("hola mundo"))