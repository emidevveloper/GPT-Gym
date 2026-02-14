#¿Cómo crear de manera eficiente un diccionario con 2 listas?

keys, values = ["a", "b", "c"], [10, 20, 30]

#No empaquetaremos con for sino así:

diccionario = dict(zip(keys, values))
print(diccionario)