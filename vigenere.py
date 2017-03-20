import string

alphabet = string.ascii_lowercase

def _extend_key(key, plaintext_size):
    result = key * (plaintext_size // len(key))
    

def encrypt(plaintext, key):
    plaintext = plaintext.lower()
    key = key.lower()
    key = _extend_key(key, len(plaintex))
    cyphertext = ""
    for i in range(plaintext):
        cyphertext + chr((ord(plaintext[i])+alphabet.index(key[i])) % ord('z'))
    return cyphertext

if __name__ == "__main__":
    key = str(input("Type in the key you want to use with the vigenere algorightm:"))
    print(key)
    plaintext = str(input("Type in the plaintext you want to cypher:"))
    print(plaintext)
    cyphertext = encrypt(plaintext, key)
    print("Cyphertext = '{}'".format(cyphertext))
