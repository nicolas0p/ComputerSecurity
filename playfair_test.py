import unittest
import playfair
from collections import namedtuple

import pdb

class playfairTest(unittest.TestCase):

    def setup(self):
        pass

    def test_generate_key_matrix(self):
        key = "    boa tarde   "
        keyMatrix = playfair._generate_key_matrix(key)

        correct = [['b', 'o', 'a', 't', 'r'],
                ['d', 'e', 'c', 'f', 'g'],
                ['h', 'i', 'j', 'k', 'l'],
                ['m', 'n', 'p', 'q', 's'],
                ['u', 'v', 'w', 'x', 'z']]

        self.assertEqual(correct, keyMatrix)

        keyMatrixEmpty = playfair._generate_key_matrix("")
        defaultKey = [['a', 'b', 'c', 'd', 'e'],
                ['f', 'g', 'h', 'i', 'j'],
                ['k', 'l', 'm', 'n', 'o'],
                ['p', 'q', 'r', 's', 't'],
                ['u', 'v', 'w', 'x', 'z']]

        self.assertEqual(defaultKey, keyMatrixEmpty)

        keyMatrixLonger = playfair._generate_key_matrix("abcdefghijklmnopqrstuvwxyzs")
        self.assertEqual(defaultKey, keyMatrixLonger)

        keyMatrixWithRemovedLetter = playfair._generate_key_matrix("abcyd")
        self.assertEqual(defaultKey, keyMatrixWithRemovedLetter)


    def test_find_next_pair(self):
        text = "yayyyybyyyy"
        result = playfair._find_next_pair(text, 0)
        self.assertEqual(('a', 'b', 1, 6), result)

        result = playfair._find_next_pair(text, 1)
        self.assertEqual(('a', 'b', 1, 6), result)

        result = playfair._find_next_pair(text, 2)
        self.assertEqual(('b', 'z', 6, 11), result)

        result = playfair._find_next_pair(text, 6)
        self.assertEqual(('b', 'z', 6, 11), result)

    def test_position_in_matrix(self):
        keyMatrix = playfair._generate_key_matrix("nunca")
        keyMatrix2 = playfair._generate_key_matrix("dcba")

        result1 = playfair._position_in_matrix('a', keyMatrix)

        self.assertEqual((0,3), (result1.x, result1.y))

        result2 = playfair._position_in_matrix('j', keyMatrix2)

        self.assertEqual((1,4), (result2.x, result2.y))

    def test_encrypt_pair(self):
        keyMatrix = playfair._generate_key_matrix("plajf irexm bcdgh knoqs tuvwz")

        self.assertEqual("od", playfair._encrypt_pair("de",  keyMatrix))

        self.assertEqual("xm", playfair._encrypt_pair("ex", keyMatrix))

        self.assertEqual("zb", playfair._encrypt_pair("th", keyMatrix))

    def test_encrypt(self):
        keyMatrix = playfair._generate_key_matrix("boa tarde")

        self.assertEqual("ribypvmeb", playfair.encrypt(" olay mundo  ", keyMatrix))
        pdb.set_trace()
        self.assertEqual("vneajrmslw", playfair.encrypt("nicolasqj", keyMatrix))

        self.assertEqual("yehtyobny", playfair.encrypt("ydiaybomy", keyMatrix))

if __name__ == '__main__':
    unittest.main()
