import string
from collections import OrderedDict

alphabet = string.ascii_lowercase
removed_letter = "y"
key = "boa tarde"
key = key.replace(' ', '').strip() #remove whitespace
key = list(OrderedDict.fromkeys(key))

keyMatrix = [[0 for x in range(5)] for y in range(5)]
already_in = set()
for char in key:
    keyMatrix[len(already_in) // 5][len(already_in) % 5] = char
    already_in.add(char)

remaining = len(alphabet) - 1 - len(already_in)
alphabet = alphabet.replace(removed_letter, "")
for char in list(alphabet):
    for i in range(remaining):
        if char not in already_in:
            keyMatrix[len(already_in) // 5][len(already_in) % 5] = char
            already_in.add(char)
print(keyMatrix)
