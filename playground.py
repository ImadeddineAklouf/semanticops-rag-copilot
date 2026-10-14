# playground.py

from app.embeddings.embedding_service import (
    EmbeddingService
)

service = EmbeddingService()

vector = service.embed(
    "Semantic Layer Builder"
)

print(len(vector))