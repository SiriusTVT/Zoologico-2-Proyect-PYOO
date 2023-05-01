class ControllerZoologico:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def entradaMenu(self):
        self.modelo.entrada = self.vista.obtener_valor()
