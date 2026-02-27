"""
/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
"""
TEXT_TO_MORSE = {
    # Letras
    "A": ".—",
    "B": "—...",
    "C": "—.—.",
    "D": "—..",
    "E": ".",
    "F": "..—.",
    "G": "——.",
    "H": "....",
    "I": "..",
    "J": ".———",
    "K": "—.—",
    "L": ".—..",
    "M": "——",
    "N": "—.",
    "O": "———",
    "P": ".——.",
    "Q": "——.—",
    "R": ".—.",
    "S": "...",
    "T": "—",
    "U": "..—",
    "V": "...—",
    "W": ".——",
    "X": "—..—",
    "Y": "—.——",
    "Z": "——..",

    # Números
    "0": "—————",
    "1": ".————",
    "2": "..———",
    "3": "...——",
    "4": "....—",
    "5": ".....",
    "6": "—....",
    "7": "——...",
    "8": "———..",
    "9": "————.",

    # Signos de puntuación
    ".": ".—.—.—",
    ",": "——..——",
    "?": "..——..",
    "'": ".————.",
    "!": "—.—.——",
    "/": "—..—.",
    "(": "—.——.",
    ")": "—.——.—",
    "&": ".—...",
    ":": "———...",
    ";": "—.—.—.",
    "=": "—...—",
    "+": ".—.—.",
    "-": "—....—",
    "_": "..——.—",
    "\"": ".—..—.",
    "$": "...—..—",
    "@": ".——.—."
}

MORSE_TO_TEXT = {valor: llave for llave, valor in TEXT_TO_MORSE.items()}
def text_converter(texto: str) -> str:
    import re
    # 1. Definimos la lógica de conversión genérica una sola vez
    def procesar(datos, mapa, separador_entrada, separador_salida):
        palabras = []
        # Dividimos por el separador (espacio para morse, nada para texto)
        for item in datos.split(separador_entrada) if separador_entrada else datos:
            if item in mapa:
                palabras.append(mapa[item])
        return separador_salida.join(palabras)

    # 2. Identificamos patrones
    patron_morse = r'^[.\—\s]+$'

    if re.fullmatch(patron_morse, texto):
        # MORSE -> TEXTO (Diferente mapa y separadores)
        return procesar(texto, MORSE_TO_TEXT, " ", "")
    
    elif re.search(r'[a-zA-Z]', texto):

        return procesar(texto.upper(), TEXT_TO_MORSE, "", " ")
    
    return "Formato no reconocido"

print(text_converter(""))

# Ejercicio completado. Tipo de dificultad: Python intermedio 🔥