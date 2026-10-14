from app.embeddings.embedding_service import (
    EmbeddingService,
)
from app.generation.rag_pipeline import (
    RAGPipeline,
)
from app.retrieval.retriever import (
    Retriever,
)
from app.vectorstore.chroma_store import (
    ChromaStore,
)


def test_rag_pipeline():

    embedding_service = (
        EmbeddingService()
    )

    vector_store = ChromaStore(
        collection_name="rag_test"
    )

    text = (
        "RAG combines retrieval "
        "and generation."
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

    pipeline = RAGPipeline(
        retriever
    )

    answer = pipeline.ask(
        "What is RAG?"
    )

    assert isinstance(
        answer,
        str,
    )