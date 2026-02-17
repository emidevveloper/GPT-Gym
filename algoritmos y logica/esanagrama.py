"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""

def esanagrama(primera_palabra:str, segunda_palabra:str) -> bool:
    palabra_ordenada = "".join(sorted(primera_palabra))
    segunda_ordenada = "".join(sorted(segunda_palabra))
    if palabra_ordenada.lower() == segunda_ordenada.lower():
        return True
    else:
        return False
    
print(esanagrama("amor", "roma"))
print(esanagrama("fresa","frase"))
print(esanagrama("Abuelo", "Padre"))

#Ejercicio concluido