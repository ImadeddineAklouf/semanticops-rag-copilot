from app.embeddings.embedding_service import (
    EmbeddingService,
)
from app.vectorstore.chroma_store import (
    ChromaStore,
)

embedding_service = (
    EmbeddingService()
)

vector_store = (
    ChromaStore()
)

text = (
    "Semantic Layer Builder "
    "creates LookML models."
)

embedding = (
    embedding_service.embed(text)
)

vector_store.add_chunk(
    chunk_id="chunk_1",
    content=text,
    embedding=embedding,
)

results = vector_store.search(
    embedding
)

print(results)