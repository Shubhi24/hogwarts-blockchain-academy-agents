from tutor import TutorAgent
from quiz import QuizAgent
from reward import RewardAgent

class Orchestrator:
    def run_module(self, user, topic, answer):
        tutor = TutorAgent()
        quiz = QuizAgent()
        reward = RewardAgent()

        lesson = tutor.teach(topic)
        quiz_obj = quiz.generate_quiz(topic)
        is_correct = quiz.check_answer(answer, quiz_obj["answer"])
        nft = reward.mint_badge(user, topic) if is_correct else None

        return {"lesson": lesson, "quiz": quiz_obj, "correct": is_correct, "nft": nft}
