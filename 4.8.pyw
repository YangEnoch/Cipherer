"""
Welcome to Cipherer 4.8!
Upgrades:
1.Language choose
2. Complete algorithm
Algorithm：v1.7
"""
from random import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar, Button, Entry
import time
import pickle


###Algorithm Part
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


def copy():
    text.event_generate('<<Copy>>')


def show(event):
    popmenu.post(event.x_root, event.y_root)


###GUI Part
# English

def msgbox(title, msg):
    box = Tk()
    global text
    text = Text(box)
    text.pack(fill=BOTH, expand=True, pady=3, padx=2)
    text.insert(END, msg)
    box.title(title)
    box.geometry('320x180+400+225')
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
    box.geometry('320x180+400+225')
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
    box.geometry('320x180+400+225')
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
            root.destroy()
        else:
            messagebox.showerror('Error', 'Your password is wrong, try again.')
    else:
        _signup = messagebox.askyesno('Welcome', 'You have not sign up yet. Sign up now?')
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
            messagebox.showinfo('Welcome', 'You have successfully signed up. \
Restart this program so you can load in this account.')
            with open('info.pickle', 'rb') as file:
                info = pickle.load(file)
            box.destroy()

    box = Toplevel()
    box.geometry('300x200')
    box.title('Sign up window')
    accountStr = StringVar()
    accountStr.set(account.get())
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


def about():
    msgbox('About', 'Cipherer was programed by Yang Yile only.\n\
This program can encrypt and decrypt messages.')


def qa():
    def btn1():
        msgbox('Answers', 'You shoud look up for the menu, and click the option\"Encrypt\",\
then type message in the entry \"message\", type key in the entry \"Key\"(Key must be a number).')

    def btn2():
        msgbox('Answers', 'You shoud look up for the menu, and click the option\"Decrypt\",\
then type message in the entry \"message\", type key in the entry \"Key\"(Key must be a number).')

    def btn3():
        msgbox('Answers', 'The option \"Key\" must be a number. If you use a number and the program still don\'t not working, \n\
please reinstall this program.')

    box = Tk()
    box.geometry('2000x100+400+225')
    box.maxsize(200, 100)
    box.minsize(200, 100)
    box.title('Q&A')
    button1 = Button(box, text='How to encrypt messages?', width=200, command=btn1)
    button2 = Button(box, text='How to decrypt messages?', width=200, command=btn2)
    button3 = Button(box, text='Why does I cannot encrypt\\decrpt?', width=200, command=btn3)
    button1.pack()
    button2.pack()
    button3.pack()


def start():
    progress = Tk()
    progress.geometry('500x180+413+275')
    progress.maxsize(480, 90)
    progress.minsize(480, 90)
    progress.title('Loading')
    pb = Progressbar(progress, length=200, mode='determinate', orient=HORIZONTAL)
    pb.pack()
    pb['maximum'] = 100
    pb['value'] = 0
    textlabel = Label(progress, text='Loading...\n\
This could use several of second.')
    textlabel.pack()
    for counter in range(100):
        pb['value'] = counter + 1
        progress.update()
        time.sleep(0.01)
    time.sleep(0.25)
    time.sleep(0.25)
    progress.destroy()
    root = Tk()
    root.geometry('480x270+400+225')
    root.maxsize(480, 270)
    root.minsize(480, 270)
    root.title('Cipherer')
    menubar = Menu(root)
    helpmenu = Menu(menubar)
    menubar.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About', command=about)
    helpmenu.add_separator()
    helpmenu.add_command(label='Q&A', command=qa)
    menubar.add_command(label='Encrypt', command=enc)
    menubar.add_command(label='Decrypt', command=dec)
    menubar.add_command(label='Exit', command=root.destroy)
    root.config(menu=menubar)
    canvas = Canvas(root, width=480, height=270)
    canvas.pack()
    canvas.create_rectangle(1, 1, 480, 270, fill='LightGray')
    for counter in range(50):
        x1, y1 = randint(1, 480), randint(1, 270)
        x2, y2 = randint(1, 480), randint(1, 270)
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        canvas.create_rectangle(x1, y1, x2, y2, outline='DarkGray')
    canvas.create_text(223, 103, text='Cipherer', fill='Gray',
                       font=('Segoe Print', 50))
    canvas.create_text(220, 100, text='Cipherer', fill='Orange',
                       font=('Segoe Print', 50))
    canvas.create_text(262, 142, text='Created by Yang Yile', fill='Gray',
                       font=('Segoe Print', 12))
    canvas.create_text(260, 140, text='Created by Yang Yile', fill='Blue',
                       font=('Segoe Print', 12))


