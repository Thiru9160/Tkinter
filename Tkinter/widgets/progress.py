import tkinter as tk
from tkinter import *
from tkinter import ttk
top=tk.Tk()
top.title("progressbar example")
top.geometry("500x500")
#create progressbar widget
progress=ttk.Progressbar(top,orient="vertical",length=300,mode="determinate")
#we know the start and end points of progress
progress.pack()
#declare a function to simulate task progress
def start_progress():
    progress["value"]=0#intial value
    top.update_idletasks()
    for i in range(1,101):
        progress["value"]=i
        top.update_idletasks()
        top.after(50)#milliseconds
start_button=Button(top,text="Start Progress",command=start_progress).pack()

top.mainloop()