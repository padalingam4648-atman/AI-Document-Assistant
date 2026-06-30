"""
llm.py

Handles interaction with the Ollama Large Language Model.
"""

from langchain_ollama import ChatOllama

from src.config import Config


def create_llm():
    """
    Create the Ollama LLM instance.

    Returns
    -------
    ChatOllama
    """

    llm = ChatOllama(

        model=Config.LLM_MODEL,

        temperature=0.2,

    )

    return llm


def generate_response(prompt: str) -> str:
    """
    Generate a response from the LLM.

    Parameters
    ----------
    prompt : str

    Returns
    -------
    str
    """

    llm = create_llm()

    response = llm.invoke(prompt)

    return response.content