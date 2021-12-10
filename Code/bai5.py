
from tkinter import *
import tkinter as tk
from tkcalendar import Calendar, DateEntry
#fuction
list = []

def add():

    hoten = hoten_entry.get()
    if hoten == "":
        print('Chua co thong tin')
    else:
        hoten = hoten_entry.get()
        ngaysinh = ngaysinh_entry.get()
        gioitinh = T_gioitinh(var1.get())
        #1 -> Nam
        diem = diem_entry.get()
        str1 = " {}   ----  {}   ----  {}  ----  {} ".format(hoten,ngaysinh,gioitinh,diem)
        item = str1
        list.append(item)

        hoten_entry.delete(0, END)
        diem_entry.delete(0, END)

    listbox.delete(0,END)

    for i in range(0, len(list), 1):
        listbox.insert(i,list[i])   
def T_gioitinh(i):
    if i ==1:
        return 'Nam'
    else:
        return 'Nu'


window = Tk()
window.title("Bai 5")
window.geometry('600x400')

var1 = tk.IntVar()
hoten_lb = Label(window,text="Ho ten: ")
hoten_lb.place(anchor='nw', x='50', y='10')

btnAdd = Button(window,text="ADD",command=add)
btnAdd.place(anchor='nw', x='400', y='10')

ngaysinh_lb = Label(window,text='Ngay sinh: ')
ngaysinh_lb.place(anchor='nw', x='50', y='40')
gioitinh_lb = Label(window,text='Gioi tinh: ')
gioitinh_lb.place(anchor='nw', x='50', y='70')
diem_lb = Label(window,text='Diem: ')
diem_lb.place(anchor='nw', x='50', y='100')
ds_lb = Label(window,text='Danh sach: ')
ds_lb.place(anchor='nw', x='50', y='130')

hoten_entry = Entry(window)
hoten_entry.place(anchor='nw', x='150', y='10')

ngaysinh_entry = DateEntry(window, width= 16, foreground= "white",bd=2)
ngaysinh_entry.place(anchor='nw', x='150', y='40')

gioitinh_entry = Checkbutton(window,text="Nam", onvalue=1, offvalue=0,variable=var1)
gioitinh_entry.place(anchor='nw', x='150', y='70')

diem_entry = Entry(window)
diem_entry.place(anchor='nw', x='150', y='100')


listbox = Listbox(width= 50, background= "#c0c0c0") 
listbox.place(anchor='nw', x='50', y='170')

window.mainloop()