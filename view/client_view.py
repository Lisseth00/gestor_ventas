from model import utils

class ClientView:
    @staticmethod
    def mostrar_menu():
        """Muestra el menú de opciones."""
        print("\n---- Menú de Gestión de Clientes ----")
        print("1. Agregar cliente")
        print("2. Ver clientes")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")

    @staticmethod
    def obtener_datos_cliente():
        try:
            datos = {
                "id_persona": utils.obtener_dato("ID de la persona: ", utils.validar_id_persona),
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
    def obtener_id_cliente(accion):
        """Solicita al usuario el ID del cliente para actualizar o eliminar."""
        try:
            if accion == "actualizar":
                id_cliente = int(input("Ingrese el ID del cliente a actualizar: "))
            elif accion == "eliminar":
                id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))
            else:
                raise ValueError("Acción no válida.")
            return id_cliente
        except ValueError:
            print("Por favor ingrese un número válido para el ID.")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

    @staticmethod
    def mostrar_clientes(clientes):
        try:
            if clientes:
                print("-" * 60)
                for cliente in clientes:
                    print(f"ID: {cliente[0]} || Nombre: {cliente[1]} || Documento: {cliente[2]}")
                    print("-" * 60)
            else:
                print("No hay clientes registrados.")
        except Exception as e:
            print(f"Error al mostrar la lista de clientes: ERROR({e})")

    @staticmethod
    def confirmacion_eliminacion():
        """Solicita confirmación antes de eliminar, asegurando una respuesta válida."""
        while True:
            respuesta = input("¿Está seguro de que desea eliminar el cliente? (SI/NO): ").strip().upper()
            if respuesta in ["SI", "NO"]:
                return respuesta
            else:
                print("Respuesta no válida. Por favor, ingrese 'SI' o 'NO'.")

    @staticmethod
    def seleccionar_campo_actualizar():
        """Muestra los campos disponibles para actualizar y permite seleccionar uno."""
        print("\n--- Campos disponibles para actualizar ---")
        opciones = {
            "1": "id_persona",
        }
        
        for key, value in opciones.items():
            print(f"{key}. {value.replace('_', ' ').capitalize()}")
        
        while True:
            opcion = input("Seleccione el número del campo que desea actualizar: ").strip()
            if opcion in opciones:
                return opciones[opcion]
            else:
                print("Opción no válida. Intente de nuevo.")

    @staticmethod
    def obtener_nuevo_valor(campo):
        validacion_func = None
        if campo == "id_persona":
            validacion_func = utils.validar_id_persona
        return utils.obtener_dato(f"Ingrese el nuevo valor para {campo.replace('_', ' ').capitalize()}: ", validacion_func).strip()