
import time
import random
import math

park_miller_n = 2147483647 #2^31 - 1
park_miller_g = 48271
def park_miller(old_seed):
    return (old_seed * park_miller_g) % park_miller_n

lcg_a = 6364136223846793005
lcg_c = 1442695040888963407
def linear_congruential_generator(seed, m):
    return (lcg_a * seed + lcg_c) % m

xorshift_a = 13
xorshift_b = 17
xorshift_c = 5
def xorshift_generator(seed, m):
    x = seed
    x = x ^ (x << xorshift_a)
    x = x ^ (x >> xorshift_a)
    x = x ^ (x << xorshift_a)
    return x & m-1 #it only keeps the bits-1 more significant bits

def generate_and_verify(bits, generator, verifier, precision = 10):
    begin = time.time()
    m = pow(2, bits)
    result = int(begin)#pow(7, bits, m) #generates a seed about the size of m
    while(not verifier(result, precision)):
        result = generator(result, m)

    elapsed = (time.time() - begin)
    return result, elapsed

def fermat_test(number, times = 5):
    for i in range(times):
        a = random.randrange(number)
        if pow(a, number, number) != a:
            return False
    return True

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

def solovay_strassen_test(number, k):
    for i in range(k):
        a = random.randrange(number)
        jacobi = jacobi_symbol(a, number)
        if jacobi == 0 or pow(a, (number - 1) // 2 , number) != jacobi % number:
            return False
    return True

if __name__ == "__main__":
    bits = int(input("Type in the amount of bits of the desired prime:"))
    number, time = generate_and_verify(bits, xorshift_generator, solovay_strassen_test)
    print("Prime: " + str(number))
    print("Time elapsed(s): " + str(time))
