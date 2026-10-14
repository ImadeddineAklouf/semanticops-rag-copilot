from app.domain.answer import Answer
from app.domain.chunk import Chunk
from app.domain.document import Document
from app.domain.query import Query


def test_document_creation():
    doc = Document(
        id="1",
        title="Mon document",
        content="Contenu",
        source="test.txt"
    )

    assert doc.id == "1"


def test_chunk_creation():
    chunk = Chunk(
        id="1",
        document_id="doc1",
        content="texte",
        chunk_index=0
    )

    assert chunk.document_id == "doc1"


def test_query_creation():
    query = Query(
        question="What is RAG?"
    )

    assert query.top_k == 5


def test_answer_creation():
    answer = Answer(
        question="What is RAG?",
        answer="Retrieval Augmented Generation",
        sources=["doc1"]
    )

    assert len(answer.sources) == 1