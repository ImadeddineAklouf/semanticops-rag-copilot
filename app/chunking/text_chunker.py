from app.domain.chunk import Chunk
from app.domain.document import Document


class TextChunker:
    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 50,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(
        self,
        document: Document,
    ) -> list[Chunk]:

        chunks = []

        text = document.content

        start = 0
        index = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk_text = text[start:end]

            chunks.append(
                Chunk(
                    id=f"{document.id}_{index}",
                    document_id=document.id,
                    content=chunk_text,
                    chunk_index=index,
                )
            )

            start += (
                self.chunk_size
                - self.chunk_overlap
            )

            index += 1

        return chunks