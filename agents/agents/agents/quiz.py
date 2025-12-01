class QuizAgent:
    def generate_quiz(self, topic):
        return {
            "question": f"What best describes {topic}?",
            "options": ["A ledger", "A spell", "A potion"],
            "answer": "A ledger"
        }

    def check_answer(self, user_answer, correct_answer):
        return user_answer.strip().lower() == correct_answer.lower()
