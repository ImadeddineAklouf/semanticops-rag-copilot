from enum import StrEnum
from pathlib import Path

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    model_validator,
)


class DocumentType(StrEnum):
    """
    Types de documents pris en charge
    par la base de connaissances.
    """

    MARKDOWN = "markdown"
    TEXT = "text"
    CSV = "csv"
    JSON = "json"
    YAML = "yaml"
    LOOKML = "lookml"
    PDF = "pdf"
    HTML = "html"
    PYTHON = "python"
    UNKNOWN = "unknown"


class SourceCategory(StrEnum):
    """
    Catégories métier utilisées pour filtrer
    les documents pendant la recherche.
    """

    BUSINESS = "business"
    METADATA = "metadata"
    LOOKML = "lookml"
    ARCHITECTURE = "architecture"
    TICKET = "ticket"
    TECHNICAL = "technical"
    OTHER = "other"


class DocumentSource(BaseModel):
    """
    Décrit la provenance physique et fonctionnelle
    d'un document.
    """

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )

    source_id: str = Field(
        min_length=1,
    )

    file_path: Path

    file_name: str = Field(
        min_length=1,
    )

    document_type: DocumentType

    category: SourceCategory

    checksum: str = Field(
        min_length=1,
    )


class DocumentMetadata(BaseModel):
    """
    Métadonnées utilisées pour rechercher,
    filtrer et tracer un document.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    title: str = Field(
        min_length=1,
    )

    description: str | None = None

    language: str = Field(
        default="en",
        min_length=2,
    )

    tags: list[str] = Field(
        default_factory=list,
    )

    table_names: list[str] = Field(
        default_factory=list,
    )

    column_names: list[str] = Field(
        default_factory=list,
    )

    business_domains: list[str] = Field(
        default_factory=list,
    )

    version: str | None = None

    author: str | None = None

    created_at: str | None = None

    updated_at: str | None = None

    custom_attributes: dict[
        str,
        str | int | float | bool | None,
    ] = Field(
        default_factory=dict,
    )


class Document(BaseModel):
    """
    Représentation normalisée d'un document
    chargé dans la base de connaissances.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    document_id: str = Field(
        min_length=1,
    )

    source: DocumentSource

    metadata: DocumentMetadata

    content: str = Field(
        min_length=1,
    )

    character_count: int = Field(
        ge=1,
    )

    ingestion_timestamp: str = Field(
        min_length=1,
    )

    @model_validator(
        mode="after",
    )
    def validate_character_count(
        self,
    ) -> "Document":
        """
        Vérifie que character_count correspond
        exactement au contenu du document.
        """

        if self.character_count != len(
            self.content
        ):
            raise ValueError(
                "character_count doit correspondre "
                "à la longueur exacte de content."
            )

        return self


class DocumentChunk(BaseModel):
    """
    Fragment autonome dérivé d'un document.

    Un chunk conserve toujours la provenance
    nécessaire à la génération des citations.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    chunk_id: str = Field(
        min_length=1,
    )

    document_id: str = Field(
        min_length=1,
    )

    source_id: str = Field(
        min_length=1,
    )

    chunk_index: int = Field(
        ge=0,
    )

    content: str = Field(
        min_length=1,
    )

    character_count: int = Field(
        ge=1,
    )

    start_character: int = Field(
        ge=0,
    )

    end_character: int = Field(
        ge=1,
    )

    section_title: str | None = None

    page_number: int | None = Field(
        default=None,
        ge=1,
    )

    metadata: dict[
        str,
        str | int | float | bool | None,
    ] = Field(
        default_factory=dict,
    )

    @model_validator(
        mode="after",
    )
    def validate_chunk_boundaries(
        self,
    ) -> "DocumentChunk":
        """
        Vérifie la cohérence du contenu
        et des positions du chunk.
        """

        if self.end_character <= (
            self.start_character
        ):
            raise ValueError(
                "end_character doit être supérieur "
                "à start_character."
            )

        if self.character_count != len(
            self.content
        ):
            raise ValueError(
                "character_count doit correspondre "
                "à la longueur du contenu du chunk."
            )

        expected_character_count = (
            self.end_character
            - self.start_character
        )

        if self.character_count != (
            expected_character_count
        ):
            raise ValueError(
                "Les bornes du chunk doivent correspondre "
                "à character_count."
            )

        return self


class Citation(BaseModel):
    """
    Référence précise vers une source utilisée
    dans une réponse RAG.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    citation_id: str = Field(
        min_length=1,
    )

    document_id: str = Field(
        min_length=1,
    )

    chunk_id: str = Field(
        min_length=1,
    )

    source_name: str = Field(
        min_length=1,
    )

    source_path: str = Field(
        min_length=1,
    )

    quoted_text: str = Field(
        min_length=1,
    )

    section_title: str | None = None

    page_number: int | None = Field(
        default=None,
        ge=1,
    )

    relevance_score: float = Field(
        ge=0.0,
        le=1.0,
    )


class IngestionResult(BaseModel):
    """
    Résumé produit après l'ingestion
    d'une ou plusieurs sources.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    ingestion_id: str = Field(
        min_length=1,
    )

    started_at: str = Field(
        min_length=1,
    )

    completed_at: str = Field(
        min_length=1,
    )

    discovered_file_count: int = Field(
        ge=0,
    )

    successful_document_count: int = Field(
        ge=0,
    )

    failed_document_count: int = Field(
        ge=0,
    )

    generated_chunk_count: int = Field(
        ge=0,
    )

    document_ids: list[str] = Field(
        default_factory=list,
    )

    errors: list[str] = Field(
        default_factory=list,
    )

    @model_validator(
        mode="after",
    )
    def validate_document_counts(
        self,
    ) -> "IngestionResult":
        """
        Vérifie la cohérence des compteurs
        du résultat d'ingestion.
        """

        processed_document_count = (
            self.successful_document_count
            + self.failed_document_count
        )

        if processed_document_count != (
            self.discovered_file_count
        ):
            raise ValueError(
                "La somme des documents réussis "
                "et échoués doit correspondre au "
                "nombre de fichiers découverts."
            )

        if len(self.document_ids) != (
            self.successful_document_count
        ):
            raise ValueError(
                "Le nombre de document_ids doit "
                "correspondre au nombre de documents "
                "ingérés avec succès."
            )

        if (
            self.failed_document_count > 0
            and not self.errors
        ):
            raise ValueError(
                "Une ingestion contenant des échecs "
                "doit fournir au moins une erreur."
            )

        return self