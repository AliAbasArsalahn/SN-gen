# Projekt: Seriennummergenerator | Modul: main
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""main module"""

import argparse
import os
from re import S
from serialnumbergenerator import SerialnumberGenerator


def generate_and_save(thing: object) -> None:
    """calls generate_serialnumber and save_serialnumber functions from any given object"""
    thing.generate_serialnumber()
    thing.save_serialnumber()


def validate(thing: object) -> None:
    """-/-"""
    thing.validate_serialnumber()


def main() -> None:
    """main function"""
    parser = argparse.ArgumentParser(description="generates a serialnumber")
    parser.add_argument("-gen", "--generator", type=str, choices=["letter", "digit"],
                        help="specify the type of serialnumber")
    parser.add_argument("-qt", "--quantity", type=int,
                        help="set the amount of generated serialnumbers")
    parser.add_argument("-p", "--path", nargs="?",type=str, help="set the path",
                        default=os.getcwd())
    args = vars(parser.parse_args())

    if args["generator"] == "letter":
        generator = SerialnumberGenerator('letter')
    elif args["generator"] == "digit":
        generator = SerialnumberGenerator('digit')
    else:
        exit()

    generate_and_save(generator)


if __name__ == '__main__':
    main()