def elan():
    cl.destroy()
    global root
    global account
    global password
    root = Tk()
    root.title('Login')
    root.geometry('500x180+400+225')
    root.maxsize(500, 180)
    root.minsize(500, 180)

    msg = 'Welcome to Cipherer! \nThis is a encryption program, \nso you can encrypt message and decrypt other\'s \
    message in here.'
    text = Label(root, text=msg, compound=BOTTOM)

    accountlabel = Label(root, text='Account')
    accountlabel.grid(row=1)
    passwordlabel = Label(root, text='Password')
    passwordlabel.grid(row=2)
    text.grid(row=0, column=0, columnspan=2, )
    account = Entry(root)
    password = Entry(root, show='*')
    account.grid(row=1, column=1, pady=1)
    password.grid(row=2, column=1, pady=1)

    loginbutton = Button(root, text='Login', command=login)
    loginbutton.grid(row=3, column=0)
    signupbutton = Button(root, text='Sign up', command=signup)
    signupbutton.grid(row=3, column=1)
    quitbutton = Button(root, text='Exit', command=root.destroy)
    quitbutton.grid(row=3, column=2)

    root.mainloop()


# Chinese Part
def msgboxc(title, msg):
    box = Tk()
    global text
    text = Text(box)
    text.pack(fill=BOTH, expand=True, pady=3, padx=2)
    text.insert(END, msg)
    box.title(title)
    box.geometry('320x180+400+225')
    global popmenu
    popmenu = Menu(box, tearoff=False)
    popmenu.add_command(label='复制', command=copy)
    box.bind('<Button-3>', show)


def _encc():
    output = encrypt(message.get(), int(key.get()))
    msgbox('结果', '您的密文为：' + output)


def _decc():
    output = decrypt(message.get(), int(key.get()))
    msgbox('结果', '您的信息为：' + output)


def encc():
    box = Tk()
    box.title('加密')
    box.geometry('320x180+400+225')
    messagelabel = Label(box, text='信息')
    messagelabel.grid(row=0)
    keylabel = Label(box, text='密钥')
    keylabel.grid(row=1)
    global message
    message = Entry(box)
    global key
    key = Entry(box)
    message.grid(row=0, column=1)
    key.grid(row=1, column=1)
    encryptbutton = Button(box, text='加密', command=_encc)
    encryptbutton.grid(row=3)


def decc():
    box = Tk()
    box.title('解密')
    box.geometry('320x180+400+225')
    messagelabel = Label(box, text='信息')
    messagelabel.grid(row=0)
    keylabel = Label(box, text='密钥')
    keylabel.grid(row=1)
    global message
    message = Entry(box)
    global key
    key = Entry(box)
    message.grid(row=0, column=1)
    key.grid(row=1, column=1)
    encryptbutton = Button(box, text='解密', command=_decc)
    encryptbutton.grid(row=3)


def loginc():
    _account = account.get()
    _password = password.get()
    if _account in info:
        if _password == info[_account]:
            startc()
            root.destroy()
        else:
            messagebox.showerror('错误', '用户名或密码错误。')
    else:
        _signup = messagebox.askyesno('欢迎', '您还没有注册，现在注册？')
        if _signup:
            signupc()


def signupc():
    def signto():
        np = passwordStr.get()
        npf = confirmStr.get()
        nn = accountStr.get()
        with open('info.pickle', 'rb') as file:
            info = pickle.load(file)
        if np != npf:
            messagebox.showerror('错误', '密码与确认密码必须相同。')
        elif nn in info:
            messagebox.showerror('错误', '用户已经注册。')
        else:
            info[nn] = np
            with open('info.pickle', 'wb') as file:
                pickle.dump(info, file)
            messagebox.showinfo('   欢迎', '您已经成功注册了，重启程序即可登录此账号。')
            with open('info.pickle', 'rb') as file:
                info = pickle.load(file)
            box.destroy()

    box = Toplevel()
    box.geometry('300x200')
    box.title('注册')
    accountStr = StringVar()
    accountStr.set(account.get())
    Label(box, text='用户名').place(x=10, y=10)
    accountEnt = Entry(box, textvariable=accountStr)
    accountEnt.place(x=130, y=10)
    passwordStr = StringVar()
    Label(box, text='密码：').place(x=10, y=50)
    passwordEnt = Entry(box, textvariable=passwordStr, show='*')
    passwordEnt.place(x=130, y=50)
    confirmStr = StringVar()
    Label(box, text='确认密码：').place(x=10, y=90)
    confirmEnt = Entry(box, textvariable=confirmStr, show='*')
    confirmEnt.place(x=130, y=90)
    signupbutton = Button(box, text='注册', command=signto)
    signupbutton.place(x=180, y=120)


def aboutc():
    msgbox('关于', 'Cipherer这个程序是由羊弈乐编写的。\n它可以用来加密或者解密信息。')


