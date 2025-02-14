from binascii import Error
from model import connection
from model import utils

class ClientModel(connection.Conection):
    def __init__(self):
        super().__init__()
    
    def agregar_cliente(self, datos):
        try:
            self.cursor.execute("""
                INSERT INTO clientes (id_persona) VALUES (%s)
            """, (datos["id_persona"],))
            self.conn.commit()
            print("Cliente agregado satisfactoriamente.")
        except Error as err:
            print(f"Error al agregar cliente: {err}")
            self.conn.rollback()

    def ver_clientes(self):
        try:
            self.cursor.execute("SELECT cl.id, pe.primer_nombre, pe.documento FROM clientes cl JOIN personas pe ON cl.id_persona = pe.id")
            return self.cursor.fetchall()
        except Error as err:
            print(f"Error al obtener clientes: {err}")
            return None

    def actualizar_campo(self, id_cliente, campo, nuevo_valor):
        try:
            query = f"UPDATE clientes SET {campo} = %s WHERE id = %s"
            self.cursor.execute(query, (nuevo_valor, id_cliente))
            self.conn.commit()
            print(f"Campo '{campo}' actualizado correctamente para el cliente con ID {id_cliente}.")
        except Error as err:
            print(f"Error al actualizar el campo: {err}")
            self.conn.rollback()

    def eliminar_cliente(self, id_cliente):
        try:
            query = "DELETE FROM clientes WHERE id = %s"
            self.cursor.execute(query, (id_cliente,))
            self.conn.commit()
            print(f"Cliente con ID {id_cliente} eliminado correctamente.")
        except Error as err:
            print(f"Error al eliminar cliente: {err}")
            self.conn.rollback()

    def validar_id_cliente(self, id_cliente):
        try:
            self.cursor.execute(
                "SELECT id FROM clientes WHERE id = %s", (id_cliente,)
            )
            return self.cursor.fetchone() is not None
        except Error as e:
            print(f"Error al validar el ID: {e}")
            return False

    def validar_id_persona(self, id_persona):
        try:
            self.cursor.execute(
                "SELECT id FROM personas WHERE id = %s", (id_persona,)
            )
            return self.cursor.fetchone() is not None
        except Error as e:
            print(f"Error al validar el ID de persona: {e}")
            return False