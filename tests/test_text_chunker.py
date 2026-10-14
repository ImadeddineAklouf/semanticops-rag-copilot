from app.chunking.text_chunker import (
    TextChunker,
)
from app.domain.document import (
    Document,
)


def test_chunk_document():

    document = Document(
        id="doc1",
        title="test",
        content="A" * 1200,
        source="test.txt",
    )

    chunker = TextChunker(
        chunk_size=500,
        chunk_overlap=50,
    )

    chunks = chunker.chunk(
        document
    )

    assert len(chunks) == 3

    assert (
        chunks[0].document_id
        == "doc1"
    )

    assert (
        chunks[0].chunk_index
        == 0
    )

def test_overlap():

    document = Document(
        id="doc1",
        title="test",
        content="A" * 1000,
        source="test.txt",
    )

    chunker = TextChunker(
        chunk_size=500,
        chunk_overlap=100,
    )

    chunks = chunker.chunk(
        document
    )

    assert len(chunks) > 1