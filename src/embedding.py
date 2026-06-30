"""
embedding.py

Creates the Ollama embedding model for the RAG pipeline.
"""

from langchain_ollama import OllamaEmbeddings

from src.config import Config


def create_embedding_model() -> OllamaEmbeddings:
    """
    Create and return the Ollama embedding model.

    Returns
    -------
    OllamaEmbeddings
        Configured embedding model.
    """

    embeddings = OllamaEmbeddings(
        model=Config.EMBEDDING_MODEL
    )

    return embeddings