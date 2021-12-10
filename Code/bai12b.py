
from tkinter import *
import tkinter as tk
import pathlib
import os
def path():
    src = entry_path.get()

    obj_list=os.listdir(src)
    lb_kb.delete(0,END)
    for i in range(0, len(obj_list),1):
        lb_kb.insert(i, obj_list[i])
#fuction
window = Tk()
window.title("Bai12.b")
window.geometry('600x400')
lb1 = Label(window, text='Path:')
lb1.place(anchor='nw', x='50', y='10')

entry_path = Entry(window)
entry_path.place(anchor='nw', x='150', y='10')

btn = Button(window, text="Read", command= path)
btn.place(anchor='nw', x='300', y='10')

lb_kb = Listbox(window,background='#ffffff')
lb_kb.place(anchor='nw', x='50', y='70',height='200', width='500' )
window.mainloop()