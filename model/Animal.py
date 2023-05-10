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

    def ComprobanteAlimentos(self, alimentos):
        for clave, valor in alimentos.items():
            if self.comer == clave:
                return True
        return False

    def ComprobanteHabitatAliementos(self, dietaHabitat):
        if dietaHabitat[self.habitat] == self.comer:
            return True
        else:
            return False

    # Agregar Animal
    def agregarAnimal(self, habitatAnimal, alimentos, dietaHabitat):
        self.habitatAnimal = habitatAnimal
        self.alimentos = alimentos

        comprobante = self.ComprobanteListaHabitat(self.habitatAnimal)
        comprobante2 = self.ComprobanteAlimentos(self.alimentos)
        comprobante3 = self.ComprobanteHabitatAliementos(dietaHabitat)

        # Habitat que no coincide con los habitats agregados
        if comprobante == False:
            print("El Habitat del animal no coincide con los datos disponibles\n")
        # Alimento que no coincide con la alimentacion disponible
        if comprobante2 == False:
            print("El Alimento del animal no coincide con los datos disponibles\n")
        # Alimento que no coincide con el tipo de alimentacion que se le asignado al habitat
        if comprobante3 == False:
            print("El Alimento del animal no coincide con el alimento asignado en el habitat\n")
        else:
            self.contadorAnimal += 1
            ID = str(self.contadorAnimal)

            self.diccionarioAnimal["Nombre" + ID] = self.nombre
            self.diccionarioAnimal["Especie" + ID] = self.especie
            self.diccionarioAnimal["Habitat" + ID] = self.habitat
            self.diccionarioAnimal["Comer" + ID] = self.comer
            self.diccionarioAnimal["Juego" + ID] = self.juego.lower()
            self.diccionarioAnimal["Edad" + ID] = self.edad
            self.diccionarioAnimal["Dormir" + ID] = self.dormir

            print("Se agrego Correctamente\n")

    def mostrarAnimal(self):
        print("Lista Animales:")
        print(self.diccionarioAnimal, "\n")

    def cuposHabitatAnimal(self):
        ID = str(self.contadorAnimal)
        HabitatID = self.diccionarioAnimal["Habitat" + ID]
        ComerID = self.diccionarioAnimal["Comer" + ID]

        return HabitatID, ComerID

    def alimentarAnimales(self, alimentos):
        operacion2 = ""

        validacion1 = 0
        validacion2 = 0
        contadorAlimentos = -1
        encontrado = False

        self.dicAlimentos = alimentos

        self.mostrarAnimal()
        print("Lista de Alimentos:")
        print(self.dicAlimentos, "\n")

        while True:
            try:
                operacion = int(input("A Quien desea alimentar: ID -> "))
                operacion = str(operacion)
                break
            except ValueError:
                print("Error Se esperaba un INT y se a ingresado una cadena")
                print("Vuelva ingresar:")

        while True:
            try:
                operacion2 = input("Tipo de Alimento: -> ")
                int(operacion2)
                print("Error Se esperaba un Cadena y se a ingresado una INT")
                print("Vuelva ingresar:")
            except ValueError:
                break

        for clave, valor in self.dicAlimentos.items():
            if self.diccionarioAnimal["Comer" + operacion] == clave:
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
            print("Se dio de comer correctamente al ", self.diccionarioAnimal["Especie" + operacion])
            print("Se desea cambiar la alimentacion del ", self.diccionarioAnimal["Especie" + operacion])
            operacion3 = str(input("Respuesta: -> "))
            operacion3 = operacion3.lower()

            if operacion3 == "si":
                llave = self.diccionarioAnimal["Comer" + operacion]
                while True:
                    try:
                        operacion3 = input("Nueva alimentacion: -> ")
                        int(operacion3)
                        print("Error Se esperaba un Cadena y se a ingresado una INT")
                        print("Vuelva ingresar:")
                    except ValueError:
                        break

                self.dicAlimentos[llave][contadorAlimentos] = operacion3
                print("Se actualizo Correctamente\n")

        else:
            print("No se encontro el animal o el alimento no es correcto para el animal")

    def dormirAnimal(self):

        validacion1 = 0

        self.mostrarAnimal()
        while True:
            try:
                operacion = int(input("Escoja un animal: -> "))
                operacion = str(operacion)
                break
            except ValueError:
                print("Error Se esperaba un INT y se a ingresado una cadena")
                print("Vuelva ingresar:")

        while True:
            try:
                operacion2 = int(input("Cuantas horas Estima para el animal: : -> "))
                break
            except ValueError:
                print("Error Se esperaba un INT y se a ingresado una cadena")
                print("Vuelva ingresar:")

        guardaValor = self.diccionarioAnimal["Dormir" + operacion]
        guardaValor2 = self.diccionarioAnimal["Dormir" + operacion] * 2
        validacion1 = 1
        # manejar excepcion

        if validacion1 == 1:
            if guardaValor <= operacion2 <= guardaValor2:
                self.diccionarioAnimal["Dormir" + operacion] = operacion2
                print("Se cuadro correctamente las horas")

    def jugarAnimal(self):
        self.mostrarAnimal()

        while True:
            try:
                operacion = int(input("Escoja un animal: -> "))
                operacion = str(operacion)
                break
            except ValueError:
                print("Error Se esperaba un INT y se a ingresado una cadena")
                print("Vuelva ingresar:")

        if self.diccionarioAnimal["Juego" + operacion] == "no":
            self.diccionarioAnimal["Juego" + operacion] = "si"
            print("El animal a jugado")
        else:
            print("Ya ha jugado")
