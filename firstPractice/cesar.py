import string

alphabet = string.ascii_letters

def encrypt(plaintext, key):
    cyphertext = ""
    for char in plaintext:
        if char not in alphabet:
            cyphertext += char
            continue
        index = (alphabet.index(char) + key) % len(alphabet)
        cyphertext += alphabet[index]
    return cyphertext

def decrypt(cyphertext, key):
    plaintext = ""
    for char in cyphertext:
        if char not in alphabet:
            plaintext += char
            continue
        index = (alphabet.index(char) - key) % len(alphabet)
        plaintext += alphabet[index]
    return plaintext

if __name__ == "__main__":
    key = int(input("Type in the key you want to use with the caesar algorightm:"))
    print(key)
    plaintext = str(input("Type in the plaintext you want to cypher:"))
    print(plaintext)
    cyphertext = encrypt(plaintext, key)
    print(cyphertext)
