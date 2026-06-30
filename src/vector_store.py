"""
vector_store.py

Creates, saves, and loads the FAISS vector store.
"""

from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings

from src.config import Config


def create_vector_store(
    documents: list[Document],
    embedding_model: OllamaEmbeddings,
) -> FAISS:
    """
    Create a FAISS vector store from document chunks.

    Parameters
    ----------
    documents : list[Document]
        Chunked documents.

    embedding_model : OllamaEmbeddings
        Embedding model.

    Returns
    -------
    FAISS
        In-memory FAISS vector store.
    """

    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embedding_model
    )

    return vector_store


def save_vector_store(
    vector_store: FAISS,
) -> None:
    """
    Save the FAISS index locally.
    """

    save_path = Path(Config.FAISS_INDEX_DIR)

    save_path.mkdir(parents=True, exist_ok=True)

    vector_store.save_local(str(save_path))

    print(f"\n✅ Vector Store saved to:\n{save_path}\n")


def load_vector_store(
    embedding_model: OllamaEmbeddings,
) -> FAISS:
    """
    Load a saved FAISS vector store.
    """

    return FAISS.load_local(
        folder_path=str(Config.FAISS_INDEX_DIR),
        embeddings=embedding_model,
        allow_dangerous_deserialization=True
    )