# Projekt: Seriennummergenerator | interface
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""
Interface module
"""


from sn import SN, letter_generator, digit_generator


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

    def main_menu(self) -> None:
        """
        starts the main menu.
        Assigns the prompt as a string and displays it.
        Prompt displays
        Takes a command as an argument afterwards.
        """
        MAIN_MENU_PROMPT = """
                    Welcome to SN-GEN!
                    1 - generate serialnumber
                    2 - validate serialnumber
                    3 - exit.
                    """

        main_menu_commands = {
            1: self.generate_serialnumber(),
            2: validate_context_menu(),
            3: exit()
        }

        def validate_context_menu() -> None:
            pass

        command = input(MAIN_MENU_PROMPT)
        try:
            main_menu_commands[command]
        except IndexError:
            print("command not found! Try again")
            print(MAIN_MENU_PROMPT)

    def generate_serialnumber(self) -> None:
        """
        Displays the Serialnumber context menu and takes an argument.
        """
        generate_serialnumber_prompt = """
                                    1 - generate letterserialnumber
                                    2 - generate digitserialnumber
                                    3 - save serialnumbers
                                    4 - back to main menu
                                    """
        generate_serialnumber_commands = {
            1: letter_generator.generate_serialnumber(),
            2: digit_generator.generate_serialnumber(),
            3: SN.save_serialnumber(digit_generator) and SN.save_serialnumber(letter_generator)
        }

        command = input(generate_serialnumber_prompt)
        try:
            generate_serialnumber_commands[command]
        except IndexError:
            print("command not found! Try again")
            print(generate_serialnumber_prompt)

    def run(self) -> None:
        """
        starts the programm loop and takes user input.
        """
        while True:
            self.main_menu()
