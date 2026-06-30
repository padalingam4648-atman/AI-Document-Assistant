"""
rag_chain.py

Connects the Retriever, Prompt Builder, and LLM
to form the complete Retrieval-Augmented Generation pipeline.
"""

from src.retriever import search_documents
from src.prompt import build_prompt
from src.llm import generate_response


def ask(question: str) -> dict:
    """
    Execute the complete RAG pipeline.

    Parameters
    ----------
    question : str

    Returns
    -------
    dict
        {
            "answer": str,
            "documents": list
        }
    """

    # ------------------------------------
    # Step 1 : Retrieve Relevant Documents
    # ------------------------------------

    documents = search_documents(question)

    # ------------------------------------
    # Step 2 : Build Prompt
    # ------------------------------------

    prompt = build_prompt(question, documents)

    # ------------------------------------
    # Step 3 : Generate Answer
    # ------------------------------------

    answer = generate_response(prompt)

    return {

        "answer": answer,

        "documents": documents

    }