class ComidaINIT:
    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo

    def getNombre(self):
        return self._nombre
    
    def getTipo(self):
        return self._tipo