import streamlit as st

import model.Zoologico as modelZoo
import model.Habitat as modelHab
import model.Animal as modelAnimal
import controller.ControllerZoologico as controller

class ZoologicoView:

    def __init__(self):
        self.habitat = 0
        self.zoologico = 0
        self.vista = 0
        self.animal = 0
        self.controlador = 0

    # def obtener_valorSTR(self, mensaje):
    #     respuesta = 0
    #     while True:
    #         try:
    #             respuesta = input(mensaje)
    #             int(respuesta)
    #             print("Error Se esperaba un Cadena y se a ingresado una INT")
    #             print("Vuelva ingresar:")
    #         except ValueError:
    #             break
    #
    #     return respuesta
    #
    # def obtener_valorINT(self, mensaje):
    #     while True:
    #         try:
    #             respuesta = int(input(mensaje))
    #             return respuesta
    #         except ValueError:
    #             print("Error Se esperaba un INT y se a ingresado una cadena")
    #             print("Vuelva ingresar:")

    def Zoologico(self, habitat, zoologico, vista, animal, controlador):
        self.habitat = habitat
        self.zoologico = zoologico
        self.vista = vista
        self.animal = animal
        self.controlador = controlador

        imagen = "img/Zoo_img1.jpeg"

        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(imagen, width=750, use_column_width=False)

        with col2:
            st.title("¡Bienvenido al Bioparque Vida Salvaje!")
            col1, col2 = st.columns(2)
            col1.header("Añadir-Habitat")
            botonAnimal = col1.button("Acceder a esta opción", 1)
            col2.header("Añadir-Animal")
            botoHabitat = col2.button("Acceder a esta opción", 2)

            col1, col2 = st.columns(2)
            col1.header("Mostrar-Animales")
            botonMostrarAnimal = col1.button("Acceder a esta opción", 3)
            col2.header("Mostrar-Alimentos")
            botonMostrarAlimentos = col2.button("Acceder a esta opción", 4)

        if botonAnimal:
            st.session_state["opcion"] = 1
        elif botoHabitat:
            st.session_state["opcion"] = 2
        elif botonMostrarAnimal:
            st.session_state["opcion"] = 3
        elif botonMostrarAlimentos:
            st.session_state["opcion"] = 4

        if "opcion" in st.session_state:
            self.controlador.menuStreamlit(st.session_state["opcion"])

    def crearHabitatStreamlit(self):
        validacion = 0
        with st.container():
            st.subheader("Formulario para crear un nuevo habitat")
            habitat = st.text_input("Habitat:")
            aliHabitat = st.text_input("Tipo de Alimentacion de habitat:")
            boton_accion = st.button("Crear nuevo habitat")

        if boton_accion:
            if habitat.isdigit() or habitat == "":
                raise ValueError("El Habitat debe ser un string y no puede estar vacio")
            if aliHabitat.isdigit() or aliHabitat == "":
                raise ValueError("El tipo de alimentacion debe ser un string y no puede estar vacio")

            self.habitat.entradaSTR = habitat
            self.habitat.entradaAlimento = aliHabitat

            self.mostrar_mensaje_exitoso("El producto fue creado correctamente")

            validacion = 1
            return validacion

    def mostrar_mensaje_exitoso(self, mensaje):
        st.success(mensaje)

    def mostrar_mensaje_error(self, mensaje):
        st.error(mensaje)
