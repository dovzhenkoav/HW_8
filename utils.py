from settings import QUESTIONS_ENDPOINT
import requests


def get_questions() -> list[dict]:
    """Берём с  эндпоинта JSON и возвращаем его в формате python"""
    responce = requests.get(QUESTIONS_ENDPOINT)
    return responce.json()


class Question:
    pass
