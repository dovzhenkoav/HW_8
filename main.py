import random
from utils import get_questions, Question


def create_questions_list(bank: list[dict]) -> list[Question]:
    """Создаёт список из объектов вопросов"""
    questions_list = [Question(i['q'], i['d'], i['a']) for i in bank]
    random.shuffle(questions_list)
    return questions_list


def show_statistics(bank: list[Question]):
    """Выводит финальную статистику по викторине"""
    answered = [i for i in bank if i.question_answered]  # Из всех вопросов выбирает только правильно отвеченные
    score = sum([i.question_value for i in answered])  # Подсчёт веса вопросов из правильно отвеченных
    print(f"Вот и всё!\nОтвечено: {len(answered)} вопроса из {len(bank)}\nНабрано баллов: {score}")


def quiz_brain(question_obj_bank: list[Question]):
    """Обработчик, который задаёт вопросы, принимает ответ пользователя и сопоставляет их с правильными"""
    for question in question_obj_bank:
        user_input = input(question.build_question())
        print(question.build_feedback(user_input))


def main():
    print('Игра начинается!')

    question_bank: list[dict] = get_questions()
    questions_list: list[Question] = create_questions_list(question_bank)

    quiz_brain(questions_list)
    show_statistics(questions_list)


if __name__ == '__main__':
    main()
