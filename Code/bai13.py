from tkinter import filedialog as fd
from tkinter import *
window = Tk()
window.title("B13")
window.geometry('800x500')
list = []
list1 = []
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    list.clear()
    list.append(filename)
    f = open("{}".format(filename),encoding="utf8")
    text.delete('1.0',END)
    data = f.read()
    text.insert(END,data)
def xuly():
    f = open("{}".format(list[0]),encoding="utf8")
    text1.delete('1.0',END)
    data = f.readlines()

    dataNew = []
    for i in range(0, len(data), 1):
        if(len(data[i]) == 26 or len(data[i]) ==1):
            print('loai')
        else:
            dataNew.append(data[i])




    text1.insert(END,dataNew)
    


open_btn = Button(window, text="Open", command=select_file)
open_btn.place(anchor='nw', x='50', y='10')

xuly_btn = Button( window, text="Xu ly",command=xuly)
xuly_btn.place(anchor='nw', x='400', y='10')

text = Text(window, width = 35, height = 20, wrap = NONE,xscrollcommand = 150,yscrollcommand = 100)
text.place(anchor='nw', x='50', y='90')
text.configure(background='#ffffff')

text1 = Text(window, width = 35, height = 20, wrap = NONE,xscrollcommand = 150,yscrollcommand = 100)
text1.place(anchor='nw', x='450', y='90')
text1.configure(background='#ffffff')
window.mainloop()