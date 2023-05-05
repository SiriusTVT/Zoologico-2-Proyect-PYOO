class Zoologico:
    def __init__(self):
        self.alimentos = {
            "herbivoro": ["hierbas", "hojas", "frutas"],
            "carnivoro": ["carne", "pescado", "insectos"],
            "omnivoro": ["verduras", "carne", "huevos"]
        }

        self.controlador = 0

    def acciones(self, controlador):
        self.controlador = controlador

        print("Menu alterno de Acciones\n")
        operacion = 1

        while operacion != 0:
            print("1. Alimentar Animal\n")
            print("2. Dormir Animal\n")
            print("3. Dar juego al Animal\n")
            print("0. Salir al menu inicial\n")
            operacion = int(input())

            if operacion == 1:
                self.controlador.alimentarAnimales(self.alimentos)
            elif operacion == 2:
                print()
            elif operacion == 3:
                print()
            else:
                print("Entrada Invalida")




