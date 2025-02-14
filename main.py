from view import person_view, client_view
from model import person_model, client_model
from controller import person_controller, client_controller

if __name__ == "__main__":
    while True:
        print("\n---- Menú Principal ----")
        print("1. Gestionar Personas")
        print("2. Gestionar Clientes")
        print("3. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            view_person = person_view.PersonView()
            model_person = person_model.PersonModel()
            controller_person = person_controller.ControladorPersona(model_person, view_person)
            controller_person.ejecutar()

        elif opcion == "2":
            view_client = client_view.ClientView()
            model_client = client_model.ClientModel()
            controller_client = client_controller.ControladorCliente(model_client, view_client)
            controller_client.ejecutar()

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
