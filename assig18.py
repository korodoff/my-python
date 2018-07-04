# d={"vass":1234242,"prophrt":8878555,"serv":3423423423,"jason":34636363,"thoi":42352525235}
# from tkinter import *
# root=Tk()
# t=Text(root,height=1,width=10)
# t.pack(side=TOP)
# t.insert(END,'Dictionary')
# s=Scrollbar(root)
# s.pack(side=RIGHT,fill=Y)
# listbox=Listbox(root,yscrollcommand=s.set)
# for key in d:
 # for i in range (10):
  # listbox.insert(END,'{}:{}'.format(key,d[key]) )
# listbox.pack(side=LEFT,fill=BOTH)
# s.config(command=listbox.yview)
# root.mainloop()

#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.

import tkinter

from tkinter import *


def show():
    search_name = l.get(ACTIVE)

def insert():
    d[str(entry1.get())] =int(entry2.get())
    l.insert(END,entry1.get())
    print(d)


root = Tk()
root.config(bg='light yellow')
var=StringVar()

d={"vass":1234242,"prophrt":8878555,"serv":3423423423,"jason":34636363,"thoi":42352525235}
name_list=list(d.keys())

root.resize=(True,True)
root.geometry('500x500')


entry1=Entry(root,width=20)
entry1.pack()
entry2=Entry(root,width=20)
entry2.pack()
b=Button(root,text='click',width='10',bg='light green',fg='black',command=insert).pack()

f=Frame()
f.pack(side=LEFT)
label=Label(f,text="MyMenu",font=20,fg='black')
label.pack()

s=Scrollbar(f)
s.pack(side=RIGHT,fill=Y)
l=Listbox(f,yscrollcommand=s.set)
for name in name_list:
    l.insert(END,name)

l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview)
root.mainloop()