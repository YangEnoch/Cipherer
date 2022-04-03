"""
Welcome to Cipherer 2.1.
Upgrades:
1.Shorter but better than 1.1.
Algorithm：v1.3
"""
from random import choice
from random import randint

def encrypt(msg, key):
    output = ''
    counter = 0
    while counter < len(msg):
        new = msg[counter]
        new = chr(ord(new) + key)
        output = output + new
        counter = counter + 1
    return output

def decrypt(msg, key):
    output = ''
    counter = 0
    while counter < len(msg):
        new = msg[counter]
        new = chr(ord(new) - key)
        output = output + new
        counter = counter + 1
    return output
