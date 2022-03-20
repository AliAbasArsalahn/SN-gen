# Projekt: Seriennummergenerator | Modul: sn
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""
SN class module.
"""


from encodings import utf_8
from string import ascii_letters, digits
from random import randrange
import json

class SN():
    """
    sn-object can be iniatilized as number or letter generator.
    """

    def __init__(self, sn_type):
        self.keys = {}
        self.sn_type = sn_type

    def generate_serialnumber(self) -> None:
        """
        Generates a serialnumber. Calls seperate functions for random letter or digits.
        Iterates through a list of keys and appends them to the dictionary.
        Takes key_count, key_rows and key_row_lenght as seperate input arguments.
        """

        def generate_letter() -> str:
            """
            returns a random letter.
            """
            rnd_nmb = randrange((len(ascii_letters)) - 1)
            return ascii_letters[rnd_nmb]

        def generate_digit() -> str:
            """
            returns a random digit.
            """
            rnd_nmb = randrange((len(digits)) - 1)
            return digits[rnd_nmb]

        def generate_string(count: int, rows: int, row_length: int, tmp_list) -> list:
            """
            Generates a serialnumber. checks the object type and returns either a
            letter or digit based serialnumber. Yields a tmp_list as generator or makes
            a recursive function call if more keys need to be generated.
            """

            key = ''

            for i in range(rows * row_length):
                if self.sn_type == 'letter':
                    key += generate_letter()
                else:
                    key += generate_digit()

                # if (i >= (row_length - 1)) and (i / (row_length - 1)  == 1):
                #     key += '-'
            tmp_list.append(key)
            if count <= 1:
                return tmp_list
            return generate_string((count - 1), rows, row_length, tmp_list)

        # User input
        key_count = int(input("quantity: "))
        key_rows = int(input("rows: "))
        key_row_length = int(input("rowlength: "))

        tmp_list = []
        end_list = generate_string(key_count, key_rows, key_row_length, tmp_list)
        for key in end_list:
            self.keys[key] = True

    def save_serialnumber(self) -> None:
        """
        Takes the dictionary "keys" and writes them to a file.
        """
        with open('keys.json', 'a', encoding=utf_8) as file:
            json.dump(self.keys, file)

    def delete_serialnumbers(self) -> None:
        """
        Empties the objects dictionary.
        """
        self.keys.clear()

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

letter_generator = SN('letter')
digit_generator = SN('digit')

digit_generator.generate_serialnumber()
print(digit_generator.keys)
