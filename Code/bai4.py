
from tkinter import *

window = Tk()
window.title("Bai 4")
window.geometry('400x300')
lbl = Label(window, text="")
lbl.place(anchor='nw', height='150', width='300', x='50', y='10')
lbl.configure(background='#ffffff',wraplength='50')

sum_label = Label(window, text='')
sum_label.place(anchor='nw', height='40', width='50', x='70', y='200')
sum_label.configure(background='#ffffff',wraplength='50')
def clicked():
    f = open("data.txt", "r")
    lbl.configure(text= f.read() )
def saved():
    f = open("data.txt", "r")
    data = f.read()
    arr = data.split(" ")
    sum = 0
    for i in arr:
        sum += int(i)
    f = open("new.txt", "a")
    txt2 = "data: {0}, sum {1}".format(data,sum)
   
    f.write(txt2 )
    f.close()
def sumed():
    f = open("data.txt", "r")
    data = f.read()
    arr = data.split(" ")
    sum = 0
    for i in arr:
        sum += int(i)
    sum_label.configure(text=sum)

btn = Button(window, text="OPEN", command=clicked)
btn.place(anchor='nw', x='170', y='170')

save = Button(window, text="SAVE", command=saved)
save.place(anchor='nw', x='250', y='170')

sumed = Button(window, text="CONG", command=sumed)
sumed.place(anchor='nw', x='70', y='170')
 
window.mainloop()