from app.chunking.text_chunker import (
    TextChunker,
)
from app.domain.document import (
    Document,
)
from app.embeddings.embedding_service import (
    EmbeddingService,
)

document = Document(
    id="doc1",
    title="demo",
    content="RAG combines retrieval and generation." * 100,
    source="demo.txt",
)

chunker = TextChunker()

chunks = chunker.chunk(
    document
)

service = EmbeddingService()

vectors = []

for chunk in chunks:
    vectors.append(
        service.embed(
            chunk.content
        )
    )

print(
    f"Chunks : {len(chunks)}"
)

print(
    f"Vectors : {len(vectors)}"
)

print(
    f"Dimension : {len(vectors[0])}"
)