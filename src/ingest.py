"""
ingest.py

Builds the complete FAISS knowledge base from documents.
"""

from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.embedding import create_embedding_model
from src.vector_store import (
    create_vector_store,
    save_vector_store,
)


def ingest_documents(folder_path: str):
    """
    Build the complete FAISS vector database.

    Parameters
    ----------
    folder_path : str
        Folder containing PDF files.

    Returns
    -------
    FAISS
        Saved vector store.
    """

    print("\n" + "=" * 60)
    print("STARTING DOCUMENT INGESTION")
    print("=" * 60)

    # -----------------------------------
    # Step 1 : Load Documents
    # -----------------------------------

    documents = load_documents(folder_path)

    # -----------------------------------
    # Step 2 : Split Documents
    # -----------------------------------

    chunks = split_documents(documents)

    # -----------------------------------
    # Step 3 : Create Embedding Model
    # -----------------------------------

    embedding_model = create_embedding_model()

    # -----------------------------------
    # Step 4 : Create Vector Store
    # -----------------------------------

    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    # -----------------------------------
    # Step 5 : Save FAISS
    # -----------------------------------

    save_vector_store(vector_store)

    print("\n" + "=" * 60)
    print("INGESTION COMPLETED SUCCESSFULLY")
    print("=" * 60)

    return vector_store