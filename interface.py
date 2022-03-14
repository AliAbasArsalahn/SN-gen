# Projekt: Seriennummergenerator | interface
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
#                                   WORK-IN-PROGRESS                           #
'''Interface module'''


class SNCLI:
    '''class CLI.\n Template for building an interactive interface.'''

    def __init__(self):
        """initialize an object of the class SNCLI. Page, interactions and
        prompt are set automatically"""
        self.page = None
        self.interface = {}

        main_menu_prompt = """Welcome to SN-GEN!
        1 - generate serialnumber
        2 - save serialnumber
        3 - validate serialnumber
        4 - exit."""
        generator_prompt = """SN-GEN:
        1 - to save your generated serialnumbers
        2 - back to main menu
        3 - exit."""

    def run(self) -> None:
        """starts the programm loop and takes user input."""
        while True:
            user_interaction = input(self.prompt)

            try:
                print(self.interface[user_interaction])
            except IndexError:
                print("command not found!")
