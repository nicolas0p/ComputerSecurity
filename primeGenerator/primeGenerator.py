
import time
import random

park_miller_n = 2147483647 #2^31 - 1
park_miller_g = 48271
def park_miller(old_seed):
    return (old_seed * park_miller_g) % park_miller_n

def generate_and_verify(bits, generator, verifier, seed = 2):
    result = int(bin(seed)[:bits], 2)
    begin = time.time()
    while(not verifier(result)):
        result = generator(result)
        result = int(bin(result)[:bits], 2)

    elapsed = (time.time() - begin)
    return result, elapsed

def fermat_test(number, times = 5):
    for i in range(times):
        a = random.randrange(number)
        if pow(a, number, number) != a:
            return False
    return True

def is_quadratic_residue(a, p):
    a_mod_p = a % p
    times = 5
    for i in range(times):
        i = random.randrange(p // 2)
        if pow(i, 2, p) == a_mod_p:
            return True
    return False

def legendre(a, p):
    residue = is_quadratic_residue(a, p)
    if residue and a % p != 0:
        return 1
    if not residue:
        return -1
    if a % p == 0:
        return 0
    raise Exception

def solovay_strassen_test(number):
    a = 2
    result1 = pow(a, (number - 1)/2, number)
    result2 = legendre(a, number) % number
    return result1 == result2

if __name__ == "__main__":
    bits = input("Type in the amount of bits of the desired prime:")
    seed = input("Type in the seed(must be coprime with 2^31-1):")
    number, time = generate_and_verify(bits, park_miller, solovay_strassen_test, seed)
    print("Prime: " + str(number))
    print("Time elapsed(s): " + str(time))
