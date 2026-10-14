from pathlib import Path

import pytest
from pydantic import ValidationError

from app.core.document_schemas import (
    Citation,
    Document,
    DocumentChunk,
    DocumentMetadata,
    DocumentSource,
    DocumentType,
    IngestionResult,
    SourceCategory,
)


def create_source() -> DocumentSource:
    """
    Crée une source valide pour les tests.
    """

    return DocumentSource(
        source_id="source_shipment_rules",
        file_path=Path(
            "knowledge_base/business/"
            "shipment_rules.md"
        ),
        file_name="shipment_rules.md",
        document_type=DocumentType.MARKDOWN,
        category=SourceCategory.BUSINESS,
        checksum="abc123",
    )


def create_metadata() -> DocumentMetadata:
    """
    Crée des métadonnées documentaires valides.
    """

    return DocumentMetadata(
        title="Shipment Business Rules",
        description=(
            "Business rules for logistics shipments."
        ),
        language="en",
        tags=[
            "shipment",
            "logistics",
        ],
        table_names=[
            "shipment",
        ],
        column_names=[
            "shipment_id",
            "carrier_id",
        ],
        business_domains=[
            "logistics",
        ],
        version="1.0.0",
        author="SemanticOps Demo",
        custom_attributes={
            "confidential": False,
            "priority": 1,
        },
    )


def create_document() -> Document:
    """
    Crée un document normalisé valide.
    """

    content = (
        "The shipment_id field uniquely "
        "identifies a shipment."
    )

    return Document(
        document_id="document_shipment_rules",
        source=create_source(),
        metadata=create_metadata(),
        content=content,
        character_count=len(content),
        ingestion_timestamp=(
            "2026-10-14T10:00:00+00:00"
        ),
    )


def create_chunk() -> DocumentChunk:
    """
    Crée un chunk valide.
    """

    content = (
        "The shipment_id field uniquely "
        "identifies a shipment."
    )

    return DocumentChunk(
        chunk_id="chunk_shipment_rules_0000",
        document_id="document_shipment_rules",
        source_id="source_shipment_rules",
        chunk_index=0,
        content=content,
        character_count=len(content),
        start_character=0,
        end_character=len(content),
        section_title="Shipment identifiers",
        page_number=None,
        metadata={
            "table_name": "shipment",
        },
    )


def test_valid_document_source() -> None:
    """
    Vérifie une source documentaire valide.
    """

    source = create_source()

    assert source.source_id == (
        "source_shipment_rules"
    )

    assert source.document_type == (
        DocumentType.MARKDOWN
    )

    assert source.category == (
        SourceCategory.BUSINESS
    )

    assert source.file_name == (
        "shipment_rules.md"
    )


def test_document_source_is_immutable() -> None:
    """
    Vérifie qu'une source ne peut pas être modifiée.
    """

    source = create_source()

    with pytest.raises(ValidationError):
        source.file_name = "another_file.md"


def test_unknown_source_field_is_rejected() -> None:
    """
    Vérifie que les champs inconnus sont refusés.
    """

    source_data = (
        create_source()
        .model_dump()
    )

    source_data["unknown_field"] = "unexpected"

    with pytest.raises(ValidationError):
        DocumentSource.model_validate(
            source_data
        )


def test_invalid_document_type_is_rejected() -> None:
    """
    Vérifie qu'un type inconnu est refusé.
    """

    source_data = (
        create_source()
        .model_dump()
    )

    source_data["document_type"] = "word"

    with pytest.raises(ValidationError):
        DocumentSource.model_validate(
            source_data
        )


def test_valid_document_metadata() -> None:
    """
    Vérifie les métadonnées valides.
    """

    metadata = create_metadata()

    assert metadata.title == (
        "Shipment Business Rules"
    )

    assert metadata.language == "en"

    assert metadata.table_names == [
        "shipment",
    ]

    assert metadata.custom_attributes[
        "confidential"
    ] is False


def test_metadata_default_collections_are_independent(
) -> None:
    """
    Vérifie que les listes par défaut
    ne sont pas partagées entre instances.
    """

    first_metadata = DocumentMetadata(
        title="First document"
    )

    second_metadata = DocumentMetadata(
        title="Second document"
    )

    first_metadata.tags.append(
        "first"
    )

    assert first_metadata.tags == [
        "first",
    ]

    assert second_metadata.tags == []


def test_valid_document() -> None:
    """
    Vérifie un document normalisé valide.
    """

    document = create_document()

    assert document.document_id == (
        "document_shipment_rules"
    )

    assert document.character_count == len(
        document.content
    )

    assert document.source.category == (
        SourceCategory.BUSINESS
    )


def test_incorrect_document_character_count_is_rejected(
) -> None:
    """
    Vérifie la cohérence de character_count.
    """

    document_data = (
        create_document()
        .model_dump()
    )

    document_data["character_count"] = 999

    with pytest.raises(
        ValidationError,
        match="character_count",
    ):
        Document.model_validate(
            document_data
        )


def test_empty_document_content_is_rejected() -> None:
    """
    Vérifie qu'un document vide est refusé.
    """

    document_data = (
        create_document()
        .model_dump()
    )

    document_data["content"] = ""
    document_data["character_count"] = 0

    with pytest.raises(ValidationError):
        Document.model_validate(
            document_data
        )


