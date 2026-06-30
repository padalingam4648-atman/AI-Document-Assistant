from src.embedding import create_embedding_model


def main():

    embedding_model = create_embedding_model()

    text = "Artificial Intelligence is transforming software development."

    vector = embedding_model.embed_query(text)

    print("=" * 60)
    print("Embedding Test")
    print("=" * 60)

    print("Input:")
    print(text)

    print("\nVector Dimension:")
    print(len(vector))

    print("\nFirst 10 Values:")
    print(vector[:10])


if __name__ == "__main__":
    main()