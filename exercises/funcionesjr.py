#Función para analizar texto
texto = "Hola mundo cruel"

def analizar_texto(texto:str) -> dict:
    """Retorna datos del texto.

    Args:
        texto: El texto de entrada que analizará la función

    Returns:
        Un diccionario que contendrá todos estos datos:
            cantidad_total_caracteres (sin espacios)

            cantidad_palabras

            palabra_mas_larga

            cantidad_vocales

            cantidad_consonantes

            palabras_unicas (set)

    Raises:
        ValueError, Si no recibe ningún dato por el parámetro
    """
    resultado = {
    "cantidad_total_caracteres": len(texto),
    "cantidad_palabras": len(texto.split()),
    "palabra_mas_larga": "",
    "cantidad_vocales": 0,
    "cantidad_consonantes": int(),
    "palabras_unicas": set(),
}   
    texto = texto.split()
    vocales = "aeiouáéíóú"

    for palabra in texto:
        if len(palabra) > len(resultado["palabra_mas_larga"]):
            resultado["palabra_mas_larga"] = palabra
        
        if palabra in vocales:
            resultado["cantidad_vocales"] += 1
        
    return resultado

print(analizar_texto(texto))
