from binascii import Error
from model import connection

class ClienteModel(connection.Conection):
    def __init__(self):
        super().__init__()
    
    def agregando_persona(self, datos):
        try:
            query = """
            INSERT INTO personas (
                primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,
                documento, telefono, correo_electronico, direccion_residencia,
                fecha_nacimiento, genero
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                datos["primer_nombre"],
                datos["segundo_nombre"],
                datos["primer_apellido"],
                datos["segundo_apellido"],
                datos["documento"],
                datos["telefono"],
                datos["correo_electronico"],
                datos["direccion_residencia"],
                datos["fecha_nacimiento"],
                datos["genero"]
            )
            self.cursor.execute(query, valores)
            self.conn.commit()
            print("Cliente agregado satisfactoriamente.")
        except Error as err:
            print(f"Error al agregar persona: {err}")
            self.conn.rollback()  # Revertir la transacción en caso de error

    def ver_personas(self):
        try:
            self.cursor.execute("SELECT * FROM personas")
            return self.cursor.fetchall()
        except Error as err:
            print(f"Error al obtener personas: {err}")
            return None

    def actulizar_persona(self, id_persona, nuevos_datos):
        try:
            query = """
            UPDATE personas
            SET
                primer_nombre = %s,
                segundo_nombre = %s,
                primer_apellido = %s,
                segundo_apellido = %s,
                documento = %s,
                telefono = %s,
                correo_electronico = %s,
                direccion_residencia = %s,
                fecha_nacimiento = %s,
                genero = %s
            WHERE id = %s
            """
            valores = (
                nuevos_datos["primer_nombre"],
                nuevos_datos["segundo_nombre"],
                nuevos_datos["primer_apellido"],
                nuevos_datos["segundo_apellido"],
                nuevos_datos["documento"],
                nuevos_datos["telefono"],
                nuevos_datos["correo_electronico"],
                nuevos_datos["direccion_residencia"],
                nuevos_datos["fecha_nacimiento"],
                nuevos_datos["genero"],
                id_persona
            )
            self.cursor.execute(query, valores)
            self.conn.commit()
            print(f"Persona con ID {id_persona} actualizada correctamente.")
        except Error as err:
            print(f"Error al actualizar persona: {err}")
            self.conn.rollback()
            
    def eliminar_persona(self, id_persona):
        try:
            query = "DELETE FROM personas WHERE id = %s"
            self.cursor.execute(query, (id_persona,))
            self.conn.commit()
            print(f"Persona con ID {id_persona} eliminada correctamente.")
        except Error as err:
            print(f"Error al eliminar persona: {err}")
            self.conn.rollback()