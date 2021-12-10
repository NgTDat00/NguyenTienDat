import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = tk.Tk() #Create new window 
window.title("BÀI 1")

Main_label = Label(window,text="Cong Nghe Thong Tin",bg = "yellow",foreground="black",width="30", height="5",font=("Timer", 16))
Main_label.grid(row=0,column = 1,ipadx = 20, ipady = 20, padx = 20, pady = 20)

def thoat():
    res = messagebox.askquestion('warning', 'Bạn có muốn thoát không?')
    if res == 'yes':
        window.quit()
    else:
        pass

BT = Button(window, font=("Verdana",10,'bold'), text="Thoat", width="12", height=3,
                    bd=3, bg="gray",
                    command= thoat )
BT.grid(row = 1, column = 1)

label = Label(window,text="",foreground="black",width="50", height="5",font=("Timer", 16))
label.grid(row=2,column = 1)

window.mainloop()