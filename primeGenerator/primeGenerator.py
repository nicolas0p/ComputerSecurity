
park_miller_n = 2147483647 #2^31 - 1
park_miller_g = 48271
def park_miller(old_seed):
    return (old_seed * park_miller_g) % park_miller_n

x0 = 2
def generate_and_verify(bits, generator, verifier):
    result = int(bin(x0)[:bits], 2)
    while(not verifier(result) or len(bin(result)) < bits):
        result = generator(result)
        result = int(bin(result)[:bits], 2)

    return result

def fermat_little_theorem(number):
    return (3 ** number) % number == 3

if __name__ == "__main__":
    bits = input("Type in the amount of bits of the desired prime:")
    print(generate_and_verify(bits, park_miller, fermat_little_theorem))
