from app.loaders.text_loader import TextLoader

loader = TextLoader()

document = loader.load(
    "docs/example.txt"
)

print(document)