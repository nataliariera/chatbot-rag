# upload_kb.py: carga de documentos

import os
import glob
import time
from pathlib import Path
from typing import List
import PyPDF2
from openai import OpenAI
import pinecone
import streamlit as st
import toml
from pathlib import Path

# 1) Configuración inicial: leer secrets.toml manualmente
secrets_path = Path("./.streamlit/secrets.toml")
secrets = toml.load(secrets_path)
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
PINECONE_ENV = st.secrets["PINECONE_ENV"]
PINECONE_INDEX = st.secrets["PINECONE_INDEX"]

# 2) Inicializar clientes
client = OpenAI(api_key=OPENAI_API_KEY)
from pinecone import Pinecone, ServerlessSpec

# 3) Inicializar la instancia de Pinecone
pc = Pinecone(
    api_key=PINECONE_API_KEY,
)

# 4) Conectarse al índice existente
index = pc.Index(PINECONE_INDEX)

# 5) Verificar estadísticas del índice (opcional)
stats = index.describe_index_stats()
print(stats)

# 6) Extraer texto de PDF
def extract_text_from_pdf(path: str) -> str:
    text_parts = []
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            try:
                text = page.extract_text() or ""
                text_parts.append(text)
            except Exception:
                continue
    return "\n".join(text_parts)

# 7) Chunking por caracteres
def chunk_text(text: str, max_chars: int = 1500) -> List[str]:
    chunks = []
    start = 0
    length = len(text)
    while start < length:
        end = start + max_chars
        chunk = text[start:end]
        # intentar no cortar palabra final (simple)
        if end < length:
            last_space = chunk.rfind(" ")
            if last_space > int(max_chars * 0.6):
                chunk = chunk[:last_space]
                end = start + last_space
        chunks.append(chunk.strip())
        start = end
    return [c for c in chunks if c]

# 8) Main: leer PDFs y subir la kb
def main():
    pdf_folder = Path("./pdf")
    pdf_folder.mkdir(exist_ok=True)
    pdf_paths = glob.glob(str(pdf_folder / "*.pdf"))
    if not pdf_paths:
        print("No hay PDFs en ./pdf/ — colocá tus archivos allí y reintentá.")
        return

    batch = []
    upsert_batch_size = 100  # upserts por llamada

    total = 0
    for pdf_path in pdf_paths:
        print("Procesando:", pdf_path)
        text = extract_text_from_pdf(pdf_path)
        chunks = chunk_text(text, max_chars=1200)
        for i, chunk in enumerate(chunks):
            # generar embedding
            emb_resp = client.embeddings.create(model="text-embedding-3-small", input=chunk)
            embedding = emb_resp.data[0].embedding

            meta = {
                "source": os.path.basename(pdf_path),
                "chunk_index": i,
                "text_snippet": chunk # guardar snippet como metadata
            }
            vector_id = f"{Path(pdf_path).stem}-{i}"
            batch.append((vector_id, embedding, meta))
            total += 1

            if len(batch) >= upsert_batch_size:
                index.upsert(vectors=batch)
                print(f"Upserted {len(batch)} vectors. Total so far: {total}")
                batch = []
                time.sleep(0.2)

    if batch:
        index.upsert(vectors=batch)
        print(f"Upserted final {len(batch)} vectors. Total: {total}")

    print("Upload finalizado. Vectores subidos:", total)

if __name__ == "__main__":
    main()
