#WAP in Python Using Tkinter Interface to Write hello World
import tkinter
from tkinter import *
def show():
    print("hello world")
root= Tk()
b=Entry(root,text="hello world",widt=5)
b.pack(side=TOP)
b1=Button(root,text="exit",widt=5,command=exit)
b1.pack(side=BOTTOM)
root.mainloop()

#WAP in Python to Create a Button
import tkinter
from tkinter import *
def show():
	print("HYPEBEAST:Supreme")
root=Tk()
b=Button(root,text="click",widt=5,command=show)
b.pack(side=TOP)
b1=Button(root,text="exit",widt=5,command=exit)
b1.pack(side=BOTTOM)
root.mainloop()
#WAP To Create Frame Using Tkinter Interface
import tkinter
from tkinter import *
def display():
    var.set("blood must have blood")

def terminate():
    exit(0)

root = Tk()

var=StringVar()

root.geometry("300x300")

b1 = Button(root,text="click",width=50,bg='light blue',font='black',command=display)
b1.pack()

b2 = Button(root,text="exit",width=50,bg='light blue',font='black',command=terminate)
b2.pack()

var.set("your fight is over")
label=Label(textvariable=var)
label.pack()
root.mainloop()
#WAP To Take Input In GUI Using Tkinter Interface in Python
from tkinter import *
def display():
	print(entry.get())
root=Tk()
entry=Entry(root,width=50,bg="blue")
entry.pack()
b=Button(root,text="display",bg="red",font="blue",command=display)
b.pack()
b1=Button(root,text="exit",bg="red",font="blue",command=exit)
b1.pack()
root.mainloop()
