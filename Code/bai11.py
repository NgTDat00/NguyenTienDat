import tkinter as tk
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)

def ok():
    global bk, Window,a
    bk = int(a.get())
    create_circle(bk,bk,bk,canvas)
    Window.destroy()

def New_Window():
    global bk, Window,a
    Window = tk.Toplevel()
    a = Entry(Window,width="20")
    a.grid(row=0,column=0)
    b = Button(Window, font=("Verdana",10,'bold'), text="OK", width="6", height=2,
                    bd=3, bg="gray", activebackground="#3c9d9b",fg='#ffffff',
                    command= ok)
    b.grid(row=1,column=1)
HEIGHT = 600
WIDTH = 600

ws = tk.Tk()
ws.title("Bài 11")
canvas = tk.Canvas(ws, height=HEIGHT, width=WIDTH)
canvas.pack()

button = tk.Button(ws, text="Nhập bán kính", bg='White', fg='Black',
                              command=lambda: New_Window())

button.pack()
ws.mainloop()