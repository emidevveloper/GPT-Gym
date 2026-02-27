"""
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */

Tema: Recursividad
"""

def factorial_recursivo(x: int) -> int:
    if x == 1: # Le pregunto si el número es 1, si no, prosigue llamarse así misma
        return 1
    else:
        return x * factorial_recursivo(x - 1)

print(factorial_recursivo(5))

# Tema difícil