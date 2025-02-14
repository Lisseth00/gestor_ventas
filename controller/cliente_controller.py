class ControladorPersona:
    def __init__(self, modelo, view):
        self.modelo = modelo
        self.view = view

    def ejecutar(self):
        while True:
            self.view.mostrar_menu()
            opcion = self.view.obtener_opcion_menu()
            if opcion == "1":
                self.view.mostrar_mensaje("\n--- Agregar Persona ---")
                datos = self.view.obtener_datos_persona()
                self.modelo.agregar_persona(datos)
            elif opcion == "2":
                self.view.mostrar_mensaje("\n--- Lista de Personas ---")
                personas = self.modelo.ver_personas()
                if personas:
                    self.view.mostrar_personas(personas)
                else:
                    self.view.mostrar_mensaje("No hay personas registradas.")
            elif opcion == "3":
                personas = self.modelo.ver_personas()
                if personas:
                    self.view.mostrar_mensaje("\n--- Lista de Personas ---")
                    self.view.mostrar_personas_id(personas)
                    self.view.mostrar_mensaje("\n--- Actualizar Persona ---")
                    id_persona = self.view.obtener_id_persona("actualizar")
                    if self.modelo.validar_id_persona(id_persona):
                        nuevos_datos = self.view.obtener_datos_persona()
                        self.modelo.actualizar_persona(id_persona, nuevos_datos)
                    else:
                        self.view.mostrar_mensaje("ID no válido. Intente de nuevo.")
                else:
                    self.view.mostrar_mensaje("No hay personas registradas.")
            elif opcion == "4":
                personas = self.modelo.ver_personas()
                if personas:
                    self.view.mostrar_mensaje("\n--- Lista de Personas ---")
                    self.view.mostrar_personas_id(personas)
                    self.view.mostrar_mensaje("\n--- Eliminar Persona ---")
                    id_persona = self.view.obtener_id_persona("eliminar")
                    if self.modelo.validar_id_persona(id_persona):
                        self.modelo.eliminar_persona(id_persona)
                    else:
                        self.view.mostrar_mensaje("ID no válido. Intente de nuevo.")
                else:
                    self.view.mostrar_mensaje("No hay personas registradas.")
                
            elif opcion == "5":
                self.view.mostrar_mensaje("Saliendo del sistema...")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida. Intente de nuevo.")
                

