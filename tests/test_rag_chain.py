from src.rag_chain import RAGChain
from src.llm import LLM
from src.retriever import Retriever


def test_rag_chain_answer():
    llm = LLM(api_key="fake")
    retriever = Retriever(db_path="db/test.sqlite")
    rag = RAGChain(llm=llm, retriever=retriever)
    ans = rag.answer("What is the meaning of life?")
    assert isinstance(ans, str)
