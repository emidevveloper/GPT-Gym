"""
/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */
"""

def armstrong(numero: int):
    string_num = str(numero)
    potencia = len(string_num)

    suma_narcisista = sum(int(n) ** potencia for n in string_num)

    return suma_narcisista
    
print(armstrong(153))

# Ejercicio hardcore