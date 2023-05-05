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
        self.dicAlimentos = {}

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

            self.diccionarioAnimal["Nombre" + ID] = self.nombre
            self.diccionarioAnimal["Especie" + ID] = self.especie
            self.diccionarioAnimal["Habitat" + ID] = self.habitat
            self.diccionarioAnimal["Comer" + ID] = self.comer
            self.diccionarioAnimal["Juego" + ID] = self.juego
            self.diccionarioAnimal["Edad" + ID] = self.edad
            self.diccionarioAnimal["Dormir" + ID] = self.dormir

            print("Se agrego Correctamente\n")

    def mostrarAnimal(self):
        print("Lista Animales:")
        print(self.diccionarioAnimal, "\n")

        # for clave, valor in self.diccionarioAnimal.items():
        #     print(clave, valor)
        # print("\n")

    def cuposHabitatAnimal(self):
        ID = str(self.contadorAnimal)
        HabitatID = self.diccionarioAnimal["Habitat" + ID]
        ComerID = self.diccionarioAnimal["Comer" + ID]

        return HabitatID, ComerID

    def alimentarAnimales(self, alimentos):
        operacion = ""
        operacion2 = ""
        operacion3 = ""

        validacion1 = 0
        validacion2 = 0
        contadorAlimentos = -1
        encontrado = False

        self.dicAlimentos = alimentos

        self.mostrarAnimal()
        print("Lista de Alimentos:")
        print(self.dicAlimentos, "\n")

        operacion = str(input("A Quien desea alimentar: ID -> "))
        operacion2 = str(input("Tipo de Alimento: -> "))

        for clave, valor in self.dicAlimentos.items():
            if self.diccionarioAnimal["Comer"+operacion] == clave:
                validacion1 = 1
                for elemento in self.dicAlimentos[clave]:
                    if operacion2 == elemento:
                        contadorAlimentos += 1
                        validacion2 = 1
                        encontrado = True
                        break
                if encontrado:
                    break
        if validacion1 == 1 and validacion2 == 1:
            print("Se dio de comer correctamente al ", self.diccionarioAnimal["Especie"+operacion])
            print("Se desea cambiar la alimentacion del ", self.diccionarioAnimal["Especie"+operacion])
            operacion3 = str(input("Respuesta: -> "))
            operacion3 = operacion3.lower()

            if operacion3 == "si":
                llave = self.diccionarioAnimal["Comer" + operacion]
                operacion3 = str(input("Nueva alimentacion: -> "))
                self.dicAlimentos[llave][contadorAlimentos] = operacion3
                print("Se actualizo Correctamente\n")

        else:
            print("No se encontro el animal o el alimento no es correcto para el animal")

