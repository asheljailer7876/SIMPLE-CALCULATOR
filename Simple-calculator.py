from tkinter import *
asd =Tk()
asd.geometry("224x200")
e = Entry(asd,width = 35,borderwidth = 5)
e.place(x=0,y=0)
def btclick(num):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))
b=Button(asd,text = "1",width = 6,command = lambda: btclick(1))
b.place(x=0,y=30)
b=Button(asd,text = "2",width = 6,command = lambda: btclick(2))
b.place(x=60,y=30)
b=Button(asd,text = "3",width = 6,command = lambda: btclick(3))
b.place(x=120,y=30)
b=Button(asd,text = "4",width = 4,command = lambda: btclick(4))
b.place(x=180,y=30)
def add():
    firstno = e.get()
    e.delete(0,END)
    global math
    math ="addition"
    global f
    f = int(firstno)
b=Button(asd,text = "+",width = 6,command=add)
b.place(x=0,y=60)
def sub():
    firstno =e.get()
    e.delete(0,END)
    global math
    math = "substraction"
    global f
    f =int(firstno)
b=Button(asd,text = "-",width = 6,command = sub)
b.place(x=60,y=60)
def eql():
    secondno = e.get()
    e.delete(0,END)
    if math =="addition":
        e.insert(0,f+int(secondno))
    elif math =="substraction":
        e.insert(0,f-int(secondno))
b=Button(asd,text = "=",width = 6,command = eql)
b.place(x=120,y=60)
def clr():
    e.delete(0,END)
b=Button(asd,text = "clear",width = 6,command = clr)
b.place(x=180,y=60)
