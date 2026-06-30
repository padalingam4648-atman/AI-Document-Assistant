from src.utils import get_pdf_directory
from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.embedding import create_embedding_model
from src.vector_store import (
    create_vector_store,
    save_vector_store,
)


def main():

    folder = get_pdf_directory()

    documents = load_documents(folder)

    chunks = split_documents(documents)

    embedding_model = create_embedding_model()

    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    save_vector_store(vector_store)

    print("=" * 50)
    print("FAISS Test")
    print("=" * 50)
    print("Vector Store Created Successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()