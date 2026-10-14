class PromptBuilder:

    def build(
        self,
        question: str,
        context: str,
    ) -> str:

        return f"""
You are a helpful assistant.

Context:
{context}

Question:
{question}

Answer:
"""