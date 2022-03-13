# Projekt: Seriennummergenerator | interface
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
#                                   WORK-IN-PROGRESS                           #
'''Interface module'''
'''Interface module'''


class CLIInterface:
    def __init__(self, page: int, prompt: str, interaction: list):
        self.page = page
        self._prompt = prompt
        self.interaction = interaction

    @property
    def prompt(self):
        return self._prompt

    @prompt.setter
    def prompt(self, text: str) -> None:
        self._prompt = text




def console_input() -> str:
    '''Takes arguments from user and returns them.'''
    type_choice = input("Zahlen oder Buchstaben: ")
    length_choice = input("Gib die Länge der gewünschten SN ein: ")
    row_choice = input("Wieviele Reihen soll die Seriennummer beinhalten?")
    return type_choice, length_choice, row_choice
