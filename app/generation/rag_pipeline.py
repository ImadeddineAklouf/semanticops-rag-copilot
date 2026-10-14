from app.generation.context_builder import (
    ContextBuilder,
)
from app.generation.llm_service import (
    LLMService,
)
from app.generation.prompt_builder import (
    PromptBuilder,
)


class RAGPipeline:

    def __init__(
        self,
        retriever,
    ):
        self.retriever = retriever

        self.context_builder = (
            ContextBuilder()
        )

        self.prompt_builder = (
            PromptBuilder()
        )

        self.llm_service = (
            LLMService()
        )

    def ask(
        self,
        question: str,
    ) -> str:

        retrieval_results = (
            self.retriever.retrieve(
                question
            )
        )

        context = (
            self.context_builder.build(
                retrieval_results
            )
        )

        prompt = (
            self.prompt_builder.build(
                question,
                context,
            )
        )

        return (
            self.llm_service.generate(
                prompt
            )
        )
