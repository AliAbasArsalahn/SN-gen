# Projekt: Seriennummergenerator | Modul: sn
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""
SN class module.
"""


from string import ascii_letters, digits
from random import randrange
import json

class SN():
    """
    sn-object can be iniatilized as number, letter or mixed generator.
    """

    def __init__(self, type):
        self.keys = {}
        self.type = type

    def key_generator(self, count: int,rows: int, row_length: int) -> None:
        """
        Takes type, rows and row_length as arguments.
        Calls the function available_characters to get a random character.
        Generates the key-string and puts it in the dictionary "keys".
        """
        def generate_char(type) -> str:
            """
            Checks the type of the object and returns a random character from
            the Strings: string.ascii_letters, string.digits.
            """
            if type == 'letter':
                rnd_nmb = randrange((len(ascii_letters)) - 1)
                return ascii_letters[rnd_nmb]
            else:
                rnd_nmb = randrange((len(digits)) - 1)
                return digits[rnd_nmb]

        key: str = ''
        for i in range(count + 1):
            for i in range(rows * row_length):
                key.join(generate_char(self.type))
                if (i >= row_length) and (i / row_length == 1):
                    key += '-'
            self.keys[key[:-1]] = True

    def save_serialnumber(self) -> None:
        """
        Takes the dictionary "keys" and writes them to a file.
        """
        with open('keys.json', 'a') as file:
            json.dump(self.keys, file)

    def delete_serialnumber(self) -> None:
        pass

    def validate_serialnumber(self) -> None:
        """
        Takes a SN as an argument and checks if it is valid.
        """
        with open('keys.json', 'r') as file:
            pass
