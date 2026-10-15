import chromadb
from torch import chunk


class ChromaStore:

    def __init__(
        self,
        collection_name: str = "semanticops"
    ):
        self.client = chromadb.PersistentClient(
            path="data/vector_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=collection_name
            )
        )

    def add_chunk(
        self,
        chunk,
        embedding,
    ):
        self.collection.add(
            ids=[chunk.id],
            documents=[chunk.content],
            embeddings=[embedding],
            metadatas=[
                {
                    "document_id": chunk.document_id,
                    "source": chunk.source,
                    "file_type": chunk.file_type,
                    "chunk_index": chunk.chunk_index,
                }
            ],
        )

    def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ):
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )