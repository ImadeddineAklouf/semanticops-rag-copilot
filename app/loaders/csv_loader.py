from pathlib import Path

import csv

from app.domain.document import Document


class CsvLoader:
    def load(self, file_path: str) -> Document:
        path = Path(file_path)

        rows = []

        with open(
            path,
            "r",
            encoding="utf-8",
            newline=""
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                rows.append(row)

        content = "\n".join(
            str(row)
            for row in rows
        )

        return Document(
            id=path.stem,
            title=path.name,
            content=content,
            source=str(path),
        )