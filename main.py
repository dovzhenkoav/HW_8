from utils import get_questions, Question


def main():
    print('Игра начинается!')

    question_bank: list[dict] = get_questions()
    questions_list: list[Question] = [Question(i['q'], i['d'], i['a']) for i in question_bank]


if __name__ == '__main__':
    main()
