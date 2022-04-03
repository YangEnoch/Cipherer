"""
Welcome to Cipherer 4.6!
1.Better GUI
2.Complete sign up
3.Better home Background
4.Size change
5.Better algorithm
Algorithm:v1.6
"""

from random import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar, Button, Entry
import time
import pickle


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
    for a in range(key):
        new = chr(randint(1, key))
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


def copy():
    text.event_generate('<<Copy>>')


def show(event):
    popmenu.post(event.x_root, event.y_root)


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
    msgbox('Output', 'Your result are: ' + output)


def _dec():
    output = decrypt(message.get(), int(key.get()))
    msgbox('Output', 'Your result are: ' + output)


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


def login():
    _account = account.get()
    _password = password.get()
    if _account in info:
        if _password == info[_account]:
            start()
        else:
            messagebox.showerror(message='Error, your password is wrong, try again.')
    else:
        _signup = messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
        if _signup:
            signup()


def signup():
    def signto():
        np = passwordStr.get()
        npf = confirmStr.get()
        nn = accountStr.get()
        with open('info.pickle', 'rb') as file:
            info = pickle.load(file)
        if np != npf:
            messagebox.showerror('Error', 'Password and confirm password must be the same.')
        elif nn in info:
            messagebox.showerror('Error', 'The user has already signed up.')
        else:
            info[nn] = np
            with open('info.pickle', 'wb') as file:
                pickle.dump(info, file)
            messagebox.showinfo('Welcome', 'You have successfully signed up.')
            info = pickle.load(file)
            box.destroy()
    box = Toplevel()
    box.geometry('300x200')
    box.title('Sign up window')
    accountStr = StringVar()
    accountStr.set('guest')
    Label(box, text='User name: ').place(x=10, y=10)
    accountEnt = Entry(box, textvariable=accountStr)
    accountEnt.place(x=130, y=10)
    passwordStr = StringVar()
    Label(box, text='Password: ').place(x=10, y=50)
    passwordEnt = Entry(box, textvariable=passwordStr, show='*')
    passwordEnt.place(x=130, y=50)
    confirmStr = StringVar()
    Label(box, text='Confirm password: ').place(x=10, y=90)
    confirmEnt = Entry(box, textvariable=confirmStr, show='*')
    confirmEnt.place(x=130, y=90)
    signupbutton = Button(box, text='Sign up', command=signto)
    signupbutton.place(x=180, y=120)

def _help():
    msgbox('Help', 'Welcome to Cipherer 4.6!\n\
This item was created by Enoch Yang.\n\
Thank for using this program, if you had any questions, please send email to 313727712@qq.com.')


def start():
    progress = Tk()
    progress.geometry('600x180+400+225')
    progress.maxsize(600, 200)
    progress.minsize(600, 200)
    pb = Progressbar(progress, length=200, mode='determinate', orient=HORIZONTAL)
    pb.pack()
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
    root.geometry('600x200+400+225')
    root.maxsize(600, 200)
    root.minsize(600, 200)
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
                       font=('Segoe Print', 50))
    canvas.create_text(220, 90, text='Cipherer', fill='Blue',
                       font=('Segoe Print', 50))
    canvas.create_text(233, 153, text='4.6', fill='LightGray',
                       font=('Segoe Print', 30))
    canvas.create_text(230, 150, text='4.6', fill='Blue',
                       font=('Segoe Print', 30))

# start
try:
    with open('info.pickle', 'rb') as file:
        info = pickle.load(file)
except FileNotFoundError:
    with open('info.pickle', 'wb') as file:
        info = {'admin': 'admin'}
        pickle.dump(info, file)
        file.close()

root = Tk()
root.title('Cipherer Login')
root.geometry('500x180+400+225')
root.maxsize(500, 180)
root.minsize(500, 180)

msg = 'Welcome to Cipherer4.6!\nThis is a encrypt program,\n so you can encrypt message and decrypt other\'s \
message here.'
logo = Label(root, text=msg, compound=BOTTOM)

accountlabel = Label(root, text='Account')
accountlabel.grid(row=1)
passwordlabel = Label(root, text='Password')
passwordlabel.grid(row=2)
logo.grid(row=0, column=0, columnspan=2)

account = Entry(root)
password = Entry(root, show='*')
account.grid(row=1, column=1)
password.grid(row=2, column=1)

loginbutton = Button(root, text='Login', command=login)
loginbutton.grid(row=3, column=0)
quitbutton = Button(root, text='Quit', command=root.destroy)
quitbutton.grid(row=3, column=1)
signupbutton = Button(root, text='Sign up', command=signup)
signupbutton.grid(row=3, column=2)

root.mainloop()
