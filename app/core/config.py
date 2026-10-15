from pathlib import Path

import yaml
from pydantic import BaseModel


class ProjectSettings(BaseModel):
    name: str
    version: str
    environment: str


class ChunkingSettings(BaseModel):
    chunk_size: int
    chunk_overlap: int


class RetrievalSettings(BaseModel):
    top_k: int


class VectorStoreSettings(BaseModel):
    collection_name: str

class UploadSettings(BaseModel):
    directory: str

class MonitoringSettings(BaseModel):
    enabled: bool

class Settings(BaseModel):
    project: ProjectSettings
    chunking: ChunkingSettings
    retrieval: RetrievalSettings
    vectorstore: VectorStoreSettings
    uploads: UploadSettings
    monitoring: MonitoringSettings

def load_settings() -> Settings:
    config_path = (
        Path(__file__).parent
        / "settings.yaml"
    )

    with open(
        config_path,
        "r",
        encoding="utf-8",
    ) as file:
        data = yaml.safe_load(file)

    return Settings(**data)


settings = load_settings()
