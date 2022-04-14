# Projekt: Seriennummergenerator | Main
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
'''main Skript'''


from sn import LetterGenerator, DigitGenerator
from interface import SNCLI

def main() -> None:

    # CLI or GUI
    # main_menu prompt / main menu
    # user input
    # function call
    # interface options


    letter_gen = LetterGenerator()
    digit_gen = DigitGenerator()
    cli_interface = SNCLI()

    while True:
        user_input = int(input())


if __name__ == '__main__':
    main()
