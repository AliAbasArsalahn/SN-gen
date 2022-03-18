# Projekt: Seriennummergenerator | Modul: test_sn
# Author: Ali Abas Arsalahn
# Datum: 17.03.2022
"""
Test module for sn
"""

import unittest

from sn import SN


class TestSN(unittest.TestCase):
    """
    Testclass for SN.
    """
    def setUp(self) -> None:
        letter_generator = SN('letter')
        number_generator = SN('digit')

    def tearDown(self) -> None:
        pass

    def test_key_generator(self):
        self.assertEqual(SN.key_generator('letter', ))

    def test_save_serialnumber(self):
        pass

    def test_validate_serialnumber(self):
        pass

if __name__ == '__main__':
    unittest.main()