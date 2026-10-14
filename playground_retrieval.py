from app.embeddings.embedding_service import (
    EmbeddingService,
)
from app.retrieval.retriever import (
    Retriever,
)
from app.vectorstore.chroma_store import (
    ChromaStore,
)

embedding_service = (
    EmbeddingService()
)

vector_store = ChromaStore()

documents = [
    "Semantic Layer Builder generates LookML.",
    "RAG combines retrieval and generation.",
    "ChromaDB stores embeddings."
]

for i, text in enumerate(documents):

    embedding = (
        embedding_service.embed(text)
    )

    vector_store.add_chunk(
        chunk_id=f"chunk_{i}",
        content=text,
        embedding=embedding,
    )

retriever = Retriever(
    vector_store=vector_store,
    embedding_service=embedding_service,
)

results = retriever.retrieve(
    "What is RAG?",
    top_k=2,
)

print(results)