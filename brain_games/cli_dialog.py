import prompt

NEGATIVE = ('no', 'nope', 'nein', 'njet', 'гониш', 'хуйтам')
POSITIVE = ('yes', 'yo', 'ja', 'da', 'безбазара', 'четко')

def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")


def ask_name():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello %s!' % name)
    return name

def get_user_answer(question, answer_type='number'):
    print('Question: %s' % question)
    if answer_type == 'number':
        return prompt.integer('Your answer: ')
    else:
        return prompt.string('Your answer: ')

def compare_answers(expected_answer, user_answer):
    def is_iterable(obj):
        return hasattr(obj, '__iter__')
    def wrong_text(user_answer, expected_answer):
        return "'%s' is wrong. Correct answer: '%s'." % (user_answer, expected_answer)
    ### xmas eggs
    if user_answer == "ne ebu":
        print("А сига найдется?")
        user_answer = prompt.string('Your answer: ')
        compare_answers(expected_answer, user_answer)
    ###
    correct_text = "It's correct!"
    if is_iterable(expected_answer):
        if user_answer in expected_answer:
            print(correct_text)
            return True
        else:
            print(wrong_text(user_answer, expected_answer[0]))
            return False
    else:
        if user_answer == expected_answer:
            print(correct_text)
            return True
        else:
            print(wrong_text(user_answer, expected_answer))
            return False

