from pathlib import Path

from app.loaders.markdown_loader import (
    MarkdownLoader,
)


def test_load_markdown_file(
    tmp_path: Path,
):
    sample_file = (
        tmp_path / "sample.md"
    )

    sample_file.write_text(
        "# SemanticOps",
        encoding="utf-8",
    )

    loader = MarkdownLoader()

    document = loader.load(
        str(sample_file)
    )

    assert (
        document.content
        == "# SemanticOps"
    )

    assert (
        document.title
        == "sample.md"
    )