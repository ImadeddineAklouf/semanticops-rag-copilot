from app.embeddings.embedding_service import (
    EmbeddingService,
)
from app.vectorstore.chroma_store import (
    ChromaStore,
)


class Retriever:

    def __init__(
        self,
        vector_store: ChromaStore,
        embedding_service: EmbeddingService,
    ):
        self.vector_store = vector_store
        self.embedding_service = (
            embedding_service
        )

    def retrieve(
        self,
        question: str,
        top_k: int = 5,
    ):
        query_embedding = (
            self.embedding_service.embed(
                question
            )
        )

        return self.vector_store.search(
            embedding=query_embedding,
            top_k=top_k,
        )