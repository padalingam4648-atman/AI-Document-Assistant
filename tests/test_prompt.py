from src.prompt import build_prompt


def test_build_prompt_contains_query_and_context():
    query = "What is 2+2?"
    context = "Math facts"
    prompt = build_prompt(query, context)
    assert isinstance(prompt, str)
    assert query in prompt
    assert context in prompt
