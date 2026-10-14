from app.generation.prompt_builder import (
    PromptBuilder,
)


def test_prompt_builder():

    prompt = (
        PromptBuilder()
        .build(
            question="What is RAG?",
            context="RAG combines retrieval and generation."
        )
    )

    assert "What is RAG?" in prompt
    assert "retrieval" in prompt