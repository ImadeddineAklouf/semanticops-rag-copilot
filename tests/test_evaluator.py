from app.evaluation.evaluator import (
    Evaluator,
)


def test_evaluator():

    evaluator = Evaluator()

    result = (
        evaluator.evaluate_answer(
            question="What is RAG?",
            answer="RAG combines retrieval and generation.",
        )
    )

    assert (
        result["answer_generated"]
        is True
    )