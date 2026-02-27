"""
/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */
"""

def caracter_checker(str1: str, str2: str) -> tuple:
    out1 = ""
    out2 = ""
    for c in str1:
        if c not in str2:
            out1 += c
    for c in str2:
        if c not in str1:
            out2 += c

    return out1, out2

print(caracter_checker("abuelo", "buela"))