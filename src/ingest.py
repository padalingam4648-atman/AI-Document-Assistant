from typing import List

from .document_loader import load_documents
from .text_splitter import split_text
from .embedding import create_embeddings
from .vector_store import VectorStore


def ingest_documents(source_dir: str, db_path: str) -> None:
    documents = load_documents(source_dir)
    all_chunks = []
    for document in documents:
        all_chunks.extend(split_text(document))

    vectors = create_embeddings(all_chunks)
    store = VectorStore(db_path)
    store.add_vectors(all_chunks, vectors)
    store.save()
