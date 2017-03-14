
plaintext = "Nícolas"
cyphertext = ""
delta = 3
decrypted = ""
for char in plaintext:
    encrypted = chr(ord(char)+delta)
    cyphertext += encrypted
    decrypted += chr(ord(encrypted)-delta)
print("Plaintext = " + plaintext)
print("Cyphertext = " + cyphertext)
