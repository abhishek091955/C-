# python gui
from tkinter import *

root = Tk()

root.title("Welcome to Technology Hacks")
root.geometry('350x200')
lbl = Label(root, text = "Abishek Kumar.")
lbl.grid()

def clicked():
    btn['state'] = 'disabled'
    btn['text'] = 'subscribed'
    btn['bg'] = 'white'
    lbl2 = Label(root, text="   Thank you!!!")
    lbl2.grid()

btn = Button(root, text="Subscribe",
             fg="white", bg="red",
             command=clicked)

btn.grid(column=1, row=0) 

root.mainloop()
