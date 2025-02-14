from view import cliente_view
from model import person_model
from controller import person_controller


if __name__ == "__main__":
    view = cliente_view.ClienteView()
    model = person_model.PersonModel()
    person_controller = person_controller.ControladorPersona(model, view)
    person_controller.ejecutar()
    