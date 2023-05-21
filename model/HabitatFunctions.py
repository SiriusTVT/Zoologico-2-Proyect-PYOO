import streamlit as st

class Habitat:
    def __init__(self):
        if "nuevoHab" in st.session_state:
            self.nuevoHab = st.session_state["nuevoHab"]

        else:
            self.nuevoHab = []
            st.session_state["nuevoHab"] = []

    def agregarAnimal(self, animal):
        if animal is not None:
            (self.nuevoHab[animal[1]]).agregarAnimal(animal[0])
            st.session_state["nuevoHab"] = self.nuevoHab

            print("Se agrego Correctamente al habitat\n")


    def agregarHabitat(self, nuevoHabitat):
        if nuevoHabitat is not None:
            nuevoHabitat.setId(len(self.nuevoHab))
            self.nuevoHab.append(nuevoHabitat)
            st.session_state["nuevoHab"] = self.nuevoHab

            print("Se agrego Correctamente el habitat\n")

    def asignarHorario(self, horario, ids):
        if horario is not None and ids is not None:
            animalId = int(ids.split(".")[1])
            habitatId = int(ids.split(".")[0])
            self.nuevoHab[habitatId].asignarHorario(animalId, horario)
            st.session_state["nuevoHab"] = self.nuevoHab

            print("Se asigno Correctamente el horaripo\n")

    def getHabitats(self):
        return self.nuevoHab
    
    def getHabitat(self, id):
        return self.nuevoHab[id]
    
    def getHabitatsWith(self, habitatNombre, tipoAlimentacion, tempMin, tempMax):
        habitatsPosibles = []
        for habitat in self.nuevoHab:
            if habitatNombre == habitat.getTipoHabitat() and (tempMin <= habitat.getTemperatura() and tempMax >= habitat.getTemperatura()) and habitat.quedaCupo():
                for tipo in tipoAlimentacion:
                    if tipo in habitat.getTipoAliemntacion():
                        habitatsPosibles.append(habitat)
                        break

        return habitatsPosibles
