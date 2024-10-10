import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
top=tk.Tk()
top.title("Background Image")

image=Image.open("spiderman.jpeg").resize(())
tk_image=ImageTk.PhotoImage(image)


#create a label
bg_label=Label(top,image=tk_image)
bg_label.place(relwidth=1,relheight=1)#it cover entire window

top.mainloop()
