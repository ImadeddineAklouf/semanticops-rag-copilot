from pathlib import Path

from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile
from pathlib import Path

from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile
from app.core.config import settings
from app.embeddings.embedding_service import (
    EmbeddingService,
)
from app.ingestion.ingestion_service import (
    IngestionService,
)
from app.vectorstore.chroma_store import (
    ChromaStore,
)

router = APIRouter()

vector_store = ChromaStore(
    collection_name="api"
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

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):
    upload_path = (
        settings.uploads.directory
        / file.filename
    )

    content = await file.read()

    upload_path.write_bytes(
        content
    )

    chunks_created = (
        ingestion_service.ingest(
            str(upload_path)
        )
    )

    return {
        "filename": file.filename,
        "chunks_created": chunks_created
    }