from pathlib import Path

from app.loaders.text_loader import TextLoader


def test_load_text_file(
    tmp_path: Path,
):
    sample_file = (
        tmp_path / "sample.txt"
    )

    sample_file.write_text(
        "Hello SemanticOps",
        encoding="utf-8",
    )

    loader = TextLoader()

    document = loader.load(
        str(sample_file)
    )

    assert (
        document.content
        == "Hello SemanticOps"
    )

    assert (
        document.title
        == "sample.txt"
    )

    assert (
        document.id
        == "sample"
    )