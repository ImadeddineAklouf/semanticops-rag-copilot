from pydantic import BaseModel


class Chunk(BaseModel):
    id: str
    document_id: str
    content: str
    chunk_index: int