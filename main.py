# Projekt: Seriennummergenerator | Modul: main
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""main module"""

import argparse
import os
from serialnumbergenerator import SerialnumberGenerator


def main() -> None:
    """main function"""
    parser = argparse.ArgumentParser(description="generates a serialnumber")
    parser.add_argument("-g", "--generator", type=str, choices=["letter", "digit"],
                        help="specify the type of serialnumber")
    parser.add_argument("-qt", "--quantity", type=int,
                        help="set the amount of generated serialnumbers")
    parser.add_argument("-p", "--path", nargs="?", type=str, help="set the path",
                        default=os.getcwd())
    parser.add_argument("-v", "--validate", help="validate a given serialnumber",
                        type=str)
    args = vars(parser.parse_args())

    sn_generator = SerialnumberGenerator()
    if args["generator"]:
        sn_generator.generate_serialnumber(args["generator"])
        sn_generator.save_serialnumber()
    if args["validate"]:
        sn_generator.validate_serialnumber(args["validate"])

if __name__ == '__main__':
    main()
