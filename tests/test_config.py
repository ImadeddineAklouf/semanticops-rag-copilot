from app.core.config import settings


def test_settings_loaded():
    assert settings.project.name == "SemanticOps RAG"
    assert settings.chunking.chunk_size == 500