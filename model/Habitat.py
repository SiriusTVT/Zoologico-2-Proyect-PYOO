class Habitat:
    def __init__(self):
        self.entradaSTR = ""
        self.listaHabitats = ["desertico", "selvatico", "polar", "acuatico"]
        self.AdHabitat = []

        self.cupos = {"desertico":0,"selvatico":0, "polar":0, "acuatico":0}
        # cantidad de animales asignados en cada habitat
        self.dietaHabitat = {"desertico":[],"selvatico":[], "polar":[], "acuatico":[]}
        # los tipos de dieta que se encuentran en esa habitat

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

    #Agregar Habitat
    def agregarHabitat(self):

        existe = self.ComprobanteListaHabitat(self.entradaSTR)
        comprobante = self.Comprobante(self.entradaSTR)

        if existe == False and comprobante == True:
            self.AdHabitat.append(self.entradaSTR)
            print("Se agrego Correctamente\n")

        elif existe == True:
            print("El Dato YA EXISTE\n")

        else:
            print("El dato no coincide con los habitas disponibles\n")

    def mostrarCupos(self):
        print("Cupos en Zoologico")
        print(self.cupos, "\n")
        print("Dietas Segun su Habitat")
        print(self.dietaHabitat, "\n")