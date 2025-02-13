from model import connection

class ClienteModel(connection.Conection):
    def __init__(self):
        super().__init__()
    
    def agregando_persona(self, datos):
        self.cursor.execute(    "INSERT INTO personas ( primer_nombre, segundo_nombre, primer_apellido,segundo_apellido, documento, telefono, correo_electronico, direccion_residencia, fecha_nacimiento, genero) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (datos["primer_nombre"], datos["segundo_nombre"], datos["primer_apellido"], datos["segundo_apellido"], datos["documento"], datos["telefono"], datos["correo_electronico"], datos["direccion_residencia"], datos["fecha_nacimiento"], datos["genero"]),)
        self.conn.commit()
        print("Cliente agregado satisfactoriamente")    
    
    def ver_personas(self):
        self.cursor.execute("SELECT * FROM personas")
        return self.cursor.fetchall()
    
    def actulizar_persona(self, id_persona, nuevos_datos):
        self.cursor.execute("UPDATE personas SET primer_nombre = %s, segundo_nombre = %s, primer_apellido = %s, segundo_apellido = %s, documento = %s, telefono = %s, correo_electronico = %s, direccion_residencia = %s, fecha_nacimiento = %s, genero = %s WHERE id = %s", (nuevos_datos["primer_nombre"],
        nuevos_datos["segundo_nombre"],
        nuevos_datos["primer_apellido"],
        nuevos_datos["segundo_apellido"],
        nuevos_datos["documento"],
        nuevos_datos["telefono"],
        nuevos_datos["correo_electronico"],
        nuevos_datos["direccion_residencia"],
        nuevos_datos["fecha_nacimiento"],
        nuevos_datos["genero"],
        id_persona)
        )
        self.conn.commit()
    
    def eliminar_persona(self, id_persona):
        self.cursor.execute("DELETE FROM personas WHERE id = %s", (id_persona,))
        self.conn.commit()