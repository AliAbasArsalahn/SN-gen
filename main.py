# Projekt: Seriennummergenerator | Modul: main
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""main module"""

import argparse
from generator import LetterGenerator, DigitGenerator


def generate_and_save(thing: object) -> None:
    """it's a duck!"""
    thing.generate_serialnumber()
    thing.save_serialnumber()


def validate(thing: object) -> None:
    """-/-"""
    thing.validate_serialnumber()


parser = argparse.ArgumentParser(description="generates a serialnumber")
parser.add_argument("-gen", "--generator", type=str, choices=["letter", "digit"],
                        help="specify the type of serialnumber")
parser.add_argument("-qt", "--quantity", type=int,
                        help="set the amount of generated serialnumbers")
parser.add_argument("-p", "--path", type=str, help="set the path")

args = vars(parser.parse_args())
generator = LetterGenerator() if args[generator] == "letter" else DigitGenerator()

def main() -> None:
    """main function"""
    generate_and_save(generator)


if __name__ == '__main__':
    main()
