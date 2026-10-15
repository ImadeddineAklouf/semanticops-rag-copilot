from fastapi import APIRouter

from app.monitoring.metrics import (
    metrics,
)
router = APIRouter()


@router.get("/metrics")
def get_metrics():

    return {
        "documents_ingested":
            metrics.documents_ingested,

        "chunks_created":
            metrics.chunks_created,

        "queries_count":
            metrics.queries_count,
    }