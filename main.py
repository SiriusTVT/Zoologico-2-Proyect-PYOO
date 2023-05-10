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

    while True:
        try:

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
                    controlador.acciones(controlador)
                elif operacion == 5:
                    controlador.mostrarDatosAlimentos()
                else:
                    print("Entrada Invalida")
                break

        except ValueError:
            print("Error Se esperaba un INT y se a ingresado una cadena")


if __name__ == '__main__':
    menu()
