import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *

# root window
root = tk.Tk()
root.title("Bài 3")
root.geometry('300x500')
root.resizable(False, False)
root.title('Bai 3')
def create_circle(x, y, r, canvasName): #center coordinates, radius
    canvasName.delete("all")
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill=cl)
def var():
    global cl
    var1.get()
    var2.get()
    var3.get()
    if var1.get() == 1 :
        if var2.get()==1:
            if var3.get()==0:
                cl ="yellow"
            else:
                cl = "white"
        else:
            if var3.get()==0:
                cl = "red"
            else:
                cl = "purple"
    else:
        if var2.get()==1:
            if var3.get()==1:
                cl = "green"
            else:
                cl = "green"
        else:
            if var3.get()==1:
                cl = "blue"
            else:
                cl = "white"
    return cl
def show_selected_size():
    global cl
    var()
    shape = selected_shape.get()
    if shape=="t":
        canvas.delete("all")
        canvas.create_oval(25,25,225,225,fill=cl)
    if shape=="e":
        canvas.delete("all")
        canvas.create_oval(30, 50, 270, 210,fill=cl)
    if shape=="c":
        canvas.delete("all")
        canvas.create_rectangle(30, 50, 270, 210,fill=cl)


selected_shape = tk.StringVar()
shapes = (('elip', 'e'),
         ('tron', 't'),
         ('chu nhat', 'c'))


# radio buttons
for shape in shapes:
    r = ttk.Radiobutton(
        root,
        text=shape[0],
        value=shape[1],
        variable=selected_shape
    )
    r.pack(fill='x', padx=5, pady=5)

var1 = IntVar()
c1 = Checkbutton(root, text="red", variable=var1, onvalue=1, offvalue=0)
var2 = IntVar()
c2 = Checkbutton(root, text="green", variable=var2, onvalue=1, offvalue=0)
var3 = IntVar()
c3 = Checkbutton(root, text="blue", variable=var3, onvalue=1, offvalue=0)
c1.pack(fill='x', padx=5, pady=5)
c2.pack(fill='x', padx=5, pady=5)
c3.pack(fill='x', padx=5, pady=5)

# button
button = ttk.Button(
    root,
    text="Plot",
    command=show_selected_size)

button.pack(fill='x', padx=5, pady=5)
canvas = Canvas(root,width=300,height=400)
canvas.pack(fill='x', padx=5, pady=5)
root.mainloop()