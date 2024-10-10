import tkinter as tk
from tkinter import *
top=tk.Tk()
top.title("grid unmap example")
top.geometry("500x500")
#label
label=Label(top,text="HELLO,I'M GRID")
label.grid(row=0,column=1)
#mapping and unmapping for label
def hide_label():
    label.grid_forget()
def show_label():
    label.grid(row=0,column=1)
#buttons for mapping and unmapping
btn1=Button(top,text="HIDE LABEL",command=hide_label)
btn1.grid(row=1,column=1)
btn2=Button(top,text="SHOW LABEL",command=show_label)
btn2.grid(row=2,column=1)
top.mainloop()