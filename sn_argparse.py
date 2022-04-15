# Projekt: Seriennummergenerator | Modul: argparse
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""main module"""

import argparse
from sn import LetterGenerator, DigitGenerator


parser = argparse.ArgumentParser(description="generates a serialnumber")
parser.add_argument("-gen", "--generate", metavar="gen", type=str,
                    required=False, help="generate one or more serialnumbers")
parser.add_argument("-val", "--validate", metavar="val", type=str,
                    help="validate an existing serialnumber")

args = vars(parser.parse_args())


def generate() -> None:
    """it's a duck!"""
    gen_choice = input("letter or digit serialnumber?").lower
    generator = LetterGenerator() if gen_choice == "letter" else DigitGenerator()
    generator.generate_serialnumber()
    generator.save_serialnumber()
