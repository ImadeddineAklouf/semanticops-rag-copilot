import pytest

from app.loaders.factory import (
    LoaderFactory,
)


def test_text_loader():
    loader = (
        LoaderFactory.get_loader(
            "test.txt"
        )
    )

    assert (
        loader.__class__.__name__
        == "TextLoader"
    )


def test_markdown_loader():
    loader = (
        LoaderFactory.get_loader(
            "test.md"
        )
    )

    assert (
        loader.__class__.__name__
        == "MarkdownLoader"
    )


def test_unknown_extension():
    with pytest.raises(
        ValueError
    ):
        LoaderFactory.get_loader(
            "test.pdf"
        )

def test_json_loader():
    loader = LoaderFactory.get_loader(
        "test.json"
    )

    assert (
        loader.__class__.__name__
        == "JsonLoader"
    )


def test_yaml_loader():
    loader = LoaderFactory.get_loader(
        "test.yaml"
    )

    assert (
        loader.__class__.__name__
        == "YamlLoader"
    )


def test_csv_loader():
    loader = LoaderFactory.get_loader(
        "test.csv"
    )

    assert (
        loader.__class__.__name__
        == "CsvLoader"
    )