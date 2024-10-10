import tkinter as tk
from tkinter import *
top=tk.Tk()
top.title("place unmap example")
top.geometry("500x500")
#label
button=Button(top,text="HELLO,I'M PLACE")
button.place(x=50,y=50)
#functions for mapping and unmapping
def hide_button():
    button.place_forget()#unmaps
def show_button():
    button.place(x=50,y=50)#maps the button
#buttons for mapping and unmapping
btn1=Button(top,text="HIDE BUTTON",command=hide_button)
btn1.place(x=50,y=100)
btn2=Button(top,text="SHOW BUTTON",command=show_button)
btn2.place(x=50,y=150)
top.mainloop()
