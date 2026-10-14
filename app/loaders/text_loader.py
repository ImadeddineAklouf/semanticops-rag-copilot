from pathlib import Path

from app.domain.document import Document


class TextLoader:
    def load(self, file_path: str) -> Document:
        path = Path(file_path)

        return Document(
            id=path.stem,
            title=path.name,
            content=path.read_text(
                encoding="utf-8"
            ),
            source=str(path),
        )