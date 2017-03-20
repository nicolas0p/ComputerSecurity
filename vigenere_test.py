import unittest
import vigenere
from collections import namedtuple

import pdb

class vigenereTest(unittest.TestCase):

    def setup(self):
        pass

    def test_extend_key(self):
        key = "my,ke@y!"

        self.assertEqual(list("mykeymy"), vigenere._extend_key(key, 7))

    def test_encrypt(self):
        key = "mykey"
        self.assertEqual("mzmhC", vigenere.encrypt("abcde", key))
        self.assertEqual("zGmsJmQ", vigenere.encrypt("nicolas", key))
        self.assertEqual("z,sgM@", vigenere.encrypt("n,ico@", key))
        key = "aNotherkEY"
        self.assertEqual("IfGHTiJwSyqhwB", vigenere.encrypt("IssoMesmoAquii", key))

    def test_decrypt(self):
        key = "mykey"
        #pdb.set_trace()

        self.assertEqual("abcde", vigenere.decrypt("mzmhC", key))
        self.assertEqual("nicolas", vigenere.decrypt("zGmsJmQ", key))
        self.assertEqual("nico", vigenere.decrypt("zGms", key))
        key = "aNotherkEY"
        self.assertEqual("IssoMesmoAquii", vigenere.decrypt("IfGHTiJwSyqhwB", key))

if __name__ == '__main__':
    unittest.main()
