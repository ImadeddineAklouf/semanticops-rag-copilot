from app.generation.llm_service import (
    LLMService,
)


def test_generate():

    service = LLMService()

    answer = service.generate(
        "What is RAG?"
    )

    assert isinstance(
        answer,
        str,
    )

    assert len(answer) > 0