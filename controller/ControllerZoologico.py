class ControllerZoologico:
    def __init__(self, modeloZoo, vista, modeloHab, modeloAnimal):
        self.modeloAnimal = modeloAnimal
        self.modeloHab = modeloHab
        self.modeloZoo = modeloZoo
        self.vista = vista

        self.habitatClase = []
        self.alimentos = self.modeloZoo.alimentos
        self.pHabitatAnimal = []

        self.habitat = ""
        self.comer = ""

    def agregarHabitat(self):
        validacion = 0
        print("Habitats Agregados", self.modeloHab.AdHabitat, "\n")
        print("Habitats Disponibles", self.modeloHab.listaHabitats, "\n")
        print("Alimentacion Disponibles", self.alimentos, "\n")
        self.modeloHab.entradaSTR = self.vista.obtener_valorSTR("Ingrese Habitat: ")
        self.modeloHab.entradaAlimento = self.vista.obtener_valorSTR("Tipo de alimentacion de habitat: ")
        validacion = self.modeloHab.agregarHabitat()

        if validacion == 1:

            self.modeloHab.AlimentoHabitat(self.alimentos)
            self.habitatClase = self.modeloHab.AdHabitat

    def agregarAnimal(self):
        if len(self.habitatClase) == 0:
            print("No hay Habitat Existente")
        else:
            self.pHabitatAnimal = self.habitatClase

            self.modeloAnimal.nombre = self.vista.obtener_valorSTR("Nombre: ")
            self.modeloAnimal.especie = self.vista.obtener_valorSTR("Especie: ")
            self.modeloAnimal.habitat = self.vista.obtener_valorSTR("Habitat: ")
            self.modeloAnimal.comer = self.vista.obtener_valorSTR("Comer: ")
            self.modeloAnimal.juego = self.vista.obtener_valorSTR("Juego: ")

            self.modeloAnimal.edad = self.vista.obtener_valorINT("Edad: ")
            self.modeloAnimal.dormir = self.vista.obtener_valorINT("Dormir: ")

            self.modeloAnimal.agregarAnimal(self.pHabitatAnimal, self.alimentos, self.modeloHab.dietaHabitat)
            if self.modeloAnimal.contadorAnimal != 0:
                self.habitat, self.comer = self.modeloAnimal.cuposHabitatAnimal()
                self.modeloHab.cupos[self.habitat] += 1

    def mostrarAnimal(self):
        if self.modeloAnimal.contadorAnimal == 0:
            print("No hay Animal Existente")
        else:
            self.modeloAnimal.mostrarAnimal()
            self.modeloHab.mostrarCupos()

    def acciones(self, controlador):
        if self.modeloAnimal.contadorAnimal == 0:
            print("No hay Animal Existente")
        else:
            self.modeloZoo.acciones(controlador)

    def alimentarAnimales(self, alimentos):
        self.modeloAnimal.alimentarAnimales(alimentos)

    def dormirAnimal(self):
        self.modeloAnimal.dormirAnimal()
