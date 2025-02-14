from model import utils

class ClienteView:
    @staticmethod
    def mostrar_menu():
        """Muestra el menú de opciones."""
        print("\n--- Menú de Gestión de Personas ---")
        print("1. Agregar persona")
        print("2. Ver personas")
        print("3. Actualizar persona")
        print("4. Eliminar persona")
        print("5. Salir")

    @staticmethod
    def obtener_datos_persona():
        try:
            datos = {
                "primer_nombre": utils.obtener_dato("Primer nombre: "),
                "segundo_nombre": utils.obtener_dato("Segundo nombre: "),
                "primer_apellido": utils.obtener_dato("Primer apellido: "),
                "segundo_apellido": utils.obtener_dato("Segundo apellido: "),
                "documento": utils.obtener_dato("Documento: "),
                "telefono": utils.obtener_dato("Teléfono: ", utils.validar_telefono),
                "correo_electronico": utils.obtener_dato("Correo electrónico: ", utils.validar_correo),
                "direccion_residencia": utils.obtener_dato("Dirección de residencia: "),
                "fecha_nacimiento": utils.obtener_dato("Fecha de nacimiento (YYYY-MM-DD): ", utils.validar_fecha),
                "genero": utils.obtener_dato("Género (Masculino/Femenino): ", utils.validar_genero),
            }
            return datos
        except ValueError as e:
            print(f"Error de validación: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

    @staticmethod
    def mostrar_mensaje(mensaje):
        try:
            print(mensaje)
        except Exception as e:
            print(f"Error al mostrar el mensaje: ERROR({e})")

    @staticmethod
    def obtener_opcion_menu():
        try:
            opcion = input("Seleccione una opción: ")
            if opcion not in ["1", "2", "3", "4", "5"]:
                raise ValueError("Opción no válida. Intente de nuevo.")
            return opcion
        except ValueError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

    @staticmethod
    def obtener_id_persona(accion):
        """Solicita al usuario el ID de la persona para actualizar o eliminar."""
        try:
            if accion == "actualizar":
                id_persona = int(input("Ingrese el ID de la persona a actualizar: "))
            elif accion == "eliminar":
                id_persona = int(input("Ingrese el ID de la persona a eliminar: "))
            else:
                raise ValueError("Acción no válida.")
            return id_persona
        except ValueError:
            print("Por favor ingrese un número válido para el ID.")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

    @staticmethod
    def mostrar_personas(personas):
        try:
            if personas:
                print("-" * 120)
                for persona in personas:
                    print(
                        f"{persona[0]}\t{persona[1]}\t{persona[2]}\t{persona[3]}\t{persona[4]}\t{persona[5]}\t{persona[6]}\t{persona[7]}\t{persona[8]}\t{persona[9]}\t{persona[10]}"
                    )
            else:
                print("No hay personas registradas.")
        except Exception as e:
            print(f"Error al mostrar la lista de personas: ERROR({e})")