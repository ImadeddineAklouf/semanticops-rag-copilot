from app.core.config import settings

class Metrics:

    def __init__(self):
        self.documents_ingested = 0
        self.chunks_created = 0
        self.queries_count = 0

    def register_ingestion(
        self,
        chunks_created: int,
    ):
        if not settings.monitoring.enabled:
            return

        self.documents_ingested += 1
        self.chunks_created += chunks_created

    def register_query(self):

        if not settings.monitoring.enabled:
            return

        self.queries_count += 1

metrics = Metrics()