def test_valid_document_chunk() -> None:
    """
    Vérifie un chunk documentaire valide.
    """

    chunk = create_chunk()

    assert chunk.chunk_index == 0

    assert chunk.character_count == len(
        chunk.content
    )

    assert chunk.end_character == len(
        chunk.content
    )

    assert chunk.metadata[
        "table_name"
    ] == "shipment"


def test_chunk_end_must_be_after_start() -> None:
    """
    Vérifie que les limites du chunk
    sont correctement ordonnées.
    """

    chunk_data = (
        create_chunk()
        .model_dump()
    )

    chunk_data["start_character"] = 20
    chunk_data["end_character"] = 10

    with pytest.raises(
        ValidationError,
        match="end_character",
    ):
        DocumentChunk.model_validate(
            chunk_data
        )


def test_chunk_boundaries_must_match_content_length(
) -> None:
    """
    Vérifie la cohérence entre les bornes
    et la longueur réelle du chunk.
    """

    chunk_data = (
        create_chunk()
        .model_dump()
    )

    chunk_data["end_character"] = (
        chunk_data["end_character"]
        + 10
    )

    with pytest.raises(
        ValidationError,
        match="bornes",
    ):
        DocumentChunk.model_validate(
            chunk_data
        )


def test_chunk_character_count_must_match_content(
) -> None:
    """
    Vérifie que character_count correspond
    au contenu du chunk.
    """

    chunk_data = (
        create_chunk()
        .model_dump()
    )

    chunk_data["character_count"] = 1

    with pytest.raises(
        ValidationError,
        match="character_count",
    ):
        DocumentChunk.model_validate(
            chunk_data
        )


def test_page_number_must_be_positive() -> None:
    """
    Vérifie qu'un numéro de page commence à un.
    """

    chunk_data = (
        create_chunk()
        .model_dump()
    )

    chunk_data["page_number"] = 0

    with pytest.raises(ValidationError):
        DocumentChunk.model_validate(
            chunk_data
        )


def test_valid_citation() -> None:
    """
    Vérifie une citation valide.
    """

    citation = Citation(
        citation_id="citation_001",
        document_id="document_shipment_rules",
        chunk_id="chunk_shipment_rules_0000",
        source_name="shipment_rules.md",
        source_path=(
            "knowledge_base/business/"
            "shipment_rules.md"
        ),
        quoted_text=(
            "The shipment_id field uniquely "
            "identifies a shipment."
        ),
        section_title="Shipment identifiers",
        page_number=None,
        relevance_score=0.95,
    )

    assert citation.relevance_score == (
        pytest.approx(0.95)
    )

    assert citation.source_name == (
        "shipment_rules.md"
    )


def test_invalid_citation_score_is_rejected() -> None:
    """
    Vérifie que le score de pertinence
    ne peut pas dépasser un.
    """

    with pytest.raises(ValidationError):
        Citation(
            citation_id="citation_001",
            document_id="document_001",
            chunk_id="chunk_001",
            source_name="source.md",
            source_path="knowledge_base/source.md",
            quoted_text="Evidence.",
            relevance_score=1.50,
        )


def test_valid_ingestion_result() -> None:
    """
    Vérifie un résultat d'ingestion valide.
    """

    result = IngestionResult(
        ingestion_id="ingestion_001",
        started_at=(
            "2026-10-14T10:00:00+00:00"
        ),
        completed_at=(
            "2026-10-14T10:00:02+00:00"
        ),
        discovered_file_count=2,
        successful_document_count=2,
        failed_document_count=0,
        generated_chunk_count=5,
        document_ids=[
            "document_001",
            "document_002",
        ],
        errors=[],
    )

    assert result.discovered_file_count == 2

    assert result.generated_chunk_count == 5

    assert result.errors == []


def test_ingestion_counts_must_be_consistent() -> None:
    """
    Vérifie la cohérence des compteurs.
    """

    with pytest.raises(
        ValidationError,
        match="somme",
    ):
        IngestionResult(
            ingestion_id="ingestion_001",
            started_at=(
                "2026-10-14T10:00:00+00:00"
            ),
            completed_at=(
                "2026-10-14T10:00:02+00:00"
            ),
            discovered_file_count=3,
            successful_document_count=1,
            failed_document_count=1,
            generated_chunk_count=2,
            document_ids=[
                "document_001",
            ],
            errors=[
                "Unsupported file.",
            ],
        )


def test_document_ids_must_match_success_count() -> None:
    """
    Vérifie qu'un identifiant existe pour
    chaque document ingéré avec succès.
    """

    with pytest.raises(
        ValidationError,
        match="document_ids",
    ):
        IngestionResult(
            ingestion_id="ingestion_001",
            started_at=(
                "2026-10-14T10:00:00+00:00"
            ),
            completed_at=(
                "2026-10-14T10:00:02+00:00"
            ),
            discovered_file_count=2,
            successful_document_count=2,
            failed_document_count=0,
            generated_chunk_count=2,
            document_ids=[
                "document_001",
            ],
            errors=[],
        )


def test_failed_ingestion_requires_error_message(
) -> None:
    """
    Vérifie que les échecs sont documentés.
    """

    with pytest.raises(
        ValidationError,
        match="au moins une erreur",
    ):
        IngestionResult(
            ingestion_id="ingestion_001",
            started_at=(
                "2026-10-14T10:00:00+00:00"
            ),
            completed_at=(
                "2026-10-14T10:00:02+00:00"
            ),
            discovered_file_count=1,
            successful_document_count=0,
            failed_document_count=1,
            generated_chunk_count=0,
            document_ids=[],
            errors=[],
        )