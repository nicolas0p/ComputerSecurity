
import time, timeit
import random
import math

lcg_a = 6364136223846793005
lcg_c = 1442695040888963407
"""linear congruential generator function
@param seed xn-1. Number that will be operated on to generate a new number
@param m max number in the search space
@return pseudorandom number generated by the LCG function"""
def linear_congruential_generator(seed, m):
    return (lcg_a * seed + lcg_c) % m

xorshift_a = 13
xorshift_b = 17
xorshift_c = 5
"""Pseudorandom number generator function
@param seed xn-1. Number that will be operated on to generate a new number
@param m max number in the search space
@return [2,log(m)-1] significant bits of the generated number"""
def xorshift_generator(seed, m):
    x = seed
    x = x ^ (x << xorshift_a)
    x = x ^ (x >> xorshift_b)
    x = x ^ (x << xorshift_c)
    return (x & m-1) >> 2 #it only keeps the bits-1 more significant bits and ignores the 2 least significant

"""This function generates a pseudorandom prime by generating pseudorandom numbers and
testing to see if they are prime
@param bits desired bitlenght of the returned prime
@param generator pseudorandom number generator function
@param verifier primality test function
@precision number of iterations of the primality test function
@return result pseudorandom prime number
@return elapsed time spent calculating"""
def generate_and_verify(bits, generator, verifier, precision = 10):
    begin = timeit.default_timer()
    m = pow(2, bits)
    result = pow(int(time.time()), bits, m-1) #generates a seed about the size of m
    while(not verifier(result, precision)):
        result = generator(result, m)

    elapsed = (timeit.default_timer() - begin)
    return result, elapsed

def fermat_test(number, times = 5):
    for i in range(times):
        a = random.randrange(number)
        if pow(a, number, number) != a:
            return False
    return True

"""Miller-Rabin primality test
@param number number which the user wants to know whether it is prime or not
@param k related to precision. Number of iterations of the algorithm
@return False if the number is composite, True if it is a probable prime"""
def miller_rabin_test(number, k):
    s = 0
    n = number
    number = number - 1
    while number % 2 == 0:
        number = number // 2
        s = s + 1
    for i in range(k):
        a = random.randrange(2, n-1)
        x = pow(a, number, n)
        if x == 1 or x == n - 1:
            continue
        flag = True
        for r in range(s):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                flag = False
                break
        if flag:
            return False
    return True

"""Jacobi symbol calculation function
@param a jacobu symbol "numerator"
@param p jacobi symbol "denominator"
@return the jacobi symbol of (a/p). -1, 0 or 1"""
def jacobi_symbol(a, p):
    a = a % p #Rule 2 (a/b) = (a mod b / b)
    result = 1
    while a != 0:
        while a % 2 == 0: #Decomposition in powers of two
            a = a // 2
            if p % 8 == 3 or p % 8 == 5: #Rule 8
                result = -result
        if a == 1:
            return result
        if math.gcd(a, p) != 1: #not coprime
            return 0
        if a % 4 == 3 and p % 4 == 3:
            result = -result
        temp = a
        a = p
        p = temp
        a = a % p
    if p == 1:
        return result
    return 0

"""Solovay-Strassen primality test
@param number possible prime user wants to test
@param k number of iterations of the algorithm
@return False if the number is composite, True if it is a probable prime"""
def solovay_strassen_test(number, k):
    for i in range(k):
        a = random.randrange(number)
        jacobi = jacobi_symbol(a, number)
        if jacobi == 0 or pow(a, (number - 1) // 2 , number) != jacobi % number:
            return False
    return True

if __name__ == "__main__":
    bits = int(input("Type in the amount of bits of the desired prime:"))
    print("Prime = " + str(generate_and_verify(bits, xorshift_generator, solovay_strassen_test)[0]))
    """bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    for length in bits:
        number, elapsed = generate_and_verify(length, xorshift_generator, solovay_strassen_test)
        print("Prime({}): ".format(length) + str(number))
        print("Time elapsed(s)({}): ".format(length) + str(elapsed))
    """""""
    Used to measure each generators speed
    bits = int(input("Type in the amount of bits of the desired primes:"))
    #import pdb; pdb.set_trace()
    total_time = 0
    numbers = []
    m = pow(2,bits)
    number = pow(int(time.time()), bits, m-1) #x0. This is the seed
    string = ""
    k = 10000
    for i in range(k):
        begin = timeit.default_timer()
        number = linear_congruential_generator(number, m)
        elapsed = timeit.default_timer() - begin
        numbers.append(number)
        total_time += elapsed
        string += str(number) + ", "
    print("Primes:")
    #print(string)
    print("Average time elapsed(s): " + str(total_time/k))"""
