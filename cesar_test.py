import unittest
import cesar

import pdb

class vigenereTest(unittest.TestCase):

    def setup(self):
        pass

    def test_encrypt(self):
        key = 3
        self.assertEqual("defgh", cesar.encrypt("abcde", key))
        self.assertEqual("qlfrodv", cesar.encrypt("nicolas", key))
        self.assertEqual("q!lf.r", cesar.encrypt("n!ic.o", key))
        key = 4
        self.assertEqual("MwwsQiwqsEuymm", cesar.encrypt("IssoMesmoAquii", key))

    def test_decrypt(self):
        key = 3
        #pdb.set_trace()

        self.assertEqual("abcde", cesar.decrypt("defgh", key))
        self.assertEqual("nicolas", cesar.decrypt("qlfrodv", key))
        self.assertEqual("nico", cesar.decrypt("qlfr", key))
        key = 4
        self.assertEqual("IssoMesmoAquii", cesar.decrypt("MwwsQiwqsEuymm", key))

if __name__ == '__main__':
    unittest.main()
