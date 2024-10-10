import tkinter as tk 
from tkinter import *
top=tk.Tk()
top.title("Keyboard clicks")
top.geometry("500x500")
#Declare a function
def Clicker(event):
    label1=Label(top,text="Key pressed :" + event.keysym)
    label1.pack()
btn1=Button(top,text="click me")
btn1.pack()
top.bind("<KeyPress>",Clicker)
#run the application
top.mainloop()