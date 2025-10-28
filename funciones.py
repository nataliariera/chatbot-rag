### funciones.py: funciones que toma main

import streamlit as st
from pinecone import Pinecone
from langchain_openai import OpenAIEmbeddings
import openai

# 1) Configuraciones OpenAI
# Obtener key
openai.api_key = st.secrets["OPENAI_API_KEY"]
# Definir el modelo de embeddings de OpenAI
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# 2) Configuraciones Pinecone
# Inicializar instancia
from pinecone import Pinecone
pc = Pinecone(api_key=st.secrets["PINECONE_API_KEY"])
# Nombre del índice de Pinecone
index_name = st.secrets.get("PINECONE_INDEX", "rag01-index")
# Conectar al índice existente
index = pc.Index(index_name)

# 3) Generar función para obtener un embedding a partir de una pregunta
def obtener_embedding(pregunta):
    embedding = embeddings.embed_query(pregunta)
    return embedding

## (deprecar si funciona el session state)
## Inicializa una lista global para el historial de mensajes
## historial = []

def obtener_respuesta_openai(pregunta: str, top_k=5):
# Obtener el embedding de la pregunta
    embedding_pregunta = obtener_embedding(pregunta)
# Buscar los vectores más similares en Pinecone
    response = index.query(vector=embedding_pregunta,
                           top_k=top_k, include_metadata=True)
# Extraer los documentos más relevantes (cuando los metadatos contienen los textos)
    documentos_relevantes = [
    match.get('metadata', {}).get('text') or match.get('metadata', {}).get('text_snippet', '')
    for match in response['matches']
    ]

# Crear un contexto a partir de los documentos relevantes
    contexto = "\n".join(documentos_relevantes)
    pregunta_and_contexto = {
        "role": "user",
        "content": f"Pregunta: {pregunta}\n\nContexto:\n{contexto}"
    }

    # Mantener solo los últimos N mensajes para evitar sobrecargar el modelo
    N = 20  # Este valor se ajusta según la cantidad de memoria a mantener
    st.session_state.historial = st.session_state.historial[-N:]

    # Formatear el historial como texto para incluirlo en el mensaje del sistema
    historial_texto = "\n".join([f"{mensaje['role']}: {mensaje['content']}"
                                 for mensaje in st.session_state.historial])

    # Obtener la respuesta de OpenAI usando el historial
    respuesta_openai = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",  # Modelo a usar
        messages=[
            {"role": "system",
             "content": f"""
                 Eres una asistente en linguística, especializada en análisis sintático, semántico y morfológico.
                 Si se pregunta por alguno de estos temas, dile que atenderás su consulta con gusto.
                 Si la consulta está fuera de contexto, informa amablemente que no puedes ayudar con esa solicitud.
                 Solo responde con información sobre los documentos cargados o sobre linguística.
                 Ten en cuenta el siguiente historial de mensajes anteriores y utilízalos como memoria:{historial_texto}"""}
        ] + [pregunta_and_contexto],  # Agregar el historial completo
        max_tokens=1500,  # Ajustar según necesario
        temperature=0.1
    )
    # Obtener la respuesta del modelo
    respuesta = respuesta_openai.choices[0].message.content.strip()
    respuesta = respuesta.replace("$", "\\$")

    # Agregar el nuevo mensaje del usuario al historial
    st.session_state.historial.append({"role": "user", "content": pregunta})

    # Agrega la respuesta al historial
    st.session_state.historial.append(
        {"role": "assistant", "content": respuesta})

    return (respuesta)
