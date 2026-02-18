"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""
def es_primo(numero):
    if numero < 2:
        return False
    
    # Probamos si algún número desde 2 hasta la raíz del número lo divide
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # Si alguien lo divide, ya no es primo
            
    return True # Si salió del bucle sin retornar False, es primo

# Parte 2: Imprimir los números entre 1 y 100
print("Números primos entre 1 y 100:")
for n in range(1, 101):
    if es_primo(n):
        print(n, end=" ")