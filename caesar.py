import string
def alphabet_position(letter):
    alphabet_u = list(string.ascii_uppercase)
    alphabet_l = list(string.ascii_lowercase)
    if letter in alphabet_u:
        return (alphabet_u.index(letter))
    if letter in alphabet_l:
        return (alphabet_l.index(letter))
    if letter != letter.isalpha():
        return letter
def rotate_character(char, rot):
    alphabet_u = list(string.ascii_uppercase)
    alphabet_l = list(string.ascii_lowercase)
    for i in char:
        if i.isalpha():
            if i in alphabet_u:
                return alphabet_u[(alphabet_position(i)+ rot) % 26]
            if i in alphabet_l:
                return alphabet_l[(alphabet_position(i)+ rot) % 26]
        else:
            return i
def encrypt(text, rot):
    strg = ''
    for i in text:
        strg += rotate_character(i,rot)
    return strg
