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
    parser.add_argument("-lg", "--lettergenerator", type=int,
                        help="generate letter serialnumbers (default 1)")
    parser.add_argument("-dg", "--digitgenerator", type=int,
                        help="generate digit serialnumbers (default 1)")
    parser.add_argument("-kr", "--keyrows", type=int, default=3,
                        help="set the amount of rows")
    parser.add_argument("-rl", "--rowlength", type=int, default=4,
                        help="set the rowlength")
    parser.add_argument("-p", "--path", nargs="?", type=str, default=os.getcwd(),
                        help="set the path")
    parser.add_argument("-v", "--validate", type=str,
                        help="validate a given serialnumber")
    args = vars(parser.parse_args())

    sn_generator = SerialnumberGenerator()
    if args["lettergenerator"]:
        sn_generator.generate_serialnumber(
            "letter", args["lettergenerator"], args["keyrows"], args["rowlength"])
        sn_generator.save_serialnumber(args["path"])
    if args["digitgenerator"]:
        sn_generator.generate_serialnumber(
            "digit", args["digitgenerator"], args["keyrows"], args["rowlength"])
        sn_generator.save_serialnumber(args["path"])
    if args["validate"]:
        sn_generator.validate_serialnumber(args["validate"])


if __name__ == '__main__':
    main()
