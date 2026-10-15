from app.embeddings.embedding_service import (
    EmbeddingService,
)
from app.vectorstore.chroma_store import (
    ChromaStore,
)

store = ChromaStore(
    collection_name="api"
)

embedder = EmbeddingService()

documents = [
    "RAG combines retrieval and generation.",
    "ChromaDB stores vector embeddings.",
    "Semantic Layer Builder generates LookML.",
]

for index, document in enumerate(
    documents
):
    store.add_chunk(
        chunk_id=f"doc_{index}",
        content=document,
        embedding=embedder.embed(
            document
        ),
    )

print("Data loaded")