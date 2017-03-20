import unittest
import vigenere
from collections import namedtuple

import pdb

class vigenereTest(unittest.TestCase):

    def setup(self):
        pass

    def test_encrypt(self):
        key = "mykey"

        self.assertEqual("", vigenere.encrypt("abcde", key))

if __name__ == '__main__':
    unittest.main()
