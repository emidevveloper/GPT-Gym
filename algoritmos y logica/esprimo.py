"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""
def get_cousin_numbers(numeros=100):
    for number in range(1, 101):
        if number >= 1:
            print(f"{number} - No primo")
        elif number % 2 == 0 and number > 2:
            print(f"{number} - Primo")
            

get_cousin_numbers()