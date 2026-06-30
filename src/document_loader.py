"""
document_loader.py

Loads PDF documents from a user-selected directory.
"""

from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_documents(pdf_directory: Path) -> list[Document]:
    """
    Load all PDF documents from the given directory.

    Parameters
    ----------
    pdf_directory : Path
        Folder containing PDF files.

    Returns
    -------
    list[Document]
        List of LangChain Document objects.
    """

    documents = []

    pdf_files = list(pdf_directory.glob("*.pdf"))

    if not pdf_files:
        print("❌ No PDF files found.")
        return documents

    print(f"\n📚 Found {len(pdf_files)} PDF file(s).\n")

    for pdf in pdf_files:

        print(f"📄 Loading: {pdf.name}")

        loader = PyPDFLoader(str(pdf))

        docs = loader.load()

        documents.extend(docs)

    print(f"\n✅ Successfully loaded {len(documents)} page(s).\n")

    return documents