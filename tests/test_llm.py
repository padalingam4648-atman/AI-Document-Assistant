from src.llm import generate_response


def main():

    print("=" * 70)
    print("OLLAMA LLM TEST")
    print("=" * 70)

    while True:

        prompt = input("\nPrompt (type 'exit' to quit): ")

        if prompt.lower() == "exit":
            break

        answer = generate_response(prompt)

        print("\n")
        print("=" * 70)
        print("LLM RESPONSE")
        print("=" * 70)
        print(answer)


if __name__ == "__main__":
    main()