# Projekt: Seriennummergenerator | Modul: sn
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
'''sn: class definition for sn-project'''


from string import ascii_letters, digits
from random import randrange


class SN:
    '''
    sn-object can be iniatilized with varying type, rows and rowlength.\n
    key gets created according to set paramaters of the object.\n
    sn-objects get created with Valid flag on default.'''

    TYPES = ['letter', 'digit', 'mixed']

    def __init__(self, sn_type, rows: int, row_length: int, key='', valid=True):
        self._type = sn_type
        self.rows = rows
        self._row_length = row_length
        self.valid = valid
        self._key = key

    def __str__(self) -> str:
        return f"type: {self._type}, rows: {self.rows}, valid: {self.valid}"

    @property
    def sn_type(self):
        '''type getter'''
        return self._type

    @sn_type.setter
    def sn_type(self, value) -> None:
        '''Setter for type property.\n
        User can choose between set types that are defined in the CONST List TYPES.\n'''
        if value in self.TYPES:
            self._type = value

    @property
    def key(self):
        '''key getter'''
        return self._key

    @key.setter
    def key(self) -> str:
        self._key = ''

        def char_generator(type: str) -> str:
            '''Checks the type of the object and returns a random character from
            the Strings: string.ascii_letters, string.digits or both.'''
            if type == 'letter':
                rnd_nmb = randrange((len(ascii_letters)) - 1)
                return ascii_letters[rnd_nmb]
            elif type == 'digit':
                rnd_nmb = randrange((len(digits)) - 1)
                return digits[rnd_nmb]
            else:
                rnd_nmb = randrange((len(ascii_letters + digits)) - 1)
                return (ascii_letters + digits)[rnd_nmb]

        for i in range(self.rows * self._row_length):
            self._key += char_generator(self._type)
            if (i >= self._row_length) and (i / self._row_length == 1):
                self._key += '-'
