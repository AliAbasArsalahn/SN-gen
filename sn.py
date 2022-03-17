# Projekt: Seriennummergenerator | Modul: sn
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""
sn: class definition for sn-project
"""


from string import ascii_letters, digits
from random import randrange


class SN:
    """
    sn-object can be iniatilized with varying type, rows and rowlength.\n
    key gets created according to set paramaters of the object.\n
    sn-objects get created with Valid flag on default.
    """
    def __init__(self, sn_type: str, rows: int, row_length: int):
        self.type = sn_type
        self.rows = rows
        self.row_length = row_length
        self.valid = True
        self.TYPES = ['letter', 'digit', 'mixed']

    def key_generator(self) -> str:
        """
        Checks the type of the object and returns a random character from
        the Strings: string.ascii_letters, string.digits or both.
        """
        #####################WORK-IN-PROGRESS#################################
        key = ''
        if self.type == 'letter':
            rnd_nmb = randrange((len(ascii_letters)) - 1)
            return ascii_letters[rnd_nmb]
        elif self.type == 'digit':
            rnd_nmb = randrange((len(digits)) - 1)
            return digits[rnd_nmb]
        else:
            rnd_nmb = randrange((len(ascii_letters + digits)) - 1)
            return (ascii_letters + digits)[rnd_nmb]

        for i in range(self.rows * self._row_length):
            key += key_generator(self.type)
            if (i >= self._row_length) and (i / self._row_length == 1):
                key += '-'

    def save_serialnumber(self) -> None:
        """
        Takes a created SN as argument and appends it to a CSV file.
        """
        pass

    def validate_serialnumber(self) -> None:
        """
        Takes a SN as an argument and checks if it is valid.
        """
        pass