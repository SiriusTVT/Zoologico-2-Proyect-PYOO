from model.Animal import Animal
A = Animal(None,None,None,None,None,None,None)
from model.Habitat import Habitat
h = Habitat(None,None)

class Zoologico:


    def Comprobante(self, habitat):
        for i in h.listaHabitats:
            if i == habitat.lower():
                return True
        return False
    def ComprobanteListaHabitat(self, habitat):
        for i in h.AdHabitat:
            if i == habitat:
                return True
        return False

    #Agregar Habitat
    def agregarHabitat(self):

        existe = self.ComprobanteListaHabitat(h.entradaSTR)
        comprobante = self.Comprobante(h.entradaSTR)

        if existe == False and comprobante == True:
            h.AdHabitat.append(h.entradaSTR)
            print("Se agrego Correctamente\n")

        elif existe == True:
            print("El Dato YA EXISTE\n")

        else:
            print("El dato no coincide con los habitas disponibles\n")

    #Agregar Animal

    def agregarAnimal(self):
        comprobante = self.Comprobante(A.habitat)

