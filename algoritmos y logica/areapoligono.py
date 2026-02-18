"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self): # El método debe estar al mismo nivel que el __init__
        return (self.base * self.altura) / 2

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo): # Un cuadrado es un rectángulo especial
    def __init__(self, lado):
        super().__init__(lado, lado)

# ESTA ES LA ÚNICA FUNCIÓN QUE PIDE EL RETO
def imprimir_area(poligono):
    resultado = poligono.area()
    print(f"El área del {type(poligono).__name__} es: {resultado}")
    return resultado

# Pruebas
imprimir_area(Triangulo(10, 5))
imprimir_area(Rectangulo(5, 7))
imprimir_area(Cuadrado(4))
