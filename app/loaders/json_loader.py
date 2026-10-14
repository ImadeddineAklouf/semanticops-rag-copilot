import json
from pathlib import Path

from app.domain.document import Document


class JsonLoader:
    def load(self, file_path: str) -> Document:
        path = Path(file_path)

        data = json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )

        return Document(
            id=path.stem,
            title=path.name,
            content=json.dumps(
                data,
                indent=2,
                ensure_ascii=False,
            ),
            source=str(path),
        )