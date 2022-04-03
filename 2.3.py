"""
Welcome to Cipherer 2.3.
Upgrades:
1.Better Algorithm
Algorithm:v1.5
"""
from random import choice
from random import randint

class basic:
    def is_even(num):
        return num % 2 == 0
    def getEvenLetters(msg):
        even= []
        for c in range(0, len(msg)):
            if basic.is_even(c):
                even.append(msg[c])
        return even
    def getOddLetters(msg):
        odd = []
        for c in range(0, len(msg)):
            if not basic.is_even(c):
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
        even = basic.getEvenLetters(msg)
        even = tuple(even)
        newMsg = ''.join(even)
        return newMsg
    class main:
        def enc(msg, key):
            enced = basic.encF(msg, key)
            enced = basic.turn(enced)
            return enced
        def dec(msg):
            deced = basic.turn(msg)
            deced = basic.decF(deced)
            return deced
    def encrypt(msg, key):
        output = ''
        counter = 0
        while counter < len(msg):
            new = msg[counter]
            new = chr(ord(new)+key)
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

def encrypt(msg, key):
    output = basic.encrypt(msg, key)
    output = basic.main.enc(output, key)
    return output

def decrypt(msg, key):
    output = basic.main.dec(msg)
    output = basic.decrypt(output, key)
    return output