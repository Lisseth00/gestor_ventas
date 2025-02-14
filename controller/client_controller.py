class ControladorCliente:
    def __init__(self, modelo, view):
        self.modelo = modelo
        self.view = view

    def ejecutar(self):
        while True:
            self.view.mostrar_menu()
            opcion = self.view.obtener_opcion_menu()
            if opcion == "1":
                self.view.mostrar_mensaje("\n--- Agregar Cliente ---")
                datos = self.view.obtener_datos_cliente()
                if datos:
                    self.modelo.agregar_cliente(datos)
            elif opcion == "2":
                self.view.mostrar_mensaje("\n--- Lista de Clientes ---")
                clientes = self.modelo.ver_clientes()
                if clientes:
                    self.view.mostrar_clientes(clientes)
                else:
                    self.view.mostrar_mensaje("No hay clientes registrados.")
            elif opcion == "3":
                clientes = self.modelo.ver_clientes()
                if clientes:
                    self.view.mostrar_mensaje("\n--- Lista de Clientes ---")
                    self.view.mostrar_clientes(clientes)
                    
                    while True:
                        self.view.mostrar_mensaje("\n--- Actualizar Cliente ---")
                        id_cliente = self.view.obtener_id_cliente("actualizar")
                        
                        if self.modelo.validar_id_cliente(id_cliente):
                            campo = self.view.seleccionar_campo_actualizar()
                            while True:
                                nuevo_valor = self.view.obtener_nuevo_valor(campo)
                                if nuevo_valor:
                                    self.modelo.actualizar_campo(id_cliente, campo, nuevo_valor)
                                    break
                            break
                        else:
                            self.view.mostrar_mensaje("ID no válido. Intente de nuevo.")
                else:
                    self.view.mostrar_mensaje("No hay clientes registrados.")

            elif opcion == "4":  # Eliminar cliente
                clientes = self.modelo.ver_clientes()
                if clientes:
                    self.view.mostrar_mensaje("\n--- Lista de Clientes ---")
                    self.view.mostrar_clientes(clientes)
                    while True:
                        self.view.mostrar_mensaje("\n--- Eliminar Cliente ---")
                        id_cliente = self.view.obtener_id_cliente("eliminar")
                        if self.modelo.validar_id_cliente(id_cliente):
                            confirmacion = self.view.confirmacion_eliminacion()
                            if confirmacion.strip().upper() == "SI":
                                self.modelo.eliminar_cliente(id_cliente)
                            else:
                                self.view.mostrar_mensaje("Eliminación cancelada.")
                            break
                        else:
                            self.view.mostrar_mensaje("ID no válido. Intente de nuevo.")
                else:
                    self.view.mostrar_mensaje("No hay clientes registrados.")

            elif opcion == "5":
                self.view.mostrar_mensaje("Saliendo del sistema...")
                break