# playground.py

from app.chunking.text_chunker import TextChunker
from app.domain.document import Document

document = Document(
    id="doc1",
    title="demo",
    content="A" * 1200,
    source="demo.txt"
)

chunker = TextChunker()

chunks = chunker.chunk(document)

print(
    f"Nombre de chunks : {len(chunks)}"
)

for chunk in chunks:
    print(chunk.id)