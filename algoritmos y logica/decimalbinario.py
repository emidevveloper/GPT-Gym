"""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""

def to_binary(numero: int):
    """
    Convierte un número decimal a un binario
    Args: numero: float
    Returns => str
    """
    numeros = []
    binarios = []
    while numero > 0:
        if numero % 2 == 0:
            numeros.append(0)
        else:
            numeros.append(1)

print(to_binary(46))