"""
Utility functions for the Local RAG project.
"""

from pathlib import Path


def get_pdf_directory() -> Path:
    """
    Ask the user for the directory containing PDF files.

    Returns
    -------
    Path
        Valid directory path containing at least one PDF.
    """

    while True:

        folder = input("\nEnter the folder containing PDF files:\n> ").strip()

        path = Path(folder)

        # Check if folder exists
        if not path.exists():
            print("\n❌ Folder does not exist.\n")
            continue

        # Check if it is a directory
        if not path.is_dir():
            print("\n❌ That is not a folder.\n")
            continue

        # Search for PDF files
        pdf_files = list(path.glob("*.pdf"))

        if not pdf_files:
            print("\n❌ No PDF files found.\n")
            continue

        print(f"\n✅ Found {len(pdf_files)} PDF file(s).\n")

        return path