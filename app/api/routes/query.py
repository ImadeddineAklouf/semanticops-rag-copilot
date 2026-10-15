from fastapi import APIRouter

from app.api.schemas import (
    QueryRequest,
    QueryResponse,
)
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
from app.monitoring.metrics import (
    metrics,
)

router = APIRouter()

embedding_service = (
    EmbeddingService()
)

vector_store = (
    ChromaStore(
        collection_name="api"
    )
)

retriever = Retriever(
    vector_store=vector_store,
    embedding_service=embedding_service,
)

pipeline = RAGPipeline(
    retriever=retriever
)


@router.post(
    "/query",
    response_model=QueryResponse,
)
def query(
    request: QueryRequest,
):
    metrics.register_query()

    answer = pipeline.ask(
        request.question
    )

    return QueryResponse(
        answer=answer
    )
