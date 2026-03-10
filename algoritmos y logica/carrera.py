"""
/*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 */
"""
# Validar datos
def has_surpassed(action: list, track: str) -> bool:
    es_valido = True
    string_final = ""
    for paso_atleta, paso_pista in zip(action, track):
        if (paso_atleta == "run" and paso_pista == "_") or (paso_atleta == "jump" and paso_pista == "|"):
            string_final += paso_pista 
        elif paso_atleta == "jump" and paso_pista == "_":
            es_valido = False   
            string_final += "x" 
        elif paso_atleta == "run" and paso_pista == "|":
            es_valido = False
            string_final += "/"
    print(f"Pista final: {string_final}")
    return es_valido

# Pista: _|_|
# Acciones: "jump" (debería fallar en _), "run" (debería fallar en |)
resultado = has_surpassed(["jump", "run", "jump", "run"], "_|_|")
print(f"¿Superó la carrera?: {resultado}")


resultado = has_surpassed(["run", "jump", "run", "jump"], "_|_|")
print(f"¿Superó la carrera?: {resultado}")
