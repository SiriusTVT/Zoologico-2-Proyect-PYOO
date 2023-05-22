import streamlit as st
import datetime

import model.HabitatFunctions as modelHab
import controller.ControllerZoologico as controller
import model.ComidaFunctions as modelCom
import model.Comida as comida_INIT
import model.Habitat as Hab_INIT
import model.Animal as Animal_INIT


class ZoologicoView:
    def __init__(self):
        self.habitat = modelHab.Habitat()
        self.comida = modelCom.ComidaManager()
        self.controlador = controller.ControllerZoologico(self.habitat, self.comida, self)

    def Zoologico(self):  # Menu inicial del Zoologico

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

            col1.header("Mostrar-Animales")
            botonMostrarAnimal = col1.button("Acceder a esta opción", 3)
            col2.header("Mostrar-Alimentos")
            botonMostrarAlimentos = col2.button("Acceder a esta opción", 4)
            st.divider()
            botonInf = col1.button("Mas informacion")

        if botonAnimal:
            st.session_state["opcion"] = 1
        elif botoHabitat:
            st.session_state["opcion"] = 2
        elif botonMostrarAnimal:
            st.session_state["opcion"] = 3
        elif botonMostrarAlimentos:
            st.session_state["opcion"] = 4
        elif botonInf:
            st.session_state["opcion"] = 5

        if "opcion" in st.session_state:
            self.controlador.menuStreamlit(st.session_state["opcion"])

    def crearHabitatStreamlit(self):  # Crear nuevo habitat
        with st.container():
            st.subheader("Formulario para crear un nuevo habitat")
            tipoHabitat = st.selectbox("Habitat:", ("", "Desértico", "Selvático", "Polar", "Acuático"))
            tiposComida = []
            if tipoHabitat == "Desértico":
                tiposComida = ["", "Concentrado", "Carne"]
            elif tipoHabitat == "Selvático":
                tiposComida = ["", "Concentrado", "Carne", "Frutas"]
            elif tipoHabitat == "Polar":
                tiposComida = ["", "Pescado", "Carne"]
            elif tipoHabitat == "Acuático":
                tiposComida = ["", "Pescado", "vegetal"]
            else:
                tiposComida = [""]

            tipoAlimentacion = st.selectbox("Tipo de Alimentacion de habitat:", tiposComida)

            cupos = st.slider("Maximo numero de animales:", 0, 15, 5, 1)

            temperatura = st.slider("Temperatura del habitat: ", -20, 30, 18, 1)
            extra = {}
            st.subheader("Otras opciones")
            if tipoHabitat == "Desértico":
                extra["Lago"] = "Si" if st.checkbox("Laguito") else "No"
                extra["Piedra"] = "Si" if st.checkbox("Monticulo de piedra") else "No"
            elif tipoHabitat == "Selvático":
                extra["Sonidos de ambientacion"] = "Si" if st.checkbox("Sonidos de ambientacion") else "No"
                extra["Vegetacion"] = {}
                vegetaciones = ["Arboles", "Arbustos", "Flores"]
                st.write("Vegetacion del habitat:")
                numero = 0
                for veg in vegetaciones:
                    extra["Vegetacion"][veg] = "Si" if st.checkbox(f'{veg}', key=f'veg{numero}') else "No"
                    numero += 1
            elif tipoHabitat == "Polar":
                extra["Iluminacion"] = st.select_slider("Tipo de iluminacion:", ["OLED", "LED", "Bombillas"])
                extra["Agua"] = "Si" if st.checkbox("Agua en el habitat") else "No"
            elif tipoHabitat == "Acuático":
                extra["Iluminacion"] = st.slider("Intencidad de luz", 0, 100, 80, 1)
                extra["Decoracion"] = {}
                decoraciones = ["Algas", "Corales", "Estrella de mar", "Cofre de tesoro", "Corales"]
                st.write("Decoraciones del habitat:")
                numero = 0
                for dec in decoraciones:
                    extra["Decoracion"][dec] = "Si" if st.checkbox(f'{dec}', key=f'dec{numero}') else "No"
                    numero += 1
            boton_accion = st.button("Crear nuevo habitat")

        if boton_accion:
            if tipoHabitat == "":
                self.mostrar_mensaje_error("El Habitat no puede estar vacio")
            elif tipoAlimentacion.isdigit() or tipoAlimentacion == "":
                self.mostrar_mensaje_error("El tipo de alimentacion no puede estar vacio")
            else:
                nuevoHabitat = Hab_INIT.HabitatINIT(tipoHabitat, tipoAlimentacion, cupos, temperatura, extra)

                self.mostrar_mensaje_exitoso("El Habitat fue creado correctamente")
                return nuevoHabitat

    def agregarAnimalStreamlit(self):  # Crear nuevo Animal
        with st.container():
            st.subheader("Formulario para añadir un nuevo animal")
            tipoAnimal = st.text_input("Tipo de animal:")
            nombre = st.text_input("Nombre del animal")
            edad = st.slider("Edad:", 0, 100, 0, 1)
            habitat = st.selectbox("Habitat de residencia:", ("", "Desértico", "Selvático", "Acuático", "Polar"))
            tipoAlimentacion = st.select_slider("Tipo de alimentacion:", ("Carnivoro", "Omnivoro", "Herbivoro"))
            tempMin = st.slider("Temperatura minima necesaria", -20, 30, 18, 1)
            tempMax = st.slider("Temperatura maxima necesaria", tempMin, 30, 18, 1)

            st.write("Que come:")
            pescado = False
            carne = False
            fruta = False
            vegetal = False
            concentrado = False
            if tipoAlimentacion in ["Carnivoro", "Omnivoro"]:
                pescado = st.checkbox("Pescado")
                carne = st.checkbox("Carne")
            if tipoAlimentacion in ["Herbivoro", "Omnivoro"]:
                fruta = st.checkbox("Fruta")
                vegetal = st.checkbox("vegetal")
                concentrado = st.checkbox("Concentrado")

            comidas = []
            if pescado:
                comidas.append("Pescado")
            if carne:
                comidas.append("Carne")
            if fruta:
                comidas.append("Fruta")
            if vegetal:
                comidas.append("vegetal")
            if concentrado:
                comidas.append("Concentrado")

            st.write()
            habitatsPos = self.habitat.getHabitatsWith(habitat, comidas, tempMin, tempMax)
            habsDesc = [
                f'{hab.getId()}: {hab.getTipoHabitat()}, cupos: {hab.getProportion()}, alimentacion: {hab.getTipoAliemntacion()}, temperatura: {hab.getTemperatura()}'
                for hab in habitatsPos]
            habSelect = st.radio("Posiles habitats:", habsDesc)

            boton_accion = st.button("Añadir animal")

        if boton_accion:
            comidas = []
            if tipoAnimal.isdigit():
                self.mostrar_mensaje_error("Los numeros no son un tipo de animal valido")
            elif tipoAnimal == "":
                self.mostrar_mensaje_error("Escribe el tipo de animal")
            elif nombre == "":
                self.mostrar_mensaje_error("Dale un nombre al " + tipoAnimal)
            elif habitat == "":
                self.mostrar_mensaje_error("Escoge un habitat")
            elif not (pescado or carne or fruta or vegetal or concentrado):
                self.mostrar_mensaje_error("Escoge un tinpo de alimentacion")
            elif habSelect is None:
                self.mostrar_mensaje_error("Debes escoger un  habitat")
            else:
                comidas = []
                if pescado:
                    comidas.append("Pescado")
                if carne:
                    comidas.append("Carne")
                if fruta:
                    comidas.append("Fruta")
                if vegetal:
                    comidas.append("vegetal")
                if concentrado:
                    comidas.append("Concentrado")
                habId = int(habSelect.split(":")[0])
                animal = Animal_INIT.AnimalINIT(nombre, tipoAnimal, edad, tipoAlimentacion, comidas, tempMin, tempMax)

                self.mostrar_mensaje_exitoso("El Animal fue agregado correctamente")
                return [animal, habId]

    def mostrarHabitatsAgregados(self):  # Mostrar habitats Agregados
        st.divider()
        with st.container():
            st.header("Habitats")
            for hab in self.habitat.getHabitats():
                if hab is not None:
                    expander = st.expander(hab.getTipoHabitat())
                    col1, col2 = expander.columns(2)
                    col1.write(f'id: {hab.getId()}')
                    if hab.quedaCupo():
                        col1.write(f'Ocupacion: **:green[{hab.getProportion()}]**')
                    else:
                        col1.write(f'Ocupacion: **:green[{hab.getProportion()}]**')
                    col2.write(f'Alimento del habitat: {hab.getTipoAliemntacion()}')
                    if hab.getTemperatura() > 0:
                        col2.write(f'Temperatura: **:green[{hab.getTemperatura()}]**')
                    else:
                        col2.write(f'Temperatura: **:blue[{hab.getTemperatura()}]**')
                    extras = hab.getExtra()
                    numero = 0
                    for extra in extras.keys():
                        if numero % 2 != 0:
                            if type(extras[extra]) == dict:
                                col1.write(extra)
                                for ex in extras[extra].keys():
                                    col1.write(f'{ex}: **:green[{extras[extra][ex]}]**')
                            else:
                                col1.write(f'{extra}: **:green[{extras[extra]}]**')
                        else:
                            if type(extras[extra]) == dict:
                                col2.write(extra)
                                for ex in extras[extra].keys():
                                    col2.write(f'{ex}: **:green[{extras[extra][ex]}]**')
                            else:
                                col2.write(f'{extra}: **:green[{extras[extra]}]**')
                        numero += 1

    def mostrarAnimales(self):  # Mostrar animales agregados
        with st.container():
            animales = []
            for hab in self.habitat.getHabitats():
                st.write()
                animales.extend(
                    [f'{hab.getId()}.{animal.getId()}; Habitat: {hab.getTipoHabitat()} | Nombre: {animal.getNombre()}'
                     for animal in hab.getAnimales()])
            animalSelec = st.radio("Animales", animales)

        if animalSelec is not None:
            ids = animalSelec.split(";")[0]
            return ids

    def inspeccionarAnimal(self, ids):  # Acciones del Zoologico
        st.divider()
        if ids is not None:
            animalId = int(ids.split(".")[1])
            habitatId = int(ids.split(".")[0])
            animal = self.habitat.getHabitat(habitatId).getAnimal(animalId)
            with st.container():
                col1, col2 = st.columns(2)
                col1.header(animal.getNombre())
                col1.subheader("Especie:")
                col1.write(animal.getTipoAnimal())
                col1.subheader("Edad:")
                col1.write(f'{animal.getEdad()}')
                col1.subheader("Tipo de alimentacion:")
                col1.write(animal.getTipoAlimentacion())
                col1.subheader("Comidas:")
                for comida in animal.getComidas():
                    col1.write(f'{comida}')

                col1.subheader("Temperaturas aceptadas:")
                if animal.getTempMin() < 0:
                    tempMin = f'**:blue[{animal.getTempMin()}]**'
                else:
                    tempMin = f'**:green[{animal.getTempMin()}]**'
                if animal.getTempMax() < 0:
                    tempMax = f'**:blue[{animal.getTempMax()}]**'
                else:
                    tempMax = f'**:green[{animal.getTempMax()}]**'
                col1.write(f'{tempMin} - {tempMax} C')

                col1.subheader("Horarios")
                if len(animal.getHorarios()["jugar"]) > 0:
                    juExpander = col1.expander("Jugar")
                    juExpander.write(f'**:green[Hora inicion:]** {animal.getHorarios()["jugar"][0]["inicio"]}')
                    juExpander.write(f'**:red[Hora final:]** {animal.getHorarios()["jugar"][0]["final"]}')
                if len(animal.getHorarios()["dormir"]) > 0:
                    dorExpander = col1.expander("Dormir")
                    dorExpander.write(f'**:green[Hora inicion:]** {animal.getHorarios()["dormir"][0]["inicio"]}')
                    dorExpander.write(f'**:red[Hora final:]** {animal.getHorarios()["dormir"][0]["final"]}')
                for comida in animal.getHorarios()["comer"]:
                    comExpander = col1.expander("Comida")
                    comExpander.write(f'**:green[Hora:]** {comida["inicio"]}')
                    comExpander.write(f'**:blue[Comida:]** {comida["extra"]["comida"]}')
                    comExpander.write(f'**:orange[Porciones:]** {comida["extra"]["porciones"]}')

                # col2.image()
                porSelec = col2.slider("Porciones de comida:", 1, 10, 1, 1)
                comSelec = col2.selectbox("Comida: ", self.comida.getComidasWith(animal.getComidas()))
                timeSelecCom = col2.time_input('Hora de la comida', datetime.time(7, 30))
                aliButton = col2.button("Alimentar")
                timeSelecDorIn = col2.time_input('Hora de inicio', datetime.time(7, 0))
                timeSelecDorFin = col2.time_input('Hora de finalizacion', datetime.time(9, 0))
                dorButton = col2.button("Dormir")
                timeSelecJuIn = col2.time_input('Hora de inicio', datetime.time(8, 0))
                timeSelecJuFin = col2.time_input('Hora de finalizacion', datetime.time(8, 30))
                juButton = col2.button("Jugar")

                if juButton:
                    if datetime.time(6, 30) > timeSelecJuIn > timeSelecJuFin > datetime.time(18,
                                                                                             30):
                        self.mostrar_mensaje_error("Tiempos no validos")
                    else:
                        horario = {
                            "tipo": "jugar",
                            "inicio": timeSelecJuIn,
                            "final": timeSelecJuFin,
                            "extra": {
                            }
                        }
                        return horario

                if aliButton:
                    if datetime.time(6, 30) > timeSelecCom > datetime.time(18, 30):
                        self.mostrar_mensaje_error("En estos tiempos no esta permitida la comida")
                    else:
                        horario = {
                            "tipo": "comer",
                            "inicio": timeSelecCom,
                            "final": timeSelecCom,
                            "extra": {
                                "comida": comSelec,
                                "porciones": porSelec
                            }
                        }
                        return horario

                if dorButton:
                    if timeSelecDorIn < datetime.time(18, 30) or timeSelecDorFin > datetime.time(22, 0):
                        self.mostrar_mensaje_error("Acostado fuera de tiempo")
                    elif not (timeSelecDorIn <= datetime.time(6, 0) or timeSelecDorIn >= timeSelecDorIn):
                        self.mostrar_mensaje_error("Tiempo no valido")
                    else:
                        horario = {
                            "tipo": "dormir",
                            "inicio": timeSelecDorIn,
                            "final": timeSelecDorFin,
                            "extra": {
                            }
                        }
                        return horario

    def mostrarComidas(self): # Mostrar alimento agregado
        with st.container():
            st.header("Comidas")
            col1, col2 = st.columns(2)
            col1.subheader("Nuevo alimento")
            nombre = col1.text_input("Nombre del alimento:")
            tipo = col1.select_slider("Tipo de alimento:", ["Pescado", "Carne", "Fruta", "vegetal", "Concentrado"])
            button = col1.button("Agregar")

            for comida in self.comida.getComidas():
                expander = col2.expander(f'{comida}:')
                expander.write(self.comida.getComida(comida).getTipo())

            if button:
                if nombre == "":
                    self.mostrar_mensaje_error("El nombre no puede estar vacio")
                elif not nombre.isalnum():
                    self.mostrar_mensaje_error("Los caracteres no son validos")
                else:
                    nombre = nombre.upper()
                    if nombre in self.comida.getComidas():
                        self.mostrar_mensaje_error("Comida ya existente")
                    else:
                        comida = comida_INIT.ComidaINIT(nombre, tipo)
                        self.mostrar_mensaje_exitoso("Nueva comida creada")
                        return comida

    def masInformacion(self):
        pass

    def mostrar_mensaje_exitoso(self, mensaje):
        st.success(mensaje)

    def mostrar_mensaje_error(self, mensaje):
        st.error(mensaje)
