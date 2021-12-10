from tkinter import *
from tkinter import messagebox
import time
import random



class Ball:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25,fill = color)
        self.canvas.move(self.id,100,200)
        self.start = [-3,-2,-1,1,2,3]
        random.shuffle(self.start)
        self.x = self.start[0]
        self.y = self.start[1]
        self.canvas_height = 400
        self.canvas_width = 500
        self.over = False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y = 3
        if pos[3]>= self.canvas_height:
            self.y = -3
        if pos[0]<=0:
            self.x = 3
        if pos[2] >=self.canvas_width:
            self.x = -3
    def stop(self):
        self.y =0
        self.x = 0
    def start_movement(self,x, y):
        if self.x == 0 and self.y == 0:
            self.x = x
            self.y = y
       
        
root = Tk()
root.title("Bài 7")
def doSomething(task):
    global var, button,canvas
    global x, y
    while task == 0:
        if bong.x != 0 and bong.y != 0:
            x = bong.x
            y = bong.y
        var.set("Started Playing")
        button.configure(text = "Pause")
        button.configure(command = lambda task = 1: doSomething(task))
        bong.start_movement(x, y)

        bong.draw()
        root.update_idletasks()
        root.update()
        time.sleep(0.03)
        #play
    while task == 1:
        
        var.set("Paused")
        button.configure(text = "Resume")
        button.configure(command = lambda task = 0: doSomething(task))
        bong.stop()
        root.update_idletasks()
        root.update()
        time.sleep(0.1)
        #pause


button = Button(root, text = "Play", command = lambda task = 0: doSomething(task))
button.pack()
canvas = Canvas(root,height=400,width=500)
canvas.pack()
bong = Ball(canvas,"Blue")

var = StringVar()
label = Label(root, textvariable = var)
label.pack()

root.mainloop()