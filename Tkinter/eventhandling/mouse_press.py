import tkinter as tk
from tkinter import *
#create a window
top=tk.Tk()
top.title("mouse_clicks")
top.geometry("500x500")
#declare a function
def clicker(event):
    label1=Label(top,text="you clicked a button")
    label1.pack()

btn1=Button(top,text="click me")
btn1.bind("<Enter>",clicker)
#btn1.bind("<Leave>",clicker)
#btn1.bind("<Button-1>",clicker)
#btn1.bind("<Button-3>",clicker)
btn1.pack()


top.mainloop()