import tkinter  as tk
from tkinter import *
top=tk.Tk()
top.title("Paint app")

#create canvas 
can=Canvas(top,width=500,height=500,bg="white")
can.pack(fill="both")

#create drawing function with mouse clicks
def draw(event):
    x,y=event.x,event.y
    can.create_oval(x-2,y-2,x+2,y+2,fill="black")
can.bind("<B3-Motion>",draw)#left mouse button
top.mainloop()