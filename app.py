from src.config import Config
from src.ingest import ingest_documents
from src.llm import LLM
from src.retriever import Retriever
from src.rag_chain import RAGChain
from src.utils import safe_load_env


def main():
    safe_load_env()
    config = Config.from_env()
    llm = LLM(api_key=config.openai_api_key, model=config.llm_model)
    retriever = Retriever(db_path=config.db_path)
    rag = RAGChain(llm=llm, retriever=retriever)

    print("Local-RAG skeleton application")
    print("1) Ingest documents")
    print("2) Ask a question")
    choice = input("Choose an option: ")

    if choice == "1":
        ingest_documents("data", config.db_path)
        print("Ingestion complete.")
    else:
        question = input("Enter your question: ")
        answer = rag.answer(question)
        print("Answer:\n", answer)


if __name__ == "__main__":
    main()
