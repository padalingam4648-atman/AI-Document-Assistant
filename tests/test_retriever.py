from src.retriever import search_documents


def main():

    while True:

        print("\n" + "=" * 60)

        question = input("Ask a Question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        documents = search_documents(question)

        print("\nRetrieved Chunks")

        print("=" * 60)

        if not documents:
            print("No documents found.")
            continue

        for i, doc in enumerate(documents, start=1):

            print(f"\nChunk {i}")

            print("-" * 60)

            print("Source :", doc.metadata.get("source"))

            print("Page   :", doc.metadata.get("page"))

            print()

            print(doc.page_content)

            print("-" * 60)


if __name__ == "__main__":
    main()