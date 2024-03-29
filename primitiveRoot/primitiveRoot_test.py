import unittest
import primitiveRoot

class primitiveRootTest(unittest.TestCase):

    def test_prime_factorization(self):
        five = primitiveRoot.prime_factorization(5)
        fifteen = primitiveRoot.prime_factorization(15)
        seventyfive = primitiveRoot.prime_factorization(75)
        last = primitiveRoot.prime_factorization(112)
        prime = primitiveRoot.prime_factorization(191)

        self.assertEqual(five, {5:1})
        self.assertEqual(fifteen, {5:1, 3:1})
        self.assertEqual(seventyfive, {5:2, 3:1})
        self.assertEqual(last, {2:4, 7:1})
        self.assertEqual(prime, {191:1})

    def test_eulers_totient(self):
        first = primitiveRoot.phi(5)
        second = primitiveRoot.phi(12)
        third = primitiveRoot.phi(36)
        fourth = primitiveRoot.phi(99)

        self.assertEqual(first, 4)
        self.assertEqual(second, 4)
        self.assertEqual(third, 12)
        self.assertEqual(fourth, 60)

    def test_find_primitive_roots(self):
        first = primitiveRoot.find_primitive_roots(23)

        self.assertEqual(first, {5, 7, 10, 11, 14, 15, 17, 19, 20, 21})
        self.assertEqual(len(first), primitiveRoot.phi(primitiveRoot.phi(23)))

    def test_find_primitive_roots_given_one(self):
        first = primitiveRoot.find_primitive_roots_given_one(23, 5)
        second = primitiveRoot.find_primitive_roots_given_one(2089, 7)

        self.assertEqual(first, {5, 7, 10, 11, 14, 15, 17, 19, 20, 21})
        euler = primitiveRoot.phi(2089)
        for i in second:
            self.assertTrue(pow(i, euler, 2089) == 1)

if __name__ == '__main__':
    unittest.main()
