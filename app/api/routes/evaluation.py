from fastapi import APIRouter

from app.evaluation.evaluator import (
    Evaluator,
)

router = APIRouter()


@router.get("/evaluation")
def evaluation():

    evaluator = Evaluator()

    return evaluator.evaluate_answer(
        question="What is RAG?",
        answer="RAG combines retrieval and generation.",
    )