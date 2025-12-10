[README.md](https://github.com/user-attachments/files/23196843/README.md)
# **Chatbot RAG**

Framework: Streamlit | NLP: LangChain | Embeddings: Pinecone | API: OpenAI

## **Descripción del proyecto**
Este proyecto implementa un chatbot basado en RAG (Retrieval-Augmented Generation).

El modelo combina generación de lenguaje con un sistema de recuperación de información, lo cual permite responder preguntas utilizando como base de conocimiento, en este caso, un paper académico del área de la lingüística, centrado en la interacción entre humanos y chatbots.

El objetivo es explorar cómo integrar contenido especializado dentro de un flujo conversacional y ofrecer respuestas basadas en una fuente científica. 

Documento fuente: Salerno, Paula & Vilar, Milagros. (2025). Interacción humanx-chatbot : estudio exploratorio sobre variedades lingüísticas, acomodación y desigualdad Spanish. Matraga - Revista do Programa de Pós-Graduação em Letras da UERJ. 32. 266-289. 10.12957/matraga.2025.88189.

Disponible en: [acceso a la base de conocimiento](https://www.researchgate.net/publication/392355242_Interaccion_humanx-chatbot_estudio_exploratorio_sobre_variedades_linguisticas_acomodacion_y_desigualdadSpanish)


### **Tecnologías utilizadas**
- **LangChain:** integración del flujo conversacional.  
- **OpenAI:** generación de respuestas utilizando GPT.  
- **Pinecone:** almacenamiento y búsqueda de embeddings del documento fuente.  
- **Streamlit:** interfaz interactiva para el usuario.

---

### Probar el proyecto

Visitar la versión desplegada del proyecto y probar todas sus funcionalidades en tiempo real. 

[Acceder al proyecto aquí](https://chatbot-rag-ling.streamlit.app/)


### Algunas preguntas de ejemplo sobre el documento cargado para probar el funcionamiento:

1. ¿Cuál fue el propósito de iniciar la conversación con GPT y Gemini en el estudio?

2. ¿Qué tipo de acomodación se identificó en las conversaciones obtenidas?

3. ¿Cuál fue la diferencia entre la acomodación léxica y formal en GPT y Gemini?

4. ¿Cómo se superaron las dificultades en la acomodación del bot en el estudio?

5. ¿Por qué se optó por trabajar con los chatbots ChatGPT de OpenAI y Gemini de Google DeepMind?

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

1. Crear un entorno virtual:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate # Si powershell tira error de politica, ejecutar: Set-ExecutionPolicy Bypass -Scope Process y luego venv\Scripts\activate

2. Instalar las dependencias
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

1. Una vez instaladas las dependencias y configuradas las variables de entorno, ejecutar el siguiente comando para abrir la aplicación en el navegador:
    ```bash
    streamlit run main.py
    ```


### **5. Próximos pasos del proyecto**
* Analizar el lenguaje utilizado en las respuestas generadas por el chatbot para identificar patrones, sesgos y características lingüísticas.
* Evaluar la calidad de las respuestas mediante métricas de recuperación y generación.
* Comparar distintos modelos de búsqueda semántica.
* Mejorar la extracción de fragmentos relevantes para optimizar la etapa de retrieval.
* Ajustar un modelo para detectar intenciones y clasificar preguntas.
* Integrar herramientas de análisis lingüístico (POS tagging, dependencias, análisis pragmático).

### **Contact me**

<a href="https://www.linkedin.com/in/nataliariera/">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="25"/>
</a>

<a href="https://www.instagram.com/tradunati/">
  <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/instagram.svg" width="25"/>
</a>

