"""
prompt.py

Builds the prompt that is sent to the LLM.
"""

from langchain_core.documents import Document


def format_context(documents: list[Document]) -> str:
    """
    Convert retrieved documents into formatted context.

    Parameters
    ----------
    documents : list[Document]

    Returns
    -------
    str
    """

    if not documents:
        return "No relevant context found."

    context = []

    for i, doc in enumerate(documents, start=1):

        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "Unknown")

        context.append(
            f"""
==============================
Document {i}

Source : {source}

Page   : {page}

Content:
{doc.page_content}
==============================
"""
        )

    return "\n".join(context)


def build_prompt(question: str, documents: list[Document]) -> str:
    """
    Build the final prompt for the LLM.

    Parameters
    ----------
    question : str

    documents : list[Document]

    Returns
    -------
    str
    """

    context = format_context(documents)

    prompt = f"""
You are an intelligent AI Document Assistant.

Your job is to answer the user's question ONLY using the
information available in the provided context.

Instructions:

1. Use only the provided context.
2. Do not make up information.
3. If the answer is not found, reply:
   "I couldn't find the answer in the provided documents."
4. Summarize clearly.
5. Use bullet points whenever appropriate.
6. Mention important technologies, tools, or project names.
7. Keep the answer professional and easy to understand.

============================================================
CONTEXT
============================================================

{context}

============================================================
QUESTION
============================================================

{question}

============================================================
ANSWER
============================================================
"""

    return prompt