lista = [-4, 7, 10, 3] #Lista de enteros
def contador(lista: list[int]) -> dict: #Single responsability (La función hace una sola cosa)
    """
    Docstring para contador
    
    :param lista: Una lista de números enteros
    :type lista: list
    :return: Retorna un diccionario con números pares, impares, la suma total de los números y el número menor de la lista.
    :rtype: dict
    """

    if not lista:
        raise ValueError("La lista no puede estar vacía")
         
    resultado = { #Se retornará el diccionario con todos los datos
        "pares": [],
        "impares": [],
        "suma": 0,
        "mayor": lista[0],
        "menor": lista[0],
        "cantidad_pares": 0,
        "cantidad_impares": 0,
        "promedio": 0,
    }

    for i, numero in enumerate(lista):
        resultado["suma"] += numero

        if numero > resultado["mayor"]:
            resultado["mayor"] = numero
        
        if numero < resultado["menor"]:
            resultado["menor"] = numero
        
        if numero % 2 == 0:
            resultado["pares"].append(numero)
            resultado["cantidad_pares"] = i
        else:
            resultado["impares"].append(numero)
            resultado["cantidad_impares"] = i

    resultado["promedio"] = (resultado["cantidad_pares"] + resultado["cantidad_impares"]) / 5

    return resultado
print(contador(lista), end="\n", sep="*")
#Refactorizar esta mierda :v