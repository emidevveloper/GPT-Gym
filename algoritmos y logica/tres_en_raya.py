"""
/*
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *   O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.
 */
"""

matriz = [
    ["X", "O", "X"],
    ["", "X", "O"],
    ["O", "", "X"]
]

def evaluar(diccionario:dict):
    if diccionario["X"] >= diccionario["O"]:
        return "X"
    elif diccionario["X"] < diccionario["O"]:
        return "O"
    else:
        return "Empate o nulo"
    
def tres_en_raya(matriz: list) -> str:
    veredicto = ""
    notario = {
        "X": 0,
        "O": 0,
    }
    for fila in matriz:
        for celda in fila:
            if celda == "X":
                notario["X"] += 1
            elif celda == "O":
                notario["O"] += 1

    diferencia = abs(notario["X"] - notario["O"])
    if diferencia > 1:
        return "Nulo"
    
    veredicto = evaluar(notario)
    print(notario)
    return veredicto

print(tres_en_raya(matriz))