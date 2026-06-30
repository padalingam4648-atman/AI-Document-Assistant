from src.retriever import search_documents
from src.prompt import build_prompt


def main():

    while True:

        question = input("\nAsk a Question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        documents = search_documents(question)

        prompt = build_prompt(question, documents)

        print("\n")
        print("=" * 80)
        print("GENERATED PROMPT")
        print("=" * 80)
        print(prompt)


if __name__ == "__main__":
    main()