"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""

TEXTO = "Hola mundo"

def revertir_cadena(texto: str) -> str:
    """
    Retorna una cadena de texto revertida
    Args texto
    return str
    """

    texto_revertido = ""
    for caracter in texto:
        texto_revertido = caracter + texto_revertido
    
    return texto_revertido 

print(revertir_cadena(TEXTO))