def qac():
    def btn1():
        msgbox('解答', '你应该在主菜单中点击“加密”选项，然后在“信息”一栏中输入需要加密的信息，在“密钥“一栏中输入密钥（密钥必须是纯数字）。')

    def btn2():
        msgbox('解答', '你应该在主菜单中点击“解密”选项，然后在“信息”一栏中输入需要解密的信息，在“密钥“一栏中输入密钥（密钥必须是纯数字）。')

    def btn3():
        msgbox('解答', '”密钥“一栏中必须输入小于三位的纯数字，如果还是不能使用，请重新下载这个程序。')

    box = Tk()
    box.geometry('2000x100+400+225')
    box.maxsize(200, 100)
    box.minsize(200, 100)
    box.title('Q&A')
    button1 = Button(box, text='怎样加密信息？', width=200, command=btn1)
    button2 = Button(box, text='H怎样解密信息？', width=200, command=btn2)
    button3 = Button(box, text='为什么我无法加密\\解密？', width=200, command=btn3)
    button1.pack()
    button2.pack()
    button3.pack()


def startc():
    progress = Tk()
    progress.geometry('500x180+413+275')
    progress.maxsize(480, 90)
    progress.minsize(480, 90)
    progress.title('加载中')
    pb = Progressbar(progress, length=200, mode='determinate', orient=HORIZONTAL)
    pb.pack()
    pb['maximum'] = 100
    pb['value'] = 0
    textlabel = Label(progress, text='加载中...\n\
这可能会用去几秒。')
    textlabel.pack()
    for counter in range(100):
        pb['value'] = counter + 1
        progress.update()
        time.sleep(0.01)
    time.sleep(0.25)
    time.sleep(0.25)
    progress.destroy()
    root = Tk()
    root.geometry('480x270+400+225')
    root.maxsize(480, 270)
    root.minsize(480, 270)
    root.title('Cipherer')
    menubar = Menu(root)
    helpmenu = Menu(menubar)
    menubar.add_cascade(label='帮助', menu=helpmenu)
    helpmenu.add_command(label='关于', command=aboutc)
    helpmenu.add_separator()
    helpmenu.add_command(label='Q&A', command=qac)
    menubar.add_command(label='加密', command=encc)
    menubar.add_command(label='解密', command=decc)
    menubar.add_command(label='退出', command=root.destroy)
    root.config(menu=menubar)
    canvas = Canvas(root, width=480, height=270)
    canvas.pack()
    canvas.create_rectangle(1, 1, 480, 270, fill='LightGray')
    for counter in range(50):
        x1, y1 = randint(1, 480), randint(1, 270)
        x2, y2 = randint(1, 480), randint(1, 270)
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        canvas.create_rectangle(x1, y1, x2, y2, outline='DarkGray')
    canvas.create_text(223, 103, text='Cipherer', fill='Gray',
                       font=('Segoe Print', 50))
    canvas.create_text(220, 100, text='Cipherer', fill='Orange',
                       font=('Segoe Print', 50))
    canvas.create_text(262, 142, text='Created by Yang Yile', fill='Gray',
                       font=('Segoe Print', 12))
    canvas.create_text(260, 140, text='Created by Yang Yile', fill='Blue',
                       font=('Segoe Print', 12))


def clan():
    cl.destroy()
    global root
    global account
    global password
    root = Tk()
    root.title('登录')
    root.geometry('500x180+400+225')
    root.maxsize(500, 180)
    root.minsize(500, 180)

    msg = '欢迎使用Cipherer! \n这是一个实现信息加密的程序， \n所以你可以在这里加密或解密别人发送的信息。'
    text = Label(root, text=msg, compound=BOTTOM)

    accountlabel = Label(root, text='账号：')
    accountlabel.grid(row=1)
    passwordlabel = Label(root, text='密码：')
    passwordlabel.grid(row=2)
    text.grid(row=0, column=0, columnspan=2, )
    account = Entry(root)
    password = Entry(root, show='*')
    account.grid(row=1, column=1, pady=1)
    password.grid(row=2, column=1, pady=1)

    loginbutton = Button(root, text='登录', command=loginc)
    loginbutton.grid(row=3, column=0)
    signupbutton = Button(root, text='注册', command=signupc)
    signupbutton.grid(row=3, column=1)
    quitbutton = Button(root, text='退出', command=root.destroy)
    quitbutton.grid(row=3, column=2)

    root.mainloop()


def _start():
    global info
    try:
        with open('info.pickle', 'rb') as file:
            info = pickle.load(file)
    except FileNotFoundError:
        with open('info.pickle', 'wb') as file:
            info = {'admin': 'admin'}
            pickle.dump(info, file)
            file.close()


_start()
cl = Tk()
cl.title('Welcome')
cl.geometry('400x90+500+250')
cl.maxsize(300, 90)
cl.minsize(300, 90)
text = 'Welcome to Cipherer! \nPlease choose your Language.'
textlabel = Label(cl, text=text)
textlabel.grid(row=0, column=0)
cbtn = Button(cl, text='简体中文', command=clan)
cbtn.grid(row=1, column=0)
ebtn = Button(cl, text='English', command=elan)
ebtn.grid(row=1, column=1)
cl.mainloop()
