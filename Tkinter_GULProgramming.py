import tkinter

from tkinter import Tk
from tkinter import ttk
#from tkinter import Tcl
from tkinter import *

root = Tk()
frame = Frame(root)
labelText = StringVar()

label = Label(frame,textvariable = labelText)
button = Button(frame,text ='Hey i am button')

labelText.set('Hey,Wassup')

label.pack()
button.pack()
frame.pack()

root.mainloop()
