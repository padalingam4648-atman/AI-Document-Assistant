from src.utils import get_pdf_directory
from src.document_loader import load_documents

# Ask the user for the folder
folder = get_pdf_directory()

# Load all documents
documents = load_documents(folder)

print("=" * 50)
print("RESULT")
print("=" * 50)

print(f"Total Pages Loaded : {len(documents)}")

if documents:

    print("\nFirst Page Preview:\n")

    print(documents[0].page_content[:500])

    print("\nMetadata:\n")

    print(documents[0].metadata)