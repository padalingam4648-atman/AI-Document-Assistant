"""
text_splitter.py

Splits loaded LangChain documents into smaller chunks
for embedding and retrieval.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from src.config import Config


def split_documents(documents: list[Document]) -> list[Document]:
    """
    Split loaded documents into smaller chunks.

    Parameters
    ----------
    documents : list[Document]
        Documents loaded from PDFs.

    Returns
    -------
    list[Document]
        Chunked documents.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ],
        length_function=len,
        is_separator_regex=False,
    )

    chunks = splitter.split_documents(documents)

    print("=" * 50)
    print("Text Splitter")
    print("=" * 50)
    print(f"Input Documents : {len(documents)}")
    print(f"Output Chunks   : {len(chunks)}")
    print("=" * 50)

    return chunks