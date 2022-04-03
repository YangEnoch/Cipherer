"""
Welcome to Cipherer 3.6!
Upgrades：
1.Better algorithm
Algorithm:v1.7
"""

from random import *

def is_even(num):
    return num % 2 == 0


def geteveneetters(msg):
    even = []
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
    for a in range(len(msg)):
        _msg = ord(msg[a - 1])
        new = chr(randint(_msg - key, _msg + key))
        fake.append(new)
    for b in range(0, len(msg)):
        enced.append(msg[b])
        enced.append(choice(fake))
    enced = tuple(enced)
    newMsg = ''.join(enced)
    return newMsg


def decF(msg):
    even = geteveneetters(msg)
    even = tuple(even)
    newMsg = ''.join(even)
    return newMsg


def __enc(msg, key):
    enced = encF(msg, key)
    enced = turn(enced)
    return enced


def __dec(msg):
    deced = turn(msg)
    deced = decF(deced)
    return deced


def _encrypt(msg, key):
    output = ''
    counter = 0
    while counter < len(msg):
        new = msg[counter]
        new = chr(ord(new) + key)
        output = output + new
        counter = counter + 1
    return output


def _decrypt(msg, key):
    output = ''
    counter = 0
    while counter < len(msg):
        new = msg[counter]
        new = chr(ord(new) - key)
        output = output + new
        counter = counter + 1
    return output


def encrypt(msg, key):
    output = _encrypt(msg, key)
    output = __enc(output, key)
    return output


def decrypt(msg, key):
    output = __dec(msg)
    output = _decrypt(output, key)
    return output


# start
def cut(msg, cut):
    output = msg.split(cut)
    return output


if __name__ == '__main__':
    enc = ['encrypt', 'ENC']
    dec = ['decrypt', 'DEC']
    quit = ['exit', 'EXI']
    help = ['support', 'SUP']
    info = ['information', 'INF']
    print('cipher version 3.5')
    print('type command \'SUP\' to see the supports.')
    while True:
        msg = input('command>>')
        try:
            com = cut(msg, ' ')
            com1, com2 = com[0], com[1]
            if com1 in enc:
                try:
                    msgkey = cut(com2, ',')
                    msg, key = msgkey[0], int(msgkey[1])
                    print('encrypt_result>>>{0}'.format(encrypt(msg, key)))
                    continue
                except:
                    print('[encrypt_error]')
                    continue
            elif com1 in dec:
                try:
                    msgkey = cut(com2, ',')
                    msg, key = msgkey[0], int(msgkey[1])
                    print('decrypt_result>>>{0}'.format(decrypt(msg, key)))
                    continue
                except:
                    print('[decrypt_error]')
                    continue
        except:
            pass
        if msg in dec:
            print('\'decrypt\' command must come with msg and key.')
            continue
        if msg in enc:
            print('\'encrypt\' command must come with msg and key.')
            continue
        elif msg in quit:
            print('exit>>>')
            break
        elif msg in help:
            print('========SUPPORT========\n'
                  'Use commands to encrypt or dcrypt messages.\n If you want to encrypt, please use '
                  '\'encrypt\' or \'ENC\' command.\nIf you want to decrypt, please use\n'
                  '\'decrypt\' or \'DEC\' command.\n Encrypt or decrypt command should be like this:\n'
                  'command>>>ENC(or DEC) message,key(key option shall be integer form)\n'
                  '=======================\n'
                  'Use \'exit\' or \'EXI\' to exit.\n'
                  '=======================\n'
                  'Use \'information\' or \'INF\' '
                  'to see the informations about this program.')
            continue
        elif msg in info:
            print('Welcome to Cipherer 3.5!\n'
                  'This program was programed by Enoch Yang.\n'
                  'Thank for using this program, if you have any questions, please sent email to\n'
                  'yangyile330@gmail.com.')
        else:
            print('[error]: no command named \'{0}\'.'.format(msg))
            continue
