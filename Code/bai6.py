
from tkinter import *
import tkinter as tk
from tkcalendar import Calendar, DateEntry
#fuction
list =[]
listR = []
def listbox_copy(event):
    selected = listLeft.get(ANCHOR)
    
    print(selected)
    listR.append(selected)
    listRight.delete(0,END) 
    for i in range(0,len(listR),1):
        listRight.insert(i,listR[i])
    for x in range(0,len(list),1):
        if selected == list[i]:
            list.pop(i)
    listLeft.delete(0,END)  
    for i in range(0, len(list),1):
        listLeft.insert(i,list[i])
def add():
    txt = "So luong {}".format(len(list)+1)
    label2.configure(text= txt)
    traicay = traicay_entry.get()
    if traicay == "":
        print('CHua nhap')
    else:
        traicay = traicay_entry.get()
        list.append(traicay)
    listLeft.delete(0,END)  
    for i in range(0, len(list),1):
        listLeft.insert(i,list[i])  
    traicay_entry.delete(0, END)



window = Tk()
window.title("Bai 6")
window.geometry('600x400')

lb1 = Label(window,text='Trai Cay')
lb1.place(anchor='nw', x='50', y='10')


traicay_entry = Entry(window)
traicay_entry.place(anchor='nw', x='150', y='10')

btn = Button(window, text='Add', command=add)
btn.place(anchor='nw', x='300', y='10')


listLeft = Listbox(width= 20, background= "#c0c0c0")
listLeft.place(anchor='nw', x='50', y='150')
listLeft.bind('<<ListboxSelect>>', listbox_copy)


listRight = Listbox(width= 20, background= "#c0c0c0")
listRight.place(anchor='nw', x='350', y='150')

label2 = Label(window, text="So luong")
label2.place(anchor='nw', x='50', y='350')
window.mainloop()