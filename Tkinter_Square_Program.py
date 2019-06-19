import tkinter

from tkinter import Tk
from tkinter import ttk
from tkinter import *


def square(event):
    a = int(num1.get())
    b = a * a
    result.delete(0,"end")
    result.insert(0, b)


root = Tk()

Label(root,text="Find the square of number").pack()
num1 = Entry(root)
num1.pack(side=LEFT)

btn = Button(root, text="Squares to")
btn.bind("<Button-1>", square)
btn.pack(side=LEFT)

result = Entry(root)
result.pack(side=LEFT)
root.mainloop()