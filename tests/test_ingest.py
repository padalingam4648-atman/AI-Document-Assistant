from src.utils import get_pdf_directory
from src.ingest import ingest_documents


def main():

    folder = get_pdf_directory()

    ingest_documents(folder)


if __name__ == "__main__":
    main()