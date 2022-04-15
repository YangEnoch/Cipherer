"""
Welcome to Cipherer 3.7!
Upgrades：
1.Better algorithm
2.Key exchange
Algorithm:v1.8
"""

from random import *


def is_even(num):
    return num % 2 == 0


def getEvenLetters(msg):
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


def fake_encrypt(msg, key):
    encrypted = []
    fake = []
    for a in range(len(msg)):
        _msg = ord(msg[a - 1])
        fake.append(chr(randint(_msg - key - a, _msg + key + a)))
    for b in range(0, len(msg)):
        encrypted.append(msg[b])
        encrypted.append(choice(fake))
    return ''.join(tuple(encrypted))


def fake_decrypt(msg):
    even = getEvenLetters(msg)
    return ''.join(tuple(even))


def turn_encrypt(msg, key):
    return turn(fake_encrypt(msg, key))


def turn_decrypt(msg):
    return fake_decrypt(turn(msg))


def _encrypt(msg, key):
    output = ''
    counter = 0
    while counter < len(msg):
        new = msg[counter]
        new = chr(ord(new) + key + counter)
        output = output + new
        counter = counter + 1
    return output


def _decrypt(msg, key):
    output = ''
    counter = 0
    while counter < len(msg):
        new = msg[counter]
        new = chr(ord(new) - key - counter)
        output = output + new
        counter = counter + 1
    return output


def encrypt(msg, key):
    return turn_encrypt(_encrypt(msg, key), key)


def decrypt(msg, key):
    return _decrypt(turn_decrypt(msg), key)


def mod(num, mod=11):
    try:
        return num % mod
    except:
        return TypeError


def px7(x, b=7):
    result = 1
    for i in range(0, x):
        result = result * b
    return result


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
    exchange = ['exchange', 'EXC']
    print('cipher version 3.7')
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
            elif com1 in exchange:
                try:
                    _as = com2
                    while True:
                        if _as == 'host':
                            a = int(input('exchange_a>>>'))
                            print('exchange_alpha>>>{0}'.format(str(px7(a))))
                            beta = int(input('exchange_beta>>>'))
                            print('exchange_key>>>{0}'.format(str(mod(beta ** a))))
                            break
                        elif _as == 'guest':
                            b = int(input('exchange_b>>>'))
                            print('exchange_beta>>>{0}'.format(str(px7(b))))
                            alpha = int(input('exchange_alpha>>>'))
                            print('exchange_key>>>{0}'.format(str(mod(alpha ** b))))
                            break
                        else:
                            print('[exchange_error]')
                            break
                    continue
                except:
                    print('[exchange_error]')
                    continue
        except:
            pass
        if msg in dec:
            print('\'decrypt\' command must come with msg and key.')
            continue
        elif msg in enc:
            print('\'encrypt\' command must come with msg and key.')
            continue
        elif msg in exchange:
            print('\'exchange\' command must come with int\'a\'.')
        elif msg in quit:
            print('exit>>>')
            break
        elif msg in help:
            print('========SUPPORT========\n'
                  'Use commands to encrypt or dcrypt messages.\n If you want to encrypt, please use '
                  '\'encrypt\' or \'ENC\' command.\nIf you want to decrypt, please use\n'
                  '\'decrypt\' or \'DEC\' command.\n Encrypt or decrypt command should be like this:\n'
                  'command>>>ENC(or DEC) message,key(key option shall be integer form)\n'
                  '======================='
                  'Use \'EXC\' or \'exchange\' command to exchange key.\n'
                  'Exchange command should be like this:\n'
                  'command>>>EXC identity'
                  'exchange_a(or exchange_b)>>>int'
                  'exchange_alpha(or exchange_beta>>>solution of exchange object'
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