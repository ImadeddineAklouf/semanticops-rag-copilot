from app.embeddings.embedding_service import (
    EmbeddingService,
)
from app.loaders.factory import (
    LoaderFactory,
)
from app.chunking.text_chunker import (
    TextChunker,
)
from app.vectorstore.chroma_store import (
    ChromaStore,
)
from app.monitoring.metrics import (
    metrics,
)

class IngestionService:

    def __init__(
        self,
        vector_store: ChromaStore,
        embedding_service: EmbeddingService,
    ):
        self.vector_store = vector_store
        self.embedding_service = embedding_service
        self.chunker = TextChunker()

    def ingest(
        self,
        file_path: str,
    ) -> int:

        loader = (
            LoaderFactory.get_loader(
                file_path
            )
        )

        document = loader.load(
            file_path
        )

        chunks = self.chunker.chunk(
            document
        )

        for chunk in chunks:

            embedding = (
                self.embedding_service.embed(
                    chunk.content
                )
            )

            self.vector_store.add_chunk(
                chunk=chunk,
                embedding=embedding,
            )
        metrics.register_ingestion(
            len(chunks)
        )
        return len(chunks)
