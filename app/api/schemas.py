from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str

class IngestRequest(BaseModel):
    file_path: str


class IngestResponse(BaseModel):
    chunks_created: int