from tkinter import *
a = Tk()
a.geometry("600x400")
form = Label(a,text = "python  Registeration Form",bg = "red",font  =("time 15 bold")).place(x =180,y =15)
name = Label(a,text = "NAME",font =("vendana",12)).place(x=10,y = 60)
e1 = Entry(width =16).place(x = 120,y =60)
pas = Label(a,text = "PASSWORD",font =("vendana",12)).place(x=10,y = 110)
e1 = Entry(width =16).place(x = 120,y =110)
Eid = Label(a,text = "Email id",font =("vendana",12)).place(x=10,y = 160)
e1 = Entry(width =32).place(x = 120,y =160)
Eid = Label(a,text = "Contact no",font =("vendana",12)).place(x=10,y = 210)
e1 = Entry(width =16).place(x = 120,y =210)
gen = Label(a,text = "Gender",font =("vendana",12)).place(x=10,y = 260)
gender = IntVar()
mal = Radiobutton(a,text = "male",variable =gender,value =1).place(x =100,y =260)
mal = Radiobutton(a,text = "female",variable =gender,value =2).place(x =160,y =260)
mal = Radiobutton(a,text = "other",variable =gender,value =3).place(x =220,y =260)
but = Button(a,text ="SUBMITT",bg ="red").place(x=160,y =320)



