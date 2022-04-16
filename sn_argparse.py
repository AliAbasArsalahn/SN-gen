# Projekt: Seriennummergenerator | Modul: argparse
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""main module"""

import argparse
from sn import LetterGenerator, DigitGenerator


parser = argparse.ArgumentParser(description="generates a serialnumber")
parser.add_argument("ops", "operation", metavar="ops", type=str,
                    required=False, help="specify which operation to run")

args = vars(parser.parse_args())

generator = LetterGenerator() if args.ops == 

def generate() -> None:
    """it's a duck!"""
    gen_choice = input("letter or digit serialnumber?").lower
    generator = LetterGenerator() if gen_choice == "letter" else DigitGenerator()
    generator.generate_serialnumber()
    generator.save_serialnumber()

def validate() -> None:
    """-/-"""
    pass


def main() -> None:
    pass


if __name__ == '__main__':
    main()