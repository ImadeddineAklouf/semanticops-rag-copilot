from pydantic import BaseModel


class RetrievalResult(BaseModel):
    chunk_id: str
    content: str
    score: float