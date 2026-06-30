from src.llm import LLM


def test_llm_generate_and_embed():
    llm = LLM(api_key="fake", model="gpt-test")
    resp = llm.generate("hello")
    assert isinstance(resp, str)
    vecs = llm.embed(["a", "b"])
    assert isinstance(vecs, list)
    assert len(vecs) == 2
    assert len(vecs[0]) == 1536
