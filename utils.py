import requests

from settings import QUESTIONS_ENDPOINT


def get_questions() -> list[dict]:
    """Берём с  эндпоинта JSON и возвращаем его в формате python"""
    response = requests.get(QUESTIONS_ENDPOINT)
    return response.json()


class Question:
    def __int__(self, text: str, difficulty: str, answer: str):
        self.text: str = text
        self.difficulty: int = int(difficulty)
        self.answer: str = answer

        self.question_asked: bool = False
        self.user_answer: None = None
        self.question_value: int = self.difficulty * 10
