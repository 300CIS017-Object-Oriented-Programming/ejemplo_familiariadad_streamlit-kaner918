import streamlit as st

def probar_streamlit():
    """ Ponga aqui todos los controles de prueba para que entienda como funciona"""
    st.write("Agregue aquí botones, paneles, y opciones tal como se describe en el readme")
    boton = st.button("Soy un boton")

    agree = st.checkbox("quieres saludar a la profe ? ")
    if agree:

        st.write("hola profe, como estas ?")

    option = st.selectbox(
        "como queires que te contactemos",
        ('Email', 'numero de telefono'))

    title = st.text_input(option)
    number = st.number_input('seleccione su edad')

# Main call
if __name__ == "__main__":
    probar_streamlit()