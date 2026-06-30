from src.rag_chain import ask


def main():

    print("=" * 70)
    print("LOCAL RAG TEST")
    print("=" * 70)

    while True:

        question = input("\nAsk a Question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        result = ask(question)

        print("\n")
        print("=" * 70)
        print("AI ANSWER")
        print("=" * 70)

        print(result["answer"])

        print("\n")
        print("=" * 70)
        print("SOURCE DOCUMENTS")
        print("=" * 70)

        for i, doc in enumerate(result["documents"], start=1):

            print(f"\nDocument {i}")

            print(f"Source : {doc.metadata.get('source')}")

            print(f"Page   : {doc.metadata.get('page')}")

            print("-" * 60)


if __name__ == "__main__":
    main()