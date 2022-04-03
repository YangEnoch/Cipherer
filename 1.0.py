"""
Welcome to Cipherer 1.0!
Upgrades:
1.Caesar Encryption
Algorithm：v1.0
"""

encrypt_dict = {
    "x" : "a",
    "y" : "b",
    "z" : "c",
    "X" : "A",
    "Y" : "B",
    "Z" : "C"
    }

decrypt_dict = {
    "a" : "x",
    "b" : "y",
    "c" : "z",
    "A" : "X",
    "B" : "Y",
    "C" : "Z"
    }

def shift_character(in_character, shift):
    return chr(ord(in_character) + shift)

def encrypt(input_string):
    encrypted = ""
    for character in input_string:
        if character.isalpha():
            if character in encrypt_dict.keys():
                encrypted = encrypted + encrypt_dict[character]
            else:
                encrypted = encrypted + shift_character(character, 3)
        else:
            encrypted = encrypted + character
    return encrypted

def decrypt(input_string):
    decrypted = ""
    for character in input_string:
        if character.isalpha():
            if character in decrypt_dict.keys():
                decrypted = decrypted + decrypt_dict[character]
            else:
                decrypted = decrypted + shift_character(character, -3)
        else:
            decrypted = decrypted + character
    return decrypted