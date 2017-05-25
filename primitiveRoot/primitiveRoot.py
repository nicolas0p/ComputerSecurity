
def prime_factorization(n):
    result = {}
    while (n/2).is_integer():
        n = n/2
        if 2 in result:
            result[2] += 1
        else:
            result[2] = 1
    i = 3
    while n > 1:
        while (n/i).is_integer():
            n = n/i
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        i += 2
        if i > n:
            break
    if len(result) == 0:
        result[n] = 1 #prime number
    return result

"""@returns a^-1 mod n"""
def inverse(a, n):
    t = 0; newt = 1
    r = n; newr = a
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        return False #a is not invertible mod n
    if t < 0:
        t += n
    return t

"""Euler's Totient function"""
def phi_with_factors(n):
    primes = prime_factorization(n)
    result = n
    for prime in primes.keys():
        result *= (1 - 1/prime)
    return int(result), primes

def phi(n):
    return phi_with_factors(n)[0]

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def coprimes(n):
    result = set()
    for i in range(1,n):
        if gcd(n, i) == 1:
            result.add(i)
    return result

def find_primitive_roots_given_one(n, root):
    power = coprimes(phi(n))
    roots = set()
    for i in power:
        roots.add(pow(root, i, n))
    return roots

def _is_primitive_root(toTest, n, euler, primes_phi):
    for prime in primes_phi.keys():
        if pow(toTest, int(euler/prime), n) == 1:
            return False
    return True

"""Finds the first primitive root modulo n
@param euler phi(n)
@param primes_phi integer factorization of phi(n)"""
def find_first_primitive_root(n, euler, primes_phi):
    for i in range(2, n):
        if _is_primitive_root(i, n, euler, primes_phi):
            return i

def find_primitive_roots(n):
    euler = phi(n)
    primes_phi = prime_factorization(euler)
    first_root = find_first_primitive_root(n, euler, primes_phi)
    return find_primitive_roots_given_one(n, first_root)

if __name__ == "__main__":
    n = int(input("Type in the number for which you want to know the primitive roots:"))
    roots = find_primitive_roots(n)
    print(roots)
