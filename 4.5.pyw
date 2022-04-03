"""
Welcome to Cipherer 4.5!
1.Testing sign up
Algorithm:v1.5
"""

from random import *
from time import sleep
from tkinter import *
from tkinter.ttk import Progressbar
import time

class basic:
    def _get(path):
        with open(path) as file:
            for line in file:
                line = line.rstrip('\n')
                account, password = line.split(',')
                dict_account[account] = password

    def _add(account, password, path):
        with open(path, 'a') as file:
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

def copy():
    text.event_generate('<<Copy>>')

def show(event):
    popmenu.post(event.x_root,event.y_root)

def msgbox(title, msg):
    box = Tk()
    global text
    text = Text(box)
    text.pack(fill=BOTH, expand=True, pady=3, padx=2)
    text.insert(END, msg)
    box.title(title)
    box.geometry('160x90+400+225')
    global popmenu
    popmenu = Menu(box, tearoff=False)
    popmenu.add_command(label='Copy', command=copy)
    box.bind('<Button-3>', show)

def _enc():
    output = encrypt(message.get(), int(key.get()))
    msgbox('Output', 'Your result are: '+output)

def _dec():
    output = decrypt(message.get(), int(key.get()))
    msgbox('Output', 'Your result are: '+output)
    
def enc():
    box = Tk()
    box.title('Encrypt')
    box.geometry('160x80+400+225')
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
    box.geometry('160x80+400+225')
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
    msgbox('Help', 'Welcome to Cipherer 4.5!\n\
This item was created by Enoch Yang.\n\
Thank for using this program, if you had any questions, please send email to 313727712@qq.com.')
    
def start():
    progress = Tk()
    progress.geometry('400x180+400+225')
    pb = Progressbar(progress, length=200, mode='determinate', orient=HORIZONTAL)
    pb.pack(padx=10, pady=10)
    pb['maximum'] = 100
    pb['value'] = 0
    textlabel = Label(progress, text='Loading...')
    textlabel.pack()
    for counter in range(100):
        pb['value'] = counter + 1
        progress.update()
        time.sleep(0.005)
    time.sleep(0.25)
    time.sleep(0.25)
    progress.destroy()
    root = Tk()
    root.geometry('480x270+400+225')
    root.title('Cipherer')
    menubar = Menu(root)
    menubar.add_command(label='Help', command=_help)
    menubar.add_command(label='Encrypt', command=enc)
    menubar.add_command(label='Decrypt', command=dec)
    menubar.add_command(label='Quit', command=root.destroy)
    root.config(menu=menubar)
    canvas = Canvas(root, width=480, height=270)
    canvas.pack()
    for counter in range(40):
        x1, y1 = randint(1, 480), randint(1, 270)
        x2, y2 = randint(1, 480), randint(1, 270)
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        canvas.create_rectangle(x1, y1, x2, y2, outline='DarkGray')
    canvas.create_text(223, 93, text='Cipherer', fill='LightGray',
                       font=('Times New Roman Baltic', 50))
    canvas.create_text(220, 90, text='Cipherer', fill='Blue',
                       font=('Times New Roman Baltic', 50))
    canvas.create_text(233, 153, text='4.5', fill='LightGray',
                       font=('Times New Roman Baltic', 30))
    canvas.create_text(230, 150, text='4.5', fill='Blue',
                       font=('Times New Roman Baltic', 30))

def login():
    if account.get() == 'guest' and password.get() == '2022':
            root.destroy()


def add():
    basic._add(_account.get(), _password.get(), 'AccountData.txt')
        
def signup():
    global _account
    global _password
    box = Tk()
    box.title('Sign up')
    box.geometry('160x90+400+225')
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
dict_answers = {}
file = open('AccountData.txt', 'a')
file.close()

root = Tk()
root.title('Cipherer Login')
root.geometry('500x180+400+225')

msg = 'Welcome to Cipherer4.5!\nThis is a encrypt program,\n so you can encrypt message and decrypt other\'s \
message here.'
logo = Label(root, text=msg, compound=BOTTOM)
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
signupbutton = Button(root, text='Sign up', command=signup)
signupbutton.grid(row=3, column=2)

root.mainloop()
