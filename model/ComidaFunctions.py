import streamlit as st


class ComidaManager:
    def __init__(self):
        if "comidas" in st.session_state:
            self._comidas = st.session_state["comidas"]
        else:
            self._comidas = {}
            st.session_state["comidas"] = {}

    def getComida(self, nombre):
        return self._comidas[nombre]

    def agregarComida(self, comida):
        if comida is not None:
            self._comidas[comida.getNombre()] = comida
            st.session_state['comidas'] = self._comidas

    def getComidas(self):
        return list(self._comidas.keys())
    
    def getComidasWith(self, tipos):
        comidas = []
        for comida in self.getComidas():
            print(comida)
            if self._comidas[comida].getTipo() in tipos:
                print(comida)
                comidas.append(comida)
        print(comidas)
        return comidas