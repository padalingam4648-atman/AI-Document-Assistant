from src.retriever import Retriever


def test_retriever_returns_list():
    r = Retriever(db_path="db/test.sqlite")
    results = r.retrieve([0.0] * 1536)
    assert isinstance(results, list)
