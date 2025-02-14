from binascii import Error
from model import connection
from model import utils

class PersonModel(connection.Conection):
    def __init__(self):
        super().__init__()
    
    def agregar_persona(self, datos):
        try:
            self.cursor.execute(""" INSERT INTO personas (
                primer_nombre, 
                segundo_nombre, 
                primer_apellido, 
                segundo_apellido,
                documento, 
                telefono, 
                correo_electronico, 
                direccion_residencia,
                fecha_nacimiento, 
                genero
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, datos["primer_nombre"],
                datos["segundo_nombre"],
                datos["primer_apellido"],
                datos["segundo_apellido"],
                datos["documento"],
                datos["telefono"],
                datos["correo_electronico"],
                datos["direccion_residencia"],
                datos["fecha_nacimiento"],
                datos["genero"])
            self.conn.commit()
            print("Cliente agregado satisfactoriamente.")
        except Error as err:
            print(f"Error al agregar persona: {err}")
            self.conn.rollback()


    def ver_personas(self):
        try:
            self.cursor.execute("SELECT * FROM personas")
            return self.cursor.fetchall()
        except Error as err:
            print(f"Error al obtener personas: {err}")
            return None

    def actualizar_campo(self, id_persona, campo, nuevo_valor):
        try:
            query = f"UPDATE personas SET {campo} = %s WHERE id = %s"
            self.cursor.execute(query, (nuevo_valor, id_persona))
            self.conn.commit()
            print(f"Campo '{campo}' actualizado correctamente para la persona con ID {id_persona}.")
        except Error as err:
            print(f"Error al actualizar el campo: {err}")
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

    def validar_id_persona(self, id_persona):
        try:
            self.cursor.execute(
                "SELECT id FROM personas WHERE id = %s", (id_persona,)
            )
            return self.cursor.fetchone() is not None
        except Error as e:
            print(f"Error al validar el ID: {e}")
            return False
    
    def documento_existe(self, documento):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM personas WHERE documento = %s", (documento,))
            resultado = self.cursor.fetchone()
            return resultado[0] > 0  # Retorna True si ya existe
        except Error as err:
            print(f"Error al verificar documento: {err}")
            return True  # Evita la inserción si hay error

    def telefono_existe(self, telefono):
        """Verifica si el teléfono ya está registrado en la base de datos."""
        try:
            self.cursor.execute("SELECT COUNT(*) FROM personas WHERE telefono = %s", (telefono,))
            resultado = self.cursor.fetchone()
            return resultado[0] > 0
        except Error as err:
            print(f"Error al verificar teléfono: {err}")
            return True

    def correo_existe(self, correo):
        """Verifica si el correo ya está registrado en la base de datos."""
        try:
            self.cursor.execute("SELECT COUNT(*) FROM personas WHERE correo_electronico = %s", (correo,))
            resultado = self.cursor.fetchone()
            return resultado[0] > 0
        except Error as err:
            print(f"Error al verificar correo: {err}")
            return True
