from fastapi import APIRouter

from app.api.schemas import (
    IngestRequest,
    IngestResponse,
)
from app.embeddings.embedding_service import (
    EmbeddingService,
)
from app.ingestion.ingestion_service import (
    IngestionService,
)
from app.vectorstore.chroma_store import (
    ChromaStore,
)
from fastapi import HTTPException

router = APIRouter()

vector_store = ChromaStore(
    collection_name="api"
)

embedding_service = (
    EmbeddingService()
)

ingestion_service = (
    IngestionService(
        vector_store,
        embedding_service,
    )
)


@router.post(
    "/ingest",
    response_model=IngestResponse,
)
def ingest(
    request: IngestRequest,
):

    chunks_created = (
        ingestion_service.ingest(
            request.file_path
        )
    )

    return IngestResponse(
        chunks_created=chunks_created
    )
