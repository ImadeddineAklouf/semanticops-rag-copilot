from app.loaders.markdown_loader import (
    MarkdownLoader,
)
from app.loaders.text_loader import (
    TextLoader,
)


class LoaderFactory:

    @staticmethod
    def get_loader(
        file_path: str,
    ):
        if file_path.endswith(".txt"):
            return TextLoader()

        if file_path.endswith(".md"):
            return MarkdownLoader()

        raise ValueError(
            f"Unsupported file type: "
            f"{file_path}"
        )