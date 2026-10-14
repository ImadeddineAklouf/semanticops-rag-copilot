from app.embeddings.embedding_service import (
    EmbeddingService,
)


def test_embedding_generation():

    service = EmbeddingService()

    vector = service.embed(
        "SemanticOps RAG"
    )

    assert (
        isinstance(
            vector,
            list,
        )
    )

    assert len(vector) > 0