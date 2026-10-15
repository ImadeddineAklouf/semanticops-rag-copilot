from app.embeddings.embedding_service import (
    EmbeddingService,
)
from app.ingestion.ingestion_service import (
    IngestionService,
)
from app.vectorstore.chroma_store import (
    ChromaStore,
)

vector_store = ChromaStore(
    collection_name="ingestion_test"
)

embedding_service = (
    EmbeddingService()
)

ingestion_service = (
    IngestionService(
        vector_store=vector_store,
        embedding_service=embedding_service,
    )
)

chunks_created = (
    ingestion_service.ingest(
        "docs/sample.txt"
    )
)

print(
    f"Chunks créés : {chunks_created}"
)

print(
    f"Documents dans la collection : "
    f"{vector_store.collection.count()}"
)