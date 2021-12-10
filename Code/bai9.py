from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd

ws = Tk()
ws.title("Bài 9")
ws.title('Bai 9')
ws.geometry('400x300')
ws.config(bg='#5F734C')

def select_file():
    global filename ,canvas
    filetypes = (
        ('Type files', '*.jpg'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename()

    
    img = Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    ws.photo = photo
    canvas.create_image(0,0,image=photo,anchor=NW)
    #panel = Label(ws, image=img)
    #panel.photo = img
    #panel.pack()
    return filename

def clear():
    global canvas,filename
    canvas = Canvas(ws,width=800,height=600)
    canvas.pack()
frame = Frame(
    ws,
    width=800,
    height=600
    )
frame.pack(expand=True, fill=BOTH)

canvas=Canvas(
    frame,
    bg='#4A7A8C',
    width=800,
    height=600,
    scrollregion=(0,0,700,700)
    )

vertibar=Scrollbar(
    frame,
    orient=VERTICAL
    )
vertibar.pack(side=RIGHT,fill=Y)
vertibar.config(command=canvas.yview)

horibar=Scrollbar(
    frame,
    orient=HORIZONTAL
    )
horibar.pack(side=BOTTOM,fill=X)
horibar.config(command=canvas.xview)

canvas.config(width=800,height=600)

canvas.config(
    xscrollcommand=horibar.set, 
    yscrollcommand=vertibar.set
    )
canvas.pack(expand=True,side=LEFT,fill=BOTH)

menubar = Menu(ws)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=select_file)
filemenu.add_command(label="Clear", command=clear)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=ws.quit)
menubar.add_cascade(label="File", menu=filemenu)
ws.config(menu=menubar)
ws.mainloop()