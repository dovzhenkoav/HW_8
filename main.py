import random

from utils import get_questions, Question


def create_questions_list(bank):
    questions_list = [Question(i['q'], i['d'], i['a']) for i in bank]
    random.shuffle(questions_list)
    return questions_list


def main():
    print('Игра начинается!')

    question_bank: list[dict] = get_questions()
    questions_list: list[Question] = create_questions_list(question_bank)


if __name__ == '__main__':
    main()
