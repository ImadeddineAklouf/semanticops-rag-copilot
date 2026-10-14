from app.embeddings.embedding_service import (
    EmbeddingService,
)
from app.vectorstore.chroma_store import (
    ChromaStore,
)


def test_store_creation():

    store = ChromaStore()

    assert store.collection is not None


def test_insert_and_search():

    store = ChromaStore()

    embedding_service = (
        EmbeddingService()
    )

    text = "SemanticOps"

    embedding = (
        embedding_service.embed(text)
    )

    store.add_chunk(
        chunk_id="test_chunk",
        content=text,
        embedding=embedding,
    )

    result = store.search(
        embedding
    )

    assert result is not None