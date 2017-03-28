import string

alphabet = string.ascii_letters

def _extend_key(key, plaintext_size):
    key = key.replace(' ','').strip()
    key = [x for x in key if x in alphabet]
    result = key * (plaintext_size // len(key))
    char_left = plaintext_size - len(result)
    result += key[:char_left]
    return result

def encrypt(plaintext, key):
    key = _extend_key(key, len(plaintext))
    cyphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i] not in alphabet:
            cyphertext += plaintext[i]
            continue
        index = (alphabet.index(plaintext[i])+alphabet.index(key[i])) % len(alphabet)
        cyphertext += alphabet[index]
    return cyphertext

def decrypt(cyphertext, key):
    key = _extend_key(key, len(cyphertext))
    plaintext = ""
    for i in range(len(cyphertext)):
        if cyphertext[i] not in alphabet:
            plaintext += cyphertext[i]
            continue
        index = (alphabet.index(cyphertext[i])-alphabet.index(key[i])) % len(alphabet)
        plaintext += alphabet[index]
    return plaintext

if __name__ == "__main__":
    key = str(input("Type in the key you want to use with the vigenere algorightm:"))
    print(key)
    plaintext = str(input("Type in the plaintext you want to cypher:"))
    print(plaintext)
    cyphertext = encrypt(plaintext, key)
    print("Cyphertext = '{}'".format(cyphertext))
