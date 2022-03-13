# Projekt: Seriennummergenerator | interface
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
#                                   WORK-IN-PROGRESS                           #
'''Interface module'''


class CLIInterface:
    '''class CLI.\n Template for buidling an interactive interface.'''
    def __init__(self, page: int, display: str, interaction: list):
        self.page = page
        self._display = display
        self.interaction = interaction

    @property
    def prompt(self):
        '''Display getter.'''
        return self._display

    @prompt.setter
    def prompt(self, text: str) -> None:
        self._display = text
