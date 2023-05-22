class AnimalINIT:
    def __init__(self, nombre, tipoAnimal, edad, tipoAlimentacion, comidas, tempMin, tempMax):
        self._nombre = nombre
        self._tipoAnimal = tipoAnimal
        self._edad = edad
        self._tipoAlimentacion = tipoAlimentacion
        self._comidas = comidas
        self._vida = 100
        self._id = -1
        self._tempMin = tempMin
        self._tempMax = tempMax
        self._horarios = {
            "jugar": [],
            "comer": [],
            "dormir": []
        }

    def getHorarios(self):
        return self._horarios

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getTipoAlimentacion(self):
        return self._tipoAlimentacion

    def getComidas(self):
        return self._comidas

    def getTipoAnimal(self):
        return self._tipoAnimal

    def getId(self):
        return self._id

    def getTempMin(self):
        return self._tempMin

    def getTempMax(self):
        return self._tempMax

    def setId(self, id):
        self._id = id

    def setHorario(self, horario):
        if horario["tipo"] == "dormir" or horario["tipo"] == "jugar":
            self._horarios[horario["tipo"]] = []
        self._horarios[horario["tipo"]].append(horario)
