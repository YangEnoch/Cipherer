"""
Welcome to Cipherer 3.4!
Upgrades:
1.Better CMD-like UI
Algorithm:v1.6
"""
from random import *
from time import sleep


# Algorithim part
def is_even(num):
    return num % 2 == 0


def get_even_letters(msg):
    even = []
    for c in range(0, len(msg)):
        if is_even(c):
            even.append(msg[c])
    return even


def get_odd_letters(msg):
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
        new = chr(randint(0, key))
        fake.append(new)
    for b in range(0, len(msg)):
        enced.append(msg[b])
        enced.append(choice(fake))
    enced = tuple(enced)
    newMsg = ''.join(enced)
    return newMsg


def decF(msg):
    even = get_even_letters(msg)
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
    help = ['help', 'SUP']
    info = ['information', 'INF']
    print('cipher version 3.4')
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
            print('\'decrypt\' command shall come with msg and key.')
            continue
        if msg in enc:
            print('\'encrypt\' command shall come with msg and key.')
            continue
        elif msg in quit:
            print('exit>>>')
            sleep(1)
            break
        elif msg in help:
            print('[S]:'
                  'type command to encrypt or dcrypt messages.\n if you want to encrypt, please type\n'
                  '[\'encrypt\',\'ENC\']\n if you want to decrypt, please type\n'
                  '[\'decrypt\',\'DEC\']\n encrypt or decrypt command shall like this:\n'
                  'command>>>ENC(or DEC) message,key(key option shall be integer form)\n'
                  'type [\'exit\',\'EXI\'] to exit.')
            continue
        elif msg in info:
            print('Welcome to Cipherer 3.4!\n'
                  'This item was created by Enoch Yang.\n'
                  'Thank for using this program, if you have any questions, please sent email to\n'
                  'yangyile330@gmail.com.')
        else:
            print('[error]: no command named \'{0}\'.'.format(msg))
            continue
