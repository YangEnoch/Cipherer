"""
Welcome to Cipherer 4.0!
Upgrades:
1.Testing GUI
Algorithm: NONE
"""

from tkinter import *
from tkinter import simpledialog
from cipherer import *

def enc(msg):
    output = encrypt(msg,int(key))
    messagebox.showinfow(output)
def dec():
    output = decrypt(msg,int(key))
    messagebox.showinfow(output)
def inputbox(msg,command):
    box =Tk()
    global keyinp
    global msginp
    msgL = Label(box,text='Message')
    msgL.grid(row=1)
    keyL = Label(box,text='Key')
    keyL.grid(row=2)
    msgE = Entry(box)
    keyE = Entry(box)
    msgE.grid(row=1,column=1,pady=10)
    keyE.grid(row=2,column=1,pady=10)
    quitbtn = Button(box, text='Quit',command=box.destroy)
    if command == 'encrypt':
        loginbtn = Button(box,text=msg,compound=enc)
    elif command == 'decrypt':
        loginbtn = Button(box,text=msg,compound=dec)
    loginbtn.grid(row=3,column=0)
    quitbtn.grid(row=3,column=1)
    key = keyE.get()
    msg = msgE.get()
    return (key, msg)
def e():
    inputbox('Encrypt','encrypt')
def d():
    inputbox('Decrypt','decrypt')
    
#Start
root = Tk()
root.title('Cipherer4.0')
root.geometry('300x200')
mbar = Menu(root)
enc = mbar.add_command(label='Encrypt',command=e)
dec = mbar.add_command(label='Decrypt',command=d)
mbar.add_command(label='Quit',command=root.destroy)
root.config(menu=mbar)
root.mainloop()