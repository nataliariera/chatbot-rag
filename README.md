[README.md](https://github.com/user-attachments/files/23196843/README.md)
# **Chatbot RAG**

![Badge: Streamlit](https://img.shields.io/badge/Framework-Streamlit-red) 
![Badge: LangChain](https://img.shields.io/badge/NLP-LangChain-blue) 
![Badge: Pinecone](https://img.shields.io/badge/Embeddings-Pinecone-green) 
![Badge: OpenAI](https://img.shields.io/badge/API-OpenAI-lightblue) 


## **Descripción del proyecto**
Este chatbot está diseñado para operar como un sistema RAG (Retrieval-Augmented Generation) y utiliza como base de conocimiento un paper de investigación académica del área de la lingüística sobre la interacción entre humanos y chatbots.

Documento fuente: [acceso a la base de conocimiento](https://www.researchgate.net/publication/392355242_Interaccion_humanx-chatbot_estudio_exploratorio_sobre_variedades_linguisticas_acomodacion_y_desigualdadSpanish)


### **Tecnologías utilizadas**
- **LangChain:** para la integración del flujo conversacional.  
- **OpenAI:** generación de respuestas utilizando GPT.  
- **Pinecone:** para almacenar y buscar embeddings de los documentos.  
- **Streamlit:** interfaz interactiva y amigable para el usuario.

---

### Probar el proyecto

Visitar la versión desplegada del proyecto y probar todas sus funcionalidades en tiempo real. 

🔗 [Accede al proyecto aquí](https://chatbot-rag-ling.streamlit.app/)


### Algunas preguntas de ejemplo sobre el texto cargado para probar el funcionamiento:

1. ¿Cuál fue el propósito de iniciar la conversación con GPT y Gemini en el estudio?

2. ¿Qué tipo de acomodación se identificó en las conversaciones obtenidas?

3. ¿Cuál fue la diferencia entre la acomodación léxica y formal en GPT y Gemini?

4. ¿Cómo se superaron las dificultades en la acomodación del bot en el estudio?

5. ¿Por qué se eligieron trabajar con los chatbots ChatGPT de OpenAI y Gemini de Google DeepMind?

6. ¿Qué elementos se consideraron al diseñar los prompts para las interacciones?

7. ¿Qué tipo de pregunta se utilizó para precisar el uso de elementos léxicos en el estudio?

8. ¿Por qué se consideró fundamental incorporar un análisis cualitativo en el estudio?

9. ¿Qué variables se utilizaron en el experimento 2x2 factorial para analizar la acomodación comunicativa?

10. ¿Qué diferencias se observaron en la acomodación entre GPT y Gemini en el estudio?


## **Contenido del repositorio:**
* main.py: ejecución del programa

* funciones.py: llamadas desde main

* requirements.txt: dependencias necesarias

* upload_kb.py: carga de documentación, vectorización

* pdf: carpeta con documentos a cargar

## **Clonar el proyecto**
### **1. Prerrequisitos**  
- Python 3.9+  
- Tener configurados servicios externos como OpenAI y Pinecone.  
- Subir la base de conocimiento a Pinecone con upload_kb.py

### **2. Instalación de Dependencias**  

1. Crea un entorno virtual:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate # Si powershell tira error de politica, ejecutar: Set-ExecutionPolicy Bypass -Scope Process y luego venv\Scripts\activate

2. Instala las dependencias
    ```bash
    pip install -r requirements.txt

### **3. Configuración de Variables de Entorno**

1. En la raíz del proyecto, crear una carpeta llamada .streamlit.
2. Dentro de esta carpeta, crear un archivo secrets.toml con el siguiente formato:
    ```toml
    OPENAI_API_KEY = "tu_api_key"
    PINECONE_API_KEY = "tu_api_key"
    PINECONE_ENV = "nombre_de_tu_entorno"
    PINECONE_INDEX = "nombre_de_tu_indice"

### **4. Ejecución del Chatbot**
Una vez instaladas las dependencias y configuradas las variables, ejecutar para abrir la aplicación en navegador:
   ```bash
   streamlit run main.py
