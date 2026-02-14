def contador(lista: list[int]) -> dict:
    if not lista:
        raise ValueError("La lista no puede estar vacía")

    resultado = {
        "pares": [],
        "impares": [],
        "suma": 0,
        "mayor": lista[0],
        "menor": lista[0],
        "promedio": 0.0,
        "mediana": 0.0,
        "rango": 0,
        "únicos": set(),
    }

    for numero in lista:
        # Suma y acumulación
        resultado["suma"] += numero

        # Mayor y menor
        if numero > resultado["mayor"]:
            resultado["mayor"] = numero
        if numero < resultado["menor"]:
            resultado["menor"] = numero

        # Pares e impares
        if numero % 2 == 0:
            resultado["pares"].append(numero)
        else:
            resultado["impares"].append(numero)

        # Valores únicos
        resultado["únicos"].add(numero)

    # Promedio
    resultado["promedio"] = resultado["suma"] / len(lista)

    # Rango
    resultado["rango"] = resultado["mayor"] - resultado["menor"]

    # Mediana
    numeros_ordenados = sorted(lista)
    n = len(numeros_ordenados)
    mid = n // 2
    if n % 2 == 0:
        resultado["mediana"] = (numeros_ordenados[mid - 1] + numeros_ordenados[mid]) / 2
    else:
        resultado["mediana"] = numeros_ordenados[mid]

    return resultado

# Test
lista = [-4, 7, 10, 3]
print(contador(lista))
