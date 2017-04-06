
import time
import random
import fractions

park_miller_n = 2147483647 #2^31 - 1
park_miller_g = 48271
def park_miller(old_seed):
    return (old_seed * park_miller_g) % park_miller_n

lcg_a = 6364136223846793005
lcg_c = pow(2,31)-1
def linear_congruential_generator(seed, m):
    return (lcg_a * seed + lcg_c) % m

def generate_and_verify(bits, generator, verifier, seed, precision = 10):
    result = int(bin(seed)[:bits], 2)
    begin = time.time()
    m = pow(2, bits)
    while(not verifier(result, precision)):
        result = generator(result, m)
        #result = int(bin(result)[:bits], 2)

    elapsed = (time.time() - begin)
    return result, elapsed

def fermat_test(number, times = 5):
    for i in range(times):
        a = random.randrange(number)
        if pow(a, number, number) != a:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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
        if fractions.gcd(a, p) != 1: #not coprime
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
        if jacobi == 0 or pow(a, (number - 1) / 2 , number) != jacobi % number:
            return False
    return True

if __name__ == "__main__":
    bits = input("Type in the amount of bits of the desired prime:")
    seed = input("Type in the seed:")
    number, time = generate_and_verify(bits, linear_congruential_generator, solovay_strassen_test, seed)
    print("Prime: " + str(number))
    print("Time elapsed(s): " + str(time))
