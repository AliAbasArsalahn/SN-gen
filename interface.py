# Projekt: Seriennummergenerator | interface
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""
Interface module
"""


from sn import SN
import sys


class SNCLI:
    '''
    Template for SNGEN CLI
    '''
    # ggf. implicit setzen

    def __init__(self):
        """
        constructer of class SNCLI.
        """
        pass

    def interface(self) -> None:
        """
        starts the main menu.
        Assigns the prompt as a string and displays it.
        Prompt displays
        Takes a command as an argument afterwards.
        creates two objects of the class "SN"
        """

        def main_menu() -> None:
            main_menu_prompt = """
                        Welcome to SN-GEN!
                        1 - generate serialnumber
                        2 - validate serialnumber
                        3 - exit.
                        """

            command = int(input(main_menu_prompt))

            if command == 1:
                generate_serialnumber()
            elif command == 2:
                validate_serialnumber()
            else:
                exit()

        def generate_serialnumber() -> None:
            """
            Displays the Serialnumber context menu and takes an argument.
            """
            generate_serialnumber_prompt = """
                                        1 - generate letterserialnumber
                                        2 - generate digitserialnumber
                                        3 - save serialnumbers
                                        4 - back to main menu
                                        """

            command = input(generate_serialnumber_prompt)


        def validate_serialnumber() -> None:
            user_serialnumber = input("enter you serialnumber: ")
