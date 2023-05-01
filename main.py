
import model.Zoologico as model
import view.ZoologicoView as view
import controller.ControllerZoologico as controller

def menu():
    modelo = model.Zoologico()
    vista = view.ZoologicoView()
    controlador = controller.ControllerZoologico(modelo, vista)
    operacion = 1

    while(operacion != 0):
        print("1. Agregar habitat")
        print("2. Agregar Animal")
        print("3. Mostrar Dato Animal")
        print("4. Acciones")
        print("5. Mostrar alimentos")

        operacion = int(input())
        if operacion == 1:
            print(1)
        elif operacion == 2:
            print(2)
        elif operacion == 3:
            print(3)
        elif operacion == 4:
            print(4)
        elif operacion == 5:
            print(5)
        else:
            print("Entrada Invalida")


if __name__ == '__main__':
    menu()

