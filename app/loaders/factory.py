from app.loaders.csv_loader import CsvLoader
from app.loaders.json_loader import JsonLoader
from app.loaders.markdown_loader import MarkdownLoader
from app.loaders.text_loader import TextLoader
from app.loaders.yaml_loader import YamlLoader


class LoaderFactory:

    @staticmethod
    def get_loader(file_path: str):

        if file_path.endswith(".txt"):
            return TextLoader()

        if file_path.endswith(".md"):
            return MarkdownLoader()

        if file_path.endswith(".json"):
            return JsonLoader()

        if (
            file_path.endswith(".yaml")
            or file_path.endswith(".yml")
        ):
            return YamlLoader()

        if file_path.endswith(".csv"):
            return CsvLoader()

        raise ValueError(
            f"Unsupported file type: {file_path}"
        )