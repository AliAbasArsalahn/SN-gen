# Projekt: Seriennummergenerator | Modul: sn
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""
SN class module.
"""


from string import ascii_letters, digits
from random import randrange


class SN:
    """
    sn-object can be iniatilized with varying type, rows and rowlength.\n
    key gets created according to set paramaters of the object.\n
    sn-objects get created with Valid flag on default.
    """

    def __init__(self):
        """Creates a class objekt and assigns the constant TYPES as property."""
        self.TYPES = ['letter', 'digit', 'mixed']
        self.keys = {}

    def key_generator(self, type: str, rows: int, row_length: int) -> None:
        """
        Takes type, rows and row_length as arguments.
        Calls the function available_characters to get a random character.
        Generates the key-string and puts it in the dictionary "keys".
        """
        def available_characters(type: str) -> str:
            """
            Checks the type of the object and returns a random character from
            the Strings: string.ascii_letters, string.digits or both.
            """
            if type == 'letter':
                rnd_nmb = randrange((len(ascii_letters)) - 1)
                return ascii_letters[rnd_nmb]
            elif type == 'digit':
                rnd_nmb = randrange((len(digits)) - 1)
                return digits[rnd_nmb]
            else:
                rnd_nmb = randrange((len(ascii_letters + digits)) - 1)
                return (ascii_letters + digits)[rnd_nmb]

        key: str = ''
        for i in range(rows * row_length):
            key.join(available_characters(type))
            if (i >= row_length) and (i / row_length == 1):
                key += '-'
        self.keys[key[:-1]] = True

    def save_serialnumber(self) -> None:
        """
        Takes the dictionary "keys" and writes them to a file.
        """
        with open('keys.csv', 'w') as file:
            pass

    def validate_serialnumber(self) -> None:
        """
        Takes a SN as an argument and checks if it is valid.
        """
        with open('keys.csv', 'w') as file:
            pass
