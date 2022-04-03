"""
Welcome to Cipherer 3.2!
Upgrades:
1.Better CMD-like UI
Algorithm:v1.5
"""
from random import *
from time import sleep

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
#start
def cut(msg):
    output = msg.split(',')
    return output
if __name__ == '__main__':
    print('Welcome to Cipher3.2!')
    sleep(0.2)
    while True:
        msg = input('Please type\'encrypt\', \'decrypt\', or \'bye\'.')
        sleep(0.2)
        msg = msg.lower()
        if msg == 'encrypt':
            string = input('What is the message?(use a \',\' to in middle \
of message and key.)')
            msgkey = cut(string)
            msg, key = msgkey[0], int(msgkey[1])
            sleep(0.2)
            print('The string is {0}.'.format(encrypt(msg,key)))
            continue
        elif msg == 'decrypt':
            string = input('What is the string?(use a \',\' to in middle \
of string and key.)')
            msgkey = cut(string)
            msg, key = msgkey[0], int(msgkey[1])
            sleep(0.2)
            print('The message is {0}.'.format(decrypt(msg,key)))
            continue
        elif msg == 'bye':
            print('Bye')
            sleep(0.2)
            break
        else:
            sleep(0.2)
            print('error')
            continue
