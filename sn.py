# Projekt: Seriennummergenerator | Modul: sn
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""
SN class module.
"""


from random import randrange
from string import ascii_letters, digits
from abc import ABC, abstractmethod
from encodings import utf_8
import json


class SN(ABC):
    """
    Base glass for serialnumbergenerators.
    """

    def __init__(self) -> None:
        self.keys = {}

    @abstractmethod
    def generate_serialnumber(self) -> None:
        """abstract method"""
        pass

    def validate_serialnumber(self) -> None:
        """
        Takes a SN as an argument and checks if it is valid.
        """
        validate_serialnumber = input("serialnumber to validate: ")
        with open('keys.json', 'r', encoding=utf_8) as file:
            data = json.load(file)
            try:
                if data[validate_serialnumber]:
                    print("key is valid!")
                else:
                    print("key is not valid")
            except IndexError:
                print("key not found!")

    def save_serialnumber(self) -> None:
        """
        writes existing keys to a json file.
        """
        with open('keys.json', 'a', encoding=utf_8) as file:
            json.dump(self.keys, file)

    def delete_serialnumbers(self) -> None:
        """
        Empties the objects dictionary.
        """
        self.keys.clear()


class LetterGenerator(SN):
    """
    Subclass of SN. Generates letterbased serialnumbers
    """

    def generate_serialnumber(self) -> None:
        """
        Generates a letterbased serialnumber.
        Calls seperate functions to generate chars.
        Takes key_count, key_rows as row_lenght as seperate arguments.
        """

        def generate_letter() -> str:
            """
            returns a random letter.
            """
            rnd_nmb = randrange(len(ascii_letters) - 1)
            return ascii_letters[rnd_nmb]

        def generate_string(count: int, rows: int, row_length: int, tmp_list: list) -> list:
            """
            Generates a serialnumber. Calls function "generate_letter" to receive letters.
            """

            key = ''

            for i in range(rows * row_length):
                key += generate_letter()

            tmp_list.append(key)
            if count <= 1:
                return tmp_list
            else:
                return generate_string((count - 1), rows, row_length, tmp_list)

        # user input
        key_count = int(input("quanitity: "))
        key_rows = int(input("rows: "))
        row_length = int(input("rowlength: "))

        tmp_list = []
        end_list = generate_string(key_count, key_rows, row_length, tmp_list)
        for key in end_list:
            self.keys[key] = True


class DigitGenerator(SN):
    """
    Subclass of SN. Generates letterbased serialnumbers
    """

    def generate_serialnumber(self) -> None:
        """
        generates a digitbased serialnumber.
        """

        def generate_digit() -> str:
            """
            returns a random digit.
            """
            rnd_nmb = randrange((len(digits)) - 1)
            return digits[rnd_nmb]

        def generate_string(count: int, rows: int, row_length: int, tmp_list: list) -> list:
            """
            generates a serialnumber. Returns either a tmp_list or a recursive call.
            """

            key = ''

            for i in range(rows * row_length):
                key += generate_digit()

            tmp_list.append(key)
            if count <= 1:
                return tmp_list
            else:
                return generate_string((count - 1), rows, row_length, tmp_list)

        # user input
        key_count = int(input("quantity: "))
        key_rows = int(input("rows: "))
        key_row_length = int(input("rowlength: "))

        tmp_list = []
        end_list = generate_string(
            key_count, key_rows, key_row_length, tmp_list)
        for key in end_list:
            self.keys[key] = True
