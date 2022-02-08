from brain_games.cli_dialog import get_user_answer, compare_answers, POSITIVE, NEGATIVE
import random

min_number, max_number = 3, 100

def guess_even_number_turn():

    def is_even (number):  
        return number % 2 == 0

    number = random.randint(min_number, max_number)
    expected_answer = POSITIVE if is_even(number) else NEGATIVE
    user_answer = get_user_answer(number, 'string')
    return compare_answers(expected_answer, user_answer)