import requests

from settings import QUESTIONS_ENDPOINT


def get_questions() -> list[dict]:
    """Берём с  эндпоинта JSON и возвращаем его в формате python"""
    response = requests.get(QUESTIONS_ENDPOINT)
    return response.json()


class Question:
    def __init__(self, text: str, difficulty: str, answer: str):
        self.text: str = text
        self.difficulty: int = int(difficulty)
        self.answer: str = answer

        self.question_answered: bool = False
        self.user_answer: None = None
        self.question_value: int = self.difficulty * 10

    def get_points(self) -> int:
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.question_value

    def _is_correct(self, user_input: str) -> bool:
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        self.user_answer = user_input
        return self.answer.lower() == self.user_answer.lower()

    def build_question(self) -> str:
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'\nВопрос: {self.text}\nСложность: {self.difficulty}/5\n'

    def build_feedback(self, user_input: str) -> str:
        """Возвращает :
        Ответ верный, получено __ баллов,
        Ответ неверный, верный ответ __
        """
        if self._is_correct(user_input):
            self.question_answered = True
            return f"Ответ верный, получено {self.question_value} баллов"
        else:
            return f"Ответ неверный. Верный ответ – {self.answer}"
