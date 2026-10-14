from app.generation.context_builder import (
    ContextBuilder,
)


def test_context_builder():

    results = {
        "documents": [
            [
                "chunk 1",
                "chunk 2",
                "chunk 3",
            ]
        ]
    }

    builder = ContextBuilder()

    context = builder.build(results)

    assert "chunk 1" in context
    assert "chunk 2" in context
    assert "chunk 3" in context