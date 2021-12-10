import tkinter as tk
from tkinter import *
from tkinter import messagebox
from threading import Thread

w1 = Tk()
w1.title("Bài 10")

a_label = Label(w1,text="Ban Kinh",foreground="black",width="12", height="2",font=("Timer", 16))
a_label.grid(row=0,column = 0)
a_entry = Entry(w1,width="20")
a_entry.grid(row = 0,column = 1,sticky = W)
def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)

def giai():
    global w2, thread
    bk = int(a_entry.get())
    w2 = Tk()
    w2.title("Vẽ Hình")
    canvas = Canvas(w2, width=4*bk, height=4*bk)
    canvas.grid(row=0)
    thread = Thread(target = w2.mainloop)
    create_circle(2*bk,2*bk,bk,canvas)
    thread.start()

giai_BT = Button(w1, font=("Verdana",10,'bold'), text="Vẽ", width="6", height=2,
                    bd=3, bg="gray", activebackground="#3c9d9b",fg='#ffffff',
                    command= giai )
giai_BT.grid(row = 1, column = 1,sticky=E)


w1.mainloop()
