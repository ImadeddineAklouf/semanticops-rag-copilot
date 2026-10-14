from pathlib import Path

import yaml

from app.domain.document import Document


class YamlLoader:
    def load(self, file_path: str) -> Document:
        path = Path(file_path)

        data = yaml.safe_load(
            path.read_text(
                encoding="utf-8"
            )
        )

        return Document(
            id=path.stem,
            title=path.name,
            content=yaml.dump(
                data,
                allow_unicode=True,
            ),
            source=str(path),
        )
