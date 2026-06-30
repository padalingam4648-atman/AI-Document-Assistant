from src.utils import get_pdf_directory
from src.document_loader import load_documents
from src.text_splitter import split_documents


def main():
    folder = get_pdf_directory()

    documents = load_documents(folder)

    chunks = split_documents(documents)

    print("\nFirst Chunk\n")
    print("-" * 60)
    print(chunks[0].page_content)
    print("-" * 60)

    print("\nMetadata\n")
    print(chunks[0].metadata)


if __name__ == "__main__":
    main()