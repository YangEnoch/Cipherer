"""
Welcome to Cipherer 2.0.
Upgrades:
1.Shorter but better than 1.0.
Algorithm:v1.2
"""
from random import choice
from random import randint

def encrypt(msg):
    output = ''
    counter = 0
    while counter < len(msg):
        new = msg[counter]
        new = chr(ord(new) + 3)
        output = output + new
        counter = counter + 1
    return output

def decrypt(msg):
    output = ''
    counter = 0
    while counter < len(msg):
        new = msg[counter]
        new = chr(ord(new) - 3)
        output = output + new
        counter = counter + 1
    return output
