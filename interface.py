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
        self._page = None
        self.interactions = {}
        self.prompt = ''

    @page.setter
    def page(self, value) -> int:
        '''page setter'''
        if value >= 1:
            self._page = value

    @property
    def interaction(self):
        """returns the interaction property"""
        return self.interaction

    @interaction.setter
    def interaction(self) -> None:
        """sets the available interactions based on page"""
        self.interaction = (1, 2, 3) if self._page == 1 else (1, 2)

    @property
    def prompt(self):
        """returns prompt property"""
        return self.prompt

    @prompt.setter
    def prompt(self) -> str:
        """sets the prompt attribute based on page number"""
        main_menu_prompt = """Welcome to SN-GEN!
        1 - generate serialnumber
        2 - save serialnumber
        3 - validate serialnumber
        4 - exit."""
        generator_prompt = """SN-GEN:
        1 - to save your generated serialnumbers
        2 - back to main menu
        3 - exit."""

        self._prompt = main_menu_prompt if self._page == 1 else generator_prompt

    def run(self) -> None:
        """starts the programm loop and takes user input."""
        while True:
            user_interaction = input(self.prompt)

            if user_interaction == 
