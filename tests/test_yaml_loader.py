from app.loaders.yaml_loader import (
    YamlLoader,
)


def test_yaml_loader(tmp_path):
    file_path = tmp_path / "sample.yaml"

    file_path.write_text(
        "name: SemanticOps",
        encoding="utf-8",
    )

    document = (
        YamlLoader()
        .load(str(file_path))
    )

    assert (
        "SemanticOps"
        in document.content
    )