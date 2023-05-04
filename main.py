import model.Zoologico as modelZoo
import model.Habitat as modelHab
import model.Animal as modelAnimal

import view.ZoologicoView as view
import controller.ControllerZoologico as controller


def menu():
    modeloHab = modelHab.Habitat()
    modeloAnimal = modelAnimal.Animal()
    modeloZoo = modelZoo.Zoologico()
    vista = view.ZoologicoView()

    controlador = controller.ControllerZoologico(modeloZoo, vista, modeloHab, modeloAnimal)
    operacion = 1

    while operacion != 0:
        print("1. Agregar habitat")
        print("2. Agregar Animal")
        print("3. Mostrar Dato Animal")
        print("4. Acciones")
        print("5. Mostrar alimentos")

        operacion = int(input())
        if operacion == 1:
            controlador.agregarHabitat()
        elif operacion == 2:
            controlador.agregarAnimal()
        elif operacion == 3:
            controlador.mostrarAnimal()
        elif operacion == 4:
            print(4)
        elif operacion == 5:
            print(5)
        else:
            print("Entrada Invalida")


if __name__ == '__main__':
    menu()
