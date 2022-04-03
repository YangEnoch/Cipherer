"""
Welcome to Cipherer 4.1!
Upgrades:
1.No shell
2.Complete GUI
3.Login interface
Algorithm:v1.5
"""

from random import *
from time import sleep
from tkinter import *
from tkinter import messagebox

class basic:
    def add(path):
        file = open(path,'w')
        file.close
        
    def _find(path, fdb=None):
        try:
            f =open(path)
            fdb = True
            f.close()
            return fdb
        except FileNotFoundError:
            fdb = False
            return fdb in globals()
        
    def _get(path):
        with open(path) as file:
            for line in file:
                line = line.rstrip('\n')
                account, password = line.split(',')
                dictaccount[account] = password
            
    def _add(account, password, path):
        with open(path,'a') as file:
            file.write('\n' + account + ',' + password)

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

def msgbox(title, msg):
    messagebox.showinfo(title, msg)

def _enc():
    output = encrypt(message.get(), int(key.get()))
    msgbox('Output', 'Your message is '+output)

def _dec():
    output = decrypt(message.get(), int(key.get()))
    msgbox('Output', 'Your message is '+output)
def enc():
    box = Tk()
    box.title('Encrypt')
    messagelabel = Label(box, text='Message')
    messagelabel.grid(row=0)
    keylabel = Label(box, text='Key')
    keylabel.grid(row=1)
    global message
    message = Entry(box)
    global key
    key = Entry(box)
    message.grid(row=0, column=1)
    key.grid(row=1, column=1)
    encryptbutton = Button(box, text='Encrypt', command=_enc)
    encryptbutton.grid(row=3)
    
def dec():
    box = Tk()
    box.title('Decrypt')
    messagelabel = Label(box, text='Message')
    messagelabel.grid(row=0)
    keylabel = Label(box, text='Key')
    keylabel.grid(row=1)
    global message
    message = Entry(box)
    global key
    key = Entry(box)
    message.grid(row=0, column=1)
    key.grid(row=1, column=1)
    encryptbutton = Button(box, text='Decrypt', command=_dec)
    encryptbutton.grid(row=3)
    
def _help():
    msgbox('Help', 'Welcome to Cipherer 4.1!\n\
This item was created by Enoch Yang.\n\
Thank for using this program, if you had any questions, please send email to 313727712@qq.com.')
    
def start():
    root = Tk()
    root.geometry('320x180')
    menubar = Menu(root)
    menubar.add_command(label='Help', command=_help)
    menubar.add_command(label='Encrypt', command=enc)
    menubar.add_command(label='Decrypt', command=dec)
    menubar.add_command(label='Quit', command=root.destroy)
    root.config(menu=menubar)

def login():
    if account.get() == 'guest' and password.get() == '2022':
        root.destroy()
        start()

def add():
    basic._add(_account.get(), _password.get(), 'account_data.txt')
        
def signup():
    global _account
    global _password
    box = Tk()
    box.title('Sign up')
    accountlabel = Label(box, text='Account')
    accountlabel.grid(row=1)
    passwordlabel = Label(box, text='Password')
    passwordlabel.grid(row=2)
    _account = Entry(box)
    _password = Entry(box, show='*')
    _account.grid(row=1, column=1)
    _password.grid(row=2, column=1, pady=10)
    loginbutton = Button(box, text='Sign up', command=add)
    loginbutton.grid(row=3, column=0)
    quitbutton = Button(box, text='Quit', command=box.destroy)
    quitbutton.grid(row=3, column=1)
    
#start
root = Tk()
root.title('Cipher!')
root.geometry('400x180')
msg = 'Welcome to Cipherer!\nThe guest account is guest, password is 2022'
logo = Label(root, text=msg, compound=BOTTOM)
iffind = basic._find('account_data.txt')
if iffind == True:
    pass
else:
    basic.add('account_data.txt')
accountlabel = Label(root, text='Account')
accountlabel.grid(row=1)
passwordlabel = Label(root, text='Password')
passwordlabel.grid(row=2)
logo.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
account = Entry(root)
password = Entry(root, show='*')
account.grid(row=1, column=1)
password.grid(row=2, column=1, pady=10)
loginbutton = Button(root, text='Login', command=login)
loginbutton.grid(row=3, column=0)
quitbutton = Button(root, text='Quit', command=root.destroy)
quitbutton.grid(row=3, column=1)
root.mainloop()