from app.embeddings.embedding_service import (
    EmbeddingService,
)
from app.retrieval.retriever import (
    Retriever,
)
from app.vectorstore.chroma_store import (
    ChromaStore,
)


def test_retrieval():

    embedding_service = (
        EmbeddingService()
    )

    vector_store = (
        ChromaStore(
            collection_name="test"
        )
    )

    text = (
        "SemanticOps platform"
    )

    embedding = (
        embedding_service.embed(
            text
        )
    )

    vector_store.add_chunk(
        chunk_id="1",
        content=text,
        embedding=embedding,
    )

    retriever = Retriever(
        vector_store=vector_store,
        embedding_service=embedding_service,
    )

    results = retriever.retrieve(
        "SemanticOps"
    )

    assert results is not None