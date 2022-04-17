# Projekt: Seriennummergenerator | Modul: argparse
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""main module"""

import argparse
from sn import LetterGenerator, DigitGenerator


def generate_and_save(thing: object) -> None:
    """it's a duck!"""
    thing.generate_serialnumber()
    thing.save_serialnumber()


def validate(thing: object) -> None:
    """-/-"""
    thing.validate_serialnumber()


def main() -> None:
    """main function"""
    parser = argparse.ArgumentParser(description="generates a serialnumber")
    parser.add_argument("-gen", "--generate", type=str, choices=["letter", "digit"],
                        help="specify the type of serialnumber")
    args = parser.parse_args()


if __name__ == '__main__':
    main()
