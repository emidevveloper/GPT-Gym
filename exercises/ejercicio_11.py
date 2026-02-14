# Calcular área del rectángulo pidiendo base y altura al usuario

def calcular_area():
    base = int(input("Ingrese la base del rectángulo: "))
    altura = int(input("Ingrese la altura del rectángulo: "))

    if not base or not altura:
        return "No agregó nada"
    area = base * altura
    return f"El área del rectángulo es: {area}"

if __name__ == "__main__":
    print(calcular_area())