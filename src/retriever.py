from typing import List

from .vector_store import VectorStore


class Retriever:
    def __init__(self, db_path: str):
        self.store = VectorStore(db_path)

    def retrieve(self, query_vector: List[float], top_k: int = 5) -> List[str]:
        return self.store.search(query_vector, top_k=top_k)
