import hashlib


class EmbeddingService:

    def embed(
        self,
        text: str,
    ) -> list[float]:

        hash_bytes = hashlib.sha256(
            text.encode("utf-8")
        ).digest()

        return [
            float(byte)
            for byte in hash_bytes
        ]

    def embed_batch(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        return [
            self.embed(text)
            for text in texts
        ]