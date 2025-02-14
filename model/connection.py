import mysql.connector
from mysql.connector import Error


class Conection:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "ventas_2025"
            )
            if not self.conn.is_connected():
                raise Error("No se pudo establecer la conexión.")
            self.cursor = self.conn.cursor()
            self.commit = self.conn.commit()
        except Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            self.conn = None
            self.cursor = None

