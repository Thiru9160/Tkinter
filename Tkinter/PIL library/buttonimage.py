import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
top=tk.Tk()
top.title("images using PIL(pillow) library")
top.geometry("500x500")

def msg():
    label=Label(top,text="button is clicked")
    label.pack()

image=Image.open("spiderman.jpeg").resize((50,50))
tk_image=ImageTk.PhotoImage(image)

image_gif=Image.open("s[idy2.gif")
tk_image_gif=ImageTk.PhotoImage(image)

label=Label(top,image=tk_image_gif)
label.pack()

button=Button(top,text="clickhere",image=tk_image,command=msg,compound="right")
button.pack()

top.mainloop()
