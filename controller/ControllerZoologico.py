class ControllerZoologico:
    def __init__(self, modeloZoo, vista, modeloHab, modeloAnimal):
        self.modeloAnimal = modeloAnimal
        self.modeloHab = modeloHab
        self.modeloZoo = modeloZoo
        self.vista = vista

        self.habitatClase = []
        self.pHabitatAnimal = []

    def agregarHabitat(self):
        self.modeloHab.entradaSTR = self.vista.obtener_valorSTR("Ingrese Habitat: ")
        self.modeloHab.agregarHabitat()
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

            self.modeloAnimal.agregarAnimal(self.pHabitatAnimal)
