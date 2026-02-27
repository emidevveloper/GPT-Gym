"""
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */
"""

# Para esto, creamos una función para verificar.
def check_expressions(expression: str) -> bool:
    """
    Retorna True o False dependiendo de la expresión
    Args: str
    Return: bool
    """
    pila = []
    diccionario = {'{':'}','(':')', '[':']'}

    for caracter in expression:
        if caracter in diccionario:
            pila.append(caracter)
        elif len(pila) == 0 or caracter != diccionario[pila.pop()]:
            return f'No es balanceada: {False}'
        
    return f'Balanceada {len(pila) == 0}'

print(check_expressions('{[()]}'))