from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd

root = Tk()
root.title("BÀI 8")
def select_file():
    global filename ,canvas
    filetypes = (
        ('Type files', '*.jpg'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename()

    canvas = Canvas(root,width=400,height=300)
    canvas.grid(row=1,column=1)
    img = Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    root.photo = photo
    canvas.create_image(0,0,image=photo,anchor=NW)
    c_entry.delete(0,"end")
    c_entry.insert(0,filename)
    return filename

def clear():
    global canvas,filename
    canvas = Canvas(root,width=400,height=300)
    canvas.grid(row=1,column=1)
    filename = ""
    c_entry.delete(0,"end")
    c_entry.insert(0,filename)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=select_file)
filemenu.add_command(label="Clear", command=clear)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
canvas = Canvas(root,width=400,height=300)
canvas.grid(row=1,column=1)
c_label = Label(root,text="Filename",foreground="black",width="12", height="2",font=("Timer", 16))
c_label.grid(row=2,column = 0,sticky=W)
c_entry = Entry(root,width="50")
c_entry.grid(row = 2,column = 1,sticky = W)
root.config(menu=menubar)

root.mainloop()