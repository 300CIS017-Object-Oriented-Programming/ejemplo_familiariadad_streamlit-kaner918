import streamlit as st
from controller.AppController import AppController


def mostrar():
    return """
        #### 
        Aplicación de **streamlit**.

        ####
        Ejemplo elaborado para @   por Luisa Rincón,  por parte de kaner murillo conrado.
        
        ###
        me gusta mucho este tema.\n
        quiero aprender y profundizar mas sobre el streamlit.\n
        gracias <3.
        """



# Main call
if __name__ == "__main__":
    st.write(mostrar())