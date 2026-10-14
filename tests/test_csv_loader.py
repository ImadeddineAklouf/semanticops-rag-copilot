from app.loaders.csv_loader import (
    CsvLoader,
)


def test_csv_loader(tmp_path):
    file_path = tmp_path / "sample.csv"

    file_path.write_text(
        "id,name\n1,SemanticOps",
        encoding="utf-8",
    )

    document = CsvLoader().load(
        str(file_path)
    )

    assert (
        "SemanticOps"
        in document.content
    )