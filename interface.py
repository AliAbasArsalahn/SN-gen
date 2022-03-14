# Projekt: Seriennummergenerator | interface
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
'''Interface module'''


class SNCLI:
    '''class CLI.\n Template for building an interactive interface.'''

    def __init__(self, page: int):
        """initialize an object of the class SNCLI. Page, interactions and
        prompt are set automatically"""
        self._page = page
        self._interface = interface

        @property
        def interface(self) -> dict:
            return self._interface

        @interface.setter
        def interface(self):
            """sets interface propterty."""
            ###########################SUBJECT-TO-CHANGE######################
            main_page = """Welcome to SN-GEN!
                    1 - generate serialnumber
                    2 - save serialnumber
                    3 - validate serialnumber
                    4 - exit."""
            generator_prompt = """1 - to save your generated serialnumbers
        2 - back to main menu
        3 - exit."""
            validate_prompt = """something"""
            self.interface = {
                1: main_page,
                2: generator_prompt,
                3: validate_prompt
            }

    def run(self) -> None:
        """starts the programm loop and takes user input."""
        while True:
            user_interaction = input(self._interface[self._page])

            try:
                print(self._interface[user_interaction])
            except IndexError:
                print("command not found!")
