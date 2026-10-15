from fastapi import APIRouter

from app.vectorstore.chroma_store import (
    ChromaStore,
)

router = APIRouter()


@router.get("/debug/chunks")
def debug_chunks():

    store = ChromaStore(
        collection_name="api"
    )

    return store.collection.get()