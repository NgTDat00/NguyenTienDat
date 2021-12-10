import tkinter as tk
from tkinter import *
from tkinter import messagebox
import math

window = tk.Tk() #Create new window 
window.title("BÀI 2")

a_label = Label(window,text="Nhap a",foreground="black",width="12", height="2",font=("Timer", 16))
a_label.grid(row=0,column = 0)
a_entry = Entry(window,width="20")
a_entry.grid(row = 0,column = 1,sticky = W)

b_label = Label(window,text="Nhap b",foreground="black",width="12", height="2",font=("Timer", 16))
b_label.grid(row=1,column = 0)
b_entry = Entry(window,width="20")
b_entry.grid(row = 1,column = 1,sticky = W)

c_label = Label(window,text="Nhap c",foreground="black",width="12", height="2",font=("Timer", 16))
c_label.grid(row=2,column = 0)
c_entry = Entry(window,width="20")
c_entry.grid(row = 2,column = 1,sticky = W)

Nghiem_label = Label(window,text="Nghiem",foreground="black",width="12", height="2",font=("Timer", 16))
Nghiem_label.grid(row=3,column = 0)
Nghiem_entry = Entry(window,width="40",state = DISABLED)
Nghiem_entry.grid(row = 3,column = 1,sticky = W)



def giai():
    try:  
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())

        if a==0:
            if b==0:
                if c==0:
                    Nghiem_entry['state'] = NORMAL
                    Nghiem_entry.delete(0,"end")
                    Nghiem_entry.insert(0,"PTVSN")
                else:
                    Nghiem_entry['state'] = NORMAL
                    Nghiem_entry.delete(0,"end")
                    Nghiem_entry.insert(0,"PTVN")
            else:
                Nghiem_entry['state'] = NORMAL
                Nghiem_entry.delete(0,"end")
                Nghiem_entry.insert(0,f"Phuong trinh co nghiem duy nhat x = {-c/b}")
        else:
            delta = b**2 - 4*a*c
            if delta >0:
                Nghiem_entry['state'] = NORMAL
                Nghiem_entry.delete(0,"end")
                Nghiem_entry.insert(0,f"Phuong trinh co 2 nghiem  x1 = {(-b+math.sqrt(delta))/(2*a)} và x2 = {(-b-math.sqrt(delta))/(2*a)}")
            if delta ==0:
                Nghiem_entry['state'] = NORMAL
                Nghiem_entry.delete(0,"end")
                Nghiem_entry.insert(0,f"Phuong trinh co nghiem kep x = {-b/(2*a)}")
            if delta<0:
                Nghiem_entry['state'] = NORMAL
                Nghiem_entry.delete(0,"end")
                Nghiem_entry.insert(0,"PTVN")
    except:
        messagebox.showinfo('Warning', 'ban can nhap so')

def xoa():
    a_entry.delete(0,"end")
    b_entry.delete(0,"end")
    c_entry.delete(0,"end")
    Nghiem_entry['state'] = DISABLED
def thoat():
    window.quit()
giai_BT = Button(window, font=("Verdana",10,'bold'), text="Giai", width="6", height=2,
                    bd=3, bg="gray", activebackground="#3c9d9b",fg='#ffffff',
                    command= giai )
giai_BT.grid(row = 0, column = 1,sticky=E)

xoa_BT = Button(window, font=("Verdana",10,'bold'), text="Xoa", width="6", height=2,
                    bd=3, bg="gray", activebackground="#3c9d9b",fg='#ffffff',
                    command= xoa )
xoa_BT.grid(row = 1, column = 1,sticky=E)

thoat_BT = Button(window, font=("Verdana",10,'bold'), text="Thoat", width="6", height=2,
                    bd=3, bg="gray", activebackground="#3c9d9b",fg='#ffffff',
                    command= thoat )
thoat_BT.grid(row = 2, column = 1,sticky=E)




window.mainloop()