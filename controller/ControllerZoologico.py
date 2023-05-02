class ControllerZoologico:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def agregarHabitat(self):
        self.modelo.entradaSTR = self.vista.obtener_valorSTR("Ingrese Habitat: ")
        self.modelo.agregarHabitat()

    def agregarAnimal(self):
        self.modelo.nombre = self.vista.obtener_valorSTR("Nombre: ")
        self.modelo.especie = self.vista.obtener_valorSTR("Especie: ")
        self.modelo.habitat = self.vista.obtener_valorSTR("Habitat: ")
        self.modelo.comer = self.vista.obtener_valorSTR("Comer: ")
        self.modelo.juego = self.vista.obtener_valorSTR("Juego: ")

        self.modelo.edad = self.vista.obtener_valorINT("Edad: ")
        self.modelo.dormir = self.vista.obtener_valorINT("Dormir: ")

        self.modelo.agregarAnimal()
