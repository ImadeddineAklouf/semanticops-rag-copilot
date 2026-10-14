class ContextBuilder:

    def build(
        self,
        retrieval_results,
    ) -> str:

        documents = (
            retrieval_results.get(
                "documents",
                [],
            )
        )

        if not documents:
            return ""

        chunks = documents[0]

        return "\n\n".join(chunks)