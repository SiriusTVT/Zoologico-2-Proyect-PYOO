class HabitatINIT:
    def __init__(self, tipoHabitat, tipoAlimentacion, cupos, temperatura):
        self._tipoHabitat = tipoHabitat
        self._tipoAlimentacion = tipoAlimentacion
        self._cupos = cupos
        self._animales = []
        self._temperatura = temperatura
        self._id = -1

    def agregarAnimal(self, animal):
        animal.setId(self.getOcupados())
        self._animales.append(animal)

    def getAnimales(self):
        return self._animales
    
    def getAnimal(self, id):
        return self._animales[id]

    def getTipoHabitat(self):
        return self._tipoHabitat
    
    def getTipoAliemntacion(self):
        return self._tipoAlimentacion
    
    def getCupos(self):
        return self._cupos
    
    def getTemperatura(self):
        return self._temperatura
    
    def getOcupados(self):
        return len(self._animales)
    
    def getProportion(self):
        return (f'{self.getOcupados()}/{self.getCupos()}')
    
    def quedaCupo(self):
        return self.getOcupados() < self._cupos
    
    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def asignarHorario(self, id, horario):
        self._animales[id].setHorario(horario)