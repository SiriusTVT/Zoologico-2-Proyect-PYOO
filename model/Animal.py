class Animal:
    def __init__(self):
        self.nombre = ""
        self.especie = ""
        self.habitat = ""
        self.comer = ""
        self.juego = ""
        self.edad = 0
        self.dormir = 0

        self.diccionarioAnimal = {}
        self.contadorAnimal = 0
        self.habitatAnimal = []


    def ComprobanteListaHabitat(self, habitat):
        for i in habitat:
            if i == self.habitat:
                return True
        return False


    # Agregar Animal
    def agregarAnimal(self, habitatAnimal):
        self.habitatAnimal = habitatAnimal


        comprobante = self.ComprobanteListaHabitat(self.habitatAnimal)

        if comprobante == False:
            print("El Habitat del animal no coincide con los datos disponibles\n")
        else:
            self.contadorAnimal += 1
            ID = str(self.contadorAnimal)

            self.diccionarioAnimal["Nombre" + " " + ID] = self.nombre
            self.diccionarioAnimal["Especie" + " " + ID] = self.especie
            self.diccionarioAnimal["Habitat" + " " + ID] = self.habitat
            self.diccionarioAnimal["Comer" + " " + ID] = self.comer
            self.diccionarioAnimal["Juego" + " " + ID] = self.juego
            self.diccionarioAnimal["Edad" + " " + ID] = self.edad
            self.diccionarioAnimal["Dormir" + " " + ID] = self.dormir

            print("Se agrego Correctamente")
