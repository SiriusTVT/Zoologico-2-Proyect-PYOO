class Habitat:
    def __init__(self):
        self.entradaSTR = ""
        self.entradaAlimento = ""
        self.listaHabitats = ["desertico", "selvatico", "polar", "acuatico"]
        self.AdHabitat = []

        self.cupos = {"desertico": 0, "selvatico": 0, "polar": 0, "acuatico": 0}
        self.dietaHabitat = {"desertico": "", "selvatico": "", "polar": "", "acuatico": ""}
        # los tipos de dieta que se permiten en esa habitat

    def Comprobante(self, habitat):
        for i in self.listaHabitats:
            if i == habitat.lower():
                return True
        return False

    def ComprobanteListaHabitat(self, habitat):
        for i in self.AdHabitat:
            if i == habitat:
                return True
        return False

    # Comprueba el tipo de alimentacion del habitat existe en la dieta disponible
    def ComprobanteAlimentos(self, alimentos):
        for clave, valor in alimentos.items():
            if self.entradaAlimento == clave and self.dietaHabitat[self.entradaSTR] == "":
                return True
        return False

    # Tipo de alimentacion para un habitat
    def AlimentoHabitat(self, alimentosDispo):

        comprobante = self.ComprobanteAlimentos(alimentosDispo)
        if comprobante:
            self.dietaHabitat[self.entradaSTR] = self.entradaAlimento
            print("Se agrego Correctamente el alimento para esa habitat\n")

        else:
            print("El dato no coincide con la alimentacion\n")

    # Agregar Habitat
    def agregarHabitat(self):
        validacion = 0
        existe = self.ComprobanteListaHabitat(self.entradaSTR)
        comprobante = self.Comprobante(self.entradaSTR)

        if existe == False and comprobante == True:
            self.AdHabitat.append(self.entradaSTR)
            print("Se agrego Correctamente el habitat\n")
            validacion = 1
            return validacion


        elif existe == True:
            print("El Dato YA EXISTE\n")

        else:
            print("El dato no coincide con los habitas disponibles\n")

    def mostrarCupos(self):
        print("Cupos en Zoologico")
        print(self.cupos, "\n")
        print("Dietas Segun su Habitat")
        print(self.dietaHabitat, "\n")
