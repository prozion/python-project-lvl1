import time
import colorama
from brain_games.cli_dialog import ask_name


def print_star(times, newline=False, color=colorama.Fore.YELLOW):
    sym="@"
    print(color, end='')
    print(sym * times, end='')
    print('', end=None if newline else '')
    print(colorama.Style.RESET_ALL, end='')


def print_text(text, color=colorama.Fore.YELLOW):
    print(color, end='')
    print(text, end='')
    print(colorama.Style.RESET_ALL, end='')


def play(make_turn_function, description='', max_turns_count=3):
    # user_name = ask_name()
    print(description)
    # time.sleep(1)
    turns_count = 0
    while turns_count < max_turns_count:
        if make_turn_function():
            time.sleep(1)
            print_star(42, True)
            print_star(42, True)
            print_star(3); print_text("                                    "); print_star(3, True)
            print_star(3); print_text("            Oh, of no!              "); print_star(3, True)
            print_star(3); print_text("         You win. Congrats.         "); print_star(3, True)
            print_star(3); print_text("          FЯOM SOUЛ, BЯO!           ", color=colorama.Fore.RED); print_star(3, True)
            print_star(3); print_text("                                    "); print_star(3, True)
            print_star(42, True)
            print_star(42, True)
            return True
        turns_count += 1
        # time.sleep(1)
    print(colorama.Fore.CYAN)
    print("Alas, %s, you lost!" % user_name)
    print(colorama.Style.RESET_ALL)
    return False