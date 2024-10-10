import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
top=tk.Tk()
top.title("images using PIL(pillow) library")
top.geometry("500x500")

image=Image.open("spiderman.jpeg").resize((100,100))
tk_image=ImageTk.PhotoImage(image)

label=Label(top,image=tk_image)
label.pack()

top.mainloop()
