from typing import List

class LLM:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.api_key = api_key
        self.model = model

    def generate(self, prompt: str) -> str:
        return "This is a placeholder response from the LLM."

    def embed(self, texts: List[str]) -> List[List[float]]:
        return [[0.0] * 1536 for _ in texts]
