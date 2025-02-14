from model import person_model

nuevos_datos = {
    "primer_nombre": "Ana",
    "segundo_nombre": "María",
    "primer_apellido": "Pérez",
    "segundo_apellido": "García",
    "documento": "9876543210",
    "telefono": "+57 310 987 6543",
    "correo_electronico": "ana.perez@example.com",
    "direccion_residencia": "Carrera 89 # 12-34, Medellín, Colombia",
    "fecha_nacimiento": "1995-05-20",  # Formato YYYY-MM-DD para MySQL
    "genero": "Femenino"
}

cliente1 = person_model.ClienteModel()
id_persona =  4
personas = cliente1.eliminar_persona(id_persona)