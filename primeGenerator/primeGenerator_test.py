import unittest
import primeGenerator

import pdb

class primeGeneratorTest(unittest.TestCase):

    def setup(self):
        pass

    def test_solovay_strassen_test(self):
        verificator = primeGenerator.solovay_strassen_test

        primes = [104677, 104681, 104683, 104693, 104701, 104707, 104711, 104717, 104723, 104729]
        primes.extend([2 ** 4253 - 1, 2**3217-1, 2**2281-1, 2**2203-1])

        times = 10

        for i in primes:
            self.assertTrue(verificator(i, times), i)

        for i in primes:
            self.assertFalse(verificator(i - 1, times), i - 1)

    def test_jacobi_symbol(self):
        jacobi_symbol = primeGenerator.jacobi_symbol

        examples = [(1,1,1), (11,23,-1), (23,7,1), (6,45,0), (30,59,-1)]

        for k, n, correct in examples:
            result = jacobi_symbol(k, n)
            self.assertTrue(result == correct, "({}/{}) = {} not {}".format(k,n,correct, result))

if __name__ == '__main__':
    unittest.main()
