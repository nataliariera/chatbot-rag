# main.py: ejecución del programa

import streamlit as st
from funciones import obtener_respuesta_openai
from pathlib import Path

# 1) Personalizacion de interfaz (estilos, fuentes)
# Cargar CSS personalizado 
def load_custom_css():
    css_path = Path(".streamlit/custom.css")
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Llamada al inicio del programa
load_custom_css()

# Cabecera
st.markdown("<h2 style='text-align:center;'>Hola, soy tu asistente lector.</h2>", unsafe_allow_html=True)

# 2) Iniciar el programa
# Inicializar el historial en st.session_state si no existe con el mensaje de bienvenida
if "historial" not in st.session_state:
    st.session_state.historial = [
        {"role": "assistant", "content": "¿Qué te gustaría saber?"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.historial:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Preguntame lo que quieras"):
    # Add user message to chat history
    # st.session_state.historial.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display user message in chat message container
    with st.spinner('Espera un instante'):
        respuesta = obtener_respuesta_openai(prompt)
    with st.chat_message("assistant"):
        st.markdown(respuesta)



