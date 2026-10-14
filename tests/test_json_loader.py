import json

from app.loaders.json_loader import JsonLoader


def test_json_loader(tmp_path):
    file_path = tmp_path / "sample.json"

    file_path.write_text(
        json.dumps(
            {"name": "SemanticOps"}
        ),
        encoding="utf-8",
    )

    document = JsonLoader().load(
        str(file_path)
    )

    assert "SemanticOps" in document.content
