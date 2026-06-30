from typing import List

from .llm import LLM
from .prompt import build_prompt
from .retriever import Retriever


class RAGChain:
    def __init__(self, llm: LLM, retriever: Retriever):
        self.llm = llm
        self.retriever = retriever

    def answer(self, query: str) -> str:
        # Placeholder: build retrieval + prompt flow
        results = self.retriever.retrieve([0.0] * 1536)
        context = "\n\n".join(results)
        prompt = build_prompt(query, context)
        return self.llm.generate(prompt)
