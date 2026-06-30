"""
Configuration settings for the Local RAG project.
"""

from pathlib import Path


class Config:
    """
    Central configuration class.
    """

    # ==========================
    # Project Paths
    # ==========================

    BASE_DIR = Path(__file__).resolve().parent.parent

    DATA_DIR = BASE_DIR / "data"

    FAISS_INDEX_DIR = BASE_DIR / "faiss_index"

    # ==========================
    # Ollama Models
    # ==========================

    LLM_MODEL = "llama3.2"

    EMBEDDING_MODEL = "nomic-embed-text"

    # ==========================
    # Chunk Settings
    # ==========================

    CHUNK_SIZE = 1000

    CHUNK_OVERLAP = 200

    # ==========================
    # Retrieval
    # ==========================

    TOP_K = 3