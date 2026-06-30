def build_prompt(query: str, context: str) -> str:
    return f"You are a helpful assistant. Use the context to answer the question.\n\nContext:\n{context}\n\nQuestion:\n{query}\n"