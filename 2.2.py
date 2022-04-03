"""
Welcome to Cipherer 2.2.
Upgrades:
1.Fake Letters
Algorithm:v1.4
"""
from random import choice
from random import randint

def is_even(num):
    return num % 2 == 0
def getEvenLetters(msg):
    even= []
    for c in range(0, len(msg)):
        if is_even(c):
            even.append(msg[c])
    return even
def getOddLetters(msg):
    odd = []
    for c in range(0, len(msg)):
        if not is_even(c):
            odd.append(msg[c])
    return odd
def turn(msg):
    return msg[::-1]
def encF(msg, key):
    enced = []
    fake = []
    for a in range(key):
        new = chr(randint(1,key))
        fake.append(new)
    for b in range(0, len(msg)):
        enced.append(msg[b])
        enced.append(choice(fake))
    enced = tuple(enced)
    newMsg = ''.join(enced)
    return newMsg
def decF(msg):
    even = getEvenLetters(msg)
    even = tuple(even)
    newMsg = ''.join(even)
    return newMsg
def enc(msg, key):
    enced = encF(msg, key)
    enced = turn(enced)
    return enced
def dec(msg):
    deced = turn(msg)
    deced = decF(deced)
    return deced
