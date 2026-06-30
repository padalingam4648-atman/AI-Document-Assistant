"""
app.py

Main entry point for the Local RAG AI Document Assistant.
"""

from src.ingest import ingest_documents
from src.rag_chain import ask
from src.utils import get_pdf_directory


def build_knowledge_base():
    """
    Build the FAISS vector database.
    """

    print("\n" + "=" * 70)
    print("LOCAL RAG - KNOWLEDGE BASE")
    print("=" * 70)

    folder = get_pdf_directory()

    ingest_documents(folder)

    print("\nKnowledge Base Created Successfully!\n")


def chat():
    """
    Interactive RAG Chat.
    """

    print("\n" + "=" * 70)
    print("LOCAL RAG DOCUMENT ASSISTANT")
    print("=" * 70)

    print("\nType 'exit' to quit.\n")

    while True:

        question = input("Ask a Question: ")

        if question.lower() == "exit":
            print("\nGoodbye!\n")
            break

        result = ask(question)

        print("\n" + "=" * 70)
        print("AI ANSWER")
        print("=" * 70)

        print(result["answer"])

        print("\n" + "=" * 70)
        print("SOURCE DOCUMENTS")
        print("=" * 70)

        for i, doc in enumerate(result["documents"], start=1):

            page = doc.metadata.get("page", 0)

            print(f"\nDocument {i}")
            print(f"Source : {doc.metadata.get('source')}")
            print(f"Page   : {page + 1}")
            print("-" * 60)


def main():

    while True:

        print("\n")
        print("=" * 70)
        print("LOCAL RAG AI DOCUMENT ASSISTANT")
        print("=" * 70)

        print("1. Build Knowledge Base")
        print("2. Chat with Documents")
        print("3. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":

            build_knowledge_base()

        elif choice == "2":

            chat()

        elif choice == "3":

            print("\nThank you!\n")
            break

        else:

            print("\nInvalid Option.\n")


if __name__ == "__main__":
    main()