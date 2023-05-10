class ZoologicoView:
    def obtener_valorSTR(self, mensaje):
        respuesta = 0
        while True:
            try:
                respuesta = input(mensaje)
                int(respuesta)
                print("Error Se esperaba un Cadena y se a ingresado una INT")
                print("Vuelva ingresar:")
            except ValueError:
                break

        return respuesta

    def obtener_valorINT(self, mensaje):
        while True:
            try:
                respuesta = int(input(mensaje))
                return respuesta
            except ValueError:
                print("Error Se esperaba un INT y se a ingresado una cadena")
                print("Vuelva ingresar:")
