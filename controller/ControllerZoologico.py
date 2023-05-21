import streamlit as st


class ControllerZoologico:
    def __init__(self, modeloHab, modelCom, vista):
        self.modeloHab = modeloHab
        self.modelCom = modelCom
        self.vista = vista

    def menuStreamlit(self, entrada):
        if entrada == 1:
            st.divider()

            nuevoHabit = self.vista.crearHabitatStreamlit()

            self.modeloHab.agregarHabitat(nuevoHabit)

            self.vista.mostrarHabitatsAgregados()
        elif entrada == 2:

            st.divider()

            animal = self.vista.agregarAnimalStreamlit()

            self.modeloHab.agregarAnimal(animal)

        elif entrada == 3:
            st.divider()
            ids = self.vista.mostrarAnimales()

            horario = self.vista.inspeccionarAnimal(ids)

            self.modeloHab.asignarHorario(horario, ids)

        elif entrada == 4:
            st.divider()
            comida = self.vista.mostrarComidas()

            self.modelCom.agregarComida(comida)
