"""
retriever.py

Handles semantic retrieval from the FAISS vector database.
"""

from langchain_core.documents import Document

from src.config import Config
from src.embedding import create_embedding_model
from src.vector_store import load_vector_store


def create_retriever():
    """
    Load the FAISS vector store and create a retriever.

    Returns
    -------
    BaseRetriever
        LangChain retriever.
    """

    embedding_model = create_embedding_model()

    vector_store = load_vector_store(embedding_model)

    retriever = vector_store.as_retriever(

        search_type="similarity",

        search_kwargs={

            "k": Config.TOP_K

        }
    )

    return retriever


def search_documents(question: str) -> list[Document]:
    """
    Search relevant documents.

    Parameters
    ----------
    question : str

    Returns
    -------
    list[Document]
    """

    retriever = create_retriever()

    documents = retriever.invoke(question)

    return documents