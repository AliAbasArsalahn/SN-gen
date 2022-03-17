# Projekt: Seriennummergenerator | interface
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""
Interface module
"""


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
        main_menu_prompt = """
                    Welcome to SN-GEN!
                    1 - generate serialnumber
                    2 - save serialnumber
                    3 - validate serialnumber
                    4 - exit.
                    """
        main_menu_commands = {
            # function calls
            #
        }
        command = input(main_menu_prompt)

    def generate_serialnumber(self) -> None:
        """
        Displays the Serialnumber context menu and takes an argument.
        """
        generate_serialnumber_prompt = """
                                    1 - generate Serialnumber
                                    2 - change settings
                                    3 - save serialnumber
                                    """
        generate_serialnumber_commands = {
            # commands
        }

        command = input(generate_serialnumber_prompt)

    def run(self) -> None:
        """
        starts the programm loop and takes user input.
        """
#        while True:
