"""
/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
 */
"""
import datetime

def how_many_days(fecha_incial:str, fecha_anterior:str) -> int:
    try:
        fecha_incial = datetime.datetime.strptime(fecha_incial, "%d/%m/%Y")
        fecha_anterior = datetime.datetime.strptime(fecha_anterior, "%d/%m/%Y")
        
        diferencia = fecha_incial - fecha_anterior
        return abs(diferencia.days)
    
    except ValueError as error:
        raise ValueError(f"Hubo un error en el formato de las 2 o alguna de las fechas {error}")

print(how_many_days("28/02/2026", "10/05/2002"))

# Dificultad: Difícil, porque requiere de módulos externos para su resolución.