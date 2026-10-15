class Evaluator:

    def evaluate_answer(
        self,
        question: str,
        answer: str,
    ) -> dict:

        return {
            "question_length": len(question),
            "answer_length": len(answer),
            "answer_generated": (
                len(answer) > 0
            ),
        }