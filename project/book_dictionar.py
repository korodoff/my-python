from  tkinter import *
import backend
def add_function():
#insert entry via buttton
    backend.insert(e1.get(),
                   e2.get(),
                   e3.get(),
                   e4.get())
    l.delete(0,END)
    l.insert(END,
             (e1.get(),
              e2.get(),
              e3.get(),
              e4.get()))
def view_function():
	l.delete(0,END)
	for row in backend.view():
		l.insert(END,row)
def update_function():
	backend.update(selected_tuple[0],
                   e1.get(),
                   e2.get(),
                   e3.get(),
                   e4.get())
def delete_function():
	backend.delete(selected_tuple[0])
def search_function():
    l.delete(0, END)
    row = None
    for row in backend.search(e1.get(),
                              e2.get(),
                              e3.get(),
                              e4.get()):
        l.insert(END,row)
def get_selected_row(event):
    global selected_tuple
    index=l.curselection()[0]
    print(index[0])
    selected_tuple=l.get(index)

    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])

    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])

    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])

    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])


root=Tk()
root.title("ruth Directory")
root.geometry("504x295+200+300")
root.resizable(True,True)
root.config(bg="light blue")

label1=Label(root,text="Title")
label1.grid(row=0,column=0)
e1=Entry(width=35)
e1.grid(row=0,column=1)

label2=Label(root,text="Author")
label2.grid(row=0,column=2)
e2=Entry(root,width=35)
e2.grid(row=0,column=3)

label3=Label(root,text="Year")
label3.grid(row=1,column=0)
e3=Entry(root,width=35)
e3.grid(row=1,column=1)

label4=Label(root,text="ISBN    ")
label4.grid(row=1,column=2)
e4=Entry(root,width=35)
e4.grid(row=1,column=3)

b1=Button(root,text="View All",width=20,height=2,command=view_function)
b1.place(x=320,y=42)
b2=Button(root,text="Search Entry",width=20,height=2,command=search_function)
b2.place(x=320,y=84)
b3=Button(root,text="Add Entry",width=20,height=2,command=add_function)
b3.place(x=320,y=126)
b4=Button(root,text="Update Selected",width=20,height=2,command=update_function)
b4.place(x=320,y=168)
b5=Button(root,text="Delete Selected",width=20,height=2,command=delete_function)
b5.place(x=320,y=210)
b6=Button(root,text="Exit",width=20,height=2,command=exit)
b6.place(x=320,y=252)

f=Frame(root)
f.place(x=0,y=84)
s=Scrollbar(f)
s.pack(side=RIGHT,fill=Y)
l=Listbox(f,yscrollcommand=s.set,width=40,height=10)
l.pack(side=LEFT,fill=BOTH)

root.mainloop()