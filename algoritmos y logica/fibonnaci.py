"""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""

#necesitamos n números, ejemplo 50
def fibonacci(n: int) -> list[int]:
    secuencia = [0, 1]
    while len(secuencia) < n:
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia

#print(fibonacci(1_000_000)) #Complejidad o(n2). No ejecutes este código con números grandes,
#prueba con 10 o 100, pero no 1 millón. Si quieres probar 1 millón de números, usa la función
#de abajo. Esta función es ineficiente en rendimiento

# Enfoque eficiente para números gigantescos pero igual de duradero. NUNCA SE DEBE ALMACENAR NADA DE ESTO EN MEMORIA
"""
def fibonacci_1m(n):
    a, b = 0, 1
    for _ in range(0, n):
        a, b = b, a + b
    return a

print(len(str(fibonacci_1m(1000000)))) # Esto imprimirá 208988
"""

import sys

# Aumentamos el límite de dígitos para la conversión a string (necesario en Python moderno)
sys.set_int_max_str_digits(300000)

def fib_fast_doubling(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib_fast_doubling(n >> 1)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n & 1:
            return (d, c + d)
        else:
            return (c, d)

# Cálculo
n = 1000000
resultado = fib_fast_doubling(n)[0]

# Para verificar la rapidez
print(f"Calculado con éxito. El número tiene {len(str(resultado))} dígitos.")
