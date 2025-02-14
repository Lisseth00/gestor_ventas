import re
from datetime import datetime

def validar_telefono(telefono):
    if not telefono.startswith("+") or not telefono[1:].isdigit():
        raise ValueError("El teléfono debe comenzar con un signo '+' seguido de números.")

def validar_correo(correo):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        raise ValueError("El correo electrónico no es válido.")

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        raise ValueError("La fecha debe tener el formato YYYY-MM-DD.")

def validar_genero(genero):
    cambio_formato_genero = genero.strip().upper().replace(" ", "")
    print(cambio_formato_genero)
    if cambio_formato_genero not in ["MASCULINO", "FEMENINO"]:
        raise ValueError("El género no es válido.")

def obtener_dato(mensaje, validacion_func=None):
    while True:
        dato = input(mensaje)
        if dato:
            try:
                if validacion_func:
                    validacion_func(dato)
                return dato
            except ValueError as e:
                print(e)
        else:
            print("Este campo no puede estar vacío.")