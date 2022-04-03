"""
Welcome to Cipherer 3.3!
Upgrades:
1.Better CMD-like UI
2.Supporting
3.Better algorithm
Algorithm:v1.6
"""
from random import *
from time import sleep

###Algorithim part

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
#start
def cut(msg):
    output = msg.split(',')
    return output

if __name__ == '__main__':
    enc = ['encrypt','ENC']
    dec = ['decrypt','DEC']
    quit = ['quit','EXI']
    help = ['help','SUP']
    print('cipher version 3.3')
    print('type command \'SUP\' to see the supports.')
    while True:
        msg = input('command>>')
        if msg in enc:
            key = float
            try:
                string = input('encrypt>>>')
                msgkey = cut(string)
                msg, key = msgkey[0], int(msgkey[1])
                print('encrypt_result>>>{0}'.format(encrypt(msg,key)))
                continue
            except:
                if type(key) != int:
                    print('[encrypt_error]>>>key option must be integer form.')
                    continue
                else:
                    print('[encrypt_error]>>>must have two option.')
        elif msg in dec:
            key = float
            try:
                string = input('decrypt>>>')
                msgkey = cut(string)
                msg, key = msgkey[0], int(msgkey[1])
                print('decrypt_result>>>{0}'.format(decrypt(msg,key)))
                continue
            except:
                if type(key) != int:
                    print('[decrypt_error]>>>key option must be integer form.')
                    continue
                else:
                    print('[decrypt_error]>>>must have two option.')
        elif msg in quit:
            print('quit>>>')
            sleep(1)
            break
        elif msg in help:
            print('[S]:'
                  'type command to encrypt or dcrypt messages.\n if you want to encrypt, please type\n'
                  '[\'encrypt\',\'ENC\']\n if you want to decrypt, please type\n'
                  '[\'decrypt\',\'DEC\']\n encrypt or decrypt command shall like this:\n'
                  'command>>>encrpt(or decrypt)\n'
                  'encrypt(or decrypt)>>>message,key(key option shall be integer form)\n'
                  'type [\'quit\',\'EXI\'] to exit.' )
        else:
            print('[error]>>>no command named \'{0}\'.'.format(msg))
            continue
