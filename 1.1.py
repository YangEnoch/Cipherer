"""
Welcome to Cipherer 1.1!
Upgrades:
1.Key
Algorithm:v1.1
"""
#This item was created by Enoch.

import random

class basic:
    def shift_character(in_character, shift):
        char_ascii = ord(in_character)
        new_char_ascii = char_ascii + shift

        if in_character.islower():
            if new_char_ascii > ord('z'):
                new_char_ascii = new_char_ascii - 26
            elif new_char_ascii < ord('a'):
                new_char_ascii = new_char_ascii + 26
        else:
            if new_char_ascii > ord('Z'):
                new_char_ascii = new_char_ascii - 26
            elif new_char_ascii < ord('A'):
                new_char_ascii = new_char_ascii + 26

        return chr(new_char_ascii)

    def encrypt_caesar(input_string, shift):
        encrypted = ""
        for character in input_string:
            if character.isalpha():
                encrypted = encrypted + basic.shift_character(character, shift)
            else:
                encrypted = encrypted + character
        return encrypted

    def decrypt_caesar(input_string, shift):
        decrypted = ""
        for character in input_string:
            if character.isalpha():
                decrypted = decrypted + basic.shift_character(character, -shift)
            else:
                decrypted = decrypted + character
        return decrypted

def makeCipher(mistring, key=None):
    if key == None:
        key = random.randint(1,26)
        for shift in range(key):
            encrypted = basic.encrypt_caesar(mistring,shift)
        return encrypted, key
    else:
        for shift in range(key):
            encrypted = basic.encrypt_caesar(mistring,shift)
        return encrypted

def readCipher(mistring, key):
    for shift in range(key):
        decrypted = basic.decrypt_caesar(mistring, shift)
    return decrypted