import string
from collections import OrderedDict
from collections import namedtuple

removed_letter = 'y'

def _generate_key_matrix(key):
    alphabet = string.ascii_lowercase
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
    if text[leftPosition] == removed_letter:
        return _find_next_pair(text, leftPosition + 1)
    if text[rightPosition] == removed_letter:
        return _find_next_pair(text, leftPosition, rightPosition + 1)
    return text[leftPosition], text[rightPosition], leftPosition, rightPosition

def _encrypt_pair(pair, keyMatrix):
    left_char_position = _position_in_matrix(pair[0], keyMatrix)
    right_char_position = _position_in_matrix(pair[1], keyMatrix)
    if left_char_position.x == right_char_position.x:
        #same row get char to the right
        left = keyMatrix[left_char_position.x][left_char_position.y + 1 % len(keyMatrix)]
        right = keyMatrix[right_char_position.x][right_char_position.y + 1 % len(keyMatrix)]
        return left + right
    if left_char_position.y == right_char_position.y:
        #same column get char below
        left = keyMatrix[left_char_position.x + 1 % len(keyMatrix)][left_char_position.y]
        right = keyMatrix[right_char_position.x + 1 % len(keyMatrix)][right_char_position.y]
        return left + right
    left = keyMatrix[left_char_position.x][right_char_position.y]
    right = keyMatrix[right_char_position.x][left_char_position.y]
    return left + right

def encrypt(plaintext, keyMatrix):
    plaintext = plaintext.replace(' ', '').strip()
    cyphertext = ""
    i = 0
    while i < len(plaintext) - 1:
        char_left, char_right, left, right = _find_next_pair(plaintext, i)
        cypherpair = _encrypt_pair(char_left + char_right, keyMatrix)
        removed = removed_letter * (right - left - 1)
        cyphertext += cypherpair[0] + removed + cypherpair[1]
        i = right + 1
    return cyphertext

def decrypt(cyphertext, keyMatrix):
    pass
