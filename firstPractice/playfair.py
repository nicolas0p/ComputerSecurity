import string
from collections import OrderedDict
from collections import namedtuple

removed_letter = 'y'
alphabet = string.ascii_lowercase.replace(removed_letter, '')

def _generate_key_matrix(key):
    key = key.replace(' ', '').strip() #remove whitespace
    key = key.replace(removed_letter, '')
    key = [x for x in key if x in alphabet]
    key = list(OrderedDict.fromkeys(key))

    keyMatrix = [[0 for x in range(5)] for y in range(5)]
    already_in = set()
    for char in key:
        keyMatrix[len(already_in) // 5][len(already_in) % 5] = char
        already_in.add(char)

    remaining = len(alphabet) - len(already_in)
    for char in list(alphabet):
        for i in range(remaining):
            if char not in already_in:
                keyMatrix[len(already_in) // 5][len(already_in) % 5] = char
                already_in.add(char)
    return keyMatrix

def _position_in_matrix(character, keyMatrix):
    position = namedtuple('Position', ['x', 'y'])
    for x in range(len(keyMatrix)):
        if character in keyMatrix[x]:
            position.x = x
            position.y = keyMatrix[x].index(character)
            return position
    return False

def _find_next_pair(text, leftPosition, rightPosition = 0):
    if rightPosition == 0:
        rightPosition = leftPosition + 1
    """Finds the next available pair of characters in 'text' starting at 'leftPosition'
    @param text string where the pair will be found
    @param leftPosition the first position the left character could be positioned
    @param rightPosition the first position the right character could be positioned
    """
    if rightPosition == len(text):
        text += "z"
    if text[leftPosition] not in alphabet:
        return _find_next_pair(text, leftPosition + 1)
    if text[rightPosition] not in alphabet:
        return _find_next_pair(text, leftPosition, rightPosition + 1)
    return text[leftPosition], text[rightPosition], leftPosition, rightPosition

def _encrypt_pair(pair, keyMatrix):
    left_char_position = _position_in_matrix(pair[0], keyMatrix)
    right_char_position = _position_in_matrix(pair[1], keyMatrix)
    if left_char_position.x == right_char_position.x:
        #same row get char to the right
        left = keyMatrix[left_char_position.x][(left_char_position.y + 1) % len(keyMatrix)]
        right = keyMatrix[right_char_position.x][(right_char_position.y + 1) % len(keyMatrix)]
        return left + right
    if left_char_position.y == right_char_position.y:
        #same column get char below
        left = keyMatrix[(left_char_position.x + 1) % len(keyMatrix)][left_char_position.y]
        right = keyMatrix[(right_char_position.x + 1) % len(keyMatrix)][right_char_position.y]
        return left + right
    left = keyMatrix[left_char_position.x][right_char_position.y]
    right = keyMatrix[right_char_position.x][left_char_position.y]
    return left + right

def _decrypt_pair(pair, keyMatrix):
    left_char_position = _position_in_matrix(pair[0], keyMatrix)
    right_char_position = _position_in_matrix(pair[1], keyMatrix)
    if left_char_position.x == right_char_position.x:
        #same row get char to the left
        left = keyMatrix[left_char_position.x][(left_char_position.y - 1) % len(keyMatrix)]
        right = keyMatrix[right_char_position.x][(right_char_position.y - 1) % len(keyMatrix)]
        return left + right
    if left_char_position.y == right_char_position.y:
        #same column get char above
        left = keyMatrix[(left_char_position.x - 1) % len(keyMatrix)][left_char_position.y]
        right = keyMatrix[(right_char_position.x - 1) % len(keyMatrix)][right_char_position.y]
        return left + right
    left = keyMatrix[left_char_position.x][right_char_position.y]
    right = keyMatrix[right_char_position.x][left_char_position.y]
    return left + right

"""Ignored characters are the removed character plus special characters"""
def _preceding_ignored(plaintext):
    i = 0
    for i in range(len(plaintext)):
        if plaintext[i] in alphabet:
            return plaintext[i:], removed_letter * i
    return "", plaintext

def _following_ignored(plaintext):
    i = len(plaintext) - 1
    for i in range(len(plaintext)-1, -1, -1):
        if plaintext[i] is not removed_letter:
            return plaintext[:i+1], removed_letter * (len(plaintext) - i - 1)
    return "", plaintext

def encrypt(plaintext, keyMatrix):
    plaintext = plaintext.replace(' ', '').lower()
    if len([x for x in plaintext if x in alphabet]) % 2 == 1:
        plaintext += 'z'
    plaintext, preceding = _preceding_ignored(plaintext)
    plaintext, following = _following_ignored(plaintext)
    cyphertext = ""
    i = 0
    last_right = 0
    while i < len(plaintext):
        char_left, char_right, left, right = _find_next_pair(plaintext, i)
        cypherpair = _encrypt_pair(char_left + char_right, keyMatrix)
        removed = plaintext[left+1:right]
        between_pairs = plaintext[last_right+1:left]
        cyphertext += between_pairs + cypherpair[0] + removed + cypherpair[1]
        i = right + 1
        last_right = right
    return preceding + cyphertext + following

def decrypt(cyphertext, keyMatrix):
    cyphertext = cyphertext.replace(' ', '').lower()
    cyphertext, preceding = _preceding_ignored(cyphertext)
    cyphertext, following = _following_ignored(cyphertext)
    plaintext = ""
    i = 0
    last_right = 0
    while i < len(cyphertext):
        char_left, char_right, left, right = _find_next_pair(cyphertext, i)
        plainpair = _decrypt_pair(char_left + char_right, keyMatrix)
        removed = cyphertext[left+1:right]
        between_pairs = cyphertext[last_right+1:left]
        plaintext += between_pairs + plainpair[0] + removed + plainpair[1]
        i = right + 1
        last_right = right
    return preceding + plaintext + following

if __name__ == "__main__":
    key = str(input("Type in the key you want to use with the playfair algorightm:"))
    print(key)
    plaintext = str(input("Type in the plaintext you want to cypher:"))
    print(plaintext)
    keyMatrix = _generate_key_matrix(key)
    cyphertext = encrypt(plaintext, keyMatrix)
    print("Cyphertext = '{}'".format(cyphertext))
