import streamlit as st
import view.ZoologicoView as view

if __name__ == '__main__':
    st.set_page_config(
        page_title="Bioparque Vida Salvaje",
        layout="wide"
    )

    vista = view.ZoologicoView()
    vista.Zoologico()
