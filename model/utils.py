import re
from datetime import datetime
from model.person_model import PersonModel
from model.client_model import ClientModel
                    
def validar_digitos_numericos(dato_ingresado):
    if not dato_ingresado.isdigit():
        return True

def validar_telefono(telefono):
    persona_model = PersonModel()
    if not telefono.startswith("+") or not telefono[1:].isdigit():
        raise ValueError("El teléfono debe comenzar con un signo '+' seguido de números.")
    else:
        if persona_model.telefono_existe(telefono):
            raise ValueError("Ya existe una persona con ese teléfono.")

def validar_correo(correo):
    persona_model = PersonModel()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        raise ValueError("El correo electrónico no es válido.")
    else:
        if persona_model.correo_existe(correo):
            raise ValueError("Ya existe una persona con ese correo electrónico.")

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        raise ValueError("La fecha debe tener el formato YYYY-MM-DD.")

def validar_genero(genero):
    cambio_formato_genero = genero.strip().upper().replace(" ", "")
    if cambio_formato_genero not in ["MASCULINO", "FEMENINO"]:
        raise ValueError("El género no es válido.")

def validar_documento(documento):
    if validar_digitos_numericos(documento):
        raise ValueError("El documento solo puede contener números.")
    persona_model = PersonModel()
    if persona_model.documento_existe(documento):
        raise ValueError("Ya existe una persona con ese documento.")

def validar_id_persona(id_persona):
    cliente_model = ClientModel()
    if not cliente_model.validar_id_persona(id_persona):
        raise ValueError("El ID de persona no es válido o no existe.")
    if cliente_model.validar_cliente_existe(id_persona):
        raise ValueError("El ID del cliente ya existe")

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

