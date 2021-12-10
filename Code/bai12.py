#Vẽ hình tròn
import tkinter as tk 
root = tk.Tk() 
canvas = tk.Canvas(root, width=400, height=400, borderwidth=0, highlightthickness=0, bg="black") 
canvas.grid() 
def _create_circle(self, x, y, r, **kwargs): 
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs) 
tk.Canvas.create_circle = _create_circle 
def _create_circle_arc(self, x, y, r, **kwargs): 
    if "start" in kwargs and "end" in kwargs: 
     kwargs["extent"] = kwargs["end"] - kwargs["start"] 
     del kwargs["end"] 
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs) 
tk.Canvas.create_circle_arc = _create_circle_arc 
canvas.create_circle(150, 150, 150, fill="#ff0000", outline="") 
root.wm_title("B12") 
root.mainloop()