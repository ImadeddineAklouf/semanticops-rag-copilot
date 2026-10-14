import chromadb


class ChromaStore:

    def __init__(
        self,
        collection_name: str = "semanticops"
    ):
        self.client = chromadb.PersistentClient(
            path="./data/vector_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=collection_name
            )
        )

    def add_chunk(
        self,
        chunk_id: str,
        content: str,
        embedding: list[float],
    ) -> None:

        self.collection.add(
            ids=[chunk_id],
            documents=[content],
            embeddings=[embedding],
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