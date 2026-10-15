from fastapi import FastAPI

from app.api.routes.health import (
    router as health_router,
)
from app.api.routes.query import (
    router as query_router,
)
from app.api.routes.ingest import (
    router as ingest_router,
)
from app.api.routes.upload import (
    router as upload_router,
)
from app.api.routes.debug import (
    router as debug_router,
)
from app.api.routes.metrics import (
    router as metrics_router,
)
from app.api.routes.evaluation import (
    router as evaluation_router,
)
from app.api.routes.config import (
    router as config_router,
)


app = FastAPI(
    title="SemanticOps RAG",
    version="0.1.0",
)

app.include_router(
    health_router
)

app.include_router(
    query_router
)

app.include_router(
    ingest_router
)

app.include_router(
    upload_router
)

app.include_router(
    debug_router
)

app.include_router(
    metrics_router
)

app.include_router(
    evaluation_router
)

app.include_router(
    config_router
)