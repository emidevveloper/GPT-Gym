# Calcular el área de un círculo con su radio dado
# Fórmula: area = π x radio²

def calcular_area(radio: float) -> float:
    """
    Retorna el área de un círculo por un radio
    Params: radio: float
    returns: float

    raises:
    ValueError: Si no se inserta nada en la función, retornará un error
    """
    from math import pi
    if not radio:
        raise ValueError("Tiene que ingresar el radio")
    
    return f"El área del círculo es: {pi * radio**2:.2f}"

print(calcular_area(3))