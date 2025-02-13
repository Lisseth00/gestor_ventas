from model import connection

class ClienteModel(connection.Conection):
    def __init__(self):
        super().__init__()
    
    def agregando_persona(self, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, documento,telefono, correo_electronico, direccion_residencia, fecha_nacimiento, genero):
        self.cursor.execute(    """INSERT INTO personas (
            primer_nombre,
            segundo_nombre,
            primer_apellido,
            segundo_apellido,
            documento,
            telefono,
            correo_electronico,
            direccion_residencia,
            fecha_nacimiento,
            genero) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", 
            (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, documento, telefono, correo_electronico, direccion_residencia, fecha_nacimiento, genero),)
        self.conn.commit()
        print("Cliente agregado satisfactoriamente")    